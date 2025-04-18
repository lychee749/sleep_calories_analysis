from scipy import stats
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))

data_folder = os.path.join(current_dir, "dataset")
calories_sleep = os.path.abspath(os.path.join(data_folder, "calories_sleep_merged.csv"))
print("Calories Sleep Path:", calories_sleep)

# Load sleep and calories merged data
calories_sleep_merged = pd.read_csv(calories_sleep)
print(calories_sleep_merged.head())

# Split the data into two groups based on CaloriesGroup
high_group = calories_sleep_merged[calories_sleep_merged["CaloriesGroup"] == "High"]["SleepEfficiency"]
low_group = calories_sleep_merged[calories_sleep_merged["CaloriesGroup"] == "Low"]["SleepEfficiency"]

# Print basic information
print("High group count:", len(high_group))
print("Low group count:", len(low_group))

# Perform Welch's t-test (does not assume equal variance)
t_stat, p_value = stats.ttest_ind(high_group, low_group, equal_var=False)

# Print the results
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Set the style
sns.set(style="whitegrid")

# Prepare figure
plt.figure(figsize=(8, 5))

# Create the boxplot
sns.boxplot(x='CaloriesGroup', y='SleepEfficiency', data=calories_sleep_merged, palette=["#e74c3c","#2ecc71"])

# Add mean points on top of the boxplot
sns.pointplot(x='CaloriesGroup', y='SleepEfficiency', data=calories_sleep_merged,
              estimator=np.mean, color='black', markers='D', linestyles='')

# Add title and axis labels
plt.title('A/B Test: Sleep Efficiency by Calorie Group', fontsize=14)
plt.xlabel('Calories Group')
plt.ylabel('Sleep Efficiency')

# Show plot
plt.tight_layout()
plt.show()