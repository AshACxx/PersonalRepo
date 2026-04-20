"""
Classroom Challenge: 24-Hour Temperature Simulation and Analysis
"""

import csv
from fileinput import filename
import numpy as np

# --- Configuration ---
np.random.seed(2026)  # For reproducibility

# Simulation parameters
DURATION_HOURS = 24
SAMPLES_PER_HOUR = 60  # One reading per minute
TOTAL_READINGS = DURATION_HOURS * SAMPLES_PER_HOUR

# Temperature parameters
BASE_TEMP = 18.0       # Base temperature (night minimum)
DAY_AMPLITUDE = 8.0    # Temperature swing (night to day)
NOISE_LEVEL = 0.3      # Random noise standard deviation

print("=" * 60)
print("TEMPERATURE SENSOR SIMULATION CHALLENGE")
print("=" * 60)
print(f"\nSimulating {DURATION_HOURS} hours, {TOTAL_READINGS} readings")



# TODO: Implement simulate_daily_temperature()
def simulate_daily_temperature(num_readings, base_temp, amplitude, noise_std):
    """
    Simulate 24-hour temperature readings.

    The daily pattern follows a sinusoidal curve:
    - Minimum temperature at 4 AM (index ~240)
    - Maximum temperature at 4 PM (index ~960)

    Formula: temp = base + amplitude * sin((hour - 4) * pi / 12)

    Args:
        num_readings: Total number of readings (1440 for 24h at 1/min)
        base_temp: Baseline temperature (night minimum)
        amplitude: Temperature range (max - min) / 2
        noise_std: Standard deviation of noise

    Returns:
        NumPy array of temperature readings
    """
    # STEP 1: Create time array in hours (0 to 24)
    time = np.linspace(0, 24, num_readings)
    # Hint: np.linspace(0, 24, num_readings)

    # STEP 2: Calculate daily pattern using sine wave
    pattern = amplitude * np.sin((time - 4) * np.pi / 12)

    # Peak at hour 16 (4 PM), minimum at hour 4 (4 AM)
    # Hint: amplitude * np.sin((hours - 4) * np.pi / 12)

    # STEP 3: Add base temperature and noise
    spread = base_temp + pattern + np.random.normal(0, noise_std, num_readings)
    # Hint: base_temp + pattern + np.random.normal(0, noise_std, num_readings)

    return spread  # Return the generated temperature readings

# Generate data
temperatures = simulate_daily_temperature(
    TOTAL_READINGS, BASE_TEMP, DAY_AMPLITUDE, NOISE_LEVEL
)

print(f"\n--- Task 1: Generated Data ---")
print(f"Shape: {temperatures.shape}")
print(f"Min: {np.min(temperatures):.1f}°C")
print(f"Max: {np.max(temperatures):.1f}°C")
print(f"First 5 readings: {np.round(temperatures[:5], 2)}")




# TODO: Implement add_anomalies()
def add_anomalies(temperatures, num_anomalies=5):
    """
    Add random anomalies to temperature data.

    Anomalies simulate:
    - Sensor errors (sudden spikes/drops)
    - External events (door opened, heater malfunction)

    Args:
        temperatures: Original temperature array
        num_anomalies: Number of anomalies to add

    Returns:
        Modified temperature array with anomalies
    """
    # Make a copy to avoid modifying original
    temps_with_anomalies = temperatures.copy()

    # STEP 1: Select random indices for anomalies
    # Hint: np.random.choice(len(temperatures), num_anomalies, replace=False)

    indices =np.random.choice(len(temperatures), num_anomalies, replace=False)

    # STEP 2: Add large deviations (+/- 10-15°C)
    # Hint: np.random.uniform(-15, 15, num_anomalies)

    deviations = np.random.uniform(-15, 15, num_anomalies)

    temps_with_anomalies[indices] += deviations
    return temps_with_anomalies  # Return modified array with anomalies
# Add anomalies
temps_with_anomalies = add_anomalies(temperatures, num_anomalies=8)

# TODO: Implement save_to_csv()
def save_to_csv(temperatures, filename):
    """
    Save temperature data to CSV file.

    CSV format:
    timestamp,sensor_id,temperature,unit
    2026-02-03T00:00:00,TEMP_101,18.2,celsius

    Args:
        temperatures: Array of temperature values
        filename: Output filename
    """
    # STEP 1: Create base timestamp
    # Hint: np.datetime64("2026-02-03T00:00:00")

    base = np.datetime64("2026-02-03T00:00:00")

    # STEP 2: Create timestamps at 1-minute intervals
    # Hint: base + np.arange(len(temperatures)).astype("timedelta64[m]")

    timestamps = base + np.arange(len(temperatures)).astype("timedelta64[m]")

    # STEP 3: Write to CSV using csv.writer
    # Include header: timestamp,sensor_id,temperature,unit
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "sensor_id", "temperature", "unit", "quality"])  # matches your earlier example

        for ts, temp in zip(timestamps, temperatures):
            writer.writerow([str(ts), "TEMP_101", round(float(temp), 2), "celsius", "good"])

    print(f"Created: {filename}")


