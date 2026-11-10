# ==========================================================
# PROJECT: DIAMONDS PRICE PREDICTION USING MACHINE LEARNING
# ==========================================================
# Objective:
# Predict diamond prices using different Machine Learning
# regression algorithms and compare their performance.
#
# Algorithms:
# 1. Linear Regression
# 2. Decision Tree Regressor
# 3. Random Forest Regressor
# 4. K-Nearest Neighbors (KNN)
# 5. XGBoost Regressor
# 6. Ridge Regression
# 7. Lasso Regression
# 8. Elastic Net Regression
# 9. Gradient Boosting Regressor
# 10. Extra Trees Regressor
#
# Deep Learning Models:
# 1. Artificial Neural Network (ANN)
# 2. Residual Neural Network (ResNet-MLP)
# 3. TabNet Neural Network
#
# ==========================================================


# ==========================================================
# 1. IMPORTING REQUIRED LIBRARIES
# ==========================================================

# Pandas: Used for data manipulation and analysis.
import pandas as pd

# NumPy: Used for numerical calculations.
import numpy as np

# Matplotlib: Used for creating graphs and visualizations.
import matplotlib.pylab as plt

# Seaborn: Used for statistical data visualization.
import seaborn as sns

# LabelEncoder: Converts categorical values into numerical values.
from sklearn.preprocessing import LabelEncoder

# train_test_split: Splits the dataset into training and testing data.
from sklearn.model_selection import train_test_split

# StandardScaler: Standardizes numerical features.
from sklearn.preprocessing import StandardScaler

# Linear Regression algorithm.
from sklearn.linear_model import LinearRegression

# Decision Tree Regression algorithm.
from sklearn.tree import DecisionTreeRegressor

# Random Forest Regression algorithm.
from sklearn.ensemble import RandomForestRegressor

# K-Nearest Neighbors Regression algorithm.
from sklearn.neighbors import KNeighborsRegressor

# XGBoost Regression algorithm.
from xgboost import XGBRegressor

# Ridge Regression algorithm.
from sklearn.linear_model import Ridge

# Lasso Regression algorithm.
from sklearn.linear_model import Lasso

# Elastic Net Regression algorithm.
from sklearn.linear_model import ElasticNet

# Gradient Boosting Regression algorithm.
from sklearn.ensemble import GradientBoostingRegressor

# Extra Trees Regression algorithm.
from sklearn.ensemble import ExtraTreesRegressor

# Deep Learning Libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# ==========================================================
# 2. LOADING THE DATASET
# ==========================================================

# pd.read_csv() reads the CSV file and loads it into a DataFrame.
df = pd.read_csv("10-diamonds.csv")

# Display the first five rows of the dataset.
print(df.head())


# ==========================================================
# 3. INITIAL DATA EXPLORATION
# ==========================================================

# Display the number of rows and columns.
print(df.shape)

# Display column names, data types, non-null values, and memory usage.
print(df.info())

# Remove the unnecessary index column from the dataset.
df = df.drop(["Unnamed: 0"], axis=1)

# Display the first five rows after removing the unnecessary column.
print(df.head())

# Generate descriptive statistical information about numerical columns.
print(df.describe())


# ==========================================================
# 4. DATA CLEANING
# ==========================================================

# Remove rows where the x column contains 0.
df = df.drop(df[df["x"] == 0].index)

# Remove rows where the y column contains 0.
df = df.drop(df[df["y"] == 0].index)

# Remove rows where the z column contains 0.
df = df.drop(df[df["z"] == 0].index)

# Display the updated number of rows and columns.
print(df.shape)


# ==========================================================
# 5. EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================================

# ----------------------------------------------------------
# 5.1 Pairplot: Visualizing Relationships Between Features
# ----------------------------------------------------------

# Create a pairplot to visualize relationships between numerical
# features, with diamond cut categories represented by different colors.
ax = sns.pairplot(df, hue="cut", palette="viridis")
plt.show()


# ----------------------------------------------------------
# 5.2 Regression Plots Before Removing Outliers
# ----------------------------------------------------------

# Visualize the relationship between diamond price and y dimension.
ax = sns.regplot(x="price", y="y", data=df)
plt.title("Price vs Y with Outliers")
plt.show()

# Visualize the relationship between diamond price and z dimension.
ax = sns.regplot(x="price", y="z", data=df)
plt.title("Price vs Z with Outliers")
plt.show()

