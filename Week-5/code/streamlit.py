import streamlit as st
import numpy as np

st.title("This is the APP for the House Prediction")
st.write("Enter your size")

house_size = st.number_input(
    "House Size in Feet :",
    min_value = 1000,
    max_value = 10000,
    value = 1500,
    step = 100
)

if st.button("Predict"):
    # import numpy as np
    
    mean =2027.95625
    std = 858.2023388082425
    house_size_scale = (house_size - mean )/ std
    price = 103633*house_size_scale + 264469
    st.success( f"Your Price in Square is {price:.2f}") 
    