from flask import Flask, render_template, request, jsonify
import numpy as np
from PIL import Image
import io
import tensorflow as tf
from model import load_model, predict_class

app = Flask(__name__)

# Load the model once at startup
model = load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Open image and ensure it's in RGB mode
    image = Image.open(file.stream).convert("RGB")
    image = image.resize((224, 224))  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0)  

    # Make prediction
    prediction = predict_class(model, image)

    return jsonify({'class': prediction})

if __name__ == '__main__':
    app.run(debug=True)
