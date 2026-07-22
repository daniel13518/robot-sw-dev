import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("정기구학 시뮬레이션 (6DOF, 6자유도)")

# 과제에 제시되어있는 DH 파라미터 고정값
a = np.array([0, -0.425, -0.392, 0, 0, 0]) #(각 링크기준 x축 방향으로 얼마나 떨어져있는가)
d = np.array([0.089, 0, 0, 0.109, 0.095, 0.082]) #(각 링크 기준 z축 방향으로 얼마나 떨어져있는가)
alpha = np.array([np.pi / 2, 0, 0, np.pi / 2, -np.pi / 2, 0])


def dh_transform(theta, d, a, alpha):
    """각 관절 기준의 DH 파라미터 기반 변환 행렬을 산출해 반환"""
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha),  np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta),  np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0,              np.sin(alpha),                   np.cos(alpha),                  d],
        [0,              0,                                  0,                             1],
    ])


def forward_kinematics(theta_list, a, d, alpha):
    """각 관절의 변환 행렬을 순서대로 곱해 링크 끝단 위치들을 구한다"""
    T = np.eye(4) #관절 위치 저장 위한 4x4 단위 행렬 생성
    positions = [T[:3, 3]]  # 행 0부터 2까지의 3번째 열의 값을 저장
    for i in range(len(theta_list)): #1부터 5까지 각 관절마다 반복
        T_i = dh_transform(theta_list[i], d[i], a[i], alpha[i])
        T = T @ T_i # !! i번째 이전까지 모든 행렬곱값에 연산
        positions.append(T[:3, 3]) #관심있는건 0부터 3의 3번째 열값(px,py,pz) 그래서 여기만 append
    return T, positions


st.subheader("관절 각도 (theta)")
theta_deg = []
cols = st.columns(6)
for i in range(6):
    with cols[i]:
        val = st.slider(f"link {i + 1}", min_value=-180, max_value=180, value=0, step=1, key=f"theta_{i}")
        theta_deg.append(val)

theta_rad = np.radians(theta_deg)
T_end, positions = forward_kinematics(theta_rad, a, d, alpha)
positions = np.array(positions)
end_effector = T_end[:3, 3]

st.subheader("로봇 팔 끝(End-Effector)의 위치")
st.write(f"X = {end_effector[0]:.4f} m, Y = {end_effector[1]:.4f} m, Z = {end_effector[2]:.4f} m")

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], "o-", linewidth=3, markersize=6, color="tab:blue")
ax.scatter(*end_effector, color="red", s=80, label="End-Effector")

limit = 1.5
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title(" ")
ax.legend()

st.pyplot(fig)
