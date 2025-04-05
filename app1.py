import os
import requests
import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Hugging Face direct model link
MODEL_URL = "https://huggingface.co/aditya1310/yolov8-model/resolve/main/yolov8_best_model.pt"
MODEL_PATH = "yolov8_best_model.pt"

# Download the model if not already present
if not os.path.exists(MODEL_PATH):
    with st.spinner("🔽 Downloading model from Hugging Face..."):
        response = requests.get(MODEL_URL)
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)

# Load the YOLO model
model = YOLO(MODEL_PATH)

# Rest of your Streamlit UI
st.title("🚀 YOLOv8 Object Detection Web App")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])


if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    with st.spinner("Detecting..."):
        results = model.predict(image)
    result_img = results[0].plot()
    st.image(result_img, caption="Detected Image", use_container_width=True)
