# A3 - Resistor Colour Code
# Takes the colour of the first band of a resistor and prints its digit.

colour = input("Enter band colour: ").strip().lower()

if colour == "black":
    digit = 0
elif colour == "brown":
    digit = 1
elif colour == "red":
    digit = 2
elif colour == "orange":
    digit = 3
elif colour == "yellow":
    digit = 4
elif colour == "green":
    digit = 5
elif colour == "blue":
    digit = 6
elif colour == "violet":
    digit = 7
elif colour == "grey" or colour == "gray":
    digit = 8
elif colour == "white":
    digit = 9
else:
    digit = None

if digit is None:
    print("Invalid colour")
else:
    print("Digit =", digit)
