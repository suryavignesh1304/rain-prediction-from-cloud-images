import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the saved model
model = load_model('cloud_rain_predictor.h5')

st.title("🌦️ Rain Prediction from Cloud Images")

uploaded_file = st.file_uploader("Upload a cloud image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded file
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension

    # Predict with the model
    prediction = model.predict(img)

    if prediction[0][0] > 0.5:
        st.success(f"Rain likely (Confidence: {prediction[0][0]:.2f})")
    else:
        st.info(f"No rain likely (Confidence: {1 - prediction[0][0]:.2f})")
else:
    st.write("Please upload an image to get started.")
