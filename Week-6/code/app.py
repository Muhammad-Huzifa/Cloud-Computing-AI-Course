import streamlit as st


st.title("Laptop_Price_Predction")
import joblib
model  = joblib.load(r'C:\Users\Muhammad Huzifa\Desktop\AI_Course_Huawei\Week-6\code\multiple_linear_regression.pkl')


brand = st.selectbox("Please Select the Brand"
    , ['Asus', 'Acer', 'Lenovo', 'HP', 'Dell']

)

processor = float(st.number_input(
    "Please enter the detials of Processor",
    max_value = 3.9985343144266654,
    min_value = 1.511580057511507,
    value = 2.0,
    step = 0.1
))

ram  =st.selectbox(
    "Please enter the Size  of RAM in GB",
    [4,   8 ,16, 32]
    
    )


storage = st.selectbox(
    "PLease enter the size of Storage in GB",
    [ 256,512, 1000]
)

screen  = st.number_input(
    "Enter the size of the Screen in Inch",
    max_value = 17,
    min_value = 12,
    value = 12,
    step = 1
)

weight = st.number_input(
    "Please enter the weight of Laptop",
    max_value = 5,
    min_value  = 2,
    value = 2,
    step = 1
)

import pandas as pd
if st.button("Predict Price"):
    input = pd.DataFrame({
        "Brand" : [brand],
        "Processor_Speed" : [processor],
        "RAM_Size" : [ram],
        "Storage_Capacity" : [storage],
        "Screen_Size": [screen],
        "Weight" : [weight]

    })
    prediction = model.predict(input)[0]
    st.success(f"The Predicted Price of Laptop should be {prediction}")