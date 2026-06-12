import streamlit as st

# 1. 페이지 설정 (최상단 필수 배치로 에러 원천 차단)
st.set_page_config(
    page_title="FitForge 다이어트 솔루션",
    page_icon="🔥",
    layout="centered"
)

# 2. 대시보드 타이틀 및 서비스 소개
st.title("🔥 FitForge 스마트 다이어트 솔루션")
st.markdown("### \"당신의 신체 데이터에 맞춘 고정밀 식단 & 운동 매칭 시스템\"")
st.markdown("키와 몸무게를 입력하면 FitForge의 알고리즘이 당신만을 위한 맞춤형 다이어트 가이드를 실시간으로 설계합니다.")
st.markdown("---")

# 3. 사이드바 - 신체 정보 입력 세션
st.sidebar.header("📋 신체 데이터 입력")
gender = st.sidebar.radio("성별 선택", ["남성", "여성"], index=0)
age = st.sidebar.number_input("만 나이", min_value=1, max_value=120, value=26, step=1)
height = st.sidebar.number_input("키 (cm)", min_value=100.0, max_value=250.0, value=173.0, step=0.1)
weight = st.sidebar.number_input("현재 몸무게 (kg)", min_value=30.0, max_value=200.0, value=78.0, step=0.1)

# 4. 연산 및 예외 처리 구역
try:
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    
    # 기초대사량(BMR) 계산 공식 (Mifflin-St Jeor)
    if gender == "남성":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        std_weight = (height_m ** 2) * 22
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        std_weight = (height_m ** 2) * 21
        
    # 활동 대사량 (보통 활동 기준)
    tdee = bmr * 1.375

    # BMI 비만도 판정 및 시각화용 변수 설정
    if bmi < 18.5:
        status, color, bar_val = "저체중 🟡", "blue", 0.25
    elif bmi < 23.0:
        status, color, bar_val = "정상 체중 🟢", "green", 0.50
    elif bmi < 25.0:
        status, color, bar_val = "과체중 🟠", "orange", 0.75
    else:
        status, color, bar_val = "비만 🔴", "red", 1.0

    # -----------------------------------------------------------------
    # 기능 1: 눈에 잘 띄는 신체정보 대시보드 제공
    # -----------------------------------------------------------------
    st.subheader("📊 1. 나의 신체분석 리포트")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="현재 체질량지수 (BMI)", value=f"{bmi:.1f}", delta=status)
    with col2:
        st.metric(label="하루
