# import libraries

import matplotlib.pylab as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

# 2. data load

wine=load_wine()
print(wine)

# 3. divid to x and y

X=wine.data
y=wine.target

print(X)
print(y)

# 4. Train Test Split

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

# 5. scaling

scale=StandardScaler()
X_train=scale.fit_transform(X_train)
X_test=scale.transform(X_test)

# 6. Model training

model=LinearRegression()
model.fit(X_train,y_train)

# 7. prediction

y_pred=model.predict(X_test)
print(y_pred)

# 8. Accuracy

mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print("Mae:",mae)
print("Mse:",mse)
print("r2 is: ",r2)

# 9. Graph


plt.scatter(X_test[:, 0], y_test, label="Actual Data")
plt.scatter(X_test[:, 0], y_pred, label="Predicted Data")
plt.legend()
plt.show()



