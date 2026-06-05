import streamlit as st
from google import genai
from google.genai import types
from google.genai.errors import APIError

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="체형 맞춤 다이어트 챗봇", page_icon="🥗", layout="centered")
st.title("🥗 체형 맞춤 다이어트 AI 챗봇")
st.write("당신의 키와 몸무게를 입력하고, 맞춤형 다이어트 조언을 받아보세요!")

# 2. Streamlit Secrets에서 API 키 불러오기 및 클라이언트 초기화
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Streamlit Secrets에 'GEMINI_API_KEY'가 설정되지 않았습니다. 설정을 확인해 주세요.")
    st.stop()

try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error(f"클라이언트 초기화 중 오류가 발생했습니다: {e}")
    st.stop()

# 3. 사용자 신체 정보 입력 받기 (사이드바 활용)
st.sidebar.header("📋 나의 신체 정보")
height = st.sidebar.number_input("키 (cm)", min_value=100, max_value=250, value=170, step=1)
weight = st.sidebar.number_input("몸무게 (kg)", min_value=30, max_value=200, value=65, step=1)

# BMI 계산 (간단한 참고용)
bmi = weight / ((height / 100) ** 2)
st.sidebar.markdown(f"**현재 BMI:** {bmi:.1f}")

# 4. 세션 상태(Session State)를 활용한 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 채팅 기록 화면에 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. 사용자 입력 및 AI 답변 처리
if prompt := st.chat_input("다이어트에 대해 궁금한 점을 물어보세요!"):
    # 사용자가 보낸 메시지 화면에 표시 및 저장
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI의 답변 생성 중임을 표시
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # 시스템 프롬프트 설정 (사용자의 키와 몸무게 맥락 주입)
        system_instruction = (
            f"당신은 친절하고 전문적인 다이어트 및 영양 상담 전문가입니다. "
            f"현재 상담 중인 사용자의 신체 정보는 키 {height}cm, 몸무게 {weight}kg (BMI: {bmi:.1f})입니다. "
            f"이 체형 정보를 반드시 바탕으로 하여 안전하고 건강한 맞춤형 식단 및 운동 방법을 조언해 주세요. "
            f"답변은 친절하게 존댓말로 작성해 주세요."
        )

        try:
            # 대화 기록을 Gemini API 형식으로 변환 (시스템 프롬프트 제외한 이전 대화)
            contents = []
            for msg in st.session_state.messages:
                role = "user" if msg["role"] == "user" else "model"
                contents.append(types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=msg["content"])]
                ))

            # Gemini API 호출
            response = client.models.generate_content(
                model='gemini-2.5-flash-lite',
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.7,
                )
            )
            
            # 답변 출력 및 저장
            ai_response = response.text
            message_placeholder.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

        except APIError as e:
            st.error(f"Gemini API 오류가 발생했습니다: {e.message}")
        except Exception as e:
            st.error(f"예기치 못한 오류가 발생했습니다: {e}")
