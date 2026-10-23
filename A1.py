# A1 - Fuse Check (Ohm's Law)
# Takes voltage and resistance from the user, calculates the current I = V / R
# and tells whether the fuse will blow (current more than 2 A) or the circuit is safe.

voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (ohm): "))

if resistance <= 0:
    print("Invalid resistance")
else:
    current = voltage / resistance
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
