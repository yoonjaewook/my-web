import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정 (모바일 브라우저 최적화)
st.set_page_config(page_title="방학 타이머", page_icon="🎒", layout="centered")

st.title("🎒 채연이 여름방학 타이머")
st.caption("다음 주 목요일 개학까지 남은 시간!")

# 모바일 친화적 반응형 카운트다운 타이머
timer_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  .timer-card {
    background: linear-gradient(135deg, #fff3b0 0%, #ffd166 100%);
    border-radius: 16px;
    padding: 20px 15px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }
  .timer-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #2b2d42;
    margin-bottom: 12px;
  }
  .timer-display {
    background: #ffffff;
    border-radius: 12px;
    padding: 14px 10px;
    font-size: 1.4rem;
    font-weight: 800;
    color: #e63946;
    letter-spacing: -0.5px;
    word-break: keep-all;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
  }
</style>
</head>
<body>
  <div class="timer-card">
    <div class="timer-title">🏖️ 여름방학 종료까지</div>
    <div class="timer-display" id="display">계산 중...</div>
  </div>

  <script>
    const targetDate = new Date("2026-08-20T09:00:00").getTime();

    function updateCountdown() {
      const now = new Date().getTime();
      const remain = targetDate - now;

      if (remain <= 0) {
        document.getElementById("display").innerHTML = "🎉 개학! 신나는 새 학기 시작 🏫";
        return;
      }

      const d = Math.floor(remain / (1000 * 60 * 60 * 24));
      const h = Math.floor((remain % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const m = Math.floor((remain % (1000 * 60 * 60)) / (1000 * 60));
      const s = Math.floor((remain % (1000 * 60)) / 1000);

      document.getElementById("display").innerHTML = 
        d + "일 " + h + "시간 " + m + "분 " + s + "초";
    }

    setInterval(updateCountdown, 1000);
    updateCountdown();
  </script>
</body>
</html>
"""

components.html(timer_html, height=140)

st.info("💡 개학: 2026년 8월 20일(목) 오전 09:00")
