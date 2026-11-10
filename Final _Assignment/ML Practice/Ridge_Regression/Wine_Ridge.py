# import libraries

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import matplotlib.pylab as plt


# load dataset

wine=load_wine()
print(wine)

# divid to x and y

X=wine.data
y=wine.target
print(X)
print(y)


# train test split

X_train, X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

# scaler

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


# model training

model=Ridge()
model.fit(X_train,y_train)


# prediction

y_pred=model.predict(X_test)



# accuray

mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

# graph


plt.scatter(y_test,y_pred)
plt.title("Wine")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()