import streamlit as st
import pandas as pd
import datetime

# 1. 페이지 기본 설정 및 테마 (비만 예방 - 건강하고 신뢰감 주는 녹색/블루 계열 느낌)
st.set_page_config(
    page_title="BodyFit - 체형 맞춤 비만 예방 커뮤니티",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 세션 상태(Session State) 초기화 (데이터 휘발 방지 및 앱 상태 유지)
if 'posts' not in st.session_state:
    # 기본 더미 데이터 생성 (사용자가 처음 들어왔을 때 썰렁하지 않도록)
    st.session_state['posts'] = [
        {"id": 1, "type": "상체 비만형 (애플형)", "author": "건강최고", "title": "복부 비만 탈출 식단 공유합니다!", "content": "정제 탄수화물 줄이고 식이섬유 늘렸더니 허리둘레가 확실히 줄어드네요. 다들 화이팅!", "date": "2026-06-10", "likes": 5},
        {"id": 2, "type": "하체 비만형 (페어형)", "author": "나트륨아웃", "title": "하체 부종에 좋은 스트레칭 루틴 효과 보신 분?", "content": "폼롤러 매일 15분씩 하니까 다리가 한결 가벼워요. 짠 음식 줄이는 게 핵심인 듯 합니다.", "date": "2026-06-11", "likes": 8},
        {"id": 3, "type": "마른 비만형 (스키니팻)", "author": "근육몬망상", "title": "체중은 정상인데 체지방률이 30%예요 ㅠㅠ", "content": "유산소만 하다가 오늘부터 헬스장 등록하고 단백질 위주로 먹기 시작했습니다. 같이 인증해요!", "date": "2026-06-12", "likes": 3}
    ]

if 'user_bmi_history' not in st.session_state:
    st.session_state['user_bmi_history'] = []

# 3. 사이드바 - 내 정보 관리 및 체형 진단
st.sidebar.header("👤 나의 건강 프로필")

with st.sidebar.form("profile_form"):
    name = st.text_input("닉네임", value="홍길동", max_chars=10)
    gender = st.radio("성별", ["여성", "남성"])
    age = st.number_input("나이", min_value=1, max_value=120, value=25)
    
    st.markdown("---")
    height = st.number_input("키 (cm)", min_value=100.0, max_value=250.0, value=165.0, step=0.1)
    weight = st.number_input("몸무게 (kg)", min_value=30.0, max_value=200.0, value=60.0, step=0.1)
    
    submit_profile = st.form_submit_button("체형 진단 및 저장")

# 체형 진단 로직 함수
def diagnose_body_type(bmi, gender):
    if bmi < 18.5:
        return "마른 비만형 (스키니팻 주의 위험군)", "근육량이 부족하고 체지방 비율이 높을 수 있습니다. 유산소보다는 근력 운동과 단백질 섭취가 필수적입니다."
    elif 18.5 <= bmi < 23:
        return "정상 체형 (유지 및 예방 단계)", "현재 좋은 상태입니다! 균형 잡힌 식단과 꾸준한 신체 활동으로 현재 체형을 유지하세요."
    elif 23 <= bmi < 25:
        return "하체 비만형 (페어형 경향)", "하체 순환과 부종 관리가 필요한 단계입니다. 나트륨 섭취를 줄이고 하체 스트레칭 및 폼롤러 마사지를 추천합니다."
    else:
        return "상체 비만형 (애플형 내장지방 위험군)", "복부 및 내장지방 축적으로 인한 성인병 위험이 높아지는 단계입니다. 정제 탄수화물(당류, 빵, 면)을 제한하고 중강도 유산소 운동을 시작하세요."

# BMI 계산 및 진단 실행
bmi_value = weight / ((height / 100) ** 2)
body_type, body_guide = diagnose_body_type(bmi_value, gender)

if submit_profile:
    # 히스토리에 기록 추가
    st.session_state['user_bmi_history'].append({
        "date": datetime.date.today().strftime("%Y-%m-%d"),
        "weight": weight,
        "bmi": round(bmi_value, 2)
    })
    st.sidebar.success("프로필이 업데이트되었습니다!")

# 4. 메인 화면 구성
st.title("⚖️ BodyFit: 체형 맞춤형 비만 예방 플랫폼")
st.markdown("자신의 체형에 맞는 정확한 예방 수칙을 알고, 같은 고민을 가진 사람들과 소통하며 건강한 습관을 만들어보세요!")

# 메인 화면을 2개의 탭으로 분리
tab1, tab2 = st.tabs(["📊 나의 체형 분석 & 예방 가이드", "💬 체형별 소통 커뮤니티"])

with tab1:
    st.header("✨ 실시간 체형 진단 결과")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="나의 BMI 지수", value=f"{bmi_value:.2f}")
    col2.metric(label="분석된 체형 유형", value=body_type.split(" (")[0])
    col3.metric(label="목표 체중 권장량", value=f"{round(21 * ((height/100)**2), 1)} kg (적정)")
    
    # BMI 범주 시각화 안내 가이드
    st.markdown("#### 💡 체형별 맞춤 비만 예방 수칙")
    st.info(f"**[{body_type}]** \n\n {body_guide}")
    
    # 추가 차별화 기능 1: 체형별 투두 리스트 (오늘의 비만 예방 미션)
    st.markdown("---")
    st.subheader("📅 오늘의 비만 예방 투두 리스트")
    st.markdown("체형에 맞춰 제안된 오늘의 작은 습관들을 실천하고 체크해 보세요.")
    
    if "상체" in body_type:
        st.checkbox("점심/저녁 식사 시 밥 양 반으로 줄이기 (탄수화물 제한)")
        st.checkbox("빠르게 걷기 또는 자전거 타기 30분 이상 수행")
        st.checkbox("식후 바로 눕지 않고 10분간 제자리 걷기")
    elif "하체" in body_type:
        st.checkbox("찌개 국물 남기기 (나트륨 배출 및 저염식)")
        st.checkbox("하체 순환을 위한 폼롤러 스트레칭 15분")
        st.checkbox("물 1.5리터 이상 마시기")
    elif "마른" in body_type:
        st.checkbox("매끼 단백질 반찬(닭가슴살, 두부, 달걀 등) 꼭 챙기기")
        st.checkbox("맨몸 스쿼트 3세트 (정확한 자세로 근력 강화)")
        st.checkbox("가공식품 및 액상과당(음료수) 절대 먹지 않기")
    else:
        st.checkbox("가벼운 산책 20분 하기")
        st.checkbox("충분한 수면 취하기 (7시간 이상)")
        st.checkbox("과식하지 않고 알맞게 먹기")

    # 추가 차별화 기능 2: 나의 체중/BMI 변화 기록 그래프 (히스토리 시각화)
    if st.session_state['user_bmi_history']:
        st.markdown("---")
        st.subheader("📈 나의 체중/BMI 변화 추이")
        df_history = pd.DataFrame(st.session_state['user_bmi_history'])
        st.line_chart(df_history.set_index("date")[["bmi"]])


