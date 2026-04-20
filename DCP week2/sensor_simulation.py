import numpy as np
import json 

print("=" * 50)
print("SIMULATING SENSOR DATA WITH NUMPY")
print("=" * 50)

# --- Generate Temperature Data ---
print("--- Generating Temperature Data ---  ")

num_readings = 100
base_temp = 22.0
noise_level = 0.5

np.random.seed(42) # For reproducibility
temperatures  = base_temp + np.random.normal(0, noise_level, num_readings) # Add Gaussian noise
temperatures = np.round(temperatures, 2)

print(f"Genrated: {num_readings} readings")
print(f"First 10 readings: {temperatures[:10]}")

print("")

# --- Generate Timestamps ---
print("--- Generating Timestamps ---")

start_time = np.datetime64("2024-01-15T10:00:00")
timestamps = start_time + np.arange(num_readings).astype('timedelta64[s]')
print(f"Start: {timestamps[0]}")
print(f"End: {timestamps[-1]}")
print(f"dtype: {timestamps.dtype}")


# --- Convert to JSON Format ---
print("--- Converting to JSON ---")

def create_json_readings(temps, times, sensor_id="TEMP_001"):
    readings = []
    for i in range(len(temps)):
        readings.append({
            "sensor_id": sensor_id,
            "timestamp": str(times[i]) + "Z",
            "value": float(temps[i]),
            "unit": "celsius"
        })
    return readings

# Add some anomalies
temperatures_with_anomalies = temperatures.copy()
anomaly_indices = [10, 25, 50, 75, 90]
temperatures_with_anomalies[anomaly_indices] = [15.0, 32.0, 14.5, 33.0, 16.0]

readings = create_json_readings(temperatures_with_anomalies, timestamps)


# Save to file
with open("sensor_data.json", "w") as f:
    json.dump(readings, f, indent=2)

print(f"Saved {len(readings)} readings to sensor_data.json")
print(f"Sample reading: {json.dumps(readings[1])}")

print("" + "=" * 50)