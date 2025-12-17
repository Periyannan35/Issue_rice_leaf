# Issue_rice_leaf

A **web-based application** to detect diseases in rice leaves using **Convolutional Neural Networks (CNN)**. Users can upload an image of a rice leaf and get predictions for the type of disease along with confidence scores.

---

## Features

- **Login system:** Simple authentication for users.
- **Image upload:** Upload rice leaf images (`jpg`, `jpeg`, `png`).
- **Disease prediction:** Detects the following classes:
  - Bacterial Leaf Blight
  - Brown Spot
  - Leaf Smut
  - Healthy
- **Confidence score:** Shows the model's prediction confidence.
- **Web app interface:** Built using **Streamlit** for easy access.

---

## Dataset

- The CNN model is trained on a **custom dataset** of rice leaf images collected from public resources.
- Dataset includes 4 classes: Bacterial Leaf Blight, Brown Spot, Leaf Smut, and Healthy leaves.

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Periyannan35/Issue_in_leaf.git
cd Issue_in_leaf
```
2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
# Activate the environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```
3. **Install dependencies**

```bash
pip install -r requirements.txt
```

Running the App

Launch the Streamlit app:

streamlit run rice_disease_app/app.py


Open the link shown in the terminal (usually http://localhost:8501).

Login with default credentials:

Username: admin

Password: 1234

Upload a rice leaf image and click Predict Disease.

Folder Structure
Issue_in_leaf/
│
├─ rice_disease_app/
│   ├─ app.py                  # Streamlit application
│   ├─ model/
│   │   └─ rice_cnn.keras      # Trained CNN model
│
├─ train_model.py              # Script to train the CNN model
├─ dataset/                    # Folder containing training images
├─ requirements.txt            # Python dependencies
└─ README.md