with tab2:
    st.header("💬 체형별 커뮤니티 공간")
    st.markdown("나와 같은 체형 유형을 가진 사람들과 다이어트 꿀팁, 식단, 자극을 공유해 보세요.")
    
    # 필수 기능: 커뮤니티 카테고리 필터링 기능
    filter_options = ["전체보기", "상체 비만형 (애플형)", "하체 비만형 (페어형)", "마른 비만형 (스키니팻)"]
    selected_filter = st.selectbox("🎯 카테고리 필터링", filter_options)
    
    # 게시글 작성 폼 (Expander로 열고 닫을 수 있게 깔끔히 처리)
    with st.expander("📝 새 게시글 작성하기", expanded=False):
        with st.form("community_post_form", clear_on_submit=True):
            post_type = st.selectbox("체형 카테고리 선택", filter_options[1:])
            post_title = st.text_input("제목", placeholder="게시글 제목을 입력하세요.")
            post_content = st.text_area("내용", placeholder="비만 예방을 위한 식단, 운동 인증 또는 고민을 자유롭게 나누어 주세요.")
            
            submit_post = st.form_submit_button("게시하기")
            
            if submit_post:
                if post_title.strip() == "" or post_content.strip() == "":
                    st.error("제목과 내용을 모두 입력해 주세요.")
                else:
                    new_id = len(st.session_state['posts']) + 1
                    new_post = {
                        "id": new_id,
                        "type": post_type,
                        "author": name,
                        "title": post_title,
                        "content": post_content,
                        "date": datetime.date.today().strftime("%Y-%m-%d"),
                        "likes": 0
                    }
                    st.session_state['posts'].insert(0, new_post) # 최신글이 맨 위로 오도록 삽입
                    st.success("게시글이 성공적으로 등록되었습니다!")
                    st.rerun()

    st.markdown("---")
    
    # 게시글 목록 렌더링
    posts_to_show = st.session_state['posts']
    if selected_filter != "전체보기":
        posts_to_show = [p for p in posts_to_show if p['type'] == selected_filter]
        
    if not posts_to_show:
        st.info("해당 카테고리에 등록된 게시글이 없습니다. 첫 번째 이야기를 들려주세요!")
    else:
        for p in posts_to_show:
            with st.container():
                st.markdown(f"#### **[{p['type']}] {p['title']}**")
                st.markdown(f"✍️ *작성자: {p['author']}* | 📅 *날짜: {p['date']}*")
                st.write(p['content'])
                
                # 좋아요 기능 구현 (고유 key값 부여로 충돌 방지)
                col_like, col_space = st.columns([1, 10])
                if col_like.button(f"❤️ {p['likes']}", key=f"like_{p['id']}"):
                    p['likes'] += 1
                    st.rerun()
                    
                st.markdown("<hr style='margin:10px 0px; border-top: 1px solid #ddd;'/>", unsafe_allow_html=True)
