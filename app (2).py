import streamlit as st
import tensorflow as tf
import numpy as np
import pickle

from PIL import Image

# --------------------------
# Load Model
# --------------------------

model = tf.keras.models.load_model(
    "deepfer_mobilenetv2.keras"
)

# --------------------------
# Load Labels
# --------------------------

with open(
    "emotion_labels.pkl",
    "rb"
) as file:

    emotion_labels = pickle.load(file)

# --------------------------
# Page Configuration
# --------------------------

st.set_page_config(
    page_title="DeepFER",
    layout="centered"
)

st.title("😀 DeepFER")
st.subheader(
    "Facial Emotion Recognition Using Deep Learning"
)

# --------------------------
# Upload Image
# --------------------------

uploaded_file = st.file_uploader(
    "Upload Facial Image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------
# Prediction
# --------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Convert image

    image = image.convert("RGB")

    image = image.resize((96,96))

    image_array = np.array(image)

    image_array = image_array / 255.0

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    prediction = model.predict(
        image_array
    )

    predicted_class = np.argmax(
        prediction
    )

    confidence = np.max(
        prediction
    ) * 100

    emotion = emotion_labels[
        predicted_class
    ]

    st.success(
        f"Predicted Emotion: {emotion.upper()}"
    )

    st.write(
        f"Confidence: {confidence:.2f}%"
    )