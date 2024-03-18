import numpy as np
import os

# Read the file and analyze timestamp information
file_path = '/home/marmot/dixiao/ME5413_2/Lidar_file/aloam_tum.txt'

# Read the first and last lines of the file to get the range and number of timestamps
with open(file_path, 'r') as file:
    lines = file.readlines()

    start_timestamp = float(lines[0].split()[0])
    end_timestamp = float(lines[-1].split()[0])
    num_timestamps = len(lines)

# Time origin
time_origin = 1317354879.229829

# Initialize a new list for the timestamps
new_timestamps = []

# Loop through each line to calculate the new timestamps
for line in lines:
    parts = line.split()
    timestamp = float(parts[0])
    relative_timestamp = timestamp - time_origin
    new_timestamps.append(relative_timestamp)  # Add the calculated timestamp to the list

corrected_lines = []

for i, line in enumerate(lines):
    parts = line.split()
    # Directly use the new relative timestamp (already relative to the time origin)
    corrected_timestamp = f"{new_timestamps[i]:.4f}"  # Keep four decimal places for precision
    parts[0] = corrected_timestamp
    corrected_line = " ".join(parts) + "\n"
    corrected_lines.append(corrected_line)

# Save the processed data to a new file
corrected_file_path = '/home/marmot/dixiao/ME5413_2/Lidar_file/time_stamp_aloam_test.txt'

with open(corrected_file_path, 'w') as corrected_file:
    corrected_file.writelines(corrected_lines)

