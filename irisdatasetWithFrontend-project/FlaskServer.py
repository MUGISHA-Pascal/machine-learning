from flask import Flask,request,jsonify
import joblib

app=Flask(__name__)
@app.route("/predict",methods=["POST"])
def predict():
    data=request.json["data"]
    input_data = np.array([float(i) for i in data.split(',')]).reshape(1, -1)
    model=joblib.load("./irisdataset/model/iris.joblib")
    pre=model.predict(input_data)
    return jsonify({"prediction":pre.tolist()})
if __name__ == "__main__":
    app.run(port=4000,debug=True)