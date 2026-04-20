"""
Classroom Challenge: Humidity Sensor Analysis
"""

import json
import numpy as np

# --- Create Sample Data ---
def create_humidity_data():
    np.random.seed(123)
    humidity = 55.0 + np.random.normal(0, 5.0, 60)
    humidity = np.clip(np.round(humidity, 1), 20, 90)

    # Add anomalies (< 30 or > 70)
    humidity[[10, 25, 45]] = [25.0, 78.0, 22.0]

    start = np.datetime64("2024-01-15T14:00:00")
    timestamps = start + np.arange(60).astype("timedelta64[m]")

    readings = [{"sensor_id": "HUM_001", "timestamp": str(t) + "Z",
                 "value": float(v), "unit": "percent"} 
                for t, v in zip(timestamps, humidity)]

    with open("humidity_data.json", "w") as f:
        json.dump(readings, f, indent=2)
    print("Created humidity_data.json")

create_humidity_data()

# TODO: Implement load_humidity_data()
def load_humidity_data(filename):
    """Load JSON, return (values, timestamps) as NumPy arrays."""
    # 1. Load JSON with json.load()
    with open(filename, "r") as f:
        readings = json.load(f)
    
    print(f"Loaded {len(readings)} readings")

    # 2. Extract values to np.float64 array
    values = np.array([r["value"] for r in readings], dtype = np.float64)


    # 3. Extract timestamps to datetime64 array
    timestamps = np.array([r["timestamp"] for r in readings], dtype = "datetime64[ns]")
    return values, timestamps

values, timestamps = load_humidity_data("humidity_data.json")
print(f"Values: {values.shape}, dtype: {values.dtype}")
print(f"First 5: {values[:5]}")




# TODO: Implement analyze_humidity()
def analyze_humidity(values):
    """Return dict with mean, std, min, max."""
    # Use np.mean(), np.std(), np.min(), np.max()`
    stats = {
        "mean": np.mean(values),
        "std": np.std(values),
        "min": np.min(values),
        "max": np.max(values)
    }
    return stats

stats = analyze_humidity(values)




# TODO: Implement find_anomalies()
def find_anomalies(values, min_ok=30.0, max_ok=70.0):
    """Return (indices, values) of anomalies using boolean indexing."""
    # 1. Create mask: (values < min_ok) | (values > max_ok)
    is_anomaly = (values < min_ok) | (values > max_ok)


    # 2. Use np.where() for indices
    indices = np.where(is_anomaly)[0]
    # 3. Use mask for values
    anomalies = values[is_anomaly]
    return indices, anomalies

indices, anomalies = find_anomalies(values)
print(f"Found {len(anomalies)} anomalies at indices {indices}")
print(f"Values: {anomalies}")


# Combine everything
summary = {
    "sensor_id": "HUM_001",
    "total_readings": len(values),
    "statistics": analyze_humidity(values),
    "anomalies": {"count": len(find_anomalies(values)[1]),
                  "values": find_anomalies(values)[1].tolist()},
    "dtypes": {"values": str(values.dtype), 
               "timestamps": str(timestamps.dtype)}
}

with open("humidity_report.json", "w") as f:
    json.dump(summary, f, indent=2)
print("Saved humidity_report.json")