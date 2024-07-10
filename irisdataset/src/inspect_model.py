import joblib
from sklearn.ensemble import RandomForestClassifier

# Load the trained model
model = joblib.load('../models/iris_model.joblib')

# Print the model to get a basic overview
print(model)

# Print model parameters
print("\nModel Parameters:")
print(model.get_params())

# If it’s a RandomForestClassifier, we can inspect more details
if isinstance(model, RandomForestClassifier):
    print("\nFeature Importances:")
    print(model.feature_importances_)

    # Print details of individual trees (for example, the first tree)
    print("\nFirst tree details:")
    tree = model.estimators_[0]
    print(tree)
