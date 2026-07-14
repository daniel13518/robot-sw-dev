# 코멘토 로봇 SW 개발 부트캠프 업무 모음

"대기업 로봇 개발자와 함께하는 'SW개발' 실무 성과 만들기 프로그램" 기록입니다.
매주 업무를 Streamlit 앱 페이지로 정리합니다.

## 실행 방법

1. 저장소 클론
\`\`\`bash
git clone https://github.com/daniel13518/robot-sw-dev.git
cd robot-sw-dev
\`\`\`

2. 필요한 패키지 설치
\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. 앱 실행
\`\`\`bash
streamlit run Home.py
\`\`\`
🔗 **바로 실행해보기**: [배포된 앱 링크](https://robot-sw-de.streamlit.app/)
## 주차별 과제

### 1주차 - 로봇 자유도(DOF) 계산기

- 설명: Link의 개수와 Joint 개수, 각 Joint의 자유도를 입력받아 로봇의 자유도를 출력합니다.
- 사용 기술: Python, Streamlit, Kutzbach Formula
- 주요 기능:
  -Kutzbach 공식을 함수로 구현해 로봇 자유도 계산 로직 작성
  Streamlit기반, 웹 GUI로 구현해 브라우저에서 바로 실행 가능하도록 개발
  조인트 개수에 맞춰 입력창이 자동으로 늘어나도록 구성
- 성과:
  - Button으로 값을 즉각적으로 변동하여 결과값을 확인하며 이해도 높임