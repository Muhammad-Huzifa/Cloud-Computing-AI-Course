import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np
model = load_model("ann_mnist.keras")

print("Model Loaded")
st.title("MNIST Prediction APP")
st.write("Pleaes Upload an image")

image_upload = st.file_uploader(
    "Choose Image", 
    type = ["jpg" , "png"]
)

if image_upload is not None:
    image = Image.open(image_upload)
    image = image.convert("L")
    st.image(
        image , caption = "Uploaded Image"
    )
    image = image.resize((28,28))
    image = np.array(image)
    
    image = image / 255.0
    image = image.reshape(1,28,28)
if st.button("Predict"):
    prediction= model.predict(image)[0]
    digit = np.argmax(prediction)
st.success(
    f"The predicted Image: {digit}"
)   
