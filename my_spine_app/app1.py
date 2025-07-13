import streamlit as st
from PIL import Image

st.set_page_config(page_title="척추 질환 안내", layout="wide")
st.title("🦴 척추 부위별 증상 안내 페이지")

st.write("아래 척추 그림에서 증상이 있는 부위를 클릭하거나 버튼을 눌러주세요.")

# 이미지 표시
image = Image.open("spine_image.png")  # 그림은 직접 준비해 주세요
st.image(image, caption="척추 부위별 증상 위치", use_column_width=True)

st.markdown("---")

# 증상 선택 버튼
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/측만증.py", label="📌 측만증")
    st.page_link("pages/아측간판탈출증.py", label="📌 아측 간판 탈출증")
    st.page_link("pages/측추관협착증.py", label="📌 측추관 협착증")

with col2:
    st.page_link("pages/골다공증.py", label="📌 골다공증")
    st.page_link("pages/장요근.py", label="📌 장요근 이상")
    st.page_link("pages/요방형근.py", label="📌 요방형근 이상")
