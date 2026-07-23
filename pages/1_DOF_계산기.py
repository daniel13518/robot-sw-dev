import streamlit as st

st.title("DOF 계산기")

# ---- 이론 정리 (접이식) ----
with st.expander("📖 이론 정리 — 자유도(DOF) & Kutzbach 공식"):
    st.markdown(
        """
**자유도(DOF, Degrees of Freedom)** 는 로봇이 독립적으로 움직일 수 있는 방향의 수이다.
자유도가 클수록 더 다양한 자세를 만들 수 있다.

**Kutzbach 공식** 으로 링크·관절 개수와 각 관절의 자유도만 알면
로봇 전체의 자유도를 계산할 수 있다.

`F = m × (n − j − 1) + Σfᵢ`

- `m` : 공간의 자유도 → 3D 공간은 6, 2D 평면은 3
- `n` : 링크(link) 수 → 고정된 바닥(base) 링크도 포함해서 센다
- `j` : 관절(joint) 수
- `fᵢ` : 각 관절의 자유도 → 일반 회전 모터는 1

**직관**: 자유롭게 움직이던 링크들의 자유도에서, 관절로 서로 연결되며 묶이는
자유도를 빼고, 각 관절이 실제로 허용하는 움직임(Σfᵢ)만큼 다시 더한 값이다.

**참고**: 링크는 고정된 바닥까지 세어야 한다. 예를 들어 관절 하나로 이어진 팔은
링크 2개(바닥 + 팔), 관절 1개다.
"""
    )


def cal_DOF(link, joint, joint_DOF_list):
    m = 6  # 3D 공간 가정
    result_joint_DOF = 0
    for i in range(len(joint_DOF_list)):
        result_joint_DOF += joint_DOF_list[i]
    return m * (link - joint - 1) + result_joint_DOF

link = st.number_input("링크의 개수", min_value=0, step=1)
joint = st.number_input("조인트(관절)의 개수", min_value=0, step=1)

joint_dof_list = []
for i in range(int(joint)):
    dof = st.number_input(f"{i+1}번 관절의 자유도", min_value=0, step=1, key=f"joint_{i}")
    joint_dof_list.append(dof)

if st.button("계산하기"):
    result = cal_DOF(int(link), int(joint), joint_dof_list)
    st.success(f"계산된 자유도: {result}")