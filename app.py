from math import expm1

import os
import joblib
import pandas as pd
from flask import Flask, jsonify, request
from tensorflow import keras

app = Flask(__name__)
CWD = os.path.join(os.path.dirname(__file__))
ASSETS_DIR = f"{CWD}/assets"

if not os.path.exists(ASSETS_DIR):
    os.mkdir(ASSETS_DIR)

MODEL_PATH = os.path.join(ASSETS_DIR, "price_prediction_model.h5")
TRANSFORMER_PATH = os.path.join(ASSETS_DIR, "data_transformer.joblib")

if not os.path.isfile(MODEL_PATH):
    raise FileNotFoundError("Model not found.please check input")
if not os.path.isfile(TRANSFORMER_PATH):
    raise FileNotFoundError("Transformer not found.please check input")

MODEL = keras.models.load_model(MODEL_PATH)
TRANSFORMER = joblib.load(TRANSFORMER_PATH)

@app.route("/", methods=["POST"])
def index():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    prediction = MODEL.predict(TRANSFORMER.transform(df))
    predicted_price = expm1(prediction.flatten()[0])
    return jsonify({"price": str(predicted_price)})
