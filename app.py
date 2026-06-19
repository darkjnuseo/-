import streamlit as st
import random

# ==========================================
# 1. 페이지 기본 설정 및 세련된 디자인 테마
# ==========================================
st.set_page_config(
    page_title="FitMeal & Mind - 스마트 다이어트 밸런스",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 커스텀 CSS (주목도를 높이기 위한 카드 디자인 및 컬러 배치)
st.markdown("""
    <style>
    .main-title { font-size: 2.6rem; font-weight: 800; color: #2E7D32; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size: 1.15rem; color: #666666; text-align: center; margin-bottom: 30px; }
    
    /* 눈에 띄는 기능 소개 카드 디자인 */
    .feature-card { padding: 22px; border-radius: 12px; margin-bottom: 18px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 6px solid; }
    .card-green { background-color: #F1F8E9; border-left-color: #7CB342; }
    .card-orange { background-color: #FFF3E0; border-left-color: #FFB74D; }
    .card-blue { background-color: #E3F2FD; border-left-color: #64B5F6; }
    
    .feature-card h4 { margin-top: 0; color: #33691E; font-size: 1.25rem; }
    .card-orange h4 { color: #E65100; }
    .card-blue h4 { color: #0D47A1; }
    
    .chat-bubble { padding: 15px; border-radius: 15px; background-color: #F5F5F5; border-left: 4px solid #9E9E9E; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 2. 사이드바 내비게이션 & 앱 소개
# ==========================================
with st.sidebar:
    st.markdown("# 🥗 FitMeal & Mind")
    st.caption("신체 분석부터 마인드 케어까지 하나의 앱으로")
    
    # Unsplash 웰빙 이미지
    st.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500", use_container_width=True)
    
    st.info("💡 **FitMeal & Mind**는 신체 진단뿐만 아니라 다이어터들이 가장 힘들어하는 **'가짜 식욕(음식 충동)'**을 과학적·심리적으로 이겨내도록 돕는 토탈 케어 서비스입니다.")
    
    st.markdown("---")
    menu = st.selectbox(
        "이동할 화면을 선택하세요:",
        ["✨ 서비스 및 핵심 기능 소개", "📊 1분 신체 진단 & 운동 추천", "🚨 음식 충동 SOS 긴급 상담소"]
    )
    
    st.markdown("---")
    st.caption("© 2026 FitMeal & Mind Co. All rights reserved.")


# ==========================================
# 3. [화면 1] 서비스 및 핵심 기능 소개
# ==========================================
if menu == "✨ 서비스 및 핵심 기능 소개":
    st.markdown("<div class='main-title'>🥗 FitMeal & Mind 프리뷰</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>무작정 굶는 다이어트는 끝났습니다. 신체 데이터와 멘탈을 동시에 관리하세요!</div>", unsafe_allow_html=True)
    
    # 메인 배너 이미지
    st.image("https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=1000", use_container_width=True)
    st.write("")
    
    st.markdown("### ⚡ 우리 앱의 차별화된 3대 핵심 기능")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='feature-card card-green'>
            <h4>📊 1. 다각도 신체정보 제공</h4>
            <p>단순 몸무게 확인이 아닌 키, 나이, 활동량을 결합하여 <b>BMI(비만도)</b>와 하루 숨만 쉬어도 타는 <b>기초대사량(BMR)</b>을 정밀하게 계산합니다.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-card card-blue'>
            <h4>🏃‍♂️ 2. 데이터 기반 운동 추천</h4>
            <p>현재 나의 체중 상태와 활동량 계수를 조합하여, 관절에 무리 없이 체지방을 가장 빠르게 연소시킬 수 있는 <b>맞춤형 운동 루틴</b>을 제안합니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class='feature-card card-orange'>
            <h4>🚨 3. 음식 충동 SOS 상담소</h4>
            <p>참기 힘든 폭식 위험이나 가짜 식욕이 찾아왔을 때, 인공지능형 상담 모듈이 <b>즉각적인 행동 지침과 심리 멘토링</b>을 제공하여 고비를 넘기게 돕습니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("")
    st.success("👉 왼쪽 사이드바 메뉴를 클릭하여 원하는 기능을 직접 체험해 보세요!")


# ==========================================
# 4. [화면 2] 1분 신체 진단 & 맞춤 운동 추천
# ==========================================
elif menu == "📊 1분 신체 진단 & 운동 추천":
    st.markdown("<div class='main-title'>📊 1분 신체 진단 & 운동 추천</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>정보를 입력하시면 다양한 신체분석 정보와 최적의 운동을 매칭해 드립니다.</div>", unsafe_allow_html=True)
    
    with st.form("body_info_form"):
        c1, c2 = st.columns(2)
        with c1:
            gender = st.radio("성별", ["남성", "여성"], horizontal=True)
            age = st.number_input("나이 (세)", min_value=10, max_value=100, value=25)
            height = st.number_input("키 (cm)", min_value=120, max_value=230, value=170)
        with c2:
            weight = st.number_input("현재 몸무게 (kg)", min_value=30, max_value=200, value=65)
            activity = st.selectbox("평소 활동량 격차", ["활동량 적음 (사무직, 좌식 생활)", "보통 (주 1~3회 가벼운 운동)", "활동량 많음 (주 4회 이상 고강도 운동)"])
            
        submit = st.form_submit_button("⚡ 신체 정보 분석 및 운동 추천받기")
        
    if submit:
        try:
            # 신체 정보 연산
            height_m = height / 100
            bmi = weight / (height_m ** 2)
            
            if gender == "남성":
                bmr = 66.47 + (13.75 * weight) + (5 * height) - (6.76 * age)
            else:
                bmr = 655.1 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
                
            st.markdown("### 🎯 1. 나의 신체 정밀 분석 리포트")
            res_c1, res_c2, res_c3 = st.columns(3)
            
            with res_c1:
                st.metric(label="나의 BMI (체질량지수)", value=f"{bmi:.1f}")
                if bmi < 18.5: st.warning("현재 상태: **저체중**")
                elif 18.5 <= bmi < 23: st.success("현재 상태: **정상체중**")
                elif 23 <= bmi < 25: st.warning("현재 상태: **과체중**")
                else: st.error("현재 상태: **비만**")
                
            with res_c2:
                st.metric(label="하루 기초대사량 (BMR)", value=f"{int(bmr):,} kcal")
                st.caption("숨만 쉬어도 소모되는 순수 에너지입니다.")
                
            with res_c3:
                # 적정 체중 가이드 추가 제공 (차별화 요소)
                healthy_weight_min = 18.5 * (height_m ** 2)
                healthy_weight_max = 23 * (height_m ** 2)
                st.metric(label="나의 키 대비 적정 체중 범위", value=f"{int(healthy_weight_min)} ~ {int(healthy_weight_max)} kg")
                
            st.markdown("---")
            
            # [기능] 신체정보를 바탕으로 한 운동 추천
            st.markdown("### 🏃‍♂️ 2. 회원님을 위한 맞춤형 운동 가이드")
            
            if bmi >= 25 or "적음" in activity:
                st.markdown("""
                <div class='feature-card card-blue'>
                    <h4>💪 [초급자 및 관절 보호 루틴] 체지방 감소 스케줄</h4>
                    <ul>
                        <li><b>추천 운동:</b> 경사도 높은 런닝머신 걷기(인클라인 워킹) 35분 또는 실내 자전거 단계 3~4로 40분 유지</li>
                        <li><b>근력 운동:</b> 무릎에 무리가 가지 않는 맨몸 스쿼트 12회 x 3세트, 벽 짚고 푸쉬업 15회 x 3세트</li>
                        <li><b>전문가 한마디:</b> 현재 신체 상태는 과도한 점프나 달리기를 할 경우 무릎 관절에 무리가 올 수 있습니다. 충격이 적은 유산소 위주로 시작해 보세요!</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class='feature-card card-blue'>
                    <h4>🔥 [중·고급자 루틴] 근육량 보존 및 극대화 체지방 연소 스케줄</h4>
                    <ul>
                        <li><b>추천 운동:</b> 천국의 계단(스텝밀) 20분 또는 유산소 인터벌 러닝(속도 6과 11 반복) 25분</li>
                        <li><b>근력 운동:</b> 바벨 스쿼트, 데드리프트, 덤벨 숄더프레스 등 대근육 위주 복합 웨이트 트레이닝 40분</li>
                        <li><b>전문가 한마디:</b> 신체 대사 능력이 우수하므로 근력 운동 후 유산소를 결합했을 때 가장 폭발적인 다이어트 효과를 보실 수 있습니다.</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"데이터 처리 중 오류가 발생했습니다. 값을 올바르게 입력해 주세요. ({e})")


# ==========================================
# 5. [화면 3] 음식 충동 SOS 긴급 상담소 (신규 반영)
# ==========================================
elif menu == "🚨 음식 충동 SOS 긴급 상담소":
    st.markdown("<div class='main-title'>🚨 음식 충동 SOS 긴급 상담소</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>지금 무언가 미치도록 먹고 싶나요? 딱 1분만 이 화면에 집중하고 결정을 내려보세요.</div>", unsafe_allow_html=True)
    
    # 현재 당기는 음식 입력받기
    st.markdown("#### 💬 지금 어떤 음식을 가장 먹고 싶으신가요?")
    c_food = st.text_input("예: 떡볶이, 치킨, 초콜릿, 마라탕 등", placeholder="먹고 싶은 음식을 적어보세요.")
    
    if c_food:
        st.markdown("#### 🧠 당신의 상태를 체크해 보세요 (1가지 선택)")
        state = st.radio(
            "지금 내 기분이나 상태는 어떤가요?",
            [
                "스트레스를 많이 받거나 화가 나요.",
                "지루하고 심심해서 입이 심심해요.",
                "진짜 배에서 꼬르륵 소리가 나고 힘이 없어요."
            ]
        )
        
        if st.button("🚨 멘탈 케어 솔루션 받기"):
            st.markdown("---")
            st.markdown(f"### 💌 [{c_food}] 충동에 대처하는 가이드")
            
            if "꼬르륵" in state:
                st.success(f"💡 현재 충동은 가짜 식욕이 아닌 **'진짜 신체적 굶주림'**일 가능성이 높습니다! 굶는 것은 다이어트의 적입니다. {c_food} 대신 닭가슴살 샐러드, 현미밥, 계란 등 클린한 영양소를 채워주세요.")
            elif "스트레스" in state:
                st.warning(f"⚠️ 뇌가 스트레스를 해소하기 위해 자극적인 <b>{c_food}</b>을 요구하는 **'가짜 식욕(감정적 허기)'** 상태입니다! 지금 먹으면 10분만 행복하고 내일 후회하게 됩니다. 매운 음식 대신 따뜻한 차를 마시거나 10분만 산책을 다녀오세요.")
            else:
                st.info(f"🔍 뇌의 도파민이 일시적으로 심심함을 달래기 위해 <b>{c_food}</b>을 떠올렸습니다! 물 한 컵을 크게 들이켜고 양치를 하거나, 재밌는 영상/게임에 5분만 집중하면 이 충동은 마법처럼 사라집니다.")
                
            # 동기부여 명언 셔플 기능 (재미 요소 제공)
            quotes = [
                "“인생은 살이 쪘을 때와 안 쪘을 때로 나뉜다.”",
                "“먹어봤자 내가 아는 그 맛이다.”",
                "“오늘 먹은 음식은 내일의 몸뚱아리가 된다.”",
                "“힘들지 않다면, 그것은 다이어트가 아니다.”",
                "“지금 참으면 내일 아침 거울 앞이 행복해집니다.”"
            ]
            st.markdown(f"<div class='chat-bubble'><b>🔥 오늘의 동기부여 한마디:</b><br>{random.choice(quotes)}</div>", unsafe_allow_html=True)
