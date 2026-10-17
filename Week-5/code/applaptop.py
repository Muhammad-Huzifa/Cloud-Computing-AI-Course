import streamlit as st

st.title("App for the Price Prediction of Laptops")


st.write(
    "Enter the laptop specifications and click the prediction button."
)
import joblib

model = joblib.load('laptop_price.pkl')

brand = st.selectbox(
    "Select Brand",
    ["Acer" , "Asus" ,"Dell", "HP" , "Lenove" ]
)


processor_speed = st.number_input(
    "Processor Speed (GHz)",
    min_value=1.0,
    max_value=5.0,
    value=3.0,
    step=0.1
)


ram_size = st.selectbox(
    "RAM Size (GB)",
    [4, 8, 16, 32]
)



storage_capacity = st.selectbox(
    "Storage Capacity (GB)",
    [256, 512, 1000]
)

screen_size = st.number_input(
    "Screen Size (inches)",
    min_value=10.0,
    max_value=18.0,
    value=15.6,
    step=0.1
)

weight = st.number_input(
    "Laptop Weight (kg)",
    min_value=1.0,
    max_value=5.0,
    value=2.5,
    step=0.1
)

import pandas as pd
if st.button("Predict Laptop Price"):

    laptop = pd.DataFrame({
        "Brand": [brand],
        "Processor_Speed": [processor_speed],
        "RAM_Size": [ram_size],
        "Storage_Capacity": [storage_capacity],
        "Screen_Size": [screen_size],
        "Weight": [weight]
    })

    predicted_price = model.predict(laptop)[0]

    st.success(
        f"Predicted Laptop Price: {predicted_price:,.2f}"
    )