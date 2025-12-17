
from tensorflow.keras.models import load_model

def load_cnn_model(model_path: str):
    """
    Loads and returns the trained CNN model.

    Single Responsibility:
    This function only handles model loading.
    """
    return load_model(model_path)
