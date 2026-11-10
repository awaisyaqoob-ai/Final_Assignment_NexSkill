

import numpy as np
import pandas as pd

# Pandas is used only to read the CSV file. NumPy performs the calculations.
data = pd.read_csv('diabetes.csv')

# Convert each useful column into a NumPy array.
ages = np.array(data['Age'])
glucose = np.array(data['Glucose'])
bmi = np.array(data['BMI'])
blood_pressure = np.array(data['BloodPressure'])
pregnancies = np.array(data['Pregnancies'])
insulin = np.array(data['Insulin'])
outcome = np.array(data['Outcome'])

print('1. Number of records:', len(ages))
print('2. Number of rows and columns:', data.shape)
print('3. First 5 ages:', ages[:5])
print('4. First 5 glucose values:', glucose[:5])
print('5. Average age:', round(np.mean(ages), 2))
print('6. Youngest age:', np.min(ages))
print('7. Oldest age:', np.max(ages))
print('8. Median age:', np.median(ages))
print('9. Average glucose:', round(np.mean(glucose), 2))
print('10. Highest glucose:', np.max(glucose))
print('11. Lowest recorded glucose:', np.min(glucose))
print('12. Average BMI:', round(np.mean(bmi), 2))
print('13. BMI standard deviation:', round(np.std(bmi), 2))
print('14. Average blood pressure:', round(np.mean(blood_pressure), 2))
print('15. People older than 40:', np.sum(ages > 40))
print('16. Ages older than 40 (first 10):', ages[ages > 40][:10])
print('17. Records with glucose greater than 140:', np.sum(glucose > 140))
print('18. Lowest 5 ages:', np.sort(ages)[:5])
print('19. Highest 5 glucose values:', np.sort(glucose)[-5:])
print('20. Unique pregnancy counts:', np.unique(pregnancies))
print('21. Records with positive outcome:', np.sum(outcome == 1))
print('22. Records with negative outcome:', np.sum(outcome == 0))
print('23. Percentage with positive outcome:', round(np.mean(outcome == 1) * 100, 2), '%')
print('24. Average age by outcome:')
print('    Outcome 0:', round(np.mean(ages[outcome == 0]), 2))
print('    Outcome 1:', round(np.mean(ages[outcome == 1]), 2))
print('25. Average glucose by outcome:')
print('    Outcome 0:', round(np.mean(glucose[outcome == 0]), 2))
print('    Outcome 1:', round(np.mean(glucose[outcome == 1]), 2))

