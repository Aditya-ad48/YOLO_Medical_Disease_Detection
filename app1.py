import streamlit as st
from PIL import Image
from ultralytics import YOLO
import os
import requests

# Model URL from Google Drive (converted to direct download link)
MODEL_URL = "https://drive.google.com/uc?id=1A7cxBdKMr18ixMWUxEkDkq0oDG_-msYG"
MODEL_PATH = "yolov8_best_model.pt"

# Download model if not already downloaded
if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading model..."):
        response = requests.get(MODEL_URL)
        with open(MODEL_PATH, 'wb') as f:
            f.write(response.content)

# Load the model
model = YOLO(MODEL_PATH)

# Streamlit UI
st.title("🩺 Medical Disease Detection using YOLOv8")
st.markdown("Upload a medical image and get predictions.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Running detection..."):
        results = model.predict(image)

    result_image = results[0].plot()
    st.image(result_image, caption="Predicted Output", use_container_width=True)
