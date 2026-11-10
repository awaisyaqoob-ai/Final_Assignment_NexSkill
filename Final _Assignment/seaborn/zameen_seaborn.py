import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Read the CSV from the same folder as this Python file.
folder = Path(__file__).resolve().parent
DATA_FILE = folder / 'zameencom-property-data-By-Kaggle-Short.csv'
data = pd.read_csv(DATA_FILE, sep=";")

# Show charts in separate windows. Close each chart to see the next one.
sns.set_theme(style="whitegrid")

print("Total rows and columns:", data.shape)
print("Column names:", list(data.columns))

def show_chart(number, name):
    plt.tight_layout()
    print(f"Displaying chart {number}: {name}")
    plt.show()
    plt.close()


# 1. Property type counts
plt.figure(figsize=(9, 5))
sns.countplot(data=data, x="property_type", order=data["property_type"].value_counts().index, color="tab:blue")
plt.xticks(rotation=35)
plt.title("Property Types")
show_chart(1, "property_types")

# 2. Price distribution (cropped at 95th percentile to improve readability)
plt.figure(figsize=(8, 5))
sns.histplot(data=data[data["price"] <= data["price"].quantile(0.95)], x="price", bins=20, kde=True, color="tab:blue")
plt.title("Property Price Distribution")
show_chart(2, "price_distribution")

# 3. Number of bedrooms
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="bedrooms", color="tab:blue")
plt.title("Bedroom Counts")
show_chart(3, "bedroom_counts")

# 4. Number of bathrooms
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="baths", color="tab:blue")
plt.title("Bathroom Counts")
show_chart(4, "bathroom_counts")

# 5. Average price by property type
plt.figure(figsize=(9, 5))
sns.barplot(data=data, x="property_type", y="price", errorbar=None, color="tab:blue")
plt.xticks(rotation=35)
plt.title("Average Price by Property Type")
show_chart(5, "price_by_type")

# 6. Bedrooms compared with price
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x="bedrooms", y="price", hue="property_type", color="tab:blue")
plt.title("Bedrooms vs Price")
show_chart(6, "bedrooms_vs_price")

# 7. Top 8 property locations
popular = data["location"].value_counts().head(8).index
plt.figure(figsize=(10, 5))
sns.countplot(data=data[data["location"].isin(popular)], y="location", order=popular, color="tab:blue")
plt.title("Top 8 Locations")
show_chart(7, "top_locations")

# 8. Property prices by bedroom count (hide extreme prices)
plt.figure(figsize=(9, 5))
sns.boxplot(data=data[data["price"] <= data["price"].quantile(0.95)], x="bedrooms", y="price", color="tab:blue")
plt.title("Price by Bedrooms")
show_chart(8, "price_by_bedrooms")

# 9. Most common area sizes (area is stored as text)
areas = data["area"].value_counts().head(8).index
plt.figure(figsize=(9, 5))
sns.countplot(data=data[data["area"].isin(areas)], y="area", order=areas, color="tab:blue")
plt.title("Most Common Area Sizes")
show_chart(9, "popular_areas")

# 10. Correlation of numerical features
plt.figure(figsize=(7, 5))
sns.heatmap(data[["price", "bedrooms", "baths", "latitude", "longitude"]].corr(), annot=True, cmap="Blues")
plt.title("Numeric Features Correlation")
show_chart(10, "correlation")
