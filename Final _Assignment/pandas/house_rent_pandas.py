
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)

# Dataset: Indian rental housing listings
# Column names such as "Furnishing Status" have spaces, so use square brackets.
data = pd.read_csv("House_Rent_Dataset.csv")

print("1. First five rows:\n", data.head())
print("2. Last five rows:\n", data.tail())
print("3. Dataset shape (rows, columns):", data.shape)
print("4. Column names:", data.columns.tolist())
print("5. Data types:\n", data.dtypes)
print("6. Missing values:\n", data.isnull().sum())
print("7. First five rents:\n", data["Rent"].head())
print("8. Selected columns:\n", data[["City", "BHK", "Rent"]].head())
print("9. Average rent:", data["Rent"].mean())
print("10. Minimum rent:", data["Rent"].min())
print("11. Maximum rent:", data["Rent"].max())
print("12. Median rent:", data["Rent"].median())
print("13. Number of rentals in each city:\n", data["City"].value_counts())
print("14. Houses with rent below 20000:\n", data[data["Rent"] < 20000].head(10))
print("15. 2 BHK rentals:\n", data[data["BHK"] == 2].head(10))
print("16. Furnished rentals:\n", data[data["Furnishing Status"] == "Furnished"].head(10))
print("17. 10 cheapest rentals:\n", data.sort_values("Rent").head(10))
print("18. 10 most expensive rentals:\n", data.sort_values("Rent", ascending=False).head(10))
print("19. Average rent by city:\n", data.groupby("City")["Rent"].mean().round(2))
print("20. Average rent by BHK:\n", data.groupby("BHK")["Rent"].mean().round(2))
print("21. Number of different cities:", data["City"].nunique())
print("22. Duplicate rows:", data.duplicated().sum())
print("23. Rent summary:\n", data["Rent"].describe())
print("24. Rent and size correlation:", data["Rent"].corr(data["Size"]))
print("25. Create new column: rent per unit of size")
data["Rent_per_Size"] = data["Rent"] / data["Size"].replace(0, float("nan"))
print(data[["Rent", "Size", "Rent_per_Size"]].head())
# Optional: data.to_csv("house_rent_with_new_column.csv", index=False)
