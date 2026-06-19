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

# ---- 탭 2: AI 상담 및 히스토리 ----
with tab2:
    st.subheader("💬 AI 마음 닥터와 대화하기")
    
    # 시스템 인스트럭션 (AI 페르소나 설정)
    system_role = (
        "당신은 비만 예방 및 마인드풀 이팅(Mindful Eating) 전문 심리 상담사입니다. "
        "사용자가 충동적인 폭식 욕구(가짜 배고픔)를 느낄 때, 비난하지 않고 따뜻하게 공감해 주면서도 "
        "이성적으로 그 충동을 넘길 수 있도록 돕는 역할을 합니다. "
        "친절하고 부드러운 어조를 사용하고, 사용자가 음식을 먹는 행위 대신 할 수 있는 가벼운 대안(물 마시기, 산책, 스트레칭 등)을 제안해 주세요. "
        "답변은 너무 길지 않게 3~4문장 내외로 핵심만 집어 가독성 있게 작성하세요."
    )
    
    # 최근 기록 데이터가 있는지 확인 후 AI에게 상황 공유
    if st.session_state.latest_trigger:
        trigger = st.session_state.latest_trigger
        st.info(f"🤖 **AI 닥터 상태 인지 중**: 현재 당신은 **{trigger['주요 감정']}** 상태이며, **{trigger['음식']}**(충동 레벨: {trigger['충동 레벨']}/10)을 원하고 계시군요.")
        
        # 첫 인사 자동 생성 (채팅창이 비어있을 때만)
        if len(st.session_state.chat_history) == 0:
            initial_prompt = f"사용자가 지금 {trigger['주요 감정']} 때문에 {trigger['음식']}을 너무 먹고 싶어합니다. 충동 레벨은 10점 만점에 {trigger['충동 레벨']}점입니다. 사용자의 상세 상황: '{trigger['상세 내용']}'. 이 사용자를 위로하고 폭식을 멈추도록 돕는 첫 마디를 건네주세요."
            with st.spinner("AI 닥터가 마음을 분석 중입니다..."):
                initial_reply = get_gemini_response(initial_prompt, system_role)
                st.session_state.chat_history.append({"role": "assistant", "content": initial_reply})
    else:
        st.warning("💡 아직 SOS 기록이 없습니다. 먼저 '🚨 SOS 폭식 기록' 탭에서 현재 상태를 기록하시면 맞춤형 AI 상담을 받아보실 수 있습니다.")

    # 채팅 메시지 표시
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
    # 채팅 입력 창
    if user_input := st.chat_input("AI 닥터에게 하고 싶은 말을 적어보세요..."):
        # 사용자 메시지 추가
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
            
        # AI 대화 맥락 형성 및 답변 요구
        context_prompt = f"사용자의 이전 기록 및 대화 흐름을 바탕으로 답변하세요. 사용자 입력: {user_input}"
        with st.chat_message("assistant"):
            with st.spinner("생각 중..."):
                reply = get_gemini_response(context_prompt, system_role)
                st.write(reply)
                st.session_state.chat_history.append({"role": "assistant", "content": reply})

    st.divider()
    
    # ---- 나의 충동 기록 히스토리 목록 ----
    st.subheader("📊 나의 폭식 충동 히스토리")
    if st.session_state.binge_logs:
        df = pd.DataFrame(st.session_state.binge_logs)
        st.dataframe(df, use_container_width=True)
        
        # 간단한 분석 제공
        st.caption("💡 팁: 기록이 쌓이면 내가 주로 어떤 감정(예: 스트레스, 지루함)일 때 특정 음식을 찾는지 패턴을 파악할 수 있어 비만 예방에 큰 도움이 됩니다.")
    else:
        st.write("아직 기록된 히스토리가 없습니다.")