# Visualize the relationship between diamond price and depth.
ax = sns.regplot(x="price", y="depth", data=df)
plt.title("Price vs Depth with Outliers")
plt.show()

# Visualize the relationship between diamond price and table.
ax = sns.regplot(x='price', y='table', data=df)
plt.title("Price vs Table with Outliers")
plt.show()


# ==========================================================
# 6. OUTLIER REMOVAL
# ==========================================================

# Remove rows where depth is greater than or equal to 75
# or less than or equal to 45.
df = df[(df["depth"] < 75) & (df["depth"] > 45)]

# Remove rows where table is greater than or equal to 80
# or less than or equal to 40.
df = df[(df["table"] < 80) & (df["table"] > 40)]

# Remove rows where x dimension is greater than or equal to 30.
df = df[(df["x"] < 30)]

# Remove rows where y dimension is greater than or equal to 30.
df = df[(df["y"] < 30)]

# Remove rows where z dimension is greater than or equal to 30
# or less than or equal to 2.
df = df[(df["z"] < 30) & (df["z"] > 2)]

# Display the updated dataset dimensions after outlier removal.
print(df.shape)


# ----------------------------------------------------------
# 6.1 Visualizing Data After Removing Outliers
# ----------------------------------------------------------

# Visualize the relationship between price and y dimension.
ax = sns.regplot(x="price", y="y", data=df)
plt.title("Price vs Y After Removing Outliers")
plt.show()

# Visualize the relationship between price and z dimension.
ax = sns.regplot(x="price", y="z", data=df)
plt.title("Price vs Z After Removing Outliers")
plt.show()

# Visualize the relationship between price and depth.
ax = sns.regplot(x="price", y="depth", data=df)
plt.title("Price vs Depth After Removing Outliers")
plt.show()

# Visualize the relationship between price and table.
ax = sns.regplot(x="price", y="table", data=df)
plt.title("Price vs Table After Removing Outliers")
plt.show()

# Create another pairplot to observe the cleaned dataset.
ax = sns.pairplot(df, hue="cut", palette="viridis")
plt.show()

# Display the final number of rows and columns after cleaning.
print(df.shape)


# ==========================================================
# 7. IDENTIFYING CATEGORICAL VARIABLES
# ==========================================================

object_cols = list(df.select_dtypes(include="object").columns)

# Display categorical column names.
print("Categorical variables:")
print(object_cols)


# ==========================================================
# 8. VISUALIZING CATEGORICAL FEATURES
# ==========================================================

# ----------------------------------------------------------
# 8.1 Cut vs Price
# ----------------------------------------------------------

# Create a violin plot to visualize the distribution of prices
# across different diamond cut categories.
plt.figure(figsize=(12, 8))

ax = sns.violinplot(x="cut", y="price", data=df)

ax.set_title("Violinplot For Cut vs Price", color="#4e4c39")
ax.set_ylabel("Price", color="#4e4c39")
ax.set_xlabel("Cut", color="#4e4c39")

plt.show()


# ----------------------------------------------------------
# 8.2 Color vs Price
# ----------------------------------------------------------

# Visualize the distribution of diamond prices across different colors.
plt.figure(figsize=(12, 8))

ax = sns.violinplot(x="color", y="price", data=df)

ax.set_title("Violinplot For Color vs Price", color="#4e4c39")
ax.set_ylabel("Price", color="#4e4c39")
ax.set_xlabel("Color", color="#4e4c39")

plt.show()


# ----------------------------------------------------------
# 8.3 Clarity vs Price
# ----------------------------------------------------------

# Visualize the distribution of diamond prices across clarity categories.
plt.figure(figsize=(12, 8))

ax = sns.violinplot(x="clarity", y="price", data=df)

ax.set_title("Violinplot For Clarity vs Price", color="#4e4c39")
ax.set_ylabel("Price", color="#4e4c39")
ax.set_xlabel("Clarity", color="#4e4c39")

plt.show()


# ==========================================================
# 9. DATA PREPROCESSING
# ==========================================================

# Create a copy of the original cleaned dataset.
label_data = df.copy()

# Convert categorical columns into numerical values using LabelEncoder.
for col in object_cols:
    label_data[col] = LabelEncoder().fit_transform(label_data[col])

# Display the first five rows of the encoded dataset.
label_data.head()

# Display descriptive statistics of the original dataset.
print(df.describe())


