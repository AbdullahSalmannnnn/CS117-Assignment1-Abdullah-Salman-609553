# B5 - Resistor Tolerance Sorting
# Keeps asking for measured resistance values of 100 ohm resistors until the user enters 0,
# and counts how many fall in the 1% bin, the 5% bin and the reject bin.

one_percent_count = 0
five_percent_count = 0
reject_count = 0

resistance = float(input("Enter measured resistance (0 to stop): "))

while resistance != 0:
    if 99.0 <= resistance <= 101.0:
        one_percent_count = one_percent_count + 1
    elif 95.0 <= resistance <= 105.0:
        five_percent_count = five_percent_count + 1
    else:
        reject_count = reject_count + 1
    resistance = float(input("Enter measured resistance (0 to stop): "))

print("1% tolerance:", one_percent_count)
print("5% tolerance:", five_percent_count)
print("Reject:", reject_count)
