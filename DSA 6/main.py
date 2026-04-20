print("Sales System V1.0")

import csv
with open("data\source\sales.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)


    # Loop through each row 
    for row in reader:
        print(row)
        