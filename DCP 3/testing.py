import csv
import numpy as np

np.random.seed(2026)

DURATION_HOURS = 24
SAMPLES_PER_HOUR = 60
TOTAL_READINGS = DURATION_HOURS * SAMPLES_PER_HOUR

BASE_TEMP = 18.0
DAY_AMPLITUDE = 8.0
NOISE_LEVEL = 0.3


def simulate_daily_temperature(num_readings, base_temp, amplitude, noise_std):
    time = np.linspace(0, 24, num_readings, endpoint=False)  # 0..23.9833
    pattern = amplitude * np.sin((time - 4) * np.pi / 12)
    temps = base_temp + pattern + np.random.normal(0, noise_std, num_readings)
    return temps


def add_anomalies(temperatures, num_anomalies=5):
    temps_with_anomalies = temperatures.copy()
    indices = np.random.choice(len(temperatures), num_anomalies, replace=False)
    deviations = np.random.uniform(-15, 15, num_anomalies)
    temps_with_anomalies[indices] += deviations
    return temps_with_anomalies  # ✅ IMPORTANT


def save_to_csv(temperatures, filename):
    base = np.datetime64("2026-02-03T00:00:00")
    timestamps = base + np.arange(len(temperatures)).astype("timedelta64[m]")

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "sensor_id", "temperature", "unit", "quality"])  # matches your earlier example

        for ts, temp in zip(timestamps, temperatures):
            writer.writerow([str(ts), "TEMP_101", round(float(temp), 2), "celsius", "good"])

    print(f"Created: {filename}")


# --- Run ---
temperatures = simulate_daily_temperature(TOTAL_READINGS, BASE_TEMP, DAY_AMPLITUDE, NOISE_LEVEL)
temps_with_anomalies = add_anomalies(temperatures, num_anomalies=8)
save_to_csv(temps_with_anomalies, "daily_temperature.csv")


# --- Quick check: load back in ---
timestamps_list = []
temperatures_list = []

with open("daily_temperature.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        timestamps_list.append(row[0])          # timestamp column
        temperatures_list.append(float(row[2])) # temperature column

print(f"Loaded {len(temperatures_list)} readings")
print("First 5 timestamps:", timestamps_list[:5])
print("First 5 temps:", temperatures_list[:5])
