from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import joblib

app = Flask(__name__, static_folder='static')

# Cargar
model = joblib.load('src/modelo_random_forest.pkl')

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)