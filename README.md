# 🚀 Real-Time 3D Object Detection, Depth Estimation & Tracking System

## 📌 Overview

This project implements a **real-time 3D perception system** that performs:

* Object Detection using YOLOv8
* Depth Estimation using MiDaS
* Multi-Object Tracking using DeepSORT

The system processes live webcam input and outputs:

* Bounding boxes
* Object tracking IDs
* Estimated depth (distance)
* Real-time FPS performance

---

## 🎯 Features

* 🔍 Real-time object detection (YOLOv8)
* 📏 Depth estimation from monocular camera (MiDaS)
* 🧠 Multi-object tracking with unique IDs (DeepSORT)
* ⚡ Real-time performance with FPS counter
* 🎥 Live webcam processing
* 📊 Visual overlay of detection + depth

---

## 🛠️ Tech Stack

* Python
* PyTorch
* OpenCV
* Ultralytics YOLOv8
* MiDaS (Intel ISL)
* DeepSORT

---

## 📂 Project Structure

```
3D_Object_Detection/
│── main.py
│── detector.py
│── depth.py
│── tracker.py
│── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-link>
cd 3D_Object_Detection
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main file:

```
python main.py
```

Press **'q' or ESC** to exit.

---

## 📸 Output

The system displays:

* Object bounding boxes
* Tracking IDs
* Depth values
* FPS performance

---

## 🧠 Key Concepts Used

* Computer Vision
* Deep Learning (Object Detection)
* Monocular Depth Estimation
* Multi-Object Tracking
* Real-time Video Processing

---

## ⚠️ Limitations

* Depth estimation is relative (not exact distance)
* Performance depends on CPU/GPU
* Monocular depth is less accurate than stereo vision

---

## 🚀 Future Improvements

* CUDA / GPU acceleration
* TensorRT optimization
* Stereo vision for accurate depth
* Deployment on NVIDIA Jetson
* Sensor fusion (camera + radar)

---

## 👨‍💻 Author

Aniruddha Sultane

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
