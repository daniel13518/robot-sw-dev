import streamlit as st

st.title("DOF 계산기")

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