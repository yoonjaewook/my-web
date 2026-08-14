import streamlit as st
import streamlit.components.v1 as components

st.title("🎒 채연이를 위한 여름방학 카운트다운 ⏰")
st.write("다음 주 목요일 개학까지 남은 시간을 실시간으로 확인해보세요!")

timer_html = """
<div style="text-align: center; font-family: sans-serif; background: #ffeaa7; padding: 25px; border-radius: 15px;">
    <h2 style="color: #2d3436; margin-bottom: 15px;">🏖️ 여름방학 종료까지 남은 시간</h2>
    <div id="display" style="font-size: 32px; font-weight: bold; color: #d63031; background: white; padding: 15px; border-radius: 10px; display: inline-block;">
        계산 중...
    </div>
</div>

<script>
const targetDate = new Date("2026-08-20T09:00:00").getTime();

function updateCountdown() {
    const now = new Date().getTime();
    const remain = targetDate - now;

    if (remain <= 0) {
        document.getElementById("display").innerHTML = "🎉 개학을 축하합니다! 새로운 학기 시작!";
        return;
    }

    const d = Math.floor(remain / (1000 * 60 * 60 * 24));
    const h = Math.floor((remain % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const m = Math.floor((remain % (1000 * 60 * 60)) / (1000 * 60));
    const s = Math.floor((remain % (1000 * 60)) / 1000);

    document.getElementById("display").innerHTML = d + "일 " + h + "시간 " + m + "분 " + s + "초 남음";
}

setInterval(updateCountdown, 1000);
updateCountdown();
</script>
"""

components.html(timer_html, height=200)

st.info("💡 개학 시각: 2026년 8월 20일(목) 오전 09:00 기준")
