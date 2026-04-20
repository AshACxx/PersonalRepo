import numpy as np

temperatures = np.array([20.5, 22.3, 19.8, 21.0, 23.5])                 

mean_temp = np.mean(temperatures)
std_dev = np.std(temperatures)
max_temp = np.max(temperatures)

print(f"Mean: {mean_temp:.2f}C")
print(f"Std Dev: {std_dev:.2f}C")
print(f"Max Temp: {max_temp:.2f}C")

