import streamlit as st
import google.generativeai as genai
import datetime
import pandas as pd

# 1. 페이지 설정
st.set_page_config(
    page_title="폭식 브레이크 (Binge Break)",
    page_icon="🍎",
    layout="centered"
)

# 2. 세션 상태(Session State) 초기화 (앱이 실행되는 동안 데이터 유지)
if "binge_logs" not in st.session_state:
    st.session_state.binge_logs = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "latest_trigger" not in st.session_state:
    st.session_state.latest_trigger = None

# 3. Gemini API 설정 및 예외 처리
api_key = st.secrets.get("GEMINI_API_KEY")

def get_gemini_response(prompt, system_instruction):
    if not api_key:
        return "⚠️ API Key가 설정되지 않았습니다. Streamlit Secrets 설정을 확인해주세요."
    try:
        genai.configure(api_key=api_key)
        # 요구사항에 명시된 gemini-2.5-flash-lite 모델 사용
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash-lite",
            system_instruction=system_instruction
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ AI 연동 중 오류가 발생했습니다: {str(e)}"

# 4. UI 구성
st.title("🍎 폭식 브레이크 (Binge Break)")
st.markdown("### *“음식이 아니라, 마음을 채울 시간입니다.”*")
st.caption("충동적인 폭식 욕구가 올 때 이곳에 기록하고 AI와 대화하며 마음을 가라앉혀 보세요.")

st.divider()

# 사이드바: 나의 앱 이용 가이드
with st.sidebar:
    st.header("💡 사용 방법")
    st.markdown("""
    1. **1단계**: 폭식 충동이 들 때 **'🚨 SOS 폭식 기록'**에 현재 상태를 입력합니다.
    2. **2단계**: 아래 **'💬 AI 마음 닥터'** 탭으로 이동해 AI와 대화를 나누며 충동을 보듬어줍니다.
    3. **3단계**: 기록을 보며 내가 주로 어떤 감정일 때 폭식하는지 파악합니다.
    """)
    st.info("💡 폭식 충동은 보통 15분 마인드풀링을 통해 극복할 수 있습니다.")

# 탭 구성
tab1, tab2 = st.tabs(["🚨 SOS 폭식 기록", "💬 AI 마음 닥터 & 히스토리"])

# ---- 탭 1: SOS 폭식 기록 ----
with tab1:
    st.subheader("현재 내 상태 기록하기")
    st.write("지금 어떤 상태인가요? 솔직하게 적는 것만으로도 충동이 줄어듭니다.")
    
    with st.form(key="binge_form", clear_on_submit=True):
        craved_food = st.text_input("지금 가장 먹고 싶은 음식은 무엇인가요?", placeholder="예: 떡볶이, 마라탕, 초콜릿 케이크")
        
        urge_level = st.slider("현재 폭식 충동의 세기는 어느 정도인가요?", min_value=1, max_value=10, value=5, 
                              help="1: 참을 만함, 10: 당장 먹지 않으면 안 될 것 같음")
        
        emotion = st.selectbox(
            "지금 어떤 감정이 드나요? (가짜 배고픔의 원인)",
            ["스트레스/짜증", "외로움/허전함", "지루함", "불안/걱정", "단순 입터짐", "기타"]
        )
        
        detail_context = st.text_area("현재 상황이나 마음을 조금 더 구체적으로 적어주세요 (선택)", placeholder="예: 오늘 상사한테 깨져서 너무 스트레스 받아요.")
        
        submit_button = st.form_submit_button(label="🚨 SOS 브레이크 작동!")
        
    if submit_button:
        if not craved_food:
            st.warning("먹고 싶은 음식을 입력해주세요!")
        else:
            # 로그 데이터 생성
            new_log = {
                "시간": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "음식": craved_food,
                "충동 레벨": urge_level,
                "주요 감정": emotion,
                "상세 내용": detail_context
            }
            # 세션 상태에 저장
            st.session_state.binge_logs.append(new_log)
            st.session_state.latest_trigger = new_log
            
            # 첫 AI 프롬프트 세팅을 위한 대화 히스토리 초기화 및 가이드 문구 추가
            st.session_state.chat_history = [] 
            
            st.success("✅ 현재 상태가 안전하게 기록되었습니다! 'AI 마음 닥터' 탭으로 이동하여 이야기를 나누어 보세요.")
            st.balloons()

# ---- 탭
