import streamlit as st

st.set_page_config(page_title="Silver Price Predictor", layout="wide")

# --- CUSTOM CSS (Dark Theme) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
/* ลบคำสั่งซ่อน header ออกแล้ว เพื่อให้ปุ่มเมนูทำงานได้ปกติ */
#MainMenu {visibility: hidden;} footer {visibility: hidden;}
.block-container { padding-top: 2.2rem; padding-bottom: 2.5rem; }
.stApp {
  background: radial-gradient(1200px circle at 10% 0%, rgba(99,102,241,0.12), transparent 45%),
              radial-gradient(900px circle at 90% 10%, rgba(34,197,94,0.10), transparent 45%),
              #0b1220;
  color: #e5e7eb;
}
h1, h2, h3, .stMarkdown { color: #e5e7eb; }
.small-muted { color: #9ca3af; font-size: 0.92rem; }
.card {
  background: rgba(17, 24, 39, 0.72);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 18px 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)

st.title("📈 Silver Price Prediction Project")

st.markdown("""
<div class="card">
  <div style="font-size:1.5rem;font-weight:800; color:white;">ยินดีต้อนรับเข้าสู่โครงงานทำนายราคาแร่เงิน</div>
  <div style="margin-top:10px; line-height:1.6;">
    โปรเจกต์นี้เป็นการนำชุดข้อมูลการซื้อขายแร่เงินในอดีต มาผ่านกระบวนการทำความสะอาดข้อมูล (Data Preparation)<br>
    และนำมาฝึกสอนโมเดลปัญญาประดิษฐ์ 2 รูปแบบ เพื่อทำนายราคาในอนาคต ได้แก่:<br><br>
    <b>1. Machine Learning (Ensemble Model)</b><br>
    <b>2. Deep Learning (Neural Network)</b>
  </div>
  <hr style="border-color: rgba(255,255,255,0.1) !important;">
  <div style="color: #4ade80; font-weight:600;">
    👈 กรุณาเลือกเมนูที่แถบด้านซ้ายมือเพื่อดูรายละเอียดและทดสอบโมเดลครับ
  </div>
</div>
""", unsafe_allow_html=True)