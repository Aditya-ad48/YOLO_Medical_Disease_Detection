import streamlit as st
from PIL import Image
from ultralytics import YOLO
import gdown
import os

st.title("🚀 YOLOv8 Object Detection Web App")
st.markdown("Upload an image and let the model detect objects!")

# Google Drive Model URL
MODEL_URL = "https://drive.google.com/uc?id=1A7cxBdKMr18ixMWUxEkDkq0oDG_-msYG"
MODEL_PATH = "yolov8_best_model.pt"

# Download model from Drive if it doesn't exist
if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading YOLOv8 model..."):
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

# Load model
try:
    model = YOLO(MODEL_PATH)
    st.success("Model loaded successfully.")
except Exception as e:
    st.error(f"Failed to load model: {e}")

# Image upload + prediction
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Detecting..."):
        results = model.predict(image)

    result_img = results[0].plot()
    st.image(result_img, caption="Detected Image", use_column_width=True)
