🧩 Software Design Principles (SOLID)

This project is designed following SOLID principles to ensure scalability, maintainability, and clean architecture.

1️⃣ Single Responsibility Principle (SRP)

Definition:
A class or module should have only one reason to change, meaning it should handle one specific responsibility.

Usage in this Project:
Each component has a single, well-defined role.

Module	Responsibility
app.py	Handles Streamlit UI, user interaction, and workflow
src/model_loader.py	Responsible only for loading the trained CNN model
src/image_preprocessor.py	Handles image resizing and normalization
config/class_names.json	Stores disease class labels
models/rice_cnn.keras	Contains trained CNN weights

✔ This separation makes the system easier to debug and extend.

2️⃣ Open–Closed Principle (OCP)

Definition:
Software entities should be open for extension but closed for modification.

Usage in this Project:

New diseases can be added without modifying application logic

Only class_names.json and retrained model need updates

UI and prediction code remain unchanged

Example:

{
  "0": "Bacterial Leaf Blight",
  "1": "Brown Spot",
  "2": "Leaf Smut",
  "3": "Healthy"
}


✔ The system supports future extensions without rewriting core code.

3️⃣ Liskov Substitution Principle (LSP)

Definition:
Objects of a superclass should be replaceable with objects of its subclasses without affecting correctness.

Usage in this Project:

The CNN model can be replaced with another architecture (e.g., MobileNet, ResNet)

As long as input shape and output format remain consistent, the app works seamlessly

✔ Model substitution does not break prediction flow.

4️⃣ Interface Segregation Principle (ISP)

Definition:
Clients should not be forced to depend on interfaces they do not use.

Usage in this Project:

UI logic is not mixed with training logic

Model loading, preprocessing, and prediction are isolated

Streamlit interface interacts only with required prediction functions

✔ Keeps code lightweight and avoids unnecessary dependencies.

5️⃣ Dependency Inversion Principle (DIP)

Definition:
High-level modules should not depend on low-level modules. Both should depend on abstractions.

Usage in this Project:

app.py does not hardcode model or class details

Model path and class names are loaded from configuration files

Changing model file or labels requires no UI code change

✔ Improves flexibility and maintainability.

🏗 Project Architecture Overview
├── app.py                  # Main Streamlit application
├── requirements.txt        # Dependencies
├── models/                 # Trained CNN models
├── src/                    # Modular source logic
├── config/                 # Configurable parameters
├── data/                   # Dataset (local use)
├── screenshots/            # UI screenshots
└── tests/                  # Testing modules

✅ Conclusion

By following SOLID principles, this project achieves:

Clean separation of concerns

Easy scalability for new diseases

Robust and maintainable architecture

Industry-standard coding practices

This design aligns with professional software engineering standards used in real-world AI applications.
