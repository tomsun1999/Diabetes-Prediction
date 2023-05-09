from joblib import load
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import json

# load the model
clf = load("model.joblib")

# initialize the flask app
app = Flask(__name__)

# list to store previous predictions
predictions = []

# the default page of our web app
# the web page
@app.route("/")
def home():
    return render_template('index.html', predictions=predictions)
    

# use the prediction in our web app
@app.route("/predict", methods=["POST"])
def predict():
    """For rendering results on HTML GUI"""
    feature_names = ['physical health', 'Mental_health', 'employment_stats', 'general_health', 'last_visit',
                      'Income', 'MARITAL', 'WEIGHT2', 'Age','BMI_idex']
    feature_values = [float(x) for x in request.form.values()]
    features_df = pd.DataFrame([feature_values], columns=feature_names)
    prediction = clf.predict(features_df)
    output = round(float(prediction), 2)
    #convert the numeric result to string
    if output == 0.0:
        newoutput ='Your are unlikely to have diabetes'
    else:
        newoutput ='Your are likely to have diabetes'
    if request.method == 'POST':
        predictions.append(newoutput)
    return json.dumps({"prediction_text": newoutput})

