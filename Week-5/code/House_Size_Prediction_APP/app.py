import streamlit as st

import joblib

model = joblib.load('house_price_model.pkl')
scaler = joblib.load('house_price_scaler.pkl')

st.title("House Price Prediction App")

st.write("Enter the House of the price")

house_size = st.number_input(
    "House of Size in Sq",
    min_value = 1000,
    max_value  = 10000,
    value = 1500,
    step = 100
)
import numpy as np
if st.button("Predict"):
    house_size_scaler = scaler.transform([[house_size]])
    predicted_price = model.predict(house_size_scaler)
    Price = np.round(predicted_price[0] , 2)
    st.success(
        f"Predicted_Price : {Price}"
    )
if st.button("Size"):
    shape = model.coef_
    st.success(
        f"W: {shape}"
    )