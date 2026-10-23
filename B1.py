# B1 - Ohm's Law Table
# Prints the current through a fixed 10 ohm resistor for supply voltages
# from 1 V to 10 V in steps of 1 V, using a for loop.

resistance = 10

for voltage in range(1, 11):
    current = voltage / resistance
    print(f"V = {voltage} V, I = {current} A")
