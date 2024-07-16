import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

california = fetch_california_housing()
data = pd.DataFrame(california.data,columns=california.feature_names)
data["MedHouseVal"] = california.target
print(data.isnull().sum())
data["HouseClass"]=pd.qcut(data["MedHouseVal"],q=3,labels=["Low","Medium","High"])
x=data.drop(["MedHouseVal","HouseClass"],axis=1)
y=data["HouseClass"]
scale=StandardScaler()
x_scaled=scale.fit_transform(x)

print(data.head())

x_train,x_test,y_train,y_test = train_test_split(x_scaled,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)

print(f"accuracy : {accuracy}")

conf=confusion_matrix(y_test,y_pred)
print(f"confusion matrix : {conf}")

clas=classification_report(y_test,y_pred)
print(f"classification report : {clas}")