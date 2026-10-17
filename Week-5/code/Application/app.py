import streamlit as st

st.title("House Price Prediction Model")

st.write("The Values should be between 1000 and 15000")
import joblib 
model = joblib.load(r"house_price_model.pkl")
scaler = joblib.load(r"house_price_scale.pkl")

input = st.number_input(
    "Enter Size of the House",
    min_value = 501,
    max_value = 5000,
    value = 1500,
    step = 100    
)
import numpy as np
# w = 103633.77268365
# b = 264469.4033375
# mean = 2027.95625
# std = 858.2023388082425
if st.button("Predict"):
    input_scale = scaler.transform([[input]])
    predict = model.predict(input_scale)
    st.success(f"The square of the Input is {(predict)}")
