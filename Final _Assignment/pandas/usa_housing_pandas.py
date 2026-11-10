
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)

# Dataset: USA house sale listings. Prices are in US dollars.
data = pd.read_csv("USA Housing Dataset.csv")

print("1. First five rows:\n", data.head())
print("2. Last five rows:\n", data.tail())
print("3. Dataset shape:", data.shape)
print("4. Column names:", data.columns.tolist())
print("5. Data types:\n", data.dtypes)
print("6. Missing values:\n", data.isnull().sum())
print("7. First five prices:\n", data["price"].head())
print("8. Selected columns:\n", data[["city", "price", "bedrooms", "sqft_living"]].head())
print("9. Average house price:", data["price"].mean())
print("10. Lowest recorded price:", data["price"].min())
print("11. Highest price:", data["price"].max())
print("12. Median price:", data["price"].median())
print("13. Cities with most listings:\n", data["city"].value_counts().head(10))
print("14. Houses with at least 4 bedrooms:\n", data[data["bedrooms"] >= 4].head(10))
print("15. Houses costing over $1,000,000:\n", data[data["price"] > 1000000].head(10))
print("16. Houses in Seattle:\n", data[data["city"] == "Seattle"].head(10))
print("17. 10 lowest recorded prices:\n", data.sort_values("price").head(10))
print("18. 10 highest prices:\n", data.sort_values("price", ascending=False).head(10))
print("19. Average price by city (top 10):\n", data.groupby("city")["price"].mean().sort_values(ascending=False).head(10))
print("20. Average price by bedrooms:\n", data.groupby("bedrooms")["price"].mean().round(2))
print("21. Number of cities:", data["city"].nunique())
print("22. Duplicate rows:", data.duplicated().sum())
print("23. Price summary:\n", data["price"].describe())
print("24. Price and living area correlation:", data["price"].corr(data["sqft_living"]))
print("25. New column: price per square foot")
# Zero prices are recorded in this dataset; check these before price modeling.
data["price_per_sqft"] = data["price"] / data["sqft_living"].replace(0, float("nan"))
print(data[["price", "sqft_living", "price_per_sqft"]].head())
# Optional: data.to_csv("usa_housing_with_new_column.csv", index=False)
