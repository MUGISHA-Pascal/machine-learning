import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
import argparse


def main(n_estimators, test_size, random_state):
    california = fetch_california_housing()
    data = pd.DataFrame(california.data, columns=california.feature_names)
    data["MedHouseVal"] = california.target
    data["HouseClass"] = pd.qcut(data["MedHouseVal"], q=3, labels=["Low", "Medium", "High"])
    x = data.drop(["MedHouseVal", "HouseClass"], axis=1)
    y = data["HouseClass"]

    # Check for null values
    print(data.isnull().sum())

    scale = StandardScaler()
    x_scaled = scale.fit_transform(x)
    x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=test_size, random_state=random_state)

    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

    features = california.feature_names
    feature_importances = model.feature_importances_

    plt.figure(figsize=(10, 6))
    plt.barh(features, feature_importances, color="skyblue")
    plt.xlabel("Feature Importances")
    plt.ylabel("Features")
    plt.title("Feature Importances in RandomForest")
    plt.show()


def predict():
    parser = argparse.ArgumentParser(description="Train the model")
    parser.add_argument("--n_estimators", type=int, default=100, help="Enter the number of estimators")
    parser.add_argument("--test_size", type=float, default=0.2, help="Enter the test size")
    parser.add_argument("--random_state", type=int, default=42, help="Enter the random state")
    args = parser.parse_args()

    main(n_estimators=args.n_estimators, test_size=args.test_size, random_state=args.random_state)


if __name__ == "__main__":
    predict()