temperatures = simulate_daily_temperature(TOTAL_READINGS, BASE_TEMP, DAY_AMPLITUDE, NOISE_LEVEL)
temps_with_anomalies = add_anomalies(temperatures, num_anomalies=8)
save_to_csv(temps_with_anomalies, "daily_temperature.csv")

    
# Replace with your implementation
    
print(f"\n--- Task 2: Data with Anomalies ---")
print(f"Saved to: daily_temperature.csv")

# TODO: Implement analyze_temperature_data()
def analyze_temperature_data(filename):
    """
    Load and analyze temperature CSV data.

    Returns dictionary with:
    - Basic stats (mean, std, min, max)
    - Hourly averages
    - Detected anomalies
    - Overall trend
    """
    # STEP 1: Load data from CSV
    # Hint: Use csv.DictReader, extract temperatures to list
    temperatures_list = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            temperatures_list.append(float(row["temperature"]))


    # STEP 2: Convert to NumPy array
    temperatures = np.array(temperatures_list)


    # STEP 3: Calculate statistics
    mean = np.mean(temperatures)
    std = np.std(temperatures)
    min_temp = np.min(temperatures)
    max_temp = np.max(temperatures)


    # STEP 4: Calculate hourly averages (reshape to 24x60, mean on axis=1)
    hourly_averages = np.mean(temperatures.reshape(24, 60), axis=1)


    # STEP 5: Detect anomalies (readings outside mean ± 3*std)
    anomaly_indices = np.where((temperatures < mean - 3*std) | (temperatures > mean + 3*std))[0]
    anomaly_count = len(anomaly_indices)

    # STEP 6: Determine trend (compare first vs last 4 hours)
    first_quarter = temperatures[:60*4]  # First 4 hours
    last_quarter = temperatures[-60*4:]   # Last 4 hours

    first_avg = np.mean(first_quarter)
    last_avg = np.mean(last_quarter)

    if last_avg > first_avg:
        trend = "warming"
    elif last_avg < first_avg:
        trend = "cooling"
    else:
        trend = "stable"

    return {
        "mean": mean,
        "std": std,
        "min": min_temp,
        "max": max_temp,
        "hourly_averages": hourly_averages,
        "anomaly_count": anomaly_count,
        "anomaly_indices": anomaly_indices,
        "trend": trend
    }

results = analyze_temperature_data("daily_temperature.csv")

print(f"\n--- Task 3: Analysis Results ---")
print(f"Statistics:")
print(f"  Mean: {results['mean']:.2f}°C")
print(f"  Std:  {results['std']:.2f}°C")
print(f"  Min:  {results['min']:.2f}°C")
print(f"  Max:  {results['max']:.2f}°C")
print(f"\nHourly Averages (first 6 hours):")
for hour, avg in enumerate(results['hourly_averages'][:6]):
    print(f"  {hour:02d}:00 - {avg:.1f}°C")
print(f"\nAnomalies found: {results['anomaly_count']}")
print(f"Anomaly indices: {results['anomaly_indices'][:5]}...")
print(f"\nTrend: {results['trend']}")



def generate_report(results, output_file="temperature_report.txt"):
    """Generate human-readable analysis report."""

    with open(output_file, "w") as f:
        f.write("=" * 50 + "\n")
        f.write("TEMPERATURE SENSOR ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n\n")

        f.write("SUMMARY STATISTICS\n")
        f.write("-" * 30 + "\n")
        f.write(f"Mean Temperature: {results['mean']:.2f}°C\n")
        f.write(f"Std Deviation:    {results['std']:.2f}°C\n")
        f.write(f"Minimum:          {results['min']:.2f}°C\n")
        f.write(f"Maximum:          {results['max']:.2f}°C\n\n")

        f.write("DAILY PATTERN\n")
        f.write("-" * 30 + "\n")
        hourly = results['hourly_averages']
        coldest_hour = np.argmin(hourly)
        warmest_hour = np.argmax(hourly)
        f.write(f"Coldest hour: {coldest_hour:02d}:00 ({hourly[coldest_hour]:.1f}°C)\n")
        f.write(f"Warmest hour: {warmest_hour:02d}:00 ({hourly[warmest_hour]:.1f}°C)\n\n")

        f.write("ANOMALY DETECTION\n")
        f.write("-" * 30 + "\n")
        f.write(f"Anomalies found: {results['anomaly_count']}\n")
        f.write(f"Indices: {results['anomaly_indices']}\n\n")

        f.write("TREND ANALYSIS\n")
        f.write("-" * 30 + "\n")
        f.write(f"Overall trend: {results['trend']}\n")

    print(f"\n--- Task 4: Report Generated ---")
    print(f"Saved to: {output_file}")

generate_report(results)

print("\n" + "=" * 60)
print("CHALLENGE COMPLETE!")
print("=" * 60)

