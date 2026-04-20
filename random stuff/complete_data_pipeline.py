
import random
import datetime
import time
import csv
import json

data = []

def collect_data(num_readings=20):

    """Collect simulated sensor data"""

    # TODO: Implement this function
        
    for i in range(num_readings):
            temperature = round(random.uniform(18.0, 28.0), 2)  # Celsius
            humidity = round(random.uniform(40.0, 80.0), 2)     # Percentage
            pressure = round(random.uniform(980.0, 1020.0), 2)  # hPa

            reading = {
                'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'temperature_c': temperature,
                'humidity_percent': humidity,
                'pressure_hpa': pressure
            }

            return reading

    pass


def display_reading(reading):
    """Display sensor reading in a formatted way"""

    print(f"[{reading['timestamp']}] ", end="")
    print(f"Temp: {reading['temperature_c']:5.2f}°C | ", end="")
    print(f"Humidity: {reading['humidity_percent']:5.2f}% | ", end="")
    print(f"Pressure: {reading['pressure_hpa']:7.2f} hPa")

# Main execution
if __name__ == "__main__":
    print("Starting sensor data collection...")
    print("Press Ctrl+C to stop\n")

    try:
        for i in range(20):  # Collect 20 readings
            reading = collect_data()
            display_reading(reading)
            time.sleep(1)  # Wait 1 second between readings

    except KeyboardInterrupt:
        print("\n\nData collection stopped by user.")







def save_to_csv(filename, reading, write_header=False):
    """Save data to CSV file"""
    # TODO: Implement this function

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reading.keys())

        if write_header:
            writer.writeheader()

        writer.writerow(reading)

# Main execution
if __name__ == "__main__":
    filename = "sensor_data.csv"
    num_readings = 20

    print(f"Starting data collection and logging to {filename}...")
    print("Press Ctrl+C to stop\n")

    try:
        for i in range(num_readings):
            reading = collect_data()

            # Write header on first iteration
            save_to_csv(filename, reading, write_header=(i == 0))

            display_reading(reading)
            print(f"  > Logged to {filename}")

            time.sleep(1)

        print(f"\n✓ Successfully logged {num_readings} readings to {filename}")

    except KeyboardInterrupt:
        print("\n\nData collection stopped by user.")


    pass

