# import libraries

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import matplotlib.pylab as plt
from sklearn.preprocessing import StandardScaler




# load data sets


lasso_iris=load_iris()
print(lasso_iris)


# divid x and y

X=lasso_iris.data
y=lasso_iris.target

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
print(y_pred)

# acurracy

mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

# graph

plt.scatter(y_test,y_pred,label="Actual Data")
plt.scatter(y_test,y_pred,label="Predicted Data")
plt.title('Graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

