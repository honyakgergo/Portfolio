import tensorflow as tf
import numpy as np
import os

def load_model():
    """ Load the trained model with a dynamic path. """
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    model_path = r"C:\Users\honya\Documents\GitHub\2024-25c-fai1-adsai-GergoHonyak242720\Deliverables\Garbage_classifier\best_model.h5"

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    model = tf.keras.models.load_model(model_path, compile=False)
    return model

def predict_class(model, image):
    """ Predict class from the image using the model. """
    prediction = model.predict(image)
    print(prediction)
    predicted_class = np.argmax(prediction, axis=1)[0]

    
    class_labels = {0: "Food_Organics", 1:'Glass', 2:'Metal', 3:'Paper_Cardboard', 4:'Plastic', 5:'Textile Trash', 6:'Vegetation'}
    return class_labels.get(predicted_class, "Unknown")

