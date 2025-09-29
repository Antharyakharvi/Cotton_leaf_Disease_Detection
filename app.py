from flask import Flask, render_template, request, redirect, url_for
import os
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
PROCESSED_FOLDER = 'static/processed/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load your models (the same as before)
models = {
    "resnet": load_model('models/resnet152v2_bs32_ep29.h5'),
    "vgg": load_model('models/vgg16_bs32_ep29.h5'),
    "customcnn": load_model('models/custom_bs32_ep29.h5'),
    "mobilenet": load_model('models/mobilenet_bs32_ep29.h5'),
}

# Disease class labels (assuming this matches the model training labels)
class_labels = {
    0: "Bacterial Blight",
    1: "Curl Virus",
    2: "Fusarium Wilt",
    3: "Healthy"
}

# Function to preprocess the image for the model
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))  # Resize to 224x224 for ResNet/VGG
    img_array = np.array(img) / 255.0  # Normalize the pixel values to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Function to map the predicted class index to a disease name
def map_class_to_disease(predicted_class):
    return class_labels.get(predicted_class, "Unknown Disease")

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Image preprocessing
        img_array = preprocess_image(filepath)

        # Choose model for detection (e.g., ResNet as default)
        model = models["resnet"]

        # Make prediction
        predictions = model.predict(img_array)

        # Get the class with the highest probability (index of the maximum value)
        predicted_class = np.argmax(predictions, axis=1)[0]

        # Map the predicted class index to a disease name
        disease = map_class_to_disease(predicted_class)

        return render_template('index.html', result=disease, original_image=filename, segmented_image=filename)

if __name__ == '__main__':
    app.run(debug=True)
