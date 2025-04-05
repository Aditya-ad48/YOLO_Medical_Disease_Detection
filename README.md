# 🩻 Chest X-ray Abnormality Detection with YOLOv8 & Streamlit

This project presents a real-time web application that detects and localizes 14 thoracic abnormalities in chest X-ray images using a fine-tuned YOLOv8 object detection model. It was built using the VinBigData Chest X-ray Abnormalities Detection dataset and deployed via Streamlit Cloud for public use.

⚠️ This tool is designed for educational and research purposes. It does not replace professional medical advice.

🌐 **Try the Live App**  
🚀 [Click here to use the app](https://yolomedicaldiseasedetection-fiz4gqfebk7rqddppafw7n.streamlit.app/)

## 🧠 Motivation
Interpreting chest radiographs is one of the most complex tasks in radiology due to overlapping structures and subtle anomalies. This project aims to:

- Assist radiologists by acting as a second opinion
- Reduce diagnostic errors due to fatigue or limited expertise
- Provide diagnostic support in underserved or rural areas with limited access to specialists

## 📦 Dataset: VinBigData Chest X-ray
This project uses a public dataset provided by the VinBigData Institute, consisting of:

🖼️ 18,000 annotated chest X-ray scans (converted to 512×512 JPG/PNG)  
✅ 14 thoracic abnormalities  
🧑‍⚕️ Expert annotations from certified radiologists using the VinLab platform  

**Dataset paper:** [VinDr-CXR: An open dataset of chest X-rays with radiologist's annotations](https://arxiv.org/pdf/2012.15029)


### Classes Detected:
- Aortic enlargement
- Atelectasis
- Calcification
- Cardiomegaly
- Consolidation
- ILD
- Infiltration
- Lung opacity
- Mass
- Nodule
- Pleural effusion
- Pleural thickening
- Pneumothorax
- Pulmonary fibrosis

## 🧰 Tech Stack

| Component         | Tool           |
|-------------------|----------------|
| Object Detection  | YOLOv8         |
| Language          | Python         |
| Frontend          | Streamlit      |
| Libraries         | PyTorch, OpenCV, PIL, NumPy |
| Deployment        | Streamlit Cloud |

## 🚀 Features
- 🩻 Upload any chest X-ray image (JPG/PNG)
- 🔍 Real-time detection of 14 abnormalities
- 🧠 Inference using trained YOLOv8 model
- 📦 Bounding box visualization with class labels
- 🌍 Deployed & accessible through web browser

## 📸 How It Works
1. User uploads a chest X-ray image through the interface
2. The model performs object detection on the image using YOLOv8
3. Bounding boxes and labels are drawn on the image
4. The result is displayed on the web app within seconds

## 📈 Model Info
- Model: YOLOv8x (for improved accuracy)
- Input size: 640×640
- Trained for: 30 epochs
- GPUs used: 2 (Device 0, 1)
- Batch size: 16
- Training environment: Multi-GPU (CUDA enabled)

Training was done using a pre-processed version of the dataset (DICOM → PNG conversion already done).

## 🧪 Example Output
**Input**  
(002a34c58c5b758217ed1f584ccbcfe9.png)

**Output**  
(Include image with bounding boxes and class labels)

## 📤 Deployment Details
✅ Deployed on Streamlit Cloud  
✅ External users can upload images directly in-browser  

##  Acknowledgements
- VinBigData for the dataset and medical insights
- Ultralytics for YOLOv8
- Streamlit for their simple and fast deployment platform
 


