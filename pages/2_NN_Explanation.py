import streamlit as st

st.set_page_config(page_title="NN Explanation", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp {
    background: radial-gradient(1200px circle at 90% 10%, rgba(34,197,94,0.10), transparent 45%),
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
h2 { color: #6366f1; border-bottom: 2px solid #6366f1; padding-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Neural Network Model Details")

st.markdown("""
<div class="card">
    <h2>1. โครงสร้างโมเดล (Model Topology)</h2>
    <p>เราเลือกใช้โครงสร้างแบบ <b>Multi-Layer Perceptron (MLP)</b> ซึ่งเป็นพื้นฐานของ Deep Learning 
    โดยมีการจัดวาง Layer ดังนี้:</p>
    <ul>
        <li><b>Input Layer:</b> รับค่าปัจจัยทางเศรษฐกิจ</li>
        <li><b>Hidden Layers:</b> ใช้ Dense Layer พร้อมฟังก์ชันกระตุ้น (Activation Function) แบบ <b>ReLU</b></li>
        <li><b>Output Layer:</b> ทำนายราคา (Regression) โดยใช้ Linear Activation</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# โชว์สูตร ReLU แบบวิชาการ
st.write("### ReLU Activation Function:")
st.latex(r"f(x) = \max(0, x)")

st.markdown("""
<div class="card">
    <h2>2. การวัดผลประสิทธิภาพ (Evaluation)</h2>
    <p>ใช้ค่า <b>Mean Squared Error (MSE)</b> เป็นเกณฑ์หลักในการวัดค่าความผิดพลาด:</p>
</div>
""", unsafe_allow_html=True)

# โชว์สูตร MSE
st.latex(r"MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2")

st.markdown("""
<div class="card">
    <h2>3. แหล่งอ้างอิง (References)</h2>
    <ul>
        <li><b>Framework:</b> พัฒนาโดยใช้ TensorFlow และ Keras Library</li>
        <li><b>Optimizer:</b> เลือกใช้ Adam Optimizer เพื่อประสิทธิภาพสูงสุดในการ Convergence</li>
        <li><b>Citation:</b> อ้างอิงโครงสร้างประสาทเทียมจากตำรา Machine Learning โดยคณะวิศวกรรมศาสตร์</li>
    </ul>
</div>
""", unsafe_allow_html=True)