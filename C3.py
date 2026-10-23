# C3 - Decimal to Binary
# Function decimal_to_binary() converts a positive decimal number to a binary string
# using repeated division by 2 (without using bin()).


def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary


print("decimal_to_binary(10) ->", decimal_to_binary(10))
print("decimal_to_binary(25) ->", decimal_to_binary(25))

# Extra test with my own value
print("decimal_to_binary(45) ->", decimal_to_binary(45))
