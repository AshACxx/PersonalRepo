"""
Smart Building Energy Monitor Challenge
Process energy consumption data from 50 smart meters
"""

import numpy as np
import time

print("=" * 70)
print("SMART BUILDING ENERGY MONITOR CHALLENGE")
print("=" * 70)

# --- Generate Simulated Energy Data ---
print("\n--- Generating Smart Meter Data ---\n")

np.random.seed(2026)  # For reproducibility

# Configuration
NUM_METERS = 50
MINUTES_PER_DAY = 1440  # 24 hours × 60 minutes

# Generate realistic energy consumption patterns
# Each meter has a base consumption + time-based variation + random noise

# Time array (minutes from midnight)
time_minutes = np.arange(MINUTES_PER_DAY)

# Create hour of day for pattern generation
hours = time_minutes // 60

# Base consumption per meter (kW) - varies by meter type
# Meters 0-19: Office equipment (low-medium)
# Meters 20-39: HVAC systems (high, time-dependent)  
# Meters 40-49: Lighting (medium, time-dependent)

base_consumption = np.zeros((NUM_METERS, MINUTES_PER_DAY))

# Office equipment (fairly constant during work hours)
for i in range(20):
    work_hours = ((hours >= 8) & (hours < 18)).astype(float)
    base_consumption[i] = 0.5 + 1.5 * work_hours + np.random.normal(0, 0.1, MINUTES_PER_DAY)

# HVAC systems (high during work hours, medium otherwise)
for i in range(20, 40):
    work_hours = ((hours >= 7) & (hours < 19)).astype(float)
    base_consumption[i] = 2.0 + 4.0 * work_hours + np.random.normal(0, 0.3, MINUTES_PER_DAY)

# Lighting (peak morning and evening, low at night)
for i in range(40, 50):
    morning = ((hours >= 6) & (hours < 9)).astype(float)
    day = ((hours >= 9) & (hours < 17)).astype(float)
    evening = ((hours >= 17) & (hours < 22)).astype(float)
    base_consumption[i] = 0.2 + 0.8 * morning + 0.5 * day + 1.0 * evening
    base_consumption[i] += np.random.normal(0, 0.05, MINUTES_PER_DAY)

# Clip negative values (power can't be negative)
energy_data = np.clip(base_consumption, 0, None)

# Inject some anomalies (meter malfunctions)
# Meter 15: Spike at 10:30 AM
energy_data[15, 630:635] = 15.0  # Way above normal
# Meter 35: Drops to near-zero (sensor failure) 
energy_data[35, 900:960] = 0.01
# Meter 42: Erratic readings
energy_data[42, 720:780] = np.random.uniform(0, 5, 60)

print(f"Data shape: {energy_data.shape}")
print(f"  Rows: {NUM_METERS} meters")
print(f"  Columns: {MINUTES_PER_DAY} minutes (24 hours)")
print(f"Total data points: {energy_data.size:,}")

# ============================================================================
# YOUR CHALLENGE TASKS BEGIN HERE
# Complete each task using ONLY NumPy operations (NO explicit for loops!)
# ============================================================================

print("\n" + "=" * 70)
print("CHALLENGE TASKS")
print("=" * 70)

# ---------------------------------------------------------------------------
# TASK 1: Basic Statistics
# Calculate the following for the entire building:
# - Total energy consumed in the day (sum of all readings)

# - Mean consumption per minute (across all meters)

# - Peak single reading (maximum value)

# - Which meter and minute had the peak reading

# ---------------------------------------------------------------------------

print("\n--- TASK 1: Basic Statistics ---\n")

# YOUR CODE HERE
total_energy = np.sum(energy_data)
mean_per_minute = np.mean(energy_data)
peak_reading = np.max(energy_data)
peak_meter, peak_minute = np.unravel_index(np.argmax(energy_data), energy_data.shape)

# Uncomment to print results:
print(f"Total energy consumed: {total_energy:.2f} kW-minutes")
print(f"Mean consumption per minute: {mean_per_minute:.4f} kW")
print(f"Peak reading: {peak_reading:.2f} kW")
print(f"Peak occurred at Meter {peak_meter}, Minute {peak_minute} ({peak_minute//60:02d}:{peak_minute%60:02d})")


# ---------------------------------------------------------------------------
# TASK 2: Hourly Aggregation
# Reshape the data to calculate hourly statistics:
# - Reshape data to (NUM_METERS, 24 hours, 60 minutes)
# - Calculate total consumption per hour (sum across all meters and minutes)
# - Find the peak hour(s) of consumption
# - Find the lowest consumption hour(s)
# ---------------------------------------------------------------------------

print("\n--- TASK 2: Hourly Analysis ---\n")

# YOUR CODE HERE
# Hint: Use reshape and sum along appropriate axes
hourly_data = energy_data.reshape(NUM_METERS, 24, 60)

