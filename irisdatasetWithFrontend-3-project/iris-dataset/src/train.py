from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

data=pd.read_csv("../data/iris.csv")
x=data.drop("species",axis=1)
y=data["species"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)
joblib.dump(model,"../model/ir.joblib")
y_pred = model.predict(x_test)
accuracy=accuracy_score(y_pred,y_test)
print(f"the accuracy is {accuracy}")
