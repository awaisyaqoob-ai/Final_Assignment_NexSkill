# import libraries

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

import matplotlib.pylab as plt
# load data sets

diabetics=load_diabetes()
print (diabetics)

# divid x and y

X=diabetics.data
y=diabetics.target

print(X)
print(y)

# train test split

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

# scaling

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


# model training

model=Lasso()
model.fit(X_train,y_train)


# prediction

y_pred=model.predict(X_test)


# accuracy

mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print(mse)
print(mae)
print(r2)

# graph


plt.scatter(y_test,y_pred)
plt.title("Diabetics")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()