import streamlit as st

# ==========================================
# 1. 페이지 기본 설정 및 디자인 테마
# ==========================================
st.set_page_config(
    page_title="FitMeal & Move - 맞춤형 다이어트 가이드",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 커스텀 CSS 스타일링 (가독성 및 디자인 강화)
st.markdown("""
    <style>
    .main-title { font-size: 2.6rem; font-weight: 800; color: #2E7D32; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size: 1.15rem; color: #666666; text-align: center; margin-bottom: 30px; }
    .feature-card { padding: 22px; border-radius: 12px; background-color: #F1F8E9; border-left: 6px solid #7CB342; margin-bottom: 18px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .feature-card h4 { margin-top: 0; color: #33691E; }
    .result-box { padding: 20px; border-radius: 10px; background-color: #FAFAFA; border: 1px solid #E0E0E0; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 2. 사이드바 내비게이션 & 앱 소개
# ==========================================
with st.sidebar:
    st.markdown("# 🥗 FitMeal & Move")
    st.caption("당신만을 위한 스마트 다이어트 솔루션")
    
    # Unsplash 고화질 웰빙 이미지 활용
    st.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500", use_container_width=True)
    
    st.info("💡 **FitMeal & Move**는 굶는 다이어트가 아닌, 개인의 신체 데이터를 과학적으로 분석하여 지속 가능한 식단과 운동을 제안합니다.")
    
    st.markdown("---")
    # 메뉴 선택 (라디오 버튼 대신 깔끔한 셀렉트박스 활용)
    menu = st.selectbox(
        "이동할 화면을 선택하세요:",
        ["✨ 서비스 및 주요 기능 소개", "📊 1분 신체 진단 & 맞춤 제안"]
    )
    
    st.markdown("---")
    st.caption("© 2026 FitMeal & Move Co. All rights reserved.")


# ==========================================
# 3. [화면 1] 서비스 및 주요 기능 소개
# ==========================================
if menu == "✨ 서비스 및 주요 기능 소개":
    st.markdown("<div class='main-title'>🥗 FitMeal & Move</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>체중 감량, 더 이상 헤매지 마세요. 과학적인 분석으로 오늘부터 시작하세요!</div>", unsafe_allow_html=True)
    
    # 메인 배너 이미지
    st.image("https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=1000", use_container_width=True)
    st.write("")
    
    st.markdown("### ⚡ 핵심 기능 미리보기")
    
    # 2열 레이아웃으로 시각적 피로도 감소 및 주목도 향상
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <h4>📊 1. 1분 맞춤형 신체 진단</h4>
            <p>성별, 키, 몸무게, 활동량을 바탕으로 현재 나의 비만도(BMI)와 숨만 쉬어도 소비되는 기초대사량(BMR)을 즉시 계산합니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
            <h4>🥗 2. 탄·단·지 맞춤형 음식 추천</h4>
            <p>단순히 굶는 레시피가 아닌, 목적에 맞는 칼로리와 탄수화물·단백질·지방의 황금 영양 성분 비율을 계산하여 제안합니다.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h4>🏃‍♂️ 3. 맞춤형 운동 프로그램</h4>
            <p>유산소와 근력 운동의 최적 조합을 찾아내어, 부상 없이 체지방을 가장 빠르게 태울 수 있는 루틴을 구성해 드립니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
            <h4>📈 4. [특화] 목표 달성 시뮬레이터</h4>
            <p>사이드바 메뉴에서 진단을 진행하시면 목표 체중까지 소모해야 할 총 칼로리와 일일 권장 섭취량을 한눈에 시각화해 드립니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
    # 하단 행동 유도 버튼
    st.write("")
    st.success("👉 왼쪽 사이드바 메뉴를 **[📊 1분 신체 진단 & 맞춤 제안]**으로 변경하여 나만의 다이어트 가이드를 바로 확인해 보세요!")


# ==========================================
# 4. [화면 2] 1분 신체 진단 & 맞춤 제안
# ==========================================
elif menu == "📊 1분 신체 진단 & 맞춤 제안":
    st.markdown("<div class='main-title'>📊 1분 신체 진단 키트</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>정확한 정보를 입력하시면 인공지능형 맞춤 다이어트 가이드가 실시간으로 생성됩니다.</div>", unsafe_allow_html=True)
    
    # 입력 서식 블록화 (예외 처리 및 안전한 데이터 입력을 위해 수치 제한 설정)
    with st.form("user_info_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            gender = st.radio("성별 선택", ["남성", "여성"], horizontal=True)
            age = st.number_input("나이 입력 (세)", min_value=10, max_value=100, value=25, step=1)
        with col2:
            height = st.number_input("키 입력 (cm)", min_value=100, max_value=230, value=170, step=1)
            weight = st.number_input("현재 몸무게 입력 (kg)", min_value=30, max_value=200, value=65, step=1)
        with col3:
            purpose = st.selectbox("다이어트 최종 목적", ["체중 감량 (지방 연소)", "린매스업 (근육 증가+지방 감소)", "건강 및 체력 유지"])
            activity = st.selectbox("평소 활동량 격차", ["활동량 적음 (사무직, 좌식 생활)", "보통 (주 1~3회 가벼운 운동)", "활동량 많음 (주 4회 이상 고강도 운동)"])
            
        submit_button = st.form_submit_button(label="⚡ 실시간 신체 분석 및 결과 보기")
        
    # 결과 연산 및 출력 영역
    if submit_button:
        try:
            # [기능 1] 키와 몸무게로 다양한 신체정보 제공 계산
            height_m = height / 100
            bmi = weight / (height_m ** 2)
            
            # Harris-Benedict 공식 기반 기초대사량(BMR) 계산
            if gender == "남성":
                bmr = 66.47 + (13.75 * weight) + (5 * height) - (6.76 * age)
            else:
                bmr = 655.1 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
                
            # 활동계수 반영한 일일 대사량(TDEE) 계산
            activity_multipliers = {"활동량 적음 (사무직, 좌식 생활)": 1.2, "보통 (주 1~3회 가벼운 운동)": 1.375, "활동량 많음 (주 4회 이상 고강도 운동)": 1.55}
            tdee = bmr * activity_multipliers[activity]
            
            # 다이어트 목적별 하루 권장 섭취 칼로리 세팅
            if "감량" in purpose:
                recommended_kcal = tdee - 400
                carb_p, prot_p, fat_p = 4, 4, 2  # 비율 설정을 위한 변수값 (4:4:2)
            elif "린매스업" in purpose:
                recommended_kcal = tdee
                carb_p, prot_p, fat_p = 5, 3, 2  # 5:3:2
            else:
                recommended_kcal = tdee
                carb_p, prot_p, fat_p = 5, 2, 3  # 5:2:3

            # --- 결과 화면 UI 구성 ---
            st.markdown("### 🎯 1. 나의 신체 정보 분석 결과")
            
            metric_col1, metric_col2, metric_col3 = st.columns(3)
            with metric_col1:
                st.metric(label="나의 BMI (체질량지수)", value=f"{bmi:.1f}")
                if bmi < 18.5:
                    st.warning("👉 현재 **저체중** 상태입니다.")
                elif 18.5 <= bmi < 23:
                    st.success("👉 현재 **정상 체중** 상태입니다.")
                elif 23 <= bmi < 25:
                    st.warning("👉 현재 **과체중** 상태입니다.")
                else:
                    st.error("👉 현재 **비만** 상태입니다.")
                    
            with metric_col2:
                st.metric(label="하루 필수 기초대사량(BMR)", value=f"{int(bmr):,} kcal")
                st.caption("생명 유지에 필요한 최소 에너지 양입니다.")
                
            with metric_col3:
                st.metric(label="목적별 하루 권장 섭취량", value=f"{int(recommended_kcal):,} kcal")
                st.caption("활동량과 다이어트 목적이 반영된 수치입니다.")
                
            st.markdown("---")
            
            # 탭 기능을 이용해 운동과 음식 정보를 깔끔하게 분리
            tab_food, tab_exercise = st.tabs(["🥗 2. 맞춤형 음식 및 식단 가이드", "🏃‍♂️ 3. 맞춤형 운동 프로그램 추천"])
            
            # [기능 3] 신체정보 바탕 음식 추천
            with tab_food:
                st.markdown(f"#### 🍏 하루 권장 소비 칼로리 **{int(recommended_kcal):,} kcal**에 맞춘 식단")
                st.write(f"현재 선택하신 **[{purpose}]** 목적에 맞게 영양성분 비율을 **탄수화물 {carb_p*10}%, 단백질 {prot_p*10}%, 지방 {fat_p*10}%**로 구성했습니다.")
                
                food_col1, food_col2, food_col3 = st.columns(3)
                with food_col1:
                    st.info("**🍞 추천 탄수화물 (에너지원)**\n\n* 현미밥 1공기 또는 고구마 1.5개\n* 오트밀 60g\n* 통밀빵 2쪽\n\n*정제된 흰 쌀밥, 밀가루는 최소화하세요.*")
                with food_col2:
                    st.success("**🍗 추천 단백질 (근육 보존)**\n\n* 닭가슴살 150g\n* 연어 구이 1토막\n* 계란 3개 (노른자는 1개만)\n* 두부 1/2모\n\n*매 끼니 손바닥 크기만큼 꼭 섭취하세요.*")
                with food_col3:
                    st.warning("**🥑 추천 지방 (호르몬 조절)**\n\n* 아몬드 10알 내외\n* 아보카도 1/2개\n* 올리브유 가볍게 두른 샐러드\n\n*트랜스 지방이 포함된 튀김류는 금물입니다.*")
                    
            # [기능 2] 신체정보 바탕 운동 추천
            with tab_exercise:
                st.markdown(f"#### 🏋️‍♂️ 회원님의 현재 체력 계수(**{activity}**) 및 체형 맞춤 루틴")
                
                if "적음" in activity:
                    st.markdown("""
                    <div class='result-box'>
                        <strong>[초급자 추천 루틴: 관절 보호 및 기초 체력 증진]</strong><br><br>
                        1. <b>가벼운 유산소:</b> 빠른 걸음으로 걷기 하루 30분 (주 4회)<br>
                        2. <b>맨몸 근력 운동:</b> 벽 대고 푸쉬업 12회 x 3세트 / 맨몸 스쿼트 15회 x 3세트<br>
                        3. <b>마무리:</b> 전신 스트레칭 10분 (폼롤러 활용 추천)<br><br>
                        ⚠️ <i>체중으로 인해 관절에 무리가 갈 수 있으니 과도한 달리기는 피하세요!</i>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class='result-box'>
                        <strong>[중·고급자 추천 루틴: 체지방 연소 및 근육량 보존]</strong><br><br>
                        1. <b>메인 웨이트 트레이닝 (40분):</b> 덤벨 스쿼트, 데드리프트, 바벨 로우 등 대근육 위주 복합 운동<br>
                        2. <b>인터벌 유산소 (20분):</b> 런닝머신 속도 6.0(2분) -> 속도 10.0(1분) 반복 6세트 진행<br>
                        3. <b>코어 강화:</b> 플랭크 1분 x 3세트<br><br>
                        🔥 <i>기초대사량이 높아 운동 효율이 매우 좋은 상태입니다. 점진적 과부하를 적용해 보세요!</i>
                    </div>
                    """, unsafe_allow_html=True)
                    
        except Exception as e:
            st.error(f"계산 중 에러가 발생했습니다. 입력 값을 다시 확인해 주세요. 오류 내용: {e}")
