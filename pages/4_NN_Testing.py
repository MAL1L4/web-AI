import streamlit as st
import pandas as pd
import joblib
import keras
from datetime import datetime

st.set_page_config(page_title="NN Testing", layout="wide")

st.markdown("""
<style>
/* CSS ตัวเดิม */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: radial-gradient(1200px circle at 10% 0%, rgba(99,102,241,0.12), transparent 45%), radial-gradient(900px circle at 90% 10%, rgba(34,197,94,0.10), transparent 45%), #0b1220; color: #e5e7eb; }
.card { background: rgba(17, 24, 39, 0.72); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 18px 18px; }
div.stButton > button { background-color: #22c55e; color: white; border-radius: 8px; border: none; padding: 0.5rem 1.5rem; font-weight: 600;}
div.stButton > button:hover { background-color: #16a34a; }
[data-testid="stSidebar"] { background-color: rgba(17, 24, 39, 0.95); }
h1, h2, h3 { color: #e5e7eb; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_nn_assets():
    scaler = joblib.load('models/silver_scaler.pkl')
    nn_model = keras.models.load_model('models/silver_nn_model.keras')
    return scaler, nn_model

try:
    scaler, nn_model = load_nn_assets()
except Exception as e:
    st.error(f"Error loading models: {e}")

st.title("🚀 Neural Network Testing")
st.markdown("ทดสอบการทำนายราคาด้วย **Deep Learning (Keras)**")

# --- SIDEBAR INPUTS ---
st.sidebar.header("Input Features")
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
        
    data = {'close': close, 'high': high, 'low': low, 'open': open_price, 'volume': volume,
            'lower_bound': lower_b, 'upper_bound': upper_b, 'year': date.year, 'month': date.month, 'day': date.day}
    return pd.DataFrame([data])

input_df = user_input_features()
st.dataframe(input_df, use_container_width=True)

if st.button("🚀 Run NN Prediction"):
    input_scaled = scaler.transform(input_df)
    pred_nn = nn_model.predict(input_scaled)
    
    st.markdown(f"""
    <div class="card" style="text-align: center; border-color: rgba(34,197,94,0.5); max-width: 400px; margin: 20px auto;">
        <div style="color: #9ca3af;">Predicted Price (Neural Network)</div>
        <div style="font-size:2.5rem; font-weight:800; color:#4ade80;">${pred_nn[0][0]:.4f}</div>
    </div>
    """, unsafe_allow_html=True)