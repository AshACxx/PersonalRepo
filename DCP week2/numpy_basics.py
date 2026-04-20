import numpy as np


print("="*50)
print("NUMPY BASICS")
print("="*50)


# --- CREATING ARRAYS ---
print("---CREATING ARRAYS---")

#Python list 

py_list = [1,2,3,4,5]
np_array = np.array(py_list)

print(f"Python list: {py_list}")
print(f"type: {type(py_list)}")

print(f"NumPy list:{np_array}")
print(f"Type: {type(np_array)}")
print(f"dtype: {np_array.dtype}")
print(f"shape: {np_array.shape}")

print("")

# ---NumPy Data types (dtypes) ---
print("---NUMPY DATA TYPES (DTYPES)---")

# Integer types
int_array = np.array([1,2,3], dtype = np.int32)
print(f"int32: {int_array}, dtype; {int_array.dtype}, bytes: {int_array.nbytes}")

# Float Types
print("")
float_array =np.array([1.5, 2.5, 3.5], dtype = np.float64)
print(f"float64: {float_array}, dtype: {float_array.dtype}, bytes: {float_array.nbytes}")

# Boolean types
print("")
bool_array = np.array([True, False,True], dtype = np.bool_)
print(f"bool: {bool_array}, dtype : {bool_array.dtype}, bytes: {bool_array.nbytes}, shape: {bool_array.shape}")

print("")

# --- Array Operations ---
print("--- Array Operations ---")

arr2 = [22.5, 23.1, 21.8, 24.2, 22.9]
values =np.array((arr2), dtype = np.float64)

print(f"Sensor values; {values}")

# Statistics
print(f"Statistics:")
print(f"  Mean: {np.mean(values):.2f}")
print(f"  Median: {np.median(values):.2f}")
print(f"  STD: {np.std(values):.2f}")
print(f"  Max: {np.max(values):.2f}")
print(f"  Min: {np.min(values):.2f}")

threshold = 23.0
above = values[values > threshold]
print(f"Values above {threshold}: {above}")


# Differences between readings
diffs = np.diff(values)
print(f"Differences: {diffs}")

print("" + "=" * 50)