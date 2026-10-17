import streamlit as st
import joblib as jb
model  = jb.load("ml-regression-model.pkl")
scaler = jb.load("ml-regression-scaler.pkl")


st.title("House Price Prediction")
st.write("Enter Details for area , bedrooms , bathrooms , stories , parking")


# Input 1
area = st.number_input(
    "Area in square feet:",
    min_value=500,
    max_value=20000,
    value=1500,
    step=100
)


# Input 2
bedrooms = st.number_input(
    "Number of bedrooms:",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)


# Input 3
bathrooms = st.number_input(
    "Number of bathrooms:",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)


# Input 4
stories = st.number_input(
    "Number of stories:",
    min_value=1,
    max_value=5,
    value=1,
    step=1
)


# Input 5
parking = st.number_input(
    "Number of parking spaces:",
    min_value=0,
    max_value=5,
    value=1,
    step=1
)

if st.button("Predict"):
    input_data = [[
          area,
        bedrooms,
        bathrooms,
        stories,
        parking
    ]]
    scaled_input  = scaler.transform(input_data)

    predict_price = model.predict(scaled_input)
    st.success(
        f" The pricted price of the house is: {predict_price}"

    )