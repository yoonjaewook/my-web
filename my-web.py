import streamlit as st

st.title("🎉 내 첫 번째 웹페이지!")
st.write("안녕하세요! 파이썬으로 만든 나만의 웹사이트입니다.")

# 간단한 상호작용 기능
name = st.text_input("성함이 어떻게 되시나요?")
if name:
  st.success(f"환영합니다, {name}님! 앞으로 멋진 툴을 만들어봐요.")