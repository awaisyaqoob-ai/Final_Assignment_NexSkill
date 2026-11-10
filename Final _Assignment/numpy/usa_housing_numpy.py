

import numpy as np
import pandas as pd
from pathlib import Path

# Pandas only reads the CSV. NumPy does the calculations below.
file_path = Path(__file__).with_name("USA Housing Dataset.csv")
data = pd.read_csv(file_path)

# Change CSV columns into NumPy arrays.
prices = data["price"].to_numpy()
bedrooms = data["bedrooms"].to_numpy()
bathrooms = data["bathrooms"].to_numpy()
sizes = data["sqft_living"].to_numpy()
lot_sizes = data["sqft_lot"].to_numpy()
floors = data["floors"].to_numpy()
waterfront = data["waterfront"].to_numpy()
condition = data["condition"].to_numpy()
years = data["yr_built"].to_numpy()
cities = data["city"].to_numpy()

print("1. Dataset shape (rows, columns):", data.shape)
print("2. First five house prices:", prices[:5])
print("3. Total houses:", len(prices))
print("4. Average price: $", round(np.mean(prices), 2))
print("5. Minimum price: $", np.min(prices))
print("6. Maximum price: $", np.max(prices))
print("7. Median price: $", np.median(prices))
print("8. Price standard deviation: $", round(np.std(prices), 2))
print("9. Average bedrooms:", round(np.mean(bedrooms), 2))
print("10. Average bathrooms:", round(np.mean(bathrooms), 2))
print("11. Average living area (sq ft):", round(np.mean(sizes), 2))

# Boolean filtering: keep items that match a condition.
expensive = prices[prices > 1_000_000]
print("12. Houses priced above $1,000,000:", len(expensive))
print("13. First 10 house prices below $300,000:", prices[prices < 300_000][:10])

# Conditions can be combined with & (AND).
large_family_homes = (bedrooms >= 4) & (sizes >= 2000)
print("14. Houses with 4+ bedrooms and 2000+ sq ft:", np.sum(large_family_homes))

print("15. Five cheapest prices:", np.sort(prices)[:5])
print("16. Five most expensive prices:", np.sort(prices)[-5:][::-1])

# Unique values and counts.
unique_bedrooms, bedroom_counts = np.unique(bedrooms, return_counts=True)
print("17. Bedroom values:", unique_bedrooms)
print("    Number of houses for each bedroom value:", bedroom_counts)

print("18. Waterfront houses:", np.sum(waterfront == 1))
print("19. Houses built in or after 2000:", np.sum(years >= 2000))

# Find the location of the biggest value in an array.
most_expensive_index = np.argmax(prices)
print("20. City of most expensive home:", cities[most_expensive_index])

# Use the same boolean mask to compare cities.
seattle_mask = cities == "Seattle"
print("21. Seattle properties:", np.sum(seattle_mask))
print("    Average Seattle price: $", round(np.mean(prices[seattle_mask]), 2))

# Calculate new data using arrays.
price_per_sqft = np.divide(prices, sizes, out=np.zeros_like(prices), where=sizes != 0)
print("22. First 5 prices per square foot:", np.round(price_per_sqft[:5], 2))

print("23. 25th, 50th and 75th price percentiles:", np.percentile(prices, [25, 50, 75]))
print("24. Correlation between size and price:", round(np.corrcoef(sizes, prices)[0, 1], 3))
print("25. Different cities in dataset:", len(np.unique(cities)))
