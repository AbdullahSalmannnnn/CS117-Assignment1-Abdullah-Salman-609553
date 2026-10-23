# C2 - Parallel Resistance
# Function parallel_resistance() takes a list of resistors and returns the
# equivalent resistance of the parallel combination: 1/R_eq = 1/R1 + 1/R2 + ...


def parallel_resistance(resistors):
    reciprocal_sum = 0
    for resistance in resistors:
        reciprocal_sum = reciprocal_sum + 1 / resistance
    return round(1 / reciprocal_sum, 2)


print("parallel_resistance([10, 10]) ->", parallel_resistance([10, 10]))
print("parallel_resistance([100, 200, 300]) ->", parallel_resistance([100, 200, 300]))

# Extra test with my own values
print("parallel_resistance([60, 30, 20]) ->", parallel_resistance([60, 30, 20]))
