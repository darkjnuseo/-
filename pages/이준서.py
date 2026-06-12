import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 (가장 상단에 위치)
st.set_page_config(
    page_title="스마트 신체 분석기",
    page_icon="⚖️",
    layout="centered"
)

# 2. Gemini API 설정 및 예외 처리
ai_available = False
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
        ai_available = True
    except Exception as e:
        ai_available = False
else:
    ai_available = False

# 3. 앱 타이틀 및 소개
st.title("⚖️ 스마트 신체 분석 및 건강 가이드")
st.markdown("키와 몸무게를 입력하면 당신의 체형 분석과 맞춤형 건강 팁을 제공합니다.")
st.markdown("---")

# 4. 사용자 입력 섹션 (Sidebar)
st.sidebar.header("📝 신체 정보 입력")
height_cm = st.sidebar.number_input("키 (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
weight_kg = st.sidebar.number_input("몸무게 (kg)", min_value=30.0, max_value=200.0, value=65.0, step=0.1)
gender = st.sidebar.radio("성별", ["남성", "여성"])

# 5. 데이터 계산
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
normal_weight_min = 18.5 * (height_m ** 2)
normal_weight_max = 23.0 * (height_m ** 2) # 한국인 BMI 기준 (정상: 18.5~22.9)

# BMI 비만도 등급 판정
if bmi < 18.5:
    status = "저체중"
    color = "blue"
    progress_val = 0.2
elif bmi < 23:
    status = "정상"
    color = "green"
    progress_val = 0.5
elif bmi < 25:
    status = "과체중"
    color = "orange"
    progress_val = 0.75
else:
    status = "비만"
    color = "red"
    progress_val = 1.0

# 6. 결과 화면 출력 (눈에 잘 보이게 구성)
st.subheader("📊 나의 신체 지표 분석")

# 메트릭 레이아웃으로 큰 글씨 강조
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="BMI 지수", value=f"{bmi:.1f}")
with col2:
    st.metric(label="현재 상태", value=status)
with col3:
    # 적정 체중 범위 계산 및 표시
    avg_normal = (normal_weight_min + normal_weight_max) / 2
    weight_diff = weight_kg - avg_normal
    if weight_diff > 0:
        st.metric(label="조절 필요량", value=f"+{weight_diff:.1f} kg", delta=f"{weight_diff:.1f} kg")
    else:
        st.metric(label="조절 필요량", value=f"{weight_diff:.1f} kg", delta=f"{weight_diff:.1f} kg", delta_color="inverse")

# 비만도 시각적 게이지 바
st.markdown(f"**체질량지수(BMI) 위치:** ({status})")
st.progress(progress_val)

# 세부 정보 안내 매직 박스
st.info(f"💡 당신의 키({height_cm}cm)에 맞는 한국인 표준 적정 체중은 **{normal_weight_min:.1f}kg ~ {normal_weight_max:.1f}kg** 입니다.")

st.markdown("---")

# 7. AI 맞춤형 건강 피드백 세션
st.subheader("🤖 AI 맞춤형 건강 가이드 리포트")

if ai_available:
    with st.spinner("AI가 당신의 신체 데이터를 분석 중입니다..."):
        try:
            prompt = f"""
            사용자 정보:
            - 성별: {gender}
            - 키: {height_cm}cm
            - 몸무게: {weight_kg}kg
            - BMI: {bmi:.1f} ({status} 상태)
