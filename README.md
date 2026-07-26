# 😀 DeepFER: Facial Emotion Recognition Using Deep Learning

## 📌 Project Overview

DeepFER (Deep Facial Emotion Recognition) is a Computer Vision and Deep Learning project designed to automatically identify human emotions from facial expressions. The system classifies facial images into seven emotional categories:

* Angry 😠
* Disgust 🤢
* Fear 😨
* Happy 😀
* Neutral 😐
* Sad 😢
* Surprise 😲

The project leverages Deep Learning techniques, including a Custom Convolutional Neural Network (CNN) and Transfer Learning using MobileNetV2 to build an efficient facial emotion recognition system.

The final model was deployed using Streamlit, enabling real-time emotion prediction from uploaded facial images.

---

# 🎯 Problem Statement

Human emotions play a crucial role in communication and decision-making. Traditional methods of emotion recognition rely on manual observation, which can be subjective and time-consuming.

The objective of this project is to develop an automated Facial Emotion Recognition (FER) system capable of accurately classifying facial expressions into seven emotional categories using Deep Learning techniques.

---

# 🚀 Project Objectives

* Develop an automated emotion recognition system.
* Classify facial expressions into seven emotions.
* Compare a Custom CNN with a Transfer Learning model.
* Evaluate model performance using multiple metrics.
* Deploy the final model using Streamlit.
* Enable real-time emotion prediction from uploaded images.

---

# 📂 Dataset Information

### Dataset Characteristics

* Image Type: RGB Images
* Image Resolution: 48 × 48 Pixels
* Number of Classes: 7

### Emotion Categories

| Label | Emotion  |
| ----- | -------- |
| 0     | Angry    |
| 1     | Disgust  |
| 2     | Fear     |
| 3     | Happy    |
| 4     | Neutral  |
| 5     | Sad      |
| 6     | Surprise |

### Dataset Quality

✅ No corrupted images detected

✅ Consistent image dimensions

✅ RGB image format

---

# 🔍 Project Workflow

### 1. Data Understanding

* Dataset exploration
* Emotion distribution analysis
* Sample image visualization
* Pixel intensity analysis

### 2. Data Wrangling

* Loading images
* Creating labels
* Building feature and target datasets
* Dataset verification

### 3. Data Preprocessing

* Label Encoding
* One-Hot Encoding
* Train-Test Split
* Validation Split
* Pixel Normalization
* Data Augmentation

### 4. Model Development

#### Model 1: Custom CNN

Architecture Components:

* Conv2D Layers
* Batch Normalization
* MaxPooling Layers
* Dropout Layers
* Dense Layers
* Softmax Output Layer

#### Model 2: MobileNetV2 Transfer Learning

Transfer Learning Components:

* Pretrained MobileNetV2
* Global Average Pooling
* Dense Layers
* Dropout Layer
* Softmax Classification Layer

### 5. Model Evaluation

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### 6. Model Comparison

Comparison between:

* Custom CNN
* MobileNetV2

### 7. Deployment

* Streamlit Application
* Real-Time Emotion Prediction

---

# 🛠️ Technologies Used

### Programming Language

* Python

### Data Processing

* NumPy
* Pandas

### Visualization

* Matplotlib
* Seaborn

### Deep Learning

* TensorFlow
* Keras

### Computer Vision

* OpenCV

### Deployment

* Streamlit

---

# 🧠 Deep Learning Models Used

## Model 1: Custom CNN

A Convolutional Neural Network was developed from scratch to learn facial features directly from the training data.

### Advantages

* Learns task-specific features
* Simple architecture
* Easy to understand

### Performance

**Test Accuracy:** 38.61%

---

## Model 2: MobileNetV2 Transfer Learning

A pretrained MobileNetV2 model was used as a feature extractor and adapted for emotion classification.

### Advantages

* Faster convergence
* Better feature extraction
* Improved generalization

### Performance

**Test Accuracy:** 47.63%

---

# 📊 Model Performance Comparison

| Metric            | Custom CNN | MobileNetV2 |
| ----------------- | ---------- | ----------- |
| Test Accuracy     | 38.61%     | 47.63%      |
| Weighted F1 Score | 0.31       | 0.46        |
| Generalization    | Moderate   | Better      |
| Final Selection   | ❌          | ✅           |

---

# 🏆 Final Model Selection

After evaluating both models, MobileNetV2 was selected as the final model because:

* Higher Test Accuracy
* Better Precision, Recall and F1 Score
* Improved Recognition Across Emotion Classes
* Stronger Generalization Ability
* Suitable for Deployment

Final Selected Model:

✅ MobileNetV2 Transfer Learning

---

# 📈 Key Findings

* Transfer Learning significantly outperformed the Custom CNN.
* MobileNetV2 extracted more meaningful facial features.
* Data augmentation improved model robustness.
* Emotion recognition remains challenging due to similarities among emotional expressions.
* Happy emotion was classified most accurately.
* Angry, Fear, and Surprise emotions improved significantly using MobileNetV2.

---

# 💻 Streamlit Deployment

The final model was deployed using Streamlit.

### Features

* Upload facial image
* Automatic image preprocessing
* Real-time emotion prediction
* Confidence score display

### Application Workflow

Upload Image
⬇
Preprocessing
⬇
Model Prediction
⬇
Emotion Output

---

# 📁 Project Structure

```text
DeepFER/
│
├── DeepFER_Facial_Emotion_Recognition.ipynb
├── deepfer_mobilenetv2.keras
├── emotion_labels.pkl
├── app.py
├── requirements.txt
├── README.md
│
├── dataset/
│
└── DeepFER Documentation/
```

# ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/DeepFER.git
```

### Navigate to Project Directory

```bash
cd DeepFER
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

# ▶️ Run Streamlit Application

```bash
streamlit run app.py
```
# 🔮 Future Scope

* Real-Time Webcam Emotion Recognition
* Multi-Face Emotion Detection
* Fine-Tuning of Transfer Learning Models
* Cloud Deployment
* Mobile Application Development
* Higher Resolution Facial Datasets
* Emotion Analytics Dashboard

# 📚 References

* TensorFlow Documentation
* Keras Documentation
* MobileNetV2 Research Paper
* OpenCV Documentation
* Streamlit Documentation
* Facial Emotion Recognition Literature

# 👨‍💻 Author

**Premsagar Palled**
