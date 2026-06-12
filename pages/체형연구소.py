import streamlit as st
import pandas as pd
import datetime

# 1. 페이지 기본 설정 및 테마
st.set_page_config(
    page_title="FitMate - 정밀 체형 맞춤 비만 예방 커뮤니티",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 세션 상태(Session State) 초기화
if 'posts' not in st.session_state:
    st.session_state['posts'] = [
        {"id": 1, "type": "상체 비만형 (애플형)", "author": "건강최고", "title": "복부 비만 탈출 식단 공유합니다!", "content": "정제 탄수화물 줄이고 식이섬유 늘렸더니 허리둘레가 확실히 줄어드네요. 다들 화이팅!", "date": "2026-06-10", "likes": 5},
        {"id": 2, "type": "하체 비만형 (페어형)", "author": "나트륨아웃", "title": "하체 부종에 좋은 스트레칭 루틴 효과 보신 분?", "content": "폼롤러 매일 15분씩 하니까 다리가 한결 가벼워요. 짠 음식 줄이는 게 핵심인 듯 합니다.", "date": "2026-06-11", "likes": 8},
        {"id": 3, "type": "마른 비만형 (스키니팻)", "author": "근육몬망상", "title": "체중은 정상인데 체지방률이 30%예요 ㅠㅠ", "content": "유산소만 하다가 오늘부터 헬스장 등록하고 단백질 위주로 먹기 시작했습니다. 같이 인증해요!", "date": "2026-06-12", "likes": 3}
    ]

if 'user_bmi_history' not in st.session_state:
    st.session_state['user_bmi_history'] = []

# 3. 사이드바 - 상세 체형 진단 입력 폼
st.sidebar.header("👤 정밀 체형 프로필 설정")

with st.sidebar.form("profile_form"):
    name = st.text_input("닉네임", value="홍길동", max_chars=10)
    gender = st.radio("성별", ["여성", "남성"])
    
    st.markdown("#### **[1] 신체 사이즈**")
    height = st.number_input("키 (cm)", min_value=100.0, max_value=250.0, value=165.0, step=0.1)
    weight = st.number_input("몸무게 (kg)", min_value=30.0, max_value=200.0, value=60.0, step=0.1)
    
    st.markdown("#### **[2] 나의 체형 특징 (상세)**")
    body_fat_look = st.selectbox(
        "살이 찌면 주로 어디가 먼저 찌나요?",
        ["배, 허리, 등 (상체 집중형)", "허벅지, 엉덩이, 종아리 (하체 집중형)", "전체적으로 골고루 찌거나 잘 모르겠음"]
    )
    
    muscle_status = st.radio(
        "본인의 평소 근육량이나 활동량은 어떤가요?",
        ["체중에 비해 몸이 말랑하고 탄력이 없다 (근육 부족형)", "운동을 평소에 조금 하거나 보통이다", "근육이 잘 붙고 골격이 크다"]
    )
    
    body_worry = st.multiselect(
        "가장 집중 예방하고 싶은 부위/증상 (복수 선택)",
        ["내장 지방 (올챙이 배)", "하체 순환 및 부종", "급격한 피로 및 체력 저하", "식탐 및 폭식 습관"],
        default=["내장 지방 (올챙이 배)"]
    )
    
    submit_profile = st.form_submit_button("정밀 체형 진단하기")

# 4. 정밀 체형 분석 로직 함수
def diagnose_detailed_body(bmi, fat_look, muscle, worry):
    # 기본 체형 분류 판단
    if "상체" in fat_look or "내장 지방" in worry:
        b_type = "상체 비만형 (애플형)"
        b_guide = "⚠️ **내장지방 및 성인병 예방이 최우선 과제입니다.**\n\n국물류, 빵, 면류 등 정제 탄수화물과 당류를 엄격히 제한해야 합니다. 허리둘레 감소를 위해 유산소 운동(인클라인 런닝머신, 사이클)과 함께 식후 15분 산책을 필수화하세요."
    elif "하체" in fat_look or "하체 순환" in worry:
        b_type = "하체 비만형 (페어형)"
        b_guide = "⚠️ **하체 순환 저하 및 부종 관리가 핵심입니다.**\n\n체중 자체보다는 짠 음식(나트륨)을 줄이고 칼륨이 풍부한 채소(토마토, 오이 등) 섭취가 중요합니다. 하체 압박을 줄이기 위해 격렬한 하체 웨이트보다는 폼롤러 마사지, 스트레칭, L자 다리 운동을 추천합니다."
    elif bmi < 23.0 and "말랑" in muscle:
        b_type = "마른 비만형 (스키니팻)"
        b_guide = "⚠️ **체중은 정상이지만 근육량이 부족해 대사증후군 위험이 있습니다.**\n\n굶는 다이어트는 절대 금물입니다! 매끼 닭가슴살, 계란, 두부 등 양질의 단백질을 섭취하고, 유산소 운동보다는 스쿼트, 푸쉬업 같은 '근력 운동' 비율을 70% 이상으로 가져가야 기초대사량이 올라갑니다."
    else:
        b_type = "전신 관리형 (균형적 예방)"
        b_guide = "✅ **전반적인 건강 유지 및 생활습관 교정이 필요한 단계입니다.**\n\n규칙적인 삼시 세끼 식사, 충분한 수면(7시간 이상), 일상 속 활동량 늘리기(계단 이용 등)를 통해 비만을 선제적으로 예방하세요."
        
    return b_type, b_guide

# BMI 및 정밀 결과 도출
bmi_value = weight / ((height / 100) ** 2)
body_type, body_guide = diagnose_detailed_body(bmi_value, body_fat_look, muscle_status, body_worry)

if submit_profile:
    st.session_state['user_bmi_history'].append({
        "date": datetime.date.today().strftime("%Y-%m-%d"),
        "weight": weight,
        "bmi": round(bmi_value, 2)
    })
    st.sidebar.success("정밀 진단이 완료되었습니다!")

# 5. 메인 화면 구성
st.title("⚖️ FitMate: 정밀 체형 맞춤 비만 예방 플랫폼")
st.markdown("단순히 몸무게만 보는 다이어트는 끝났습니다. 내 상세 체형 분석 결과에 맞춰 똑똑하게 건강을 지키세요!")

tab1, tab2 = st.tabs(["📊 나의 정밀 분석 & 예방 루틴", "💬 체형별 소통 커뮤니티"])

with tab1:
    st.header("✨ 내 신체 특징 기반 분석 리포트")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="나의 현재 BMI", value=f"{bmi_value:.2f}")
    col2.metric(label="최종 판정 체형", value=body_type)
    col3.metric(label="선택한 집중 고민 영역", value=f"{len(body_worry)}개 부위")
    
    st.markdown("#### 💡 맞춤 처방 가이드라인")
    st.info(body_guide)
    
    # 세부 고민(worry)별 맞춤 추가 팁 제공 (초정밀 개인화 요소)
    if body_worry:
        st.markdown("#### 🔍 나의 고민별 원포인트 예방 팁")
        for item in body_worry:
            if "내장 지방" in item:
                st.warning("**[내장 지방]** 액상과당(콜라, 대용량 아이스티, 믹스커피)은 간에 바로 지방으로 쌓입니다. 물이나 아메리카노로 대체하세요.")
            elif "하체 순환" in item:
                st.warning("**[하체 순환]** 오래 앉아있거나 서 있는 습관이 쥐를 유발합니다. 50분마다 1분씩 까치발 운동을 해주세요.")
            elif "체력 저하" in item:
                st.warning("**[체력 저하]** 아침을 거르면 점심에 폭식하여 혈당이 요동칩니다. 간단한 견과류나 두유라도 챙기세요.")
            elif "폭식 습관" in item:
                st.warning("**[폭식 습관]** 가짜 가고픔에 속지 마세요. 음식을 먹고 싶을 때 물 한 컵을 마시고 10분만 참아보세요.")

    # 체형 맞춤형 투두 리스트
    st.markdown("---")
    st.subheader("📅 오늘 꼭 지켜야 할 맞춤 예방 미션")
    
    if "상체" in body_type:
        st.checkbox("흰 쌀밥 대신 잡곡밥이나 곤약밥으로 탄수화물 줄이기")
        st.checkbox("식후 눕지 않고 가볍게 제자리 걷기 10분")
    elif "하체" in body_type:
        st.checkbox("음식에 소금/간장 덜 찍어 먹기 (저염식 실천)")
        st.checkbox("자기 전 폼롤러나 손으로 종아리 마사지 15분")
    elif "마른" in body_type:
        st.checkbox("간식으로 빵 대신 삶은 달걀이나 단백질 셰이크 먹기")
        st.checkbox("집에서 맨몸 스쿼트 20회 x 3세트 진행하기")
    else:
        st.checkbox("엘리베이터 대신 계단으로 올라가기")
        st.checkbox("물 1.5리터 이상 틈틈이 마시기")

    # 체중 변화 기록 그래프
    if st.session_state['user_bmi_history']:
        st.markdown("---")
        st.subheader("📈 나의 비만 예방 트래킹 (BMI 변화)")
        df_history = pd.DataFrame(st.session_state['user_bmi_history'])
        st.line_chart(df_history.set_index("date")[["bmi"]])

