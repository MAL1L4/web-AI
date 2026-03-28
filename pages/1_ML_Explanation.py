import streamlit as st
import pandas as pd

st.set_page_config(page_title="ML Explanation", layout="wide")

st.markdown("""
<style>
/* ใส่ CSS ตัวเดิมเพื่อให้ธีมเหมือนกัน */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: radial-gradient(1200px circle at 10% 0%, rgba(99,102,241,0.12), transparent 45%), radial-gradient(900px circle at 90% 10%, rgba(34,197,94,0.10), transparent 45%), #0b1220; color: #e5e7eb; }
.card { background: rgba(17, 24, 39, 0.72); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 18px 18px; }
h1, h2, h3 { color: #e5e7eb; }
</style>
""", unsafe_allow_html=True)

st.title("📖 Machine Learning (Ensemble) — Explanation")

st.markdown("""
<div class="card">
  <div style="font-size:1.1rem;font-weight:900;">Goal</div>
  <div style="color: #9ca3af; margin-top:8px;">
    สร้างโมเดลทำนายราคาแร่เงิน (Regression) โดยใช้เทคนิค <b>Ensemble Learning</b> ที่รวมโมเดล Machine Learning อย่างน้อย 3 ประเภทเข้าด้วยกัน เพื่อลดความคลาดเคลื่อนและเพิ่มความแม่นยำ
  </div>
</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("1) Dataset & Source")
st.markdown("""
- **ชุดข้อมูลที่ 1:** Silver Price Forecast 2026 (โหลดจากเว็บไซต์ Kaggle / Investing.com...)
- **ชุดข้อมูลที่ 2:** Silver Prices Data Historical (โหลดจาก...)
- **รายละเอียด Features หลัก:**
  - `Open`, `High`, `Low`, `Close`: ราคาเปิด สูงสุด ต่ำสุด และปิด ของแต่ละวัน
  - `Volume`: ปริมาณการซื้อขาย
""")

st.subheader("2) Data Preparation (การเตรียมข้อมูล)")
st.markdown("""
ข้อมูลเริ่มต้นมีความไม่สมบูรณ์ (Missing Values) จึงได้ดำเนินการแก้ไขดังนี้:
1. ทำการ Merge ข้อมูล 2 ชุดเข้าด้วยกันโดยใช้ Date เป็น Key
2. จัดการค่าว่าง (Missing Values) ด้วยเทคนิค ... (เช่น Forward Fill, Dropna)
3. สกัดฟีเจอร์วันที่ (Date) ออกเป็น `year`, `month`, `day`
4. ทำการปรับสเกลข้อมูล (Feature Scaling) ด้วย `StandardScaler` เพื่อให้โมเดลเรียนรู้ได้ดีขึ้น
""")

st.subheader("3) Algorithm Theory (ทฤษฎีโมเดล)")
st.markdown("""
โปรเจกต์นี้ใช้เทคนิค **Stacking Ensemble** ประกอบด้วย 3 โมเดลย่อย ได้แก่:
1. **Random Forest Regressor:** ... (เขียนอธิบายสั้นๆ)
2. **Support Vector Regression (SVR):** ... (เขียนอธิบายสั้นๆ)
3. **Linear Regression (หรือตัวที่คุณใช้):** ... (อธิบายสั้นๆ)
""")

st.subheader("4) References (แหล่งอ้างอิง)")
st.markdown("""
- [1] แหล่งที่มาข้อมูล: https://...
- [2] ทฤษฎี Ensemble Learning: https://scikit-learn.org/...
""")