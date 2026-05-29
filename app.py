import streamlit as st
import streamlit as st

# 웹 앱 제목 설정
st.title("🇰🇷 재미있는 한국사 퀴즈")
st.write("아래 질문을 읽고 정답을 맞혀보세요!")

# 구분선
st.divider()

# --- 질문 1 ---
st.subheader("Q1. 조선의 제1대 왕으로, 한양을 수도로 정한 인물은 누구일까요?")
# 사용자 입력 받기 (공백 제거)
answer1 = st.text_input("1번 정답을 입력하세요:", key="q1").strip()

if st.button("1번 정답 확인"):
    if answer1 == "태조 이성계" or answer1 == "이성계" or answer1 == "태조":
        st.success("정답입니다! 🎉 (태조 이성계)")
    elif answer1 == "":
        st.warning("정답을 입력해주세요!")
    else:
        st.error("틀렸습니다. 다시 한번 생각해보세요! 🤔")

st.divider()

# --- 질문 2 ---
st.subheader("Q2. 1592년 임진왜란 때 한산도 대첩, 명량 대첩 등을 승리로 이끈 조선의 장군은?")
answer2 = st.text_input("2번 정답을 입력하세요:", key="q2").strip()

if st.button("2번 정답 확인"):
    if answer2 == "이순신" or answer2 == "이순신 장군":
        st.success("정답입니다! 🚢 (충무공 이순신)")
    elif answer2 == "":
        st.warning("정답을 입력해주세요!")
    else:
        st.error("틀렸습니다. 다시 한번 생각해보세요! 🤔")

st.divider()

# --- 질문 3 ---
st.subheader("Q3. 1919년 3월 1일 만세 운동을 주도한 독립운동가로, 아우내 장터에서 만세 시위를 벌인 인물은?")
answer3 = st.text_input("3번 정답을 입력하세요:", key="q3").strip()

if st.button("3번 정답 확인"):
    if answer3 == "유관순" or answer3 == "유관순 열사":
        st.success("정답입니다! 🇰🇷 (유관순 열사)")
    elif answer3 == "":
        st.warning("정답을 입력해주세요!")
    else:
        st.error("틀렸습니다. 다시 한번 생각해보세요! 🤔")
