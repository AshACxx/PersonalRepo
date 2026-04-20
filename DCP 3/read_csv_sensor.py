"""
Reading Temperature Sensor Data from CSV
"""

import csv
import numpy as np

print("=" * 55)
print("READING CSV SENSOR DATA")
print("=" * 55)

# --- Create Sample CSV Data ---
print("\n--- Creating Sample CSV ---\n")

csv_content = """timestamp,sensor_id,temperature,unit,quality
2026-02-03T10:00:00,TEMP_101,22.5,celsius,good
2026-02-03T10:00:01,TEMP_101,22.6,celsius,good
2026-02-03T10:00:02,TEMP_101,22.4,celsius,good
2026-02-03T10:00:03,TEMP_101,22.7,celsius,good
2026-02-03T10:00:04,TEMP_101,22.3,celsius,good
2026-02-03T10:00:05,TEMP_101,22.8,celsius,good
2026-02-03T10:00:06,TEMP_101,22.5,celsius,good
2026-02-03T10:00:07,TEMP_101,22.6,celsius,good
2026-02-03T10:00:08,TEMP_101,22.4,celsius,good
2026-02-03T10:00:09,TEMP_101,22.7,celsius,good"""

# Write to file
with open("temperature_readings.csv", "w") as f:
    f.write(csv_content)
print("Created: temperature_readings.csv")

# --- Method 1: Basic csv.reader ---
print("\n--- Method 1: csv.reader ---\n")

temperatures_list = []
timestamps_list = []

with open("temperature_readings.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header row
    print(f"Header: {header}")

    for row in reader:
        timestamps_list.append(row[0])
        temperatures_list.append(float(row[2]))  # Convert to float!

print(f"Loaded {len(temperatures_list)} readings")
print(f"Temps (list): {temperatures_list[:5]}")

# --- Method 2: csv.DictReader ---
print("\n--- Method 2: csv.DictReader ---\n")

with open("temperature_readings.csv", "r") as f:
    reader = csv.DictReader(f)

    # Access by column name (more readable!)
    for i, row in enumerate(reader):
        if i < 3:  # Show first 3
            print(f"  {row['timestamp']}: {row['temperature']}°{row['unit'][0].upper()}")

# --- Convert to NumPy Arrays ---
print("\n--- Converting to NumPy ---\n")

temperatures = np.array(temperatures_list, dtype=np.float64)
timestamps = np.array(timestamps_list, dtype="datetime64[s]")

print(f"Temperatures: shape={temperatures.shape}, dtype={temperatures.dtype}")
print(f"Timestamps: dtype={timestamps.dtype}")
print(f"Values: {temperatures}")

# --- NumPy Statistical Analysis ---
print("\n--- Statistical Analysis ---\n")

print(f"Mean: {np.mean(temperatures):.2f}°C")
print(f"Std:  {np.std(temperatures):.2f}°C")
print(f"Min:  {np.min(temperatures):.2f}°C")
print(f"Max:  {np.max(temperatures):.2f}°C")
print(f"Range: {np.ptp(temperatures):.2f}°C")  # ptp = peak-to-peak

print("\n" + "=" * 55)