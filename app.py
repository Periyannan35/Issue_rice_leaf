import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# -------------------------------
# Path to your model
MODEL_PATH = "rice_disease_app/model/rice_cnn.keras"

# Load model
@st.cache_resource
def load_cnn_model(path):
    return load_model(path)

model = load_cnn_model(MODEL_PATH)

# Classes (update as per your training)
CLASSES = ['Bacterial_Leaf_Blight', 'Brown_Spot', 'Leaf_Smut', 'Healthy']

# -------------------------------
# Session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# -------------------------------
# Login page
if not st.session_state.logged_in:
    st.title("Rice Leaf Disease Detection - Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Wrong username or password")

# -------------------------------
# Main app page
if st.session_state.logged_in:
    st.title("Rice Leaf Disease Detection")

    # File uploader
    uploaded_file = st.file_uploader("Upload Rice Leaf Image", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file

    if st.session_state.uploaded_file is not None:
        # Display uploaded image
        img = Image.open(st.session_state.uploaded_file)
        st.image(img, caption="Uploaded Leaf", width=400)

        # Prediction button
        if st.button("Predict Disease"):
            # Preprocess image to match model input
            img_resized = img.resize((224, 224))  # Matches your training IMG_SIZE
            x = image.img_to_array(img_resized)
            x = np.expand_dims(x, axis=0)
            x /= 255.0  # Normalize

            # Predict
            preds = model.predict(x)
            class_idx = np.argmax(preds, axis=1)[0]
            confidence = preds[0][class_idx] * 100

            st.success(f"Disease Prediction: **{CLASSES[class_idx]}**")
            st.info(f"Confidence: {confidence:.2f}%")

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.uploaded_file = None
        st.success("Logged out successfully.")
