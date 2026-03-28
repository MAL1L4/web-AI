import streamlit as st

st.set_page_config(page_title="NN Explanation", layout="wide")

st.markdown("""
<style>
/* CSS ตัวเดิม */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: radial-gradient(1200px circle at 10% 0%, rgba(99,102,241,0.12), transparent 45%), radial-gradient(900px circle at 90% 10%, rgba(34,197,94,0.10), transparent 45%), #0b1220; color: #e5e7eb; }
.card { background: rgba(17, 24, 39, 0.72); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 18px 18px; }
h1, h2, h3 { color: #e5e7eb; }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Neural Network — Explanation")

st.markdown("""
<div class="card">
  <div style="font-size:1.1rem;font-weight:900;">Goal</div>
  <div style="color: #9ca3af; margin-top:8px;">
    ประยุกต์ใช้ <b>Deep Learning (Keras/TensorFlow)</b> ในการสร้างสถาปัตยกรรมโครงข่ายประสาทเทียม เพื่อจับรูปแบบที่ซับซ้อน (Non-linear) ของข้อมูลราคาแร่เงิน
  </div>
</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("1) Dataset & Data Preparation")
st.markdown("""
*(ใช้ชุดข้อมูลและผ่านการเตรียมข้อมูลรูปแบบเดียวกับ Machine Learning Model เพื่อให้สามารถเปรียบเทียบประสิทธิภาพกันได้)*
""")

st.subheader("2) Neural Network Architecture (โครงสร้างโมเดล)")
st.markdown("""
โมเดลนี้เป็นการออกแบบโครงสร้างขึ้นเอง (Custom Architecture) แบบ Sequential ประกอบด้วย:
- **Input Layer:** รับค่า Features จำนวน 10 ตัวที่ผ่านการ Scale แล้ว
- **Hidden Layer 1:** Dense Layer จำนวน ... นิวรอน, Activation = 'relu'
- **Hidden Layer 2:** Dense Layer จำนวน ... นิวรอน, Activation = 'relu' (มีการใช้ Dropout ...% ป้องกัน Overfitting)
- **Output Layer:** Dense Layer จำนวน 1 นิวรอน (Linear Activation) สำหรับผลลัพธ์ที่เป็นตัวเลขราคา
""")

st.subheader("3) Model Training (การฝึกสอนโมเดล)")
st.markdown("""
- **Loss Function:** Mean Squared Error (MSE)
- **Optimizer:** Adam (Learning Rate = ...)
- **Epochs:** ... รอบ
""")

st.subheader("4) References (แหล่งอ้างอิง)")
st.markdown("""
- [1] Keras Documentation: https://keras.io/
""")