hourly_totals = np.sum(hourly_data, axis=(0,2))
peak_hour = np.argmax(hourly_totals)
quiet_hour = np.argmin(hourly_totals)

# Uncomment to print results:
print(f"Hourly totals shape: {hourly_totals.shape}")
print(f"Consimption per hour:{hourly_totals}")
print(f"Peak hour: {peak_hour}:00 ({hourly_totals[peak_hour]:.2f} kW-minutes)")
print(f"Quietest hour: {quiet_hour}:00 ({hourly_totals[quiet_hour]:.2f} kW-minutes)")


# ---------------------------------------------------------------------------
# TASK 3: Anomaly Detection
# Identify anomalous readings using statistical methods:
# - Calculate mean and std for each meter
# - Find readings more than 3 standard deviations from the meter's mean
# - Count total anomalies detected
# - Identify which meters have the most anomalies
# ---------------------------------------------------------------------------

print("\n--- TASK 3: Anomaly Detection ---\n")

# YOUR CODE HERE
# Hint: Use broadcasting for comparing each reading to its meter's mean
meter_means = np.mean(energy_data, axis=1)
meter_stds = np.std(energy_data, axis=1)
# 
# Reshape for broadcasting:
anomaly_threshold_upper = meter_means + 3 * meter_stds
anomaly_threshold_lower = meter_means - 3 * meter_stds
#
# Find anomalies:
anomalies = (energy_data > anomaly_threshold_upper[:, np.newaxis]) | (energy_data < anomaly_threshold_lower[:, np.newaxis])

# Uncomment to print results:
print(f"Total anomalies detected: {np.sum(anomalies)}")
anomalies_per_meter = np.sum(anomalies, axis=1)
worst_meter = np.argmax(anomalies_per_meter)
print(f"Meter with most anomalies: Meter {worst_meter} ({anomalies_per_meter[worst_meter]} anomalies)")


# ---------------------------------------------------------------------------
# TASK 4: Meter Classification (5 points)
# Classify meters based on their consumption patterns:
# - Calculate average consumption for each meter
# - Classify as 'LOW' (<1 kW avg), 'MEDIUM' (1-3 kW avg), 'HIGH' (>3 kW avg)
# - Use np.where() or np.select() (NO loops!)
# - Count meters in each category
# ---------------------------------------------------------------------------

print("\n--- TASK 4: Meter Classification ---\n")

# YOUR CODE HERE

#conditions


meter_averages = np.mean(energy_data, axis= 1)

condition = [meter_averages < 1,(meter_averages >= 1)&(meter_averages <= 3), meter_averages > 3]
classifications = np.select(condition, ['LOW', 'MEDIUM', 'HIGH'], default = 'UNKNOWN') 
# 
low_count = np.sum(meter_averages <1)
medium_count = np.sum ((meter_averages >= 1) & (meter_averages <=3))
high_count = np.sum(meter_averages > 3)

# Uncomment to print results:
print(f"Meter average consumption range: {np.min(meter_averages):.2f} - {np.max(meter_averages):.2f} kW")
print(f"LOW consumption meters (<1 kW):    {low_count}")
print(f"MEDIUM consumption meters (1-3 kW): {medium_count}")
print(f"HIGH consumption meters (>3 kW):   {high_count}")


# ---------------------------------------------------------------------------
# TASK 5: Performance Comparison (5 points)
# Compare your vectorised solution with a loop-based approach:
# - Implement a loop-based version of Task 1 (total energy calculation)
# - Time both approaches
# - Calculate the speedup factor
# ---------------------------------------------------------------------------

print("\n--- TASK 5: Performance Comparison ---\n")

# Vectorised approach (your Task 1 solution)
def vectorised_total(data):
    return np.sum(data)

# Loop-based approach
def loop_total(data):
    # YOUR CODE HERE
    # Implement using nested for loops
    total = 0
    for meter in range(data.shape[0]):
         
         for minute in range(data.shape[1]):
             
             total += data[meter, minute]
    return total



# Benchmark both approaches
vectorised_time = time.time()
loop_time = time.time()
speedup = (loop_time - vectorised_time) / (loop_time - vectorised_time)

# Uncomment to print results:
print(f"Vectorised time: {vectorised_time:.4f} ms")
print(f"Loop-based time: {loop_time:.4f} ms")
print(f"Speedup: {speedup:.1f}x faster")


# ---------------------------------------------------------------------------
# BONUS TASK: Consumption Report (Extra Credit)
# Generate a formatted report summarizing the analysis
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print("CONSUMPTION REPORT")
print("=" * 70)




# YOUR CODE HERE (optional bonus)

def genrate_report():
    report = []
    report.append("SMART BUILDING ENERGY REPORT")
    report.append("="*30)
    report.append(f"Total energy consumed: {total_energy:.2f} kW-minut4s")

    print("\n".join(report))



# Create a nicely formatted summary of all findings

print(genrate_report())