🧠 Handwritten Digit Classifier (CNN + Flask)
🚀 Project Overview

This project is a Deep Learning-based web application that classifies handwritten digits (0–9) using a Convolutional Neural Network (CNN).
Users can upload an image, and the model predicts the digit in real-time.

🎯 Features
📸 Upload handwritten digit image
🤖 Predict digit using trained CNN model
⚡ Real-time prediction using Flask
🌐 Simple and user-friendly web interface
🛠️ Tech Stack
Frontend: HTML
Backend: Flask (Python)
Deep Learning: TensorFlow / Keras
Libraries: NumPy, Pillow
🧠 Model Architecture
Conv2D (32 filters) + ReLU
MaxPooling
Conv2D (64 filters) + ReLU
MaxPooling
Flatten
Dense (64 neurons)
Output Layer (Softmax - 10 classes)
📂 Project Structure

digit-classifier-app/
│
├── app.py
├── train_model.py
├── model.h5
├── requirements.txt
└── templates/
└── index.html

▶️ How to Run Locally
1️⃣ Clone the repository

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Train the model

python train_model.py

4️⃣ Run the application

python app.py

5️⃣ Open in browser

http://127.0.0.1:5000
