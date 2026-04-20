# system_metrics_collector.py

import datetime
import platform
import sys

def collect_system_info():
    """Collect basic system information"""

    system_info = {
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'python_version': sys.version.split()[0],
        'platform': platform.system(),
        'platform_release': platform.release(),
        'architecture': platform.machine(),
        'processor': platform.processor() or 'Unknown'
    }

    return system_info

def display_system_info(info):
    """Display system information in a formatted way"""

    print("=" * 50)
    print("SYSTEM INFORMATION")
    print("=" * 50)

    for key, value in info.items():
        formatted_key = key.replace('_', ' ').title()
        print(f"{formatted_key:20s}: {value}")

    print("=" * 50)

# Main execution
if __name__ == "__main__":
    print("Collecting system information...\n")

    info = collect_system_info()
    display_system_info(info)