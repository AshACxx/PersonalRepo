"""
Air Quality Monitoring Dashboard Challenge
Lab 06 - Seaborn Statistical Visualization
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("=" * 65)
print("AIR QUALITY MONITORING DASHBOARD")
print("=" * 65)

# --- Generate Air Quality Dataset ---
print("\n--- Generating Air Quality Data ---\n")

np.random.seed(42)

# Parameters
n_hours = 24
samples_per_hour = 60  # 1-minute readings
locations = ['Urban', 'Suburban', 'Industrial']

data_records = []

for location in locations:
    for hour in range(n_hours):
        for minute in range(samples_per_hour):
            time_hours = hour + minute / 60

            # Base patterns by location
            if location == 'Urban':
                base_pm25 = 35 + 20 * np.sin(np.pi * (time_hours - 6) / 12)  # Peak at noon
                base_co2 = 500 + 100 * np.sin(np.pi * (time_hours - 8) / 10)  # Rush hours
                base_temp = 22 + 3  # Urban heat island
            elif location == 'Suburban':
                base_pm25 = 20 + 10 * np.sin(np.pi * (time_hours - 6) / 12)
                base_co2 = 420 + 50 * np.sin(np.pi * (time_hours - 8) / 10)
                base_temp = 21
            else:  # Industrial
                base_pm25 = 50 + 30 * np.sin(np.pi * (time_hours - 8) / 8)  # Work hours peak
                base_co2 = 550 + 150 * np.sin(np.pi * (time_hours - 9) / 8)
                base_temp = 23 + 2  # Industrial heat

            # Daily temperature cycle (same pattern, different offsets)
            temp_cycle = 5 * np.sin(np.pi * (time_hours - 6) / 12)

            record = {
                'time_hours': time_hours,
                'hour': hour,
                'location': location,
                'temperature': base_temp + temp_cycle + np.random.normal(0, 0.5),
                'humidity': 55 - 10 * np.sin(np.pi * (time_hours - 6) / 12) + np.random.normal(0, 3),
                'pm25': max(5, base_pm25 + np.random.normal(0, 5)),
                'co2': max(350, base_co2 + np.random.normal(0, 20))
            }
            data_records.append(record)

df = pd.DataFrame(data_records)

# Add time of day category
df['time_of_day'] = pd.cut(df['hour'], 
                            bins=[-1, 6, 12, 18, 24], 
                            labels=['Night', 'Morning', 'Afternoon', 'Evening'])

# Add air quality index category based on PM2.5
def pm25_category(pm):
    if pm < 12:
        return 'Good'
    elif pm < 35:
        return 'Moderate'
    elif pm < 55:
        return 'Unhealthy-Sensitive'
    else:
        return 'Unhealthy'

df['air_quality'] = df['pm25'].apply(pm25_category)

print(f"Dataset shape: {df.shape}")
print(f"\nLocations: {df['location'].unique()}")
print(f"\nSample data:")
print(df.head(10))

print(f"\n--- Summary Statistics by Location ---\n")
summary = df.groupby('location')[['temperature', 'humidity', 'pm25', 'co2']].agg(['mean', 'std'])
print(summary.round(2))

# --- YOUR CHALLENGE TASKS ---
print("\n" + "=" * 65)
print("CHALLENGE TASKS")
print("=" * 65)

"""
TASK: Distribution Analysis
=========================================
Create a figure with 4 subplots showing the distribution of PM2.5:
1. Histogram of PM2.5 for all locations combined (with KDE)
2. Overlapping KDE plots of PM2.5 by location
3. Box plot of PM2.5 by location
4. Violin plot of PM2.5 by time of day, colored by location

Requirements:
- Use appropriate titles for each subplot
- Use a consistent color palette
- Save as 'task1_distributions.png'
"""

# YOUR CODE FOR TASK HERE:
# --------------------------
print("\nTask 1: Distribution Analysis")
print("-" * 40)

# Example structure (complete this):
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# 1. Histogram of PM2.5 (all locations)
sns.histplot(data = df, x = 'pm25', kde = True, ax = axes[0,0] ,color = 'skyblue')

# 2. KDE by location
sns.kdeplot(data = df, x = 'pm25', hue = 'location', fill = True, ax = axes[0,1], palette = 'Set2')

# 3. Box plot by location
sns.boxplot(data = df, x = 'location', y = 'pm25', ax = axes[1, 0])

# 4. Violin plot by time of day
sns.violinplot(data = df, x = 'time_of_day', y = 'pm25', hue = 'location', ax = axes[1, 1], palette = 'Set2')



plt.tight_layout()
plt.savefig('task_distributions.png', dpi=150)
plt.show()

print("Complete Task code above!")


#1 industrial has the highest pm2.5 levels

#2 afternoon has the most variation

#3 industrial has the worst air quality  

#4 the time of day with the worst air quality is the morning and afternoon, the best is the night and evening

#5 the correlation between temperature and pm2.5 is the higher the temp average the higher the pm

#6 histogram is chosen to show distribution of the pm2.5 levels, the kde plot is chosen to show the distribution by location, 
#the box plot is chosen to show the median and interquartile range of pm2.5 by location, and the violin plot is chosen to show the distribution of pm2.5 by time of day and location.