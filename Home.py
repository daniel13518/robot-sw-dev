import streamlit as st

# 페이지 기본 설정 (반드시 다른 st 명령보다 먼저 와야 함)
st.set_page_config(
    page_title="로봇 SW 개발 부트캠프",
    page_icon="🤖",
    layout="wide",
)

# ---- 헤더 ----
st.title("🤖 코멘토 로봇 SW 개발 부트캠프")
st.markdown(
    "**대기업 로봇 개발자와 함께하는 'SW 개발' 실무 성과 만들기 프로그램** 기록입니다.  \n"
    "매주 진행한 업무를 Streamlit 웹 페이지로 구현합니다."
)
st.caption("📅 진행 기간: 2026.07.10 ~ 2026.08.10")

st.divider()

# ---- 주차별 업무 카드 ----
st.subheader("📚 주차별 업무")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 1주차 · 로봇 자유도(DOF) 계산기")
        st.write(
            "Kutzbach 공식으로 링크·관절 수와 각 관절의 자유도를 입력받아 "
            "로봇 전체의 자유도(DOF)를 계산합니다."
        )
        st.caption("사용 기술: Python · Streamlit · Kutzbach Formula")
        st.page_link("pages/1_DOF_계산기.py", label="바로가기", icon="➡️")

with col2:
    with st.container(border=True):
        st.markdown("### 2주차 · 정기구학(FK) 시뮬레이션")
        st.write(
            "6자유도 로봇의 DH 파라미터로 정기구학을 계산하고, "
            "관절 각도에 따른 팔 끝(end-effector) 위치를 3D로 시각화합니다."
        )
        st.caption("사용 기술: Python · NumPy · Matplotlib · Streamlit")
        st.page_link("pages/2_FK_시뮬레이션.py", label="바로가기", icon="➡️")

st.divider()

# ---- 푸터 ----
st.markdown(
    "🔗 **GitHub**: [daniel13518/robot-sw-dev](https://github.com/daniel13518/robot-sw-dev)"
)
