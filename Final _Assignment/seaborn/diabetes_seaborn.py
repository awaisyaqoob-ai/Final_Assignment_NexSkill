import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Read the CSV from the same folder as this Python file.
folder = Path(__file__).resolve().parent
DATA_FILE = folder / 'diabetes.csv'
data = pd.read_csv(DATA_FILE)

# Show charts in separate windows. Close each chart to see the next one.
sns.set_theme(style="whitegrid")

print("Total rows and columns:", data.shape)
print("Column names:", list(data.columns))

def show_chart(number, name):
    plt.tight_layout()
    print(f"Graph  {number}: {name}")
    plt.show()
    plt.close()


# Outcome is the dataset's classification label (not a clinical diagnosis).
# Some zero measurements may represent missing data. These examples keep original values.

# 1. Counts of outcome values
plt.figure(figsize=(7, 5))
sns.countplot(data=data, x="Outcome", color="tab:blue")
plt.title("Outcome Counts (0 and 1)")
show_chart(1, "outcome_counts")

# 2. Distribution of age
plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="Age", bins=20, kde=True, color="tab:blue")
plt.title("Age Distribution")
show_chart(2, "age_distribution")

# 3. Distribution of glucose
plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="Glucose", bins=25, kde=True, color="tab:blue")
plt.title("Glucose Distribution")
show_chart(3, "glucose_distribution")

# 4. BMI distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="BMI", bins=25, kde=True, color="tab:blue")
plt.title("BMI Distribution")
show_chart(4, "bmi_distribution")

# 5. Glucose levels by outcome
plt.figure(figsize=(8, 5))
sns.boxplot(data=data, x="Outcome", y="Glucose", color="tab:blue")
plt.title("Glucose by Outcome")
show_chart(5, "glucose_outcome")

# 6. Age vs BMI
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x="Age", y="BMI", hue="Outcome", alpha=0.6, color="tab:blue")
plt.title("Age vs BMI")
show_chart(6, "age_vs_bmi")

# 7. Average glucose by outcome
plt.figure(figsize=(8, 5))
sns.barplot(data=data, x="Outcome", y="Glucose", errorbar=None, color="tab:blue")
plt.title("Average Glucose by Outcome")
show_chart(7, "average_glucose_outcome")

# 8. Pregnancies distribution
plt.figure(figsize=(9, 5))
sns.countplot(data=data, x="Pregnancies", color="tab:blue")
plt.title("Pregnancies Count")
show_chart(8, "pregnancies")

# 9. Blood pressure vs glucose
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x="BloodPressure", y="Glucose", hue="Outcome", alpha=0.6, color="tab:blue")
plt.title("Blood Pressure vs Glucose")
show_chart(9, "pressure_glucose")

# 10. Numeric correlation heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(data.corr(numeric_only=True), annot=True, fmt=".2f", cmap="Blues")
plt.title("Diabetes Data Correlation")
show_chart(10, "correlation")
