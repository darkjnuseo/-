import streamlit as st

# 1. 페이지 기본 설정 및 디자인 (Emoji 활용)
st.set_page_config(
    page_title="FitMeal & Move - 나만의 다이어트 가이드",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 간단한 CSS 스타일링 (unsafe_allow_html=True 사용 필요)
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; font-weight: bold; color: #2E7D32; text-align: center; margin-bottom: 10px; }
    .sub-title { font-size: 1.2rem; color: #555555; text-align: center; margin-bottom: 30px; }
    .feature-box { padding: 20px; border-radius: 10px; background-color: #F1F8E9; border-left: 5px solid #7CB342; margin-bottom: 15px; }
    .recommend-box { padding: 15px; border-radius: 8px; background-color: #FFFFFF; border: 1px solid #E0E0E0; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 사이드바: 앱 소개 및 바로가기
# ==========================================
st.sidebar.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500", use_container_width=True)
st.sidebar.title("🥗 FitMeal & Move")
st.sidebar.info("당신의 체형과 목표에 딱 맞는 운동과 식단을 제안하는 스마트 다이어트 솔루션입니다.")

# 메뉴 선택
menu = st.sidebar.radio(
    "원하는 메뉴를 선택하세요:",
    ["✨ 앱 주요 기능 소개", "📊 1분 체형 진단 & 맞춤 제안"]
)

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 FitMeal & Move Co. All rights reserved.")


# ==========================================
# 메뉴 1: 앱 주요 기능 소개
# ==========================================
if menu == "✨ 앱 주요 기능 소개":
    st.markdown("<div class='main-title'>🥗 FitMeal & Move를 소개합니다!</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>체중 감량, 더 이상 헤매지 마세요. 과학적인 분석으로 시작하세요.</div>", unsafe_allow_html=True)
    
    # 대표 이미지 (Unsplash 헬스/식단 관련 이미지)
    st.image("https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=1000", use_container_width=True, caption="건강한 삶을 위한 완벽한 밸런스")
    
    st.markdown("### 💡 주요 핵심 기능")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='feature-box'>
            <h4>📊 1
