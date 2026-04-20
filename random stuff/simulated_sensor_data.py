# simulated_sensor_data.py

import random
import datetime
import time

def generate_sensor_reading():
    """Simulate a sensor reading with temperature and humidity"""

    # Simulate realistic sensor values
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
        for i in range(10):  # Collect 10 readings
            reading = generate_sensor_reading()
            display_reading(reading)
            time.sleep(1)  # Wait 1 second between readings

    except KeyboardInterrupt:
        print("\n\nData collection stopped by user.")