# ==========================================================
# 10. CORRELATION MATRIX
# ==========================================================

# Create a diverging color palette for the correlation heatmap.
cmap = sns.diverging_palette(70, 20, s=50, l=40, n=6, as_cmap=True)

# Calculate the correlation matrix between numerical features.
corrmat = label_data.corr()

# Create a figure for the correlation heatmap.
f, ax = plt.subplots(figsize=(12, 12))

# Display the correlation matrix using a heatmap.
sns.heatmap(corrmat, cmap=cmap, annot=True)

plt.show()


# ==========================================================
# 11. FEATURE SELECTION AND TARGET VARIABLE
# ==========================================================

# Assign independent features to X by removing the price column.
X = label_data.drop(["price"], axis=1)

# Assign the target variable (diamond price) to y.
y = label_data["price"]

# Display independent features and target variable.
print(X)
print(y)


# ==========================================================
# 12. TRAIN-TEST SPLITTING
# ==========================================================

# Split the dataset into training and testing sets.
# 80% of the data is used for training.
# 20% of the data is used for testing.
# random_state=42 ensures reproducible results.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)


# ==========================================================
# 13. FEATURE SCALING
# ==========================================================

# Create a StandardScaler object to standardize the features.
scaler = StandardScaler()

# Fit the scaler on training data and transform training features.
X_train_scaled = scaler.fit_transform(X_train)

# Use the already fitted scaler to transform testing features.
X_test_scaled = scaler.transform(X_test)


# ==========================================================
# 14. INITIALIZING MACHINE LEARNING MODELS
# ==========================================================

# Initialize Linear Regression.
lr = LinearRegression()

# Initialize Decision Tree Regressor.
dt = DecisionTreeRegressor(random_state=42)

# Initialize Random Forest Regressor.
rf = RandomForestRegressor(random_state=42)

# Initialize K-Nearest Neighbors Regressor.
kn = KNeighborsRegressor()

# Initialize XGBoost Regressor.
xgb = XGBRegressor(random_state=42)

# Initialize Ridge Regression.
ridge = Ridge()

# Initialize Lasso Regression.
lasso = Lasso(max_iter=10000)

# Initialize Elastic Net Regression.
elastic = ElasticNet(max_iter=10000)

# Initialize Gradient Boosting Regressor.
gbr = GradientBoostingRegressor(random_state=42)

# Initialize Extra Trees Regressor.
etr = ExtraTreesRegressor(random_state=42)


# ==========================================================
# 15. TRAINING MACHINE LEARNING MODELS
# ==========================================================

# Train Linear Regression using training data.
lr.fit(X_train_scaled, y_train)

# Train Decision Tree using training data.
dt.fit(X_train_scaled, y_train)

# Train Random Forest using training data.
rf.fit(X_train_scaled, y_train)

# Train K-Nearest Neighbors using training data.
kn.fit(X_train_scaled, y_train)

# Train XGBoost using training data.
xgb.fit(X_train_scaled, y_train)

# Train Ridge Regression using scaled training data.
ridge.fit(X_train_scaled, y_train)

# Train Lasso Regression using scaled training data.
lasso.fit(X_train_scaled, y_train)

# Train Elastic Net Regression using scaled training data.
elastic.fit(X_train_scaled, y_train)

# Train Gradient Boosting using scaled training data.
gbr.fit(X_train_scaled, y_train)

# Train Extra Trees using scaled training data.
etr.fit(X_train_scaled, y_train)


# ==========================================================
# 16. MAKING PREDICTIONS
# ==========================================================

# Generate predictions using Linear Regression.
lr_pred = lr.predict(X_test_scaled)

# Generate predictions using Decision Tree.
dt_pred = dt.predict(X_test_scaled)

# Generate predictions using Random Forest.
rf_pred = rf.predict(X_test_scaled)

# Generate predictions using K-Nearest Neighbors.
kn_pred = kn.predict(X_test_scaled)

# Generate predictions using XGBoost.
xgb_pred = xgb.predict(X_test_scaled)

# Generate predictions using Ridge Regression.
ridge_pred = ridge.predict(X_test_scaled)

# Generate predictions using Lasso Regression.
lasso_pred = lasso.predict(X_test_scaled)

# Generate predictions using Elastic Net Regression.
elastic_pred = elastic.predict(X_test_scaled)

# Generate predictions using Gradient Boosting.
gbr_pred = gbr.predict(X_test_scaled)

