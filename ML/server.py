from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("deadlock_model.pkl")

@app.route('/')
def home():
    return "Deadlock Detection API is running!"

@app.route('/predict_deadlock', methods=['POST'])
def predict_deadlock():
    data = request.get_json()
    features = data.get("features")

    if not features:
        return jsonify({"error": "Features are required"}), 400

    features = np.array(features).reshape(1, -1)  
    prediction = model.predict(features)[0]  
    return jsonify({"deadlock": int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
