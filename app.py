# Import Dependencies
import pandas as pd
from pathlib import Path
from flask import Flask, request, jsonify, render_template
from mlpredictor.utils.common import load_ml_model


# Initialize Flask App
app = Flask(__name__)


# Load Trained ML Model
model_path = Path('model/final_model.joblib')
model = load_ml_model(model_path=model_path)


# Default Route
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/", methods=["POST"])
def predict():
    data = request.json
    features = pd.DataFrame([data])
    prediction = int(model.predict(features)[0])

    message = (
        "The patient is healthy, no heart risk detected."
        if prediction == 0
        else "The patient is unhealthy, heart risk detected."
    )
    return jsonify({"message": message})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)
