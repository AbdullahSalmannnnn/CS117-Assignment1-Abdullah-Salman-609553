# B2 - Resistors in Series
# Asks how many resistors are in series, reads each value in a loop
# and prints the total series resistance (R_total = R1 + R2 + ...).

count = int(input("How many resistors? "))
total_resistance = 0

for number in range(1, count + 1):
    resistance = float(input(f"Enter R{number}: "))
    total_resistance = total_resistance + resistance

print(f"Total resistance = {total_resistance:g} ohm")
