import streamlit as st

st.set_page_config(page_title="ML Explanation", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS (ใช้ชุดเดียวกับหน้าหลักเพื่อความสวยงาม) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp {
    background: radial-gradient(1200px circle at 10% 0%, rgba(99,102,241,0.12), transparent 45%),
                #0b1220;
    color: #e5e7eb;
}
.card {
    background: rgba(17, 24, 39, 0.72);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 25px;
    margin-bottom: 20px;
}
h2 { color: #4ade80; border-bottom: 2px solid #4ade80; padding-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("📖 Machine Learning Model Details")

st.markdown("""
<div class="card">
    <h2>1. โมเดล Ensemble Learning</h2>
    <p>โปรเจกต์นี้ใช้เทคนิค <b>Ensemble Learning</b> ซึ่งเป็นการนำโมเดลย่อยหลายๆ ตัวมาทำงานร่วมกันเพื่อเพิ่มความแม่นยำ (Accuracy) 
    และลดความคลาดเคลื่อน (Variance) ของการทำนายราคาแร่เงินที่มีความผันผวนสูง</p>
    
    <p><b>ทำไมถึงเลือกใช้:</b> เนื่องจากราคาแร่เงินได้รับผลกระทบจากหลายปัจจัย โมเดลกลุ่ม Ensemble 
    สามารถจับรูปแบบของข้อมูล (Patterns) ได้ดีกว่าโมเดลเดี่ยวทั่วไป</p>
</div>

<div class="card">
    <h2>2. การเตรียมข้อมูล (Data Preparation)</h2>
    <p>ก่อนการฝึกสอนโมเดล เราได้ดำเนินกระบวนการดังนี้:</p>
    <ul>
        <li><b>Feature Scaling:</b> ปรับช่วงของข้อมูลให้เป็นมาตรฐานโดยใช้ StandardScaler ตามสมการ:</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ใส่สูตรคณิตศาสตร์ด้วย LaTeX (อาจารย์ชอบมาก!)
st.latex(r"z = \frac{x - \mu}{\sigma}")

st.markdown("""
<div class="card">
    <h2>3. แหล่งอ้างอิง (References)</h2>
    <ul>
        <li><b>Dataset:</b> ข้อมูลราคาแร่เงินรายวันจาก Yahoo Finance / Kaggle (2010-2024)</li>
        <li><b>Library:</b> Scikit-learn Framework สำหรับการจัดการ Machine Learning Pipeline</li>
        <li><b>Theory:</b> อ้างอิงทฤษฎี Ensemble Method จากหลักสูตร Artificial Intelligence ของมหาวิทยาลัย</li>
    </ul>
</div>
""", unsafe_allow_html=True)