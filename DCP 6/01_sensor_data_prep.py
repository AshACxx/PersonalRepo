"""
Sensor Data Preparation for Visualization
Recap: Generating and processing sensor data with NumPy
"""

import numpy as np
import json

print("=" * 65)
print("SENSOR DATA PREPARATION FOR VISUALIZATION")
print("=" * 65)

np.random.seed(42)

# --- Generate Realistic Multi-Sensor Data ---
print("\n--- Generating Multi-Sensor Data ---\n")

# Simulation parameters
duration_hours = 24
samples_per_hour = 60  # 1-minute intervals
total_samples = duration_hours * samples_per_hour

print(f"Simulation: {duration_hours} hours at {samples_per_hour} samples/hour")
print(f"Total samples: {total_samples}")

# Time array (in hours for easier interpretation)
time_hours = np.linspace(0, duration_hours, total_samples, endpoint=False) #linspace generates linear space between 0 and 24 with total_sample points

# Temperature: daily cycle + random variation
base_temp = 20.0
daily_variation = 5 * np.sin(2 * np.pi * (time_hours - 6) / 24)  # Peak at 2 PM
noise = np.random.normal(0, 0.5, total_samples)
temperature = base_temp + daily_variation + noise

# Humidity: inverse relationship with temperature
base_humidity = 55
humidity = base_humidity - 1.5 * (temperature - base_temp) + np.random.normal(0, 2, total_samples)

#np.clip limits the humiditty values so that it does not drop below 20 or exceed 95 to remove outliers
humidity = np.clip(humidity, 20, 95)  # Physical constraints

# Pressure: slow atmospheric changes
base_pressure = 1013.25
pressure_trend = 3 * np.sin(2 * np.pi * time_hours / 48)  # 48-hour cycle
pressure = base_pressure + pressure_trend + np.random.normal(0, 0.8, total_samples)

# CO2 levels: activity patterns (higher during work hours)
base_co2 = 450
activity_pattern = 200 * np.where(
    (time_hours >= 9) & (time_hours <= 17),
    np.sin(np.pi * (time_hours - 9) / 8),  # Work hours peak
    0
)
co2 = base_co2 + activity_pattern + np.random.normal(0, 25, total_samples)
co2 = np.clip(co2, 350, 1500)

print(f"\nGenerated sensors:")
print(f"  Temperature: {temperature.min():.1f}°C to {temperature.max():.1f}°C")
print(f"  Humidity: {humidity.min():.1f}% to {humidity.max():.1f}%")
print(f"  Pressure: {pressure.min():.1f} hPa to {pressure.max():.1f} hPa")
print(f"  CO2: {co2.min():.0f} ppm to {co2.max():.0f} ppm")

# --- Combine into Structured Array ---
print("\n--- Creating Structured Data Array ---\n")

# Stack all sensors: shape (4, 1440) -> (1440, 4) after transpose
sensor_data = np.column_stack([temperature, humidity, pressure, co2])
sensor_names = ['temperature', 'humidity', 'pressure', 'co2']

print(f"Combined data shape: {sensor_data.shape}")
print(f"Columns: {sensor_names}")

# --- Calculate Summary Statistics ---
print("\n--- Summary Statistics ---\n")

for i, name in enumerate(sensor_names):
    data = sensor_data[:, i]
    print(f"{name.capitalize():12} | Mean: {np.mean(data):8.2f} | "
          f"Std: {np.std(data):6.2f} | "
          f"Min: {np.min(data):8.2f} | "
          f"Max: {np.max(data):8.2f}")

# --- Hourly Aggregation ---
print("\n--- Hourly Aggregation ---\n")

# Reshape for hourly analysis: (1440,) -> (24, 60)
temp_hourly = temperature.reshape(24, 60)

hourly_means = np.mean(temp_hourly, axis=1)
hourly_stds = np.std(temp_hourly, axis=1)

print("Hourly temperature (mean ± std):")
for hour in range(0, 24, 4):  # Print every 4 hours
    print(f"  Hour {hour:02d}: {hourly_means[hour]:.2f}°C ± {hourly_stds[hour]:.2f}")

# --- Save Data for Visualization ---
print("\n--- Saving Data for Visualization ---\n")

# Save as CSV-compatible format
header = "time_hours,temperature,humidity,pressure,co2"
combined_data = np.column_stack([time_hours, sensor_data]) #column_stack stacks the time_hours array on the top
np.savetxt('sensor_data.csv', combined_data, delimiter=',', 
           header=header, comments='', fmt='%.4f')

print("Data saved to 'sensor_data.csv'")

# Save as JSON for metadata
metadata = {
    "location": "Building A - Room 101",
    "duration_hours": int(duration_hours),
    "sample_rate": "1 per minute",
    "sensors": sensor_names,
    "statistics": {
        name: {
            "mean": float(np.mean(sensor_data[:, i])),
            "std": float(np.std(sensor_data[:, i])),
            "min": float(np.min(sensor_data[:, i])),
            "max": float(np.max(sensor_data[:, i]))
        }
        for i, name in enumerate(sensor_names)
    }
}

with open('sensor_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)

print("Metadata saved to 'sensor_metadata.json'")

# --- Correlation Analysis (Important for Visualization) ---
print("\n--- Correlation Matrix ---\n")

correlation_matrix = np.corrcoef(sensor_data.T)

print("Correlation between sensors:")
print(f"{'':>12}", end='')
for name in sensor_names:
    print(f"{name:>12}", end='')
print()

for i, name in enumerate(sensor_names):
    print(f"{name:>12}", end='')
    for j in range(len(sensor_names)):
        print(f"{correlation_matrix[i, j]:>12.3f}", end='')
    print()

print("\n" + "=" * 65)
print("Data prepared for visualization exercises!")
print("=" * 65)