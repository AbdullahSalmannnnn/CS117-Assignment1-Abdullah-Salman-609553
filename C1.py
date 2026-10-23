# C1 - Current and Power
# Two functions: ohms_current() returns I = V / R and
# power_dissipated() returns P = I^2 * R. Tested with V = 12 V and R = 6 ohm.


def ohms_current(v, r):
    return v / r


def power_dissipated(i, r):
    return i ** 2 * r


voltage = 12
resistance = 6

current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)

print("Current =", current, "A")
print("Power =", power, "W")

# Extra test with my own values: V = 9 V, R = 3 ohm
current = ohms_current(9, 3)
print("\nCurrent =", current, "A")
print("Power =", power_dissipated(current, 3), "W")
