import matplotlib.pyplot as plt
import joblib
model=joblib.load("../model/ir.joblib")
plt.figure(figure=(10,6))
features=["sepal_length","sepal_width","petal_length","petal_width"]
feature_importance=model.feature_importances_
plt.barh(features,feature_importance,color="skyblue")
plt.xlabel("feature importance")
plt.ylabel("features")
plt.title("graph")
plt.show()


