
"""
Sensor Data Stream Concepts
Understanding temperature sensor characteristics
"""

import numpy as np

print("=" * 55)
print("SENSOR DATA STREAM CONCEPTS")
print("=" * 55)

# --- Stream Temporal Nature ---
print("\n--- Temporal Data Structure ---\n")

# Simulate 1 hour of data at 1-second intervals
duration_seconds = 3600  # 1 hour
sample_rate = 1  # 1 reading per second
num_readings = duration_seconds // sample_rate

print(f"Duration: {duration_seconds} seconds (1 hour)")
print(f"Sample rate: {sample_rate} Hz (reading/second)")
print(f"Total readings: {num_readings:,}")
print(f"Data generated per day: {num_readings * 24:,} readings")

# --- Data Rate Calculations ---
print("\n--- Data Volume Estimation ---\n")

# Each reading: timestamp (8 bytes) + value (8 bytes) + metadata (~20 bytes)
bytes_per_reading = 36
daily_bytes = num_readings * 24 * bytes_per_reading
monthly_bytes = daily_bytes * 30

print(f"Bytes per reading: ~{bytes_per_reading}")
print(f"Daily data: {daily_bytes / 1024:.1f} KB")
print(f"Monthly data: {monthly_bytes / (1024**2):.1f} MB")

# --- Noise Demonstration ---
print("\n--- Sensor Noise Simulation ---\n")

np.random.seed(42)

# True temperature (constant for demonstration)
true_temp = 22.0

# Different noise levels
noise_levels = [0.1, 0.3, 0.5, 1.0]

for noise in noise_levels:
    #.normal() is gaussian noise with mean=0 and std=noise
    
    readings = true_temp + np.random.normal(0, noise, 10)
    readings = np.round(readings, 2)
    spread = np.max(readings) - np.min(readings)
    print(f"Noise {noise}C: {readings[:5]} ... spread={spread:.2f}C")

# --- Resolution Effects ---
print("\n--- Resolution Effects ---\n")

# High precision reading
high_precision = 22.3456789
print(f"High precision: {high_precision}")

# Typical sensor resolutions
resolutions = [0.5, 0.1, 0.01]
for res in resolutions:
    quantized = round(high_precision / res) * res
    print(f"Resolution {res}°C: {quantized}")

print("\n" + "=" * 55)