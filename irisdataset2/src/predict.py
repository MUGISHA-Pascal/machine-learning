import argparse
import joblib
import pandas as pd

def predict(features):
    feature_names=["sepal_length","sepal_width","petal_length","petal_width"]
    inputdata=pd.DataFrame(features,columns=feature_names)
    model=joblib.load("../model/iris.joblib")
    prediction= model.predict(inputdata)
    return prediction[0]

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="train the model : ")
    parser.add_argument("sepal_length",type=float,help="sepal length")
    parser.add_argument("sepal_width",type=float,help="sepal width")
    parser.add_argument("petal_length",type=float,help="petal length")
    parser.add_argument("petal_width",type=float,help="petal width")
    args=parser.parse_args()
    features =[sepal_length=args.sepal_length,sepal_width=args.sepal_width,petal_length=args.petal_length,petal_width=args.petal_width]
    prediction=predict(features)
    print(f"the prediction is {prediction}")
