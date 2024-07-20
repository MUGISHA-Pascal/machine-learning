from flask import Flask,request,jsonify
import joblib

app=Flask(__name__)
@app.route("/predict",method=["POST"])
def predict():
    data=request.json
    features=data["features"]
    model=joblib.load("./iris-dataset/model/iris.joblib")
    prediction=model.predict([features])
    return jsonify({"prediction":prediction.toList()})

if __name__ == "__main__":
    app.run(port=5000,debug=True)