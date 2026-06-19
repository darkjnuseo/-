import streamlit as st

st.set_page_config(
    page_title="체형별 건강관리 도우미",
    page_icon="💪",
    layout="centered"
)

st.title("💪 체형별 건강관리 도우미")
st.markdown("체형에 맞는 운동 방법과 건강관리 팁을 제공합니다.")

st.divider()

# BMI 계산 함수
def calculate_bmi(height_cm, weight_kg):
    try:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 1)
    except:
        return None

# 운동 추천 데이터
exercise_data = {
    "마른형": {
        "goal": "근육량 증가",
        "exercise": [
            "스쿼트 4세트",
            "벤치프레스 4세트",
            "데드리프트 4세트",
            "풀업 3세트",
            "가벼운 유산소 15분"
        ],
        "tip": "단백질 섭취를 늘리고 충분한 휴식을 취하세요."
    },
    "보통형": {
        "goal": "체력 유지 및 균형 잡힌 몸",
        "exercise": [
            "걷기 또는 조깅 30분",
            "스쿼트 3세트",
            "푸쉬업 3세트",
            "플랭크 1분 × 3회",
            "스트레칭 10분"
        ],
        "tip": "규칙적인 운동과 식습관을 유지하세요."
    },
    "근육형": {
        "goal": "근력 유지 및 체지방 관리",
        "exercise": [
            "웨이트 트레이닝 60분",
            "인터벌 러닝 20분",
            "코어 운동 15분",
            "스트레칭 10분"
        ],
        "tip": "과도한 운동보다 회복에도 집중하세요."
    },
    "비만형": {
        "goal": "체지방 감소",
        "exercise": [
            "빠른 걷기 40분",
            "실내 자전거 30분",
            "스쿼트 15회 × 3세트",
            "플랭크 30초 × 3회",
            "전신 스트레칭"
        ],
        "tip": "무리한 운동보다 꾸준한 유산소 운동이 중요합니다."
    }
}

# 입력 영역
st.subheader("📋 기본 정보 입력")

body_type = st.selectbox(
    "체형을 선택하세요",
    ["마른형", "보통형", "근육형", "비만형"]
)

height = st.number_input(
    "키(cm)",
    min_value=100,
    max_value=250,
    value=170
)

weight = st.number_input(
    "몸무게(kg)",
    min_value=20,
    max_value=250,
    value=65
)

if st.button("운동 추천 받기"):
    try:
        bmi = calculate_bmi(height, weight)

        if bmi is None:
            st.error("BMI 계산 중 오류가 발생했습니다.")
        else:
            data = exercise_data[body_type]

            st.success("추천 결과가 생성되었습니다.")

            st.subheader("📊 건강 정보")
            st.write(f"**BMI:** {bmi}")
            st.write(f"**목표:** {data['goal']}")

            st.subheader("🏋 추천 운동")

            for item in data["exercise"]:
                st.write(f"✅ {item}")

            st.subheader("📝 건강관리 팁")
            st.info(data["tip"])

            st.subheader("📅 주간 운동 계획")

            weekly_plan = {
                "월요일": "근력 운동",
                "화요일": "유산소 운동",
                "수요일": "스트레칭 및 휴식",
                "목요일": "근력 운동",
                "금요일": "유산소 운동",
                "토요일": "전신 운동",
                "일요일": "휴식"
            }

            for day, plan in weekly_plan.items():
                st.write(f"**{day}** : {plan}")

            st.subheader("⚠ 운동 시 주의사항")
            st.warning(
                """
                - 운동 전후 충분한 스트레칭을 하세요.
                - 물을 자주 섭취하세요.
                - 통증이 심하면 운동을 중단하세요.
                - 개인 건강 상태에 따라 운동 강도를 조절하세요.
                """
            )

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

st.divider()
st.caption("건강관리도움 | 체형별 운동 추천 서비스")
