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
