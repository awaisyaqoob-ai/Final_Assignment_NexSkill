import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Read the CSV from the same folder as this Python file.
folder = Path(__file__).resolve().parent
DATA_FILE = folder / 'USA Housing Dataset.csv'
data = pd.read_csv(DATA_FILE)

# Show charts in separate windows. Close each chart to see the next one.
sns.set_theme(style="whitegrid")

print("Total rows and columns:", data.shape)
print("Column names:", list(data.columns))

def show_chart(number, name):
    plt.tight_layout()
    print(f"Displaying chart {number}: {name}")
    plt.show()
    plt.close()


# 1. House price distribution (exclude prices of zero and top 5% for readability)
valid = data[data["price"] > 0]
normal = valid[valid["price"] <= valid["price"].quantile(0.95)]
plt.figure(figsize=(8, 5))
sns.histplot(data=normal, x="price", bins=30, kde=True, color="tab:blue")
plt.title("USA House Price Distribution")
show_chart(1, "price_distribution")

# 2. Bedroom count
plt.figure(figsize=(8, 5))
sns.countplot(data=data[data["bedrooms"] <= 8], x="bedrooms", color="tab:blue")
plt.title("Number of Bedrooms")
show_chart(2, "bedroom_counts")

# 3. Price vs living area
plt.figure(figsize=(8, 5))
sns.scatterplot(data=normal, x="sqft_living", y="price", alpha=0.5, color="tab:blue")
plt.title("Living Area vs House Price")
show_chart(3, "size_vs_price")

# 4. Top 10 cities by number of homes
cities = data["city"].value_counts().head(10).index
plt.figure(figsize=(10, 6))
sns.countplot(data=data[data["city"].isin(cities)], y="city", order=cities, color="tab:blue")
plt.title("Top 10 Cities by Listings")
show_chart(4, "top_cities")

# 5. Average price across the 10 most common cities
plt.figure(figsize=(10, 6))
sns.barplot(data=data[data["city"].isin(cities) & (data["price"] > 0)], y="city", x="price", order=cities, errorbar=None, color="tab:blue")
plt.title("Average Price in Top Cities")
show_chart(5, "city_average_prices")

# 6. Condition counts
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="condition", color="tab:blue")
plt.title("House Condition Counts")
show_chart(6, "condition_counts")

# 7. Price by number of floors
plt.figure(figsize=(9, 5))
sns.boxplot(data=normal, x="floors", y="price", color="tab:blue")
plt.title("Price by Floors")
show_chart(7, "price_by_floors")

# 8. Construction year distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="yr_built", bins=25, color="tab:blue")
plt.title("Year Houses Were Built")
show_chart(8, "year_built")

# 9. Waterfront vs non-waterfront listings
plt.figure(figsize=(7, 5))
sns.countplot(data=data, x="waterfront", color="tab:blue")
plt.title("Waterfront Listings (0=No, 1=Yes)")
show_chart(9, "waterfront")

# 10. Price and house features correlation
plt.figure(figsize=(9, 6))
sns.heatmap(data[["price", "bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "condition", "yr_built"]].corr(), annot=True, fmt=".2f", cmap="Blues")
plt.title("USA Housing Correlation")
show_chart(10, "correlation")
