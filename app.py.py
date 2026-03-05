import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("triage_model.pkl")

# Page layout
st.set_page_config(page_title="SmartTriage-Ug", layout="centered")

st.title("🩺 SmartTriage-Ug")
st.subheader("AI-Powered Community Patient Triage System")

st.markdown("Enter patient vital signs below to estimate urgency level.")

# Inputs
hr = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200)
spo2 = st.number_input("SpO₂ (%)", min_value=50, max_value=100)
temp = st.number_input("Temperature (°C)", min_value=30.0, max_value=42.0)

# Prediction
if st.button("Analyze Patient"):

    input_data = np.array([[hr, spo2, temp]])
    prediction = str(model.predict(input_data)[0])

    st.subheader("Triage Result")

    if prediction == "Critical":
        st.error(f"Urgency Level: {prediction} 🔴 Immediate attention required")

    elif prediction == "Medium":
        st.warning(f"Urgency Level: {prediction} 🟡 Monitor patient")

    else:
        st.success(f"Urgency Level: {prediction} 🟢 Stable") 