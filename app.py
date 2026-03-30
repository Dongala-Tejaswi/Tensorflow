from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("model.h5")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    # Process image
    img = Image.open(file).convert('L')  # grayscale
    img = img.resize((28, 28))
    img = np.array(img) / 255.0
    img = img.reshape(1, 28, 28, 1)

    # Prediction
    prediction = model.predict(img)
    result = np.argmax(prediction)

    return f"<h2>Prediction: {result}</h2>"

if __name__ == '__main__':
    app.run(debug=True)