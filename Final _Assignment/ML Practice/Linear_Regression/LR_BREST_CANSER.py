# 1. import libraries

import pandas as pd
import seaborn as sns
from sklearn.datasets import load_breast_cancer
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# 2. data load

lbc=load_breast_cancer()
print(lbc)


# 3. divid to X and Y

X=lbc.data
y=lbc.target

print(X)
print(y)

# 4. Train Test and Split

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)


# 5. scaling

scale=StandardScaler()
X_train=scale.fit_transform(X_train)
X_test=scale.transform(X_test)

# 6. Model Training

model=LinearRegression()
model.fit(X_train,y_train)

# 7. Prediction

y_pred=model.predict(X_test)
print(y_pred)

# 8. Accuray 

mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print("Mean square error is:",mse)
print("Mean absolute error is: ",mae)
print("R2 is :",r2)

# 9. Graph

plt.scatter(X_test[:,0],y_test,label="Actual Data")
plt.scatter(X_test[:,0],y_pred,label="Predicted Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()