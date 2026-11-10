# import libraries

import matplotlib.pylab as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ridge_regression
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# Load data set

diabetes=load_diabetes()
print(diabetes)

# Diviid to X and y

X=diabetes.data
y=diabetes.target
print(X)
print(y)

# train test split

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

# scaling

scale=StandardScaler()
X_train=scale.fit_transform(X_train)
X_test=scale.transform(X_test)



# model training

model=Ridge(alpha=1.0)
model.fit(X_train, y_train)

# prediction

y_pred=model.predict(X_test)

print(y_pred)

# Accuracy

mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print("mse:",mse)
print("mae:",mae)
print("r2:",r2)


# Graph

plt.scatter(y_test, y_pred)

plt.plot(
    [y_test.min(), y_test.max()], # x axis
    [y_test.min(), y_test.max()], # y axis
    color="red"
)

plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")

plt.show()


