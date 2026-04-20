"""
Memory Comparison: Python Lists vs NumPy Arrays
Understanding why NumPy is more memory-efficient for sensor data
"""

import sys 
import numpy as np

print("=" * 60)
print("MEMORY COMPARISON: PYTHON LISTS vs NUMPY ARRAYS")
print("=" * 60)

# --- Small Scale Comparison ---
print("\n--- Small Scale (10 elements) ---\n")

# Python list of floats
py_list = [22.5, 23.1, 24.8, 22.9, 25.2, 26.1, 24.5, 23.8, 22.1, 25.5]

#Same list Numpy version 
np_array = np.array(py_list, dtype = np.float64)


#getsizeof() returns the size of the object in bytes. For a list, it returns the size of the list object itself, which includes pointers to the elements but not the size of the elements. To get the total memory usage of a list, you need to add the size of the list object and the size of each element in the list.
list_size = sys.getsizeof(py_list)
list_total = list_size + sum(sys.getsizeof(x) for x in py_list)


array_size = np_array.nbytes
array_total = sys.getsizeof(np_array)


print(f"Python list:")
print(f"  List object size: {list_size} bytes")
print(f"  Total (with elements): {list_total} bytes")
print(f"\nNumPy array:")
print(f"  Data size (nbytes): {array_size} bytes")
print(f"  Total object size: {array_total} bytes")
print(f"\nMemory ratio: Python list uses {list_total/array_size:.1f}x more memory")


# --- Sensor Scale Comparison ---
print("\n--- Sensor Scale (1 million readings) ---\n")

n = 1_000_000
print(f"Simulating {n:,} sensor readings...")

py_sensor_data = list(range(n))
py_list_size = sys.getsizeof(py_sensor_data)

np_sensor_data = np.arange(n, dtype=np.float64)
np_array_bytes = np_sensor_data.nbytes

print(f"Python list object: {py_list_size / (1024**2):.2f} MB")
print(f"NumPy array data:   {np_array_bytes / (1024**2):.2f} MB")
print(f"\nFor float data, NumPy uses ~{py_list_size * 3 / np_array_bytes:.0f}x less memory!")
