# 🌾 Issue_rice_leaf

## 📌 Project Overview
This project is an AI-powered web application designed to automatically detect diseases in rice and pulse crop leaves using **Convolutional Neural Networks (CNNs)**.  
The system allows users to log in, upload a leaf image, and receive the predicted disease along with confidence percentage through an interactive **Streamlit web interface**.

The project is developed as part of the **Infosys Internship Program (Nov Batch – 2025)** and follows **professional software engineering practices**.

---

## 🚀 Features
- 🔐 Secure Login Interface  
- 📤 Leaf Image Upload  
- 🧠 CNN-based Disease Prediction (CPU-based)  
- 📊 Confidence Percentage Output  
- 🧩 Modular and Scalable Architecture  
- 📦 GitHub Version Controlled  

---

## 🏗 Project Structure
```
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── src/ # Source code modules
│ ├── init.py
│ ├── image_preprocessor.py
│ └── model_loader.py
│
├── models/ # Trained CNN models
│ └── rice_cnn.keras
│
├── data/ # Dataset (local use only)
│
├── config/ # Configuration files
│ ├── model_config.json
│ └── class_names.json
│
├── screenshots/ # Application screenshots
│ ├── login.png
│ ├── upload.png
│ └── prediction.png
│
└── tests/ # Test modules
└── init.py
```

---

## 🧠 SOLID Design Principles Applied

This project is designed following the **SOLID principles** to ensure maintainability, scalability, and clean architecture.

---

### 1️⃣ Single Responsibility Principle (SRP)

**Definition**  
Each module should have **only one responsibility**.

**Implementation**
- `app.py` → Handles UI and user interaction
- `image_preprocessor.py` → Handles image resizing and normalization
- `model_loader.py` → Loads trained CNN model
- `class_names.json` → Stores disease labels

✔ Improves clarity and debugging.

---

### 2️⃣ Open–Closed Principle (OCP)

**Definition**  
Software entities should be **open for extension but closed for modification**.

**Implementation**
- New diseases can be added by retraining the model
- Class labels updated in `class_names.json`
- No changes required in UI or prediction logic

✔ Enables easy scalability.

---

### 3️⃣ Liskov Substitution Principle (LSP)

**Definition**  
Objects should be replaceable with their subtypes without affecting correctness.

**Implementation**
- CNN model can be replaced with other architectures (MobileNet, ResNet)
- Input/output consistency ensures seamless substitution

✔ Model flexibility is maintained.

---

### 4️⃣ Interface Segregation Principle (ISP)

**Definition**  
Clients should not depend on interfaces they do not use.

**Implementation**
- UI code does not interact with training logic
- Model loading, preprocessing, and prediction are separated

✔ Keeps code lightweight and modular.

---

### 5️⃣ Dependency Inversion Principle (DIP)

**Definition**  
High-level modules should not depend on low-level modules directly.

**Implementation**
- `app.py` loads model and labels from config files
- Model paths and class names are configurable

✔ Improves flexibility and maintainability.

---

## 📸 Application Screenshots

### 🔐 Login Page
![Login Page](screenshots/Login.png)

### 📤 Image Upload
![Upload Image](screenshots/Upload.png)

### 🧠 Prediction Result
![Prediction Result](screenshots/Prediction.png)

---

## ⚙️ Installation & Execution

### Prerequisites
- Python 3.10+
- pip

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
streamlit run app.py
```
