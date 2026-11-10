# import libraries

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import matplotlib.pylab as plt


# load dela

wine=load_wine()
print(wine)


# divid x and y

X=wine.data
y=wine.target



# train test split


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# scaling
sacler=StandardScaler()
X_train=sacler.fit_transform(X_train)
X_test=sacler.transform(X_test)


# model training

model=Lasso()
model.fit(X_train,y_train)

# prediction

y_pred=model.predict(X_test)

# accuracy

mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

# graph

plt.scatter(y_test,y_pred,label="Actual data")
plt.scatter(y_test,y_pred,label='Predicted data')
plt.title("Graph")
plt.xlabel('X')
plt.ylabel("Y")
plt.legend()

plt.show()
