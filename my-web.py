import streamlit as st
import streamlit.components.v1 as components

st.title("🎉 내 첫 번째 웹페이지!")
st.write("안녕하세요! 파이썬으로 만든 나만의 웹사이트입니다.")

# --- 아주 큰 실시간 시계 추가 ---
st.markdown("### 🕒 현재 실시간 시간")

clock_html = """
<div style="font-size: 70px; font-weight: bold; color: #ff4b4b; font-family: monospace; text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 15px;" id="clock"></div>
<script>
function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    const timeString = `${hours}:${minutes}:${seconds}`;
    document.getElementById('clock').innerText = timeString;
}
setInterval(updateClock, 1000);
updateClock();
</script>
"""

# HTML 컴포넌트를 웹페이지에 렌더링
components.html(clock_html, height=150)
# --------------------------------

# 간단한 상호작용 기능
name = st.text_input("성함이 어떻게 되시나요?")
if name:
    st.success(f"환영합니다, {name}님! 앞으로 멋진 툴을 만들어봐요.")
