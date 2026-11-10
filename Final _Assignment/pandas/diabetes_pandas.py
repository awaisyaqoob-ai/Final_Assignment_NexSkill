
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)

# Dataset: Diabetes classification data
# Outcome 1 and 0 are provided labels, not a clinical diagnosis by this script.
data = pd.read_csv("diabetes.csv")

print("1. First five rows:\n", data.head())
print("2. Last five rows:\n", data.tail())
print("3. Dataset shape:", data.shape)
print("4. Column names:", data.columns.tolist())
print("5. Data types:\n", data.dtypes)
print("6. Missing values (NaN):\n", data.isnull().sum())
print("7. First five ages:\n", data["Age"].head())
print("8. Selected columns:\n", data[["Age", "Glucose", "BMI", "Outcome"]].head())
print("9. Average age:", data["Age"].mean())
print("10. Minimum age:", data["Age"].min())
print("11. Maximum age:", data["Age"].max())
print("12. Average glucose:", data["Glucose"].mean())
print("13. Average BMI:", data["BMI"].mean())
print("14. Outcome counts:\n", data["Outcome"].value_counts())
print("15. People over age 40:\n", data[data["Age"] > 40].head(10))
print("16. Glucose above 140:\n", data[data["Glucose"] > 140].head(10))
print("17. Rows with Outcome = 1:\n", data[data["Outcome"] == 1].head(10))
print("18. 10 youngest records:\n", data.sort_values("Age").head(10))
print("19. 10 highest glucose values:\n", data.sort_values("Glucose", ascending=False).head(10))
print("20. Average glucose by outcome:\n", data.groupby("Outcome")["Glucose"].mean().round(2))
print("21. Average BMI by outcome:\n", data.groupby("Outcome")["BMI"].mean().round(2))
print("22. Duplicate rows:", data.duplicated().sum())
print("23. Age summary:\n", data["Age"].describe())
print("24. Glucose and BMI correlation:", data["Glucose"].corr(data["BMI"]))
print("25. New column: age group")
data["Age_Group"] = data["Age"].apply(lambda age: "40 or younger" if age <= 40 else "Over 40")
print(data[["Age", "Age_Group"]].head(10))
# Important: Zero Glucose, BloodPressure, BMI, SkinThickness, and Insulin
# can mean missing measurements. isnull() does not detect those zeros.
# Optional: data.to_csv("diabetes_with_new_column.csv", index=False)
