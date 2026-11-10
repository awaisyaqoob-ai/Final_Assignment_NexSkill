import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Read the CSV from the same folder as this Python file.
folder = Path(__file__).resolve().parent
DATA_FILE = folder / 'House_Rent_Dataset.csv'
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


# 1. Number of properties in each city
plt.figure(figsize=(9, 5))
sns.countplot(data=data, x="City", order=data["City"].value_counts().index, color="tab:blue")
plt.xticks(rotation=35)
plt.title("Properties in Each City")
show_chart(1, "city_count")

# 2. Rent distribution (remove only extreme values for a readable graph)
plt.figure(figsize=(8, 5))
sns.histplot(data=data[data["Rent"] <= data["Rent"].quantile(0.95)], x="Rent", bins=30, kde=True, color="tab:blue")
plt.title("Rent Distribution (Up to 95th Percentile)")
show_chart(2, "rent_distribution")

# 3. Number of properties by bedrooms (BHK)
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="BHK", color="tab:blue")
plt.title("Properties by Bedrooms")
show_chart(3, "bedrooms_count")

# 4. Rent compared with property size
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x="Size", y="Rent", alpha=0.4, color="tab:blue")
plt.title("Size vs Rent")
show_chart(4, "size_vs_rent")

# 5. Average rent in each city
plt.figure(figsize=(9, 5))
sns.barplot(data=data, x="City", y="Rent", errorbar=None, color="tab:blue")
plt.xticks(rotation=35)
plt.title("Average Rent by City")
show_chart(5, "average_rent_city")

# 6. Furnishing status counts
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="Furnishing Status", color="tab:blue")
plt.xticks(rotation=15)
plt.title("Furnishing Status")
show_chart(6, "furnishing_status")

# 7. Rent by bedroom count (show normal range for readability)
plt.figure(figsize=(9, 5))
sns.boxplot(data=data[data["Rent"] <= data["Rent"].quantile(0.95)], x="BHK", y="Rent", color="tab:blue")
plt.title("Rent by Bedrooms")
show_chart(7, "rent_by_bedrooms")

# 8. Bathroom counts
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="Bathroom", color="tab:blue")
plt.title("Number of Bathrooms")
show_chart(8, "bathroom_count")

# 9. Rent by furnishing status
plt.figure(figsize=(9, 5))
sns.barplot(data=data, x="Furnishing Status", y="Rent", errorbar=None, color="tab:blue")
plt.title("Average Rent by Furnishing")
show_chart(9, "rent_furnishing")

# 10. Correlation heatmap (numeric columns only)
plt.figure(figsize=(7, 5))
sns.heatmap(data[["BHK", "Rent", "Size", "Bathroom"]].corr(), annot=True, cmap="Blues")
plt.title("Property Features Correlation")
show_chart(10, "correlation")
