from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

california = fetch_california_housing()
data=pd.DataFrame(california.data,columns=california.feature_names)
data["MedHouseVal"]=california.target

print(data.head())

print(data.isnull().sum())

data["HouseValueClass"] = pd.qcut(data["MedHouseVal"],q=3,labels=["Low","Medium","High"])

x=data.drop(["MedHouseVal","HouseValueClass"],axis=1)
y=data["HouseValueClass"]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(x_scaled,y,test_size=0.2,random_state=42)

print(f"Training data shape : {x_train.shape}")
print(f"Testing data shape : {x_test.shape}")

model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)

print("model trained successfully")

y_pred = model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(f"accuracy : {accuracy}")

print("classification report : ")
print(classification_report(y_test,y_pred))

print("confusion matrix : ")
print(confusion_matrix(y_test,y_pred))

features = california.feature_names
feature_importance=model.feature_importances_
plt.figure(figsize=(10,6))
plt.barh(features,feature_importance,color="skyblue")
plt.xlabel("feature importances")
plt.ylabel("features")
plt.title("graph")
plt.show()