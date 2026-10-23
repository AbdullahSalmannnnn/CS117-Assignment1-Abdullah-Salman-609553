# A2 - Current Direction
# Takes a current value from the user and prints the direction in which it flows.

current = float(input("Enter current (A): "))

if current > 0:
    print("Current flows from A to B")
elif current < 0:
    print("Current flows from B to A")
else:
    print("No current flows")
