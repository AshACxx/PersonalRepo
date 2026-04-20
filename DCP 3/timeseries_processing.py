"""
Time-Series Processing for Temperature Sensor Data
"""

import numpy as np

print("=" * 60)
print("TIME-SERIES PROCESSING WITH NUMPY")
print("=" * 60)

# --- Generate Realistic Temperature Data ---
print("\n--- Generating Temperature Time-Series ---\n")

np.random.seed(42)

# 1 hour of data at 1-second intervals
num_readings = 3600
time_seconds = np.arange(num_readings)

# Base temperature with gradual rise (simulating warming)
base_temp = 20.0
trend = 0.001 * time_seconds  # Slow warming: +3.6°C over 1 hour

# Add sinusoidal variation (HVAC cycling)
hvac_cycle = 0.5 * np.sin(2 * np.pi * time_seconds / 600)  # 10-min cycle

# Add random noise
noise = np.random.normal(0, 0.2, num_readings)

# Combine all components
temperatures = base_temp + trend + hvac_cycle + noise
temperatures = np.round(temperatures, 2)

print(f"Generated {num_readings} readings (1 hour at 1 Hz)")
print(f"Start: {temperatures[0]:.2f}°C")
print(f"End: {temperatures[-1]:.2f}°C")
print(f"Shape: {temperatures.shape}")

# --- Rolling/Moving Average ---
print("\n--- Rolling Average (Smoothing) ---\n")

def rolling_average(data, window_size):
    """
    Calculate rolling average using NumPy.
    This smooths out noise while preserving trends.
    """
    # Use cumsum for efficient calculation
    cumsum = np.cumsum(data)
    cumsum = np.insert(cumsum, 0, 0)  # Insert 0 at beginning

    # Calculate rolling sum, then divide by window size
    rolling_sum = cumsum[window_size:] - cumsum[:-window_size]
    return rolling_sum / window_size

# Apply different window sizes
for window in [5, 30, 60]:
    smoothed = rolling_average(temperatures, window)
    original_std = np.std(temperatures)
    smoothed_std = np.std(smoothed)
    noise_reduction = (1 - smoothed_std/original_std) * 100
    print(f"Window {window:2d}s: noise reduced by {noise_reduction:.1f}%")

# Compare raw vs smoothed
print("\nFirst 10 raw readings:", temperatures[:10])
smoothed_30 = rolling_average(temperatures, 30)
print(f"Smoothed (window=30):  {np.round(smoothed_30[:10], 2)}")

# --- Differencing (Change Detection) ---
print("\n--- Differencing (Rate of Change) ---\n")

# Calculate differences between consecutive readings
diffs = np.diff(temperatures)

print(f"First 10 changes: {np.round(diffs[:10], 3)}")
print(f"Mean change: {np.mean(diffs):.4f}°C/s")
print(f"Max increase: {np.max(diffs):.3f}°C")
print(f"Max decrease: {np.min(diffs):.3f}°C")

# Find large changes (potential anomalies)
threshold = 0.5
large_changes = np.where(np.abs(diffs) > threshold)[0]
print(f"\nLarge changes (>{threshold}°C): {len(large_changes)} occurrences")

# --- Trend Detection ---
print("\n--- Trend Detection ---\n")

# Method 1: Compare first vs last portion
first_quarter = temperatures[:num_readings//4]
last_quarter = temperatures[-num_readings//4:]

first_mean = np.mean(first_quarter)
last_mean = np.mean(last_quarter)
overall_change = last_mean - first_mean

print(f"First 15 min average: {first_mean:.2f}°C")
print(f"Last 15 min average:  {last_mean:.2f}°C")
print(f"Overall change: {overall_change:+.2f}°C")

if overall_change > 0.5:
    trend_direction = "WARMING"
elif overall_change < -0.5:
    trend_direction = "COOLING"
else:
    trend_direction = "STABLE"
print(f"Trend: {trend_direction}")

# Method 2: Linear regression slope
x = np.arange(num_readings)
slope, intercept = np.polyfit(x, temperatures, 1)
print(f"\nLinear trend: {slope*3600:.2f}°C/hour (slope={slope:.6f})")

# --- Resampling (Downsampling) ---
print("\n--- Resampling: 1-second to 1-minute ---\n")

# Reshape into 60-second chunks and take mean
num_minutes = num_readings // 60
temps_reshaped = temperatures[:num_minutes*60].reshape(num_minutes, 60)
temps_1min = np.mean(temps_reshaped, axis=1)

print(f"Original: {num_readings} readings at 1 Hz")
print(f"Resampled: {len(temps_1min)} readings at 1/60 Hz")
print(f"First 5 minute averages: {np.round(temps_1min[:5], 2)}")

# --- Gap Detection and Interpolation ---
print("\n--- Handling Missing Data ---\n")

# Create data with gaps (simulate missing readings)
temps_with_gaps = temperatures.copy()
gap_indices = [100, 101, 102, 500, 501, 1000]  # Missing readings
temps_with_gaps[gap_indices] = np.nan

print(f"Readings with gaps: {len(gap_indices)} NaN values")
print(f"Around gap at index 100: {temps_with_gaps[98:105]}")

# Linear interpolation to fill gaps
def interpolate_gaps(data):
    """Fill NaN values using linear interpolation."""
    valid_mask = ~np.isnan(data)
    valid_indices = np.where(valid_mask)[0]
    valid_values = data[valid_mask]

    all_indices = np.arange(len(data))
    interpolated = np.interp(all_indices, valid_indices, valid_values)
    return interpolated

temps_filled = interpolate_gaps(temps_with_gaps)
print(f"After interpolation: {temps_filled[98:105]}")

print("\n" + "=" * 60)