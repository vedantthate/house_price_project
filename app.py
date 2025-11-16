from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open("house_price_model.pkl", "rb") as f:
    saved = pickle.load(f)
    model = saved["model"]
    scaler = saved["scaler"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array(data["features"]).reshape(1, -1)

    # scale incoming user features
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]

    return jsonify({"predicted_price": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
