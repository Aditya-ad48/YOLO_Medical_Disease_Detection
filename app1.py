import streamlit as st
from PIL import Image
from ultralytics import YOLO
import requests
import os

MODEL_PATH = "yolov8_best_model.pt"
MODEL_URL = "https://drive.usercontent.google.com/download?id=1A7cxBdKMr18ixMWUxEkDkq0oDG_-msYG&export=download"

# Download the model if not already present
if not os.path.exists(MODEL_PATH):
    with st.spinner("⬇️ Downloading model..."):
        response = requests.get(MODEL_URL)
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)
        st.success("Model downloaded successfully!")

# Load the trained YOLO model
model = YOLO(MODEL_PATH)

st.title("🩺 YOLOv8 Medical Image Detection App")
st.markdown("Upload an image and the model will detect conditions!")

uploaded_file = st.file_uploader("Upload a medical image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("🧠 Detecting..."):
        results = model.predict(image)

    # Show the result image
    result_img = results[0].plot()  # draw boxes on the image
    st.image(result_img, caption="Detected Image", use_container_width=True)
