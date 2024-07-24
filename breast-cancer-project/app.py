from flask import Flask,request,jsonify
import joblib
import pandas as pd

app=Flask(__name__)
@app.route("/predict",methods=["POST"])
def predict():
    model=joblib.load("./model/cancer.joblib")
    data=request.json
    features=data["features"]
    input_data=pd.DataFrame([features],columns=[""])
    prediction=model.predict(input_data)
    return JSON.jsonify({prediction.tolist()})

if __nama__ == "__main__":
    app.run(port=5000,debug=True)