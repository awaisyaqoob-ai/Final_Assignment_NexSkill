

import numpy as np
import pandas as pd
from pathlib import Path

# 1. Load the CSV file (keep it in the same folder as this Python file)
file_path = Path("House_Rent_Dataset.csv").with_name('House_Rent_Dataset.csv')
data = pd.read_csv(file_path)
print('1. First 5 rows:')
print(data.head())

# 2. Convert selected columns into NumPy arrays
rent = np.array(data['Rent'])
size = np.array(data['Size'])
bhk = np.array(data['BHK'])
bathrooms = np.array(data['Bathroom'])
city = np.array(data['City'])

print('\n2. First 10 rent values:')
print(rent[:10])
print('Array type:', type(rent))

# 3. Count the total properties
print('\n3. Total properties:', len(rent))

# 4. Find the minimum, maximum, and average rent
print('\n4. Minimum rent:', np.min(rent))
print('Maximum rent:', np.max(rent))
print('Average rent:', round(np.mean(rent), 2))

# 5. Find the median rent
print('\n5. Median rent:', np.median(rent))

# 6. Find total rent and standard deviation
print('\n6. Sum of rents:', np.sum(rent))
print('Standard deviation of rent:', round(np.std(rent), 2))

# 7. Calculate average property size
print('\n7. Average property size:', round(np.mean(size), 2))

# 8. Find the largest and smallest properties
print('\n8. Smallest size:', np.min(size))
print('Largest size:', np.max(size))

# 9. Filter properties with rent below 20,000
cheap_rent = rent[rent < 20000]
print('\n9. Number of properties with rent below 20,000:', len(cheap_rent))
print('First 10 matching rents:', cheap_rent[:10])

# 10. Filter properties with 2 bedrooms
rent_2bhk = rent[bhk == 2]
print('\n10. Number of 2 BHK properties:', len(rent_2bhk))
print('Average rent for 2 BHK:', round(np.mean(rent_2bhk), 2))

# 11. Filter properties with 2 bedrooms AND 2 bathrooms
condition = (bhk == 2) & (bathrooms == 2)
print('\n11. Properties with 2 bedrooms and 2 bathrooms:', np.sum(condition))

# 12. Sort rent in ascending order
sorted_rent = np.sort(rent)
print('\n12. Lowest 10 rent values:', sorted_rent[:10])
print('Highest 10 rent values:', sorted_rent[-10:])

# 13. Find all cities in the dataset
unique_cities = np.unique(city)
print('\n13. Cities:', unique_cities)

# 14. Calculate average rent for each city
print('\n14. Average rent by city:')
for name in unique_cities:
    city_rent = rent[city == name]
    print(name, ':', round(np.mean(city_rent), 2))

# 15. Find the property with the highest rent
highest_index = np.argmax(rent)
print('\n15. Property with highest rent:')
print(data.iloc[highest_index][['City', 'BHK', 'Rent', 'Size']])

# 16. Find the percentage of properties costing under 20,000
percentage = (np.sum(rent < 20000) / len(rent)) * 100
print('\n16. Percentage with rent below 20,000:', round(percentage, 2), '%')

# 17. Find the correlation between rent and size
correlation = np.corrcoef(rent, size)[0, 1]
print('\n17. Correlation between rent and size:', round(correlation, 3))

