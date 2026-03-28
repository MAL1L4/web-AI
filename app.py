import streamlit as st
import pandas as pd
import numpy as np
import joblib
import keras
from datetime import datetime

# --- SET PAGE CONFIG ---
st.set_page_config(page_title="Silver Price Predictor", layout="wide")

# --- CUSTOM CSS (Dark Theme & Styling) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
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
hr { border-color: rgba(255,255,255,0.10) !important; }

/* ปรับสีตัวอักษรใน sidebar ให้เข้ากับธีมมืด */
[data-testid="stSidebar"] {
    background-color: rgba(17, 24, 39, 0.95);
}
[data-testid="stSidebar"] .css-17lntkn { color: #e5e7eb; }

/* ปรับปุ่ม Predict */
div.stButton > button {
    background-color: #4f46e5;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5rem 1.5rem;
    font-weight: 600;
    transition: all 0.3s;
}
div.stButton > button:hover {
    background-color: #4338ca;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
}
</style>
""", unsafe_allow_html=True)

# --- LOAD MODELS & SCALER ---
@st.cache_resource
def load_assets():
    scaler = joblib.load('models/silver_scaler.pkl')
    ensemble_model = joblib.load('models/silver_ensemble_model.pkl')
    nn_model = keras.models.load_model('models/silver_nn_model.keras')
    return scaler, ensemble_model, nn_model

try:
    scaler, ensemble_model, nn_model = load_assets()
    # ไม่แสดง st.success เพื่อให้หน้าจอคลีนขึ้นตามสไตล์ธีมใหม่
except Exception as e:
    st.error(f"Error loading models: {e}")

# --- HEADER & GOAL CARD ---
st.title("📈 Silver Price Prediction")

st.markdown("""
<div class="card">
  <div style="font-size:1.1rem;font-weight:900;">Project Goal</div>
  <div class="small-muted" style="margin-top:8px;">
    ระบบทำนาย <b>"ราคาแร่เงิน (Silver Price)"</b> จากข้อมูลการซื้อขายในอดีต (Regression Task)<br>
    โดยผสานพลังการทำนายจาก 2 โมเดลหลัก ได้แก่ <b>Ensemble Model (RF + SVR)</b> และ <b>Neural Network (Keras)</b>
  </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- SIDEBAR INPUTS ---
st.sidebar.header("⚙️ Input Features")

def user_input_features():
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        open_price = st.number_input("Open", value=25.0)
        high = st.number_input("High", value=26.0)
        low = st.number_input("Low", value=24.0)
        close = st.number_input("Close (Prev)", value=25.5)
        volume = st.number_input("Volume", value=100000)
        
    with col2:
        lower_b = st.number_input("Lower Bound", value=23.0)
        upper_b = st.number_input("Upper Bound", value=27.0)
        date = st.date_input("Prediction Date", datetime.now())
        
    data = {
        'close': close,
        'high': high,
        'low': low,
        'open': open_price,
        'volume': volume,
        'lower_bound': lower_b,
        'upper_bound': upper_b,
        'year': date.year,
        'month': date.month,
        'day': date.day
    }
    return pd.DataFrame([data])

input_df = user_input_features()

# --- SECTION 1: INPUT SUMMARY ---
st.subheader("1) Input Summary")
st.markdown("<div class='small-muted'>ข้อมูลที่คุณกรอกจะถูกนำมาจัดรูปแแบบ (DataFrame) เพื่อเตรียมเข้าสู่ขั้นตอน Scaling</div>", unsafe_allow_html=True)
st.dataframe(input_df, use_container_width=True)

st.divider()

# --- SECTION 2: PREDICTION LOGIC ---
st.subheader("2) Model Predictions")

if st.button("🚀 Run Prediction"):
    with st.spinner("กำลังคำนวณ..."):
        # 1. Scale ข้อมูล
        input_scaled = scaler.transform(input_df)
        
        # 2. ทำนายผล
        pred_ensemble = ensemble_model.predict(input_scaled)
        pred_nn = nn_model.predict(input_scaled)
        avg_pred = (pred_ensemble[0] + pred_nn[0][0]) / 2
        
        # --- DISPLAY RESULTS IN CARDS ---
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.markdown(f"""
            <div class="card" style="text-align: center; border-color: rgba(99,102,241,0.5);">
              <div class="small-muted">Ensemble Model</div>
              <div style="font-size:2rem; font-weight:800; color:#818cf8;">${pred_ensemble[0]:.4f}</div>
            </div>
            """, unsafe_allow_html=True)

        with col_res2:
            st.markdown(f"""
            <div class="card" style="text-align: center; border-color: rgba(34,197,94,0.5);">
              <div class="small-muted">Neural Network</div>
              <div style="font-size:2rem; font-weight:800; color:#4ade80;">${pred_nn[0][0]:.4f}</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col_res3:
            st.markdown(f"""
            <div class="card" style="text-align: center; background: rgba(255, 255, 255, 0.05); border-color: rgba(255,255,255,0.3);">
              <div class="small-muted">Average Prediction</div>
              <div style="font-size:2rem; font-weight:800; color:#ffffff;">${avg_pred:.4f}</div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.caption("⚠️ **Note:** ข้อมูลนี้เป็นเพียงการทำนายจากโมเดลทางสถิติเท่านั้น ไม่ใช่คำแนะนำทางการเงิน")