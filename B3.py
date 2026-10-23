# B3 - Sensor Readings
# Uses one loop (no max(), min() or sum()) to find how many readings are above 3.2 V,
# the highest reading, the lowest reading and the average reading.

readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

above_count = 0
highest = readings[0]
lowest = readings[0]
total = 0
count = 0

for voltage in readings:
    if voltage > 3.2:
        above_count = above_count + 1
    if voltage > highest:
        highest = voltage
    if voltage < lowest:
        lowest = voltage
    total = total + voltage
    count = count + 1

average = total / count

print("Readings above 3.2 V:", above_count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print(f"Average: {average:.2f} V")
