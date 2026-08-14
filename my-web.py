import streamlit as st
import streamlit.components.v1 as components

st.title("🎒 여름방학 카운트다운 타이머 ⏰")
st.write("다음 주 목요일 개학까지 남은 시간을 실시간으로 확인해보세요!")

# 다음 주 목요일(2026-08-20 09:00:00) 기준 실시간 카운트다운
countdown_html = """
<div style="text-align: center; font-family: 'Arial', sans-serif; background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%); padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
    <h2 style="color: #333; margin-bottom: 20px; font-size: 26px;">✨ 여름방학 종료까지 남은 시간 ✨</h2>
    <div id="timer" style="font-size: 38px; font-weight: bold; color: #d63031; background: white; padding: 20px; border-radius: 15px; display: inline-block;">
        계산 중...
    </div>
</div>

<script>
// 목표 시각: 2026년 8월 20일 오전 9시
const countDownDate = new Date("2026-08-20T09:00:00+09:00").getTime();

function updateTimer() {
    const now = new Date().getTime();
    const distance = countDownDate - now;

    if (distance < 0) {
        document.getElementById("timer").innerHTML = "🎉 드디어 개학! 활기찬 새 학기 시작! 🏫";
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor아까 코드가 중간에 끊겨서 따옴표 세 개(`"""`)가 닫히지 않아 문법 오류(`SyntaxError: unterminated triple-quoted string literal`)가 발생했습니다! 

불필요한 외부 코드나 끊김 없이 깔끔하게 바로 작동하는 **완성된 전체 코드**입니다. 

아래 코드를 복사해서 깃허브의 `my-web.py` 내용에 통째로 붙여넣고 저장(`Commit changes`)해 보세요.

---

### 📝 바로 적용할 전체 코드 (`my-web.py`)

```python
import streamlit as st
import streamlit.components.v1 as components

st.title("🎒 여름방학 카운트다운 타이머 ⏰")
st.write("개학(다음 주 목요일)까지 남은 시간을 실시간으로 계산합니다!")

# 다음 주 목요일(2026년 8월 20일 오전 9시) 기준 카운트다운 컴포넌트
timer_code = """
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

components.html(timer_code, height=200)

st.info("💡 개학 시각: 2026년 8월 20일 오전 09:00 기준")
