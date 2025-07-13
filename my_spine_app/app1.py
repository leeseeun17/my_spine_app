import streamlit as st
from PIL import Image


st.set_page_config(page_title="척추 질환 안내", layout="wide")
st.title("🦴 척추 질환별 예방 및 강화 스트레칭")

st.write("")

# 이미지 표시
image = Image.open("../spine_image.png")  # 그림은 직접 준비해 주세요
st.image(image, caption="척추 부위별 증상 목록", use_column_width=True)

st.markdown("---")

# 증상 선택 버튼
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/척추측만증.py", label="📌 척추 측만증")
    st.page_link("pages/요추간판 탈출증.py", label="📌 요추간판 탈출증")
    st.page_link("pages/경추간판 탈출증.py", label="📌 경추간판 탈출증")

with col2:
    st.page_link("pages/골다공증.py", label="📌 골다공증")
    st.page_link("pages/장요근.py", label="📌 장요근")
    st.page_link("pages/요방형근.py", label="📌 요방형근")
