
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)

# Dataset: Zameen.com property sale listings (Lahore)
# Important: This CSV separates values with semicolons (;), not commas.
data = pd.read_csv("zameencom-property-data-By-Kaggle-Short.csv", sep=";")

print("1. First five rows:\n", data.head())
print("2. Last five rows:\n", data.tail())
print("3. Dataset shape:", data.shape)
print("4. Column names:", data.columns.tolist())
print("5. Data types:\n", data.dtypes)
print("6. Missing values:\n", data.isnull().sum())
print("7. Prices:\n", data["price"].head())
print("8. Selected columns:\n", data[["property_type", "location", "price", "bedrooms"]].head())
print("9. Average price:", data["price"].mean())
print("10. Lowest price:", data["price"].min())
print("11. Highest price:", data["price"].max())
print("12. Median price:", data["price"].median())
print("13. Property types:\n", data["property_type"].value_counts())
print("14. Listings by location (top 10):\n", data["location"].value_counts().head(10))
print("15. Houses only:\n", data[data["property_type"] == "House"].head(10))
print("16. Properties with 3 or more bedrooms:\n", data[data["bedrooms"] >= 3].head(10))
print("17. Properties below 10 million PKR:\n", data[data["price"] < 10000000].head(10))
print("18. Cheapest 10 listings:\n", data.sort_values("price").head(10))
print("19. Most expensive 10 listings:\n", data.sort_values("price", ascending=False).head(10))
print("20. Average price by property type:\n", data.groupby("property_type")["price"].mean().round(2))
print("21. Average price by bedrooms:\n", data.groupby("bedrooms")["price"].mean().round(2))
print("22. Different locations:", data["location"].nunique())
print("23. Duplicate rows:", data.duplicated().sum())
print("24. Price summary:\n", data["price"].describe())
print("25. New column: price in millions of PKR")
data["price_millions"] = data["price"] / 1000000
print(data[["price", "price_millions"]].head())
# Optional: data.to_csv("zameen_with_new_column.csv", index=False)
