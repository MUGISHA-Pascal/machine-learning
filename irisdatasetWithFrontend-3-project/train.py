from flask import Flask,request,jsonify
import pandas as pd
import joblib

app=Flask(__name__)
@app.route("/predict",methods=["POST"])
def predict():
    data=request.json
    features=data["features"]
    feature_names=["sepal_length","sepal_width","petal_length","petal_width"]
    input_data=pd.DataFrame([features],columns=feature_names)
    model=joblib.load("./iris-dataset/model/iris.joblib")
    prediction=model.predict(input_data)
    return jsonify({"prediction":prediction.tolist()})
if __name__=="__main__":
    app.run(port=5000,debug=True)