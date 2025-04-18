import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

data_folder = os.path.join(current_dir, "dataset", "mturkfitbit_export_4.12.16-5.12.16", "Fitabase Data 4.12.16-5.12.16")
sleep_file = os.path.abspath(os.path.join(data_folder, "sleepDay_merged.csv"))
activity_file = os.path.abspath(os.path.join(data_folder, "dailyActivity_merged.csv"))

print("Sleep data path:", sleep_file)
print("Activity data path:", activity_file)

# Load sleep and activity data
sleep = pd.read_csv(sleep_file)
activity = pd.read_csv(activity_file)

# Convert date columns to datetime format
sleep['SleepDay'] = pd.to_datetime(sleep['SleepDay'], format='%m/%d/%Y %I:%M:%S %p')
activity['ActivityDate'] = pd.to_datetime(activity['ActivityDate'])

# Merge both datasets on Id and date
merged = pd.merge(
    sleep,
    activity,
    left_on=['Id', 'SleepDay'],
    right_on=['Id', 'ActivityDate'],
    how='inner'  # keep only records that exist in both tables
)

# Calculate sleep efficiency = minutes asleep / total time in bed
merged['SleepEfficiency'] = merged['TotalMinutesAsleep'] / merged['TotalTimeInBed']

# Remove invalid rows where time in bed or asleep is 0
merged = merged[(merged['TotalTimeInBed'] > 0) & (merged['TotalMinutesAsleep'] > 0)]

# Create calorie group for A/B testing: High >= 2200, Low < 2200
merged['CaloriesGroup'] = merged['Calories'].apply(lambda x: 'High' if x >= 2200 else 'Low')

# Print group distribution
print(merged['CaloriesGroup'].value_counts())

# Preview key columns
merged[['Id', 'SleepDay', 'Calories', 'SleepEfficiency', 'CaloriesGroup']].head()

# Export cleaned and merged dataset for Tableau use
merged.to_csv('calories_sleep_merged.csv', index=False)
