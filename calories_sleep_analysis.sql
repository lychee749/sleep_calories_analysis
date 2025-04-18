SELECT *
FROM `bellabeat-analysis-453612.sleep_analysis.calories_sleep_merged`
LIMIT 100;

-- Calculate the number of records and average sleep efficiency for each calorie group
SELECT
  CaloriesGroup,                                 -- Group: 'High' or 'Low' based on daily calories burned
  COUNT(*) AS record_count,                      -- Total number of records in each group
  ROUND(AVG(SleepEfficiency), 4) AS avg_sleep_efficiency  -- Average sleep efficiency per group, rounded to 4 decimals
FROM `bellabeat-analysis-453612.sleep_analysis.calories_sleep_merged`
GROUP BY CaloriesGroup
ORDER BY CaloriesGroup;

-- Calculate the Pearson correlation between daily calories burned and sleep efficiency
SELECT
  CORR(CAST(Calories AS FLOAT64), CAST(SleepEfficiency AS FLOAT64)) AS calories_sleep_corr
FROM `bellabeat-analysis-453612.sleep_analysis.calories_sleep_merged`;

-- Get sample size, mean, and standard deviation for each CaloriesGroup
SELECT
  CaloriesGroup,
  COUNT(*) AS sample_size,
  ROUND(AVG(SleepEfficiency), 4) AS mean_efficiency,
  ROUND(STDDEV(SleepEfficiency), 4) AS std_dev
FROM `bellabeat-analysis-453612.sleep_analysis.calories_sleep_merged`
GROUP BY CaloriesGroup
ORDER BY CaloriesGroup;

