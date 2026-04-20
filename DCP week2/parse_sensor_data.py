"""
Parsing Sensor Data from JSON Format
"""

import json
import numpy as np

print("=" * 50)
print("PARSING JSON SENSOR DATA")
print("=" * 50)

# --- Load JSON ---
print("--- Loading JSON ---")

with open("sensor_data.json", "r") as f:
    readings = json.load(f)

print(f"Loaded {len(readings)} readings")
print(f"Type: {type(readings)}")

# --- Examine Types ---
print("--- JSON to Python Types ---")

first = readings[0]
for key, value in first.items():
    print(f"  {key}: {type(value).__name__} = {value}")

# --- Convert to NumPy ---
print("--- Converting to NumPy ---")

values = np.array([r["value"] for r in readings], dtype=np.float64)
timestamps = np.array([r["timestamp"].replace("Z", "") for r in readings], 
                      dtype="datetime64[s]")

print(f"Values: shape={values.shape}, dtype={values.dtype}")
print(f"Timestamps: dtype={timestamps.dtype}")

# --- Analyze with NumPy ---
print("--- Analysis ---")

print(f"Mean: {np.mean(values):.2f}")
print(f"Std:  {np.std(values):.2f}")
print(f"Min:  {np.min(values):.2f}")
print(f"Max:  {np.max(values):.2f}")

# Find anomalies (outside 18-28 range)
is_anomaly = (values < 18) | (values > 28)
anomaly_indices = np.where(is_anomaly)[0]
anomaly_values = values[is_anomaly]

print(f"Anomalies found: {len(anomaly_values)}")
print(f"Indices: {anomaly_indices}")
print(f"Values: {anomaly_values}")

print("" + "=" * 50)