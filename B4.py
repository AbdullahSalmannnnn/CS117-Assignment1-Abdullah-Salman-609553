# B4 - Continuous Discharge Analysis
# Finds the longest streak of strictly decreasing battery voltage readings
# (one reading per minute) and prints its length, starting and ending voltage.

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

longest_length = 1
longest_start = 0
current_length = 1
current_start = 0

for index in range(1, len(voltages)):
    if voltages[index] < voltages[index - 1]:
        # The voltage dropped, so the current streak continues
        current_length = current_length + 1
    else:
        # The drop stopped, so a new streak starts from this reading
        current_length = 1
        current_start = index

    if current_length > longest_length:
        longest_length = current_length
        longest_start = current_start

longest_end = longest_start + longest_length - 1

print("Longest continuous drop:", longest_length, "minutes")
print("Started at:", voltages[longest_start], "V")
print("Ended at:", voltages[longest_end], "V")
