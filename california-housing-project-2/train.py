import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.datasets import fetch_california_housing

california=fetch_california_housing()
print(california)

data=pd.DataFrame(california.data,columns=california.feature_names)
data["MedHouseVal"]=california.target
print(data.head())
x=data.drop("MedHouseVal",axis=1)
y=data["MedHouseVal"]

# print(data.isnull().sum())

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print(f"the mean square error is : {mse}")
print(f"the R squared if : {r2}")