# Generate predictions using Extra Trees.
etr_pred = etr.predict(X_test_scaled)


# ==========================================================
# 17. IMPORTING MODEL EVALUATION METRICS
# ==========================================================

# MAE: Measures average absolute prediction error.
from sklearn.metrics import mean_absolute_error

# MSE: Measures average squared prediction error.
from sklearn.metrics import mean_squared_error

# R2 Score: Measures how much variation the model explains.
from sklearn.metrics import r2_score

# NumPy and Pandas are imported again as in the original code.
import numpy as np
import pandas as pd


# ==========================================================
# 18. CALCULATING MODEL PERFORMANCE
# ==========================================================

# Store predictions from all trained Machine Learning models.
models = {
    'Linear Regression': lr_pred,
    'Decision Tree': dt_pred,
    'Random Forest': rf_pred,
    'KNN': kn_pred,
    'XGBoost': xgb_pred,
    'Ridge Regression': ridge_pred,
    'Lasso Regression': lasso_pred,
    'Elastic Net': elastic_pred,
    'Gradient Boosting': gbr_pred,
    'Extra Trees': etr_pred
}

# Create an empty list to store model evaluation results.
results = []

# Calculate evaluation metrics for every model.
for name, prediction in models.items():

    # Calculate Mean Absolute Error.
    mae = mean_absolute_error(y_test, prediction)

    # Calculate Mean Squared Error.
    mse = mean_squared_error(y_test, prediction)

    # Calculate Root Mean Squared Error.
    rmse = np.sqrt(mse)

    # Calculate R2 Score.
    r2 = r2_score(y_test, prediction)

    # Store all evaluation results in a dictionary.
    results.append({
        'Model': name,
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'R2 Score': r2
    })


# ==========================================================
# 19. DISPLAYING MODEL EVALUATION RESULTS
# ==========================================================

# Convert the evaluation results list into a DataFrame.
results_df = pd.DataFrame(results)

# Display all model results rounded to four decimal places.
print(results_df.round(4))


# ==========================================================
# 20. BEST MODEL SELECTION
# ==========================================================

# Select XGBoost as the best model based on previous evaluation results.
best_model = xgb

# Generate predictions using the selected XGBoost model.
y_pred = best_model.predict(X_test_scaled)

# Display the selected model's evaluation results.
print("Best Model: XGBoost Regressor")

print("R2 Score:", r2_score(y_test, y_pred))

print("MAE:", mean_absolute_error(y_test, y_pred))

print("MSE:", mean_squared_error(y_test, y_pred))

print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))


# ==========================================================
# 21. MODEL PERFORMANCE COMPARISON DATA
# ==========================================================

# Use the actual evaluation results of all ten trained algorithms.
# No previously saved or manually entered result values are used.
results = results_df.rename(columns={'Model': 'Algorithm'}).copy()

# ==========================================================
# 22. MODEL PERFORMANCE VISUALIZATION
# ==========================================================

# Set the Seaborn visualization style.
sns.set_style('whitegrid')

# Define the evaluation metrics to compare.
metrics = ['MAE', 'MSE', 'RMSE', 'R2 Score']

# Create a figure containing four subplots.
fig, axes = plt.subplots(2, 2, figsize=(20, 13))

# Generate a bar plot for each evaluation metric.
for ax, metric in zip(axes.flatten(), metrics):

    # Compare algorithms using the selected evaluation metric.
    sns.barplot(
        data=results,
        x='Algorithm',
        y=metric,
        hue='Algorithm',
        palette='viridis',
        legend=False,
        ax=ax
    )

    # Set graph title and axis labels.
    ax.set_title(f'{metric} Comparison', fontsize=14)
    ax.set_xlabel('Machine Learning Algorithms')
    ax.set_ylabel(metric)

    # Rotate algorithm names for better readability.
    ax.tick_params(axis='x', rotation=45, labelsize=9)
    for tick in ax.get_xticklabels():
        tick.set_horizontalalignment('right')

    # Display numerical values above the bars.
    for container in ax.containers:
        ax.bar_label(container, fmt='%.3f', padding=3, fontsize=8)

# Adjust spacing between subplots.
plt.tight_layout()

# Display all four comparison graphs.
plt.show()


# ==========================================================
# END OF DIAMONDS PRICE PREDICTION PROJECT
# ==========================================================



# ==========================================================
# 23. DEEP LEARNING USING ARTIFICIAL NEURAL NETWORK (ANN)
# ==========================================================

# Scale target variable (diamond prices)
y_scaler = StandardScaler()

y_train_scaled = y_scaler.fit_transform(
    np.array(y_train).reshape(-1, 1)
)

# Build a simple Neural Network
dl_model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1)
])

# Compile the model
dl_model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# Train the Deep Learning model
history = dl_model.fit(
    X_train_scaled,
    y_train_scaled,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# Make predictions
dl_pred_scaled = dl_model.predict(X_test_scaled)

# Convert predictions back to original prices
dl_pred = y_scaler.inverse_transform(dl_pred_scaled).flatten()


# ==========================================================
# 24. DEEP LEARNING MODEL EVALUATION
# ==========================================================

print("\nDeep Learning Results")

print("MAE:", mean_absolute_error(y_test, dl_pred))

print("MSE:", mean_squared_error(y_test, dl_pred))

print("RMSE:", np.sqrt(mean_squared_error(y_test, dl_pred)))

print("R2 Score:", r2_score(y_test, dl_pred))


models = {
    'Linear Regression': lr_pred,
    'Decision Tree': dt_pred,
    'Random Forest': rf_pred,
    'KNN': kn_pred,
    'XGBoost': xgb_pred,
    'Deep Learning': dl_pred
}

# ==========================================================
# 25. DEEP LEARNING TRAINING GRAPH
# ==========================================================

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title("Deep Learning Training Performance")
plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.legend()
plt.show()



comparison = pd.DataFrame({
    "ML (XGBoost)": [r2_score(y_test, xgb_pred), np.sqrt(mean_squared_error(y_test, xgb_pred))],
    "DL (ANN)": [r2_score(y_test, dl_pred), np.sqrt(mean_squared_error(y_test, dl_pred))]
}, index=["R2 Score", "RMSE"])

print(comparison.round(4))

# ==========================================================
# 26. EVALUATION OF FIVE NEW MACHINE LEARNING ALGORITHMS
# ==========================================================

# Display MAE, MSE, RMSE and R2 Score for each newly added model.
new_ml_models = {
    'Ridge Regression': ridge_pred,
    'Lasso Regression': lasso_pred,
    'Elastic Net Regression': elastic_pred,
    'Gradient Boosting Regressor': gbr_pred,
    'Extra Trees Regressor': etr_pred
}

print("\nRESULTS OF FIVE NEW MACHINE LEARNING ALGORITHMS")
for name, prediction in new_ml_models.items():
    print("\nAlgorithm:", name)
    print("MAE:", mean_absolute_error(y_test, prediction))
    print("MSE:", mean_squared_error(y_test, prediction))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, prediction)))
    print("R2 Score:", r2_score(y_test, prediction))


# ==========================================================
# 27. DEEP LEARNING USING RESIDUAL NEURAL NETWORK (RESNET-MLP)
# ==========================================================

# Input: Defines the input shape of the diamond features.
from tensorflow.keras.layers import Input

# Add: Creates skip connections between neural network layers.
from tensorflow.keras.layers import Add

# Model: Creates a neural network with multiple connected layers.
from tensorflow.keras.models import Model

# Create the input layer for the residual neural network.
res_input = Input(shape=(X_train_scaled.shape[1],))

# Build the first fully connected layer.
res_first = Dense(64, activation='relu')(res_input)

# Create a residual block with two hidden layers.
res_block = Dense(64, activation='relu')(res_first)
res_block = Dense(64)(res_block)

# Add the original features to the output of the residual block.
res_skip = Add()([res_first, res_block])

# Apply an activation function after the skip connection.
res_skip = tf.keras.layers.Activation('relu')(res_skip)

# Create the final layers for diamond price prediction.
res_hidden = Dense(32, activation='relu')(res_skip)
res_output = Dense(1)(res_hidden)

# Build the Residual Neural Network model.
resnet_model = Model(inputs=res_input, outputs=res_output)

