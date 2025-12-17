
import numpy as np
from PIL import Image

def preprocess_image(uploaded_file, target_size):
    """
    Preprocesses the uploaded image for CNN prediction.

    Single Responsibility Principle:
    - This function ONLY handles image preprocessing.

    Open-Closed Principle:
    - Can be extended for augmentation without changing callers.
    """

    image = Image.open(uploaded_file).convert("RGB")
    image = image.resize(tuple(target_size))

    image_array = np.array(image, dtype="float32") / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    return image_array
