# A4 - Logic Gates
# Takes two bits A and B (0 or 1) and prints the output of the AND, OR and XOR gates.

bit_a = input("Enter A: ").strip()
bit_b = input("Enter B: ").strip()

if (bit_a != "0" and bit_a != "1") or (bit_b != "0" and bit_b != "1"):
    print("Bits must be 0 or 1")
else:
    a = int(bit_a)
    b = int(bit_b)

    # AND gives 1 only when both inputs are 1
    if a == 1 and b == 1:
        and_output = 1
    else:
        and_output = 0

    # OR gives 1 when at least one input is 1
    if a == 1 or b == 1:
        or_output = 1
    else:
        or_output = 0

    # XOR gives 1 when the inputs are different
    if a != b:
        xor_output = 1
    else:
        xor_output = 0

    print("AND =", and_output)
    print("OR =", or_output)
    print("XOR =", xor_output)
