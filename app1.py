import streamlit as st
from PIL import Image
from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO('/Users/aditya/Desktop/Medical_Disease/yolov8_best_model.pt')

st.title("🚀 YOLOv8 Object Detection Web App")
st.markdown("Upload an image and let the model detect objects!")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Detecting..."):
        results = model.predict(image)

    result_img = results[0].plot()
    st.image(result_img, caption="Detected Image", use_container_width=True)
