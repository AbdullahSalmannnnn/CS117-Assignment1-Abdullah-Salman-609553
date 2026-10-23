# C4 - Loaded Voltage Divider
# Function loaded_divider() returns the unloaded (theoretical) output voltage of a
# voltage divider and the actual output voltage when a load rl is connected across r2.


def loaded_divider(vs, r1, r2, rl):
    # Unloaded output: standard voltage divider formula
    unloaded_voltage = vs * r2 / (r1 + r2)

    # The load is in parallel with r2, so find their equivalent first
    r_parallel = (r2 * rl) / (r2 + rl)

    # Loaded output: voltage divider with r1 and the parallel equivalent
    loaded_voltage = vs * r_parallel / (r1 + r_parallel)

    return round(unloaded_voltage, 2), round(loaded_voltage, 2)


print("loaded_divider(12, 1000, 1000, 500) ->", loaded_divider(12, 1000, 1000, 500))

# Extra test with my own values
print("loaded_divider(10, 2000, 3000, 6000) ->", loaded_divider(10, 2000, 3000, 6000))