with tab2:
    st.header("💬 체형별 커뮤니티 공간")
    st.markdown("카테고리를 선택해 나와 비슷한 체형과 고민을 가진 사람들의 이야기를 모아보세요.")
    
    filter_options = ["전체보기", "상체 비만형 (애플형)", "하체 비만형 (페어형)", "마른 비만형 (스키니팻)", "전신 관리형 (균형적 예방)"]
    selected_filter = st.selectbox("🎯 카테고리 필터링", filter_options)
    
    with st.expander("📝 내 체형 고민/인증 글 쓰기", expanded=False):
        with st.form("community_post_form", clear_on_submit=True):
            post_type = st.selectbox("내 체형 카테고리", filter_options[1:])
            post_title = st.text_input("제목", placeholder="예: 오늘 식단이랑 하체 운동 인증합니다!")
            post_content = st.text_area("내용", placeholder="공유하고 싶은 예방 습관이나 고민을 적어주세요.")
            
            submit_post = st.form_submit_button("게시글 올리기")
            
            if submit_post:
                if post_title.strip() == "" or post_content.strip() == "":
                    st.error("제목과 내용을 모두 적어주세요.")
                else:
                    new_id = len(st.session_state['posts']) + 1
                    st.session_state['posts'].insert(0, {
                        "id": new_id,
                        "type": post_type,
                        "author": name,
                        "title": post_title,
                        "content": post_content,
                        "date": datetime.date.today().strftime("%Y-%m-%d"),
                        "likes": 0
                    })
                    st.success("글이 성공적으로 등록되었습니다!")
                    st.rerun()

    st.markdown("---")
    
    posts_to_show = st.session_state['posts']
    if selected_filter != "전체보기":
        posts_to_show = [p for p in posts_to_show if p['type'] == selected_filter]
        
    if not posts_to_show:
        st.info("이 카테고리에는 아직 글이 없습니다. 첫 번째 주인공이 되어보세요!")
    else:
        for p in posts_to_show:
            with st.container():
                st.markdown(f"#### **[{p['type']}] {p['title']}**")
                st.markdown(f"✍️ *작성자: {p['author']}* | 📅 *날짜: {p['date']}*")
                st.write(p['content'])
                
                col_like, col_space = st.columns([1, 10])
                if col_like.button(f"❤️ {p['likes']}", key=f"like_{p['id']}"):
                    p['likes'] += 1
                    st.rerun()
                    
                st.markdown("<hr style='margin:10px 0px; border-top: 1px solid #ddd;'/>", unsafe_allow_html=True)
