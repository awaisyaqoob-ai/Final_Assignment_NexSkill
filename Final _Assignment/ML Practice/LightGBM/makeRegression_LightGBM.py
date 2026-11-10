# Import libraries

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from lightgbm import LGBMRegressor
import matplotlib.pyplot as plt


# Create dataset

X, y = make_regression(
    n_samples=200,
    n_features=1,
    noise=20,
    random_state=42
)


# Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create LightGBM model

model = LGBMRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)


# Train

model.fit(X_train, y_train)


# Prediction

y_pred = model.predict(X_test)


# Evaluation

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)


# Graph

plt.scatter(X_test, y_test, label="Actual")
plt.scatter(X_test, y_pred, label="Predicted")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("LightGBM Regression")
plt.legend()
plt.show()