import matplotlib.pyplot as plt
import joblib

model=joblib.load("../model/iris.joblib")
features=["sepal_length","sepal_width","petal_length","petal_width"]
plt.figure(figsize=(10,6))
feature_importance=model.feature_importances_
plt.barh(features,feature_importance,color="skyblue")
plt.xlabel("feature importance")
plt.ylabel("features")
plt.title("graph")
plt.show()

