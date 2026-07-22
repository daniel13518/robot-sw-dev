# 코멘토 로봇 SW 개발 부트캠프 업무 모음

"대기업 로봇 개발자와 함께하는 'SW개발' 실무 성과 만들기 프로그램" 기록입니다.
매주 업무를 Streamlit 앱 페이지로 정리합니다.

## 실행 방법

**1. 저장소 클론**

```bash
git clone https://github.com/daniel13518/robot-sw-dev.git
cd robot-sw-dev
```

**2. 필요한 패키지 설치**

```bash
pip install -r requirements.txt
```

**3. 앱 실행**

```bash
streamlit run Home.py
```

🔗 **바로 실행해보기**: [배포된 앱 링크](https://robot-sw-de.streamlit.app/)

### 1주차 - 로봇 자유도(DOF) 계산기

- 설명: Link의 개수와 Joint 개수, 각 Joint의 자유도를 입력받아 로봇의 자유도를 출력합니다.
- 사용 기술: Python, Streamlit, Kutzbach Formula
- 주요 기능:
  -Kutzbach 공식을 함수로 구현해 로봇 자유도 계산 로직 작성
  Streamlit기반, 웹 GUI로 구현해 브라우저에서 바로 실행 가능하도록 개발
  조인트 개수에 맞춰 입력창이 자동으로 늘어나도록 구성
- 성과:
  - Button으로 값을 즉각적으로 변동하여 결과값을 확인하며 이해도 높임

### 2주차 - 정기구학(Forward Kinematics) 시뮬레이션

- 설명: UR5 기준 6자유도 로봇의 DH 파라미터를 정의하고, 관절 각도에 따른 로봇 팔 끝(end-effector)의 위치를 정기구학으로 계산해 3D로 시각화합니다.
- 사용 기술: Python, NumPy, Matplotlib, Streamlit
  - 수학적 모델: DH 파라미터(Denavit-Hartenberg, Standard), 정기구학(Forward Kinematics)
- 주요 기능:
  - DH 파라미터 기반 변환 행렬(`dh_transform`)과 정기구학(`forward_kinematics`) 함수 구현
  - 각 관절 변환 행렬을 순서대로 곱해 베이스부터 끝단까지 모든 관절 위치를 계산
  - Streamlit 슬라이더 6개로 관절 각도를 조작하면 3D 로봇 팔 그래프에 즉시 반영
  - End-effector의 (x, y, z) 좌표를 수치로 함께 출력
- 성과:
  - 관절 각도 변화가 로봇 팔의 자세와 끝단 위치에 미치는 영향을 직관적으로 확인 가능