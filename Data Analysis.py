import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Input dataset
data = list(map(float, input("Enter the dataset (space-separated): ").split()))

# Create Pandas Series
s = pd.Series(data)

# Descriptive Statistics
mean = s.mean()
median = s.median()
mode = s.mode().tolist()
variance = s.var()
std_dev = s.std()

# Quartiles
Q1 = s.quantile(0.25)
Q2 = s.quantile(0.50)
Q3 = s.quantile(0.75)

# Interquartile Range
IQR = Q3 - Q1

# Display Results
print("\n========== Descriptive Statistics ==========")
print(f"Dataset               : {list(s)}")
print(f"Mean                  : {mean:.2f}")
print(f"Median                : {median:.2f}")
print(f"Mode                  : {mode}")
print(f"Variance              : {variance:.2f}")
print(f"Standard Deviation    : {std_dev:.2f}")
print(f"First Quartile (Q1)   : {Q1:.2f}")
print(f"Second Quartile (Q2)  : {Q2:.2f}")
print(f"Third Quartile (Q3)   : {Q3:.2f}")
print(f"Interquartile Range   : {IQR:.2f}")

# Histogram
plt.figure(figsize=(4, 4))
plt.hist(s, bins='auto', color='skyblue', edgecolor='black')
plt.title("Histogram of Dataset")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Box Plot
plt.figure(figsize=(3, 4))
plt.boxplot(s, vert=False)
plt.title("Box Plot of Dataset")
plt.xlabel("Values")
plt.grid(True)
plt.show()