# 1. import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

# 2. load data

iris=load_iris()
print(iris)

# 3. Divid to X and Y

X=iris.data
y=iris.target

print("X is: ",X)
print("y is :",y)

# 4. Train Test Split

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

# 5. Scaling 

scale=StandardScaler()
X_train=scale.fit_transform(X_train)
X_test=scale.transform(X_test)

# 6. Mode Training

model=LinearRegression()
model.fit(X_train,y_train)

# 7. prediction

y_pred=model.predict(X_test)
print("prediction is: ",y_pred)

# 8. Accuracy

r2=r2_score(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)

print("r2 is:",r2)
print("MSE is :",mse)
print("MAE is :",mae)

compression_df=pd.DataFrame({'Actual Data':y_test,'Predicted data':y_pred})
print(compression_df.head(5))

# 9. graph

plt.scatter(X_test[:,0],y_test,label="Actual Data")
plt.scatter(X_test[:,0],y_pred,label="Predicted Data")
plt.xlabel("Feature 1")
plt.ylabel("Target")
plt.legend()
plt.show()



# plt.scatter(X_test[:,0],y_test,label="Actual Data")
# plt.scatter(X_test[:,0],y_pred,label="Predicted Data")
# plt.xlabel("Feature 1")
# plt.ylabel('Target')
# plt.legend()
# plt.show()


# sns.lineplot(x=y_test,y=y_pred,data=compression_df)
# plt.show()

# sns.scatterplot(x=y_test,y=y_pred,data=compression_df)
# plt.show()