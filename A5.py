# A5 - Smallest and Largest Resistor
# Takes three resistor values and displays the smallest and the largest
# using only if / elif / else (no min() or max()).

r1 = float(input("Enter R1: "))
r2 = float(input("Enter R2: "))
r3 = float(input("Enter R3: "))

# Find the smallest resistor
if r1 <= r2 and r1 <= r3:
    smallest = r1
elif r2 <= r1 and r2 <= r3:
    smallest = r2
else:
    smallest = r3

# Find the largest resistor
if r1 >= r2 and r1 >= r3:
    largest = r1
elif r2 >= r1 and r2 >= r3:
    largest = r2
else:
    largest = r3

print(f"Smallest = {smallest:g} ohm")
print(f"Largest = {largest:g} ohm")