# Compile the ResNet-MLP model.
resnet_model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# Train the model using the scaled diamond features and prices.
resnet_history = resnet_model.fit(
    X_train_scaled,
    y_train_scaled,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# Make predictions using the ResNet-MLP model.
resnet_pred_scaled = resnet_model.predict(X_test_scaled)

# Convert the predictions back into the original diamond prices.
resnet_pred = y_scaler.inverse_transform(resnet_pred_scaled).flatten()


# ==========================================================
# 28. RESNET-MLP MODEL EVALUATION
# ==========================================================

print("\nResNet-MLP Deep Learning Results")

print("MAE:", mean_absolute_error(y_test, resnet_pred))

print("MSE:", mean_squared_error(y_test, resnet_pred))

print("RMSE:", np.sqrt(mean_squared_error(y_test, resnet_pred)))

print("R2 Score:", r2_score(y_test, resnet_pred))


# ==========================================================
# 29. RESNET-MLP DEEP LEARNING TRAINING GRAPH
# ==========================================================

plt.plot(resnet_history.history['loss'], label='Training Loss')
plt.plot(resnet_history.history['val_loss'], label='Validation Loss')

plt.title("ResNet-MLP Training Performance")
plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.legend()
plt.show()


# ==========================================================
# 30. DEEP LEARNING USING TABNET NEURAL NETWORK
# ==========================================================

# TabNet: Neural network designed for structured tabular data.
# Install the additional library using: pip install pytorch-tabnet
from pytorch_tabnet.tab_model import TabNetRegressor

# Create separate training and validation sets from training data.
# Keep the original test set untouched for the final evaluation.
X_tab_train, X_tab_val, y_tab_train, y_tab_val = train_test_split(
    X_train_scaled,
    y_train_scaled,
    test_size=0.2,
    random_state=42
)

# Convert input features into float32 NumPy arrays for TabNet.
X_tab_train = np.asarray(X_tab_train, dtype=np.float32)
X_tab_val = np.asarray(X_tab_val, dtype=np.float32)
X_tab_test = np.asarray(X_test_scaled, dtype=np.float32)

# Convert scaled target prices into 2D float32 NumPy arrays.
y_tab_train = np.asarray(y_tab_train, dtype=np.float32).reshape(-1, 1)
y_tab_val = np.asarray(y_tab_val, dtype=np.float32).reshape(-1, 1)

# Initialize the TabNet Regressor for diamond price prediction.
tabnet_model = TabNetRegressor(
    n_d=16,
    n_a=16,
    n_steps=3,
    seed=42,
    verbose=1
)

# Train the TabNet model using the training and validation data.
tabnet_model.fit(
    X_train=X_tab_train,
    y_train=y_tab_train,
    eval_set=[(X_tab_val, y_tab_val)],
    eval_name=['validation'],
    eval_metric=['rmse'],
    max_epochs=50,
    patience=10,
    batch_size=1024,
    virtual_batch_size=128,
    num_workers=0
)

# Make predictions using the TabNet model.
tabnet_pred_scaled = tabnet_model.predict(X_tab_test)

# Convert the predictions back into the original diamond prices.
tabnet_pred = y_scaler.inverse_transform(tabnet_pred_scaled).flatten()


# ==========================================================
# 31. TABNET MODEL EVALUATION
# ==========================================================

print("\nTabNet Deep Learning Results")

print("MAE:", mean_absolute_error(y_test, tabnet_pred))

print("MSE:", mean_squared_error(y_test, tabnet_pred))

print("RMSE:", np.sqrt(mean_squared_error(y_test, tabnet_pred)))

print("R2 Score:", r2_score(y_test, tabnet_pred))


# ==========================================================
# 32. TABNET DEEP LEARNING TRAINING GRAPH
# ==========================================================

# Show training loss and validation RMSE in separate graphs.
plt.plot(tabnet_model.history['loss'], label='Training Loss')
plt.title("TabNet Training Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

plt.plot(tabnet_model.history['validation_rmse'], label='Validation RMSE')
plt.title("TabNet Validation Performance")
plt.xlabel("Epochs")
plt.ylabel("RMSE")
plt.legend()
plt.show()


# ==========================================================
# 33. FINAL COMPARISON OF ALL MACHINE AND DEEP LEARNING MODELS
# ==========================================================

# Compare the original five ML algorithms, five new algorithms,
# and all three Deep Learning models (ANN, ResNet-MLP, and TabNet).
all_models = {
    'Linear Regression': lr_pred,
    'Decision Tree': dt_pred,
    'Random Forest': rf_pred,
    'KNN': kn_pred,
    'XGBoost': xgb_pred,
    'Ridge Regression': ridge_pred,
    'Lasso Regression': lasso_pred,
    'Elastic Net': elastic_pred,
    'Gradient Boosting': gbr_pred,
    'Extra Trees': etr_pred,
    'ANN': dl_pred,
    'ResNet-MLP': resnet_pred,
    'TabNet': tabnet_pred
}

# Create an empty list to store the final comparison results.
all_results = []

# Calculate the same evaluation metrics for every algorithm.
for name, prediction in all_models.items():

    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, prediction)

    all_results.append({
        'Model': name,
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'R2 Score': r2
    })

# Display all thirteen model results in one comparison table.
all_results_df = pd.DataFrame(all_results)

print("\nFinal Comparison of 10 ML Algorithms and 3 DL Models")
print(all_results_df.round(4).to_string(index=False))

# Identify the best-performing model using the highest R2 Score.
best_result = all_results_df.loc[all_results_df['R2 Score'].idxmax()]

print("\nBest Model Based on R2 Score:", best_result['Model'])
print("R2 Score:", round(best_result['R2 Score'], 4))


# ==========================================================
# 34. FINAL MODEL PERFORMANCE VISUALIZATION
# ==========================================================

# Plot the R2 Scores of all thirteen models for easy comparison.
plt.figure(figsize=(15, 7))

sns.barplot(
    data=all_results_df,
    x='Model',
    y='R2 Score',
    hue='Model',
    palette='viridis',
    legend=False
)

plt.title("R2 Score Comparison of All Machine and Deep Learning Models")
plt.xlabel("Machine Learning and Deep Learning Models")
plt.ylabel("R2 Score")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ==========================================================
# 35. MACHINE LEARNING VS DEEP LEARNING COMPARISON
# ==========================================================

# Separate the ten Machine Learning algorithms from three Deep Learning models.
ml_results_df = all_results_df.iloc[:10].copy()
dl_results_df = all_results_df.iloc[10:].copy()

# Display Machine Learning and Deep Learning results separately.
print("\nMachine Learning Models (10 Algorithms)")
print(ml_results_df.round(4).to_string(index=False))

print("\nDeep Learning Models (3 Neural Networks)")
print(dl_results_df.round(4).to_string(index=False))

# Identify the best model from each group using R2 Score.
best_ml = ml_results_df.loc[ml_results_df['R2 Score'].idxmax()]
best_dl = dl_results_df.loc[dl_results_df['R2 Score'].idxmax()]

# Compare the strongest Machine Learning and Deep Learning models side by side.
best_comparison = pd.DataFrame({
    'Machine Learning': best_ml[['MAE', 'MSE', 'RMSE', 'R2 Score']],
    'Deep Learning': best_dl[['MAE', 'MSE', 'RMSE', 'R2 Score']]
})

print("\nBest Machine Learning Model:", best_ml['Model'])
print("Best Deep Learning Model:", best_dl['Model'])
print("\nMachine Learning vs Deep Learning - Best Models")
print(best_comparison.round(4))


# ==========================================================
# 36. BEST MACHINE LEARNING VS DEEP LEARNING GRAPH
# ==========================================================

# Create a DataFrame containing the two best-performing models.
best_models_graph = pd.DataFrame({
    'Model': [best_ml['Model'], best_dl['Model']],
    'Category': ['Machine Learning', 'Deep Learning'],
    'R2 Score': [best_ml['R2 Score'], best_dl['R2 Score']],
    'RMSE': [best_ml['RMSE'], best_dl['RMSE']]
})

# Create only one graph.
fig, ax = plt.subplots(figsize=(8, 5))

# Compare R2 Scores: Higher is better.
sns.barplot(
    data=best_models_graph,
    x='Category',
    y='R2 Score',
    hue='Category',
    palette='viridis',
    legend=False,
    ax=ax
)

ax.set_title('Best ML vs DL - R2 Score (Higher is Better)')
ax.set_xlabel('Model Type')
ax.set_ylabel('R2 Score')
ax.set_ylim(0, max(1.0, best_models_graph['R2 Score'].max() * 1.08))

# Display each model name and its R2 Score above the bar.
for i, row in best_models_graph.iterrows():
    ax.text(i, row['R2 Score'] + 0.015,
            f"{row['Model']}\n{row['R2 Score']:.4f}",
            ha='center', fontsize=10)

# Display the final comparison graph.
plt.suptitle('Best Machine Learning Model vs Best Deep Learning Model', fontsize=14)
plt.tight_layout()
plt.show()


# ==========================================================
# END OF UPDATED DIAMONDS PRICE PREDICTION PROJECT
# ==========================================================
