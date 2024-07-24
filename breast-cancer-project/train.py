import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import mean_squared_error,explained_variance_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data_bunch = load_breast_cancer()
data = pd.DataFrame(data_bunch.data, columns=data_bunch.feature_names)
x=data.drop("worst fractal dimension",axis=1)
y=data["worst fractal dimension"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
meansq=mean_squared_error(y_test,y_pred)
print(f"the mean square error is : {meansq}")
variance_score=explained_variance_score(y_test,y_pred)
print(f"the variance score is : {variance_score}")