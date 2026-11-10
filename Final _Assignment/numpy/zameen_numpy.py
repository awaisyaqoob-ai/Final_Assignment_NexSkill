

import numpy as np
import pandas as pd

# 1. Read the dataset (this CSV uses semicolons)
data = pd.read_csv('zameencom-property-data.csv', sep=';')
print('1. FIRST FIVE ROWS')
print(data.head())

# 2. Make NumPy arrays
prices = np.array(data['price'])
bedrooms = np.array(data['bedrooms'])
bathrooms = np.array(data['baths'])
areas = np.array(data['area'])
locations = np.array(data['location'])
types = np.array(data['property_type'])
print('\n2. FIRST FIVE PRICES')
print(prices[:5])

# 3. Number of properties
print('\n3. TOTAL PROPERTIES')
print(len(prices))

# 4. Average price
print('\n4. AVERAGE PRICE (PKR)')
print(np.mean(prices))

# 5. Highest and lowest price
print('\n5. HIGHEST AND LOWEST PRICE (PKR)')
print('Highest:', np.max(prices))
print('Lowest:', np.min(prices))

# 6. Median price
print('\n6. MEDIAN PRICE (PKR)')
print(np.median(prices))

# 7. Total property values
print('\n7. SUM OF ALL LISTED PRICES (PKR)')
print(np.sum(prices))

# 8. Average bedrooms and bathrooms
print('\n8. AVERAGE BEDROOMS AND BATHROOMS')
print('Bedrooms:', np.mean(bedrooms))
print('Bathrooms:', np.mean(bathrooms))

# 9. Find properties priced below 10 million PKR
print('\n9. PRICES BELOW 10 MILLION PKR')
print(prices[prices < 10000000])
print('Count:', np.sum(prices < 10000000))

# 10. Find properties with 5 or more bedrooms
print('\n10. PROPERTIES WITH AT LEAST 5 BEDROOMS')
print('Count:', np.sum(bedrooms >= 5))
print('First ten prices:', prices[bedrooms >= 5][:10])

# 11. Sort all prices from low to high
print('\n11. 10 CHEAPEST PRICES (PKR)')
print(np.sort(prices)[:10])

# 12. Sort all prices from high to low
print('\n12. 10 MOST EXPENSIVE PRICES (PKR)')
print(np.sort(prices)[-10:][::-1])

# 13. Count each property type
print('\n13. PROPERTY TYPES AND COUNTS')
unique_types, type_counts = np.unique(types, return_counts=True)
for i in range(len(unique_types)):
    print(unique_types[i], ':', type_counts[i])

# 14. Find average price of houses (if present)
print('\n14. AVERAGE HOUSE PRICE (PKR)')
house_prices = prices[types == 'House']
if len(house_prices) > 0:
    print(np.mean(house_prices))
else:
    print('No houses found')

# 15. Properties with 3 bedrooms and 3 bathrooms
print('\n15. PROPERTIES WITH 3 BEDROOMS AND 3 BATHROOMS')
match = (bedrooms == 3) & (bathrooms == 3)
print('Count:', np.sum(match))
print('Prices:', prices[match][:10])

# 16. Standard deviation of prices
print('\n16. STANDARD DEVIATION OF PRICES (PKR)')
print(np.std(prices))

# 17. Price percentiles
print('\n17. PRICE PERCENTILES (PKR)')
print('25th percentile:', np.percentile(prices, 25))
print('75th percentile:', np.percentile(prices, 75))

# 18. Unique areas (e.g. Marla / Kanal)
print('\n18. FIRST TEN UNIQUE AREA LABELS')
print(np.unique(areas)[:10])

# 19. Number of listings in Model Town
print('\n19. MODEL TOWN PROPERTY COUNT')
print(np.sum(locations == 'Model Town'))

# 20. Find most expensive property and its location
print('\n20. MOST EXPENSIVE PROPERTY')
index = np.argmax(prices)
print('Price (PKR):', prices[index])
print('Location:', locations[index])
print('Area:', areas[index])
print('Bedrooms:', bedrooms[index])

