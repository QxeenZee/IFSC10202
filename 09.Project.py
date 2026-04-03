import csv

FILE_NAME = "09.Project Distances.csv"

distance_table = []

# Read the CSV file into a two-dimensional list
with open(FILE_NAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        distance_table.append(row)

# Print the two-dimensional list in table form
for row in distance_table:
    for item in row:
        print(f"{item:>10}", end="")
    print()

# Prompt for cities
from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

from_index = -1
to_index = -1

# Search the zeroth column for the From City
for row_index in range(1, len(distance_table)):
    if distance_table[row_index][0] == from_city:
        from_index = row_index
        break

# Search the zeroth row for the To City
for col_index in range(1, len(distance_table[0])):
    if distance_table[0][col_index] == to_city:
        to_index = col_index
        break

# Display results
if from_index == -1:
    print("Invalid From City")

if to_index == -1:
    print("Invalid To City")

if from_index != -1 and to_index != -1:
    distance = distance_table[from_index][to_index]
    print(f"{from_city} to {to_city} - {distance} miles")