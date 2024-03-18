import os
import numpy as np
from scipy.spatial.transform import Rotation as R

# Define the path to the file
file_path = "/home/marmot/dixiao/ME5413_2/Lidar_file/lego_tum.txt"
print("working:", os.getcwd())
# Read the file content
with open(file_path, "r") as file:
    lines = file.readlines()

# Define the transformation matrix from camera 0 to body frame
cam0_T_body = np.array([
    [0.00875116, -0.99986423, 0.01396015, -0.33908972],
    [-0.00479609, -0.01400249, -0.99989048, 0.74680283],
    [0.99995014, 0.00868325, -0.00491798, -1.09574845],
    [0., 0., 0., 1.]
])
# Process and transform each line, results will be saved with four decimal places
transformed_lines_precise = []

# Process and transform each line
transformed_lines = []
for line in lines:
    parts = line.strip().split(" ")
    timestamp = parts[0]  # Keep the timestamp
    position = np.array([float(parts[1]), float(parts[2]), float(parts[3])])
    quaternion = np.array([float(parts[4]), float(parts[5]), float(parts[6]), float(parts[7])])

    # Transform position
    transformed_position = np.dot(cam0_T_body[:3, :3], position.T).T + cam0_T_body[:3, 3]

    # Transform rotation
    rotation = R.from_quat(quaternion)
    transformed_rotation = R.from_matrix(cam0_T_body[:3, :3]) * rotation
    transformed_quaternion = transformed_rotation.as_quat()

    # Combine transformed data and retain four decimal places
    transformed_line = np.hstack((transformed_position, transformed_quaternion))
    transformed_line_precise = np.round(transformed_line, 4)

    # Combine the timestamp and transformed data into one line, then add to the results list
    transformed_lines_precise.append(timestamp + " " + " ".join(map(str, transformed_line_precise)))

# Write the transformed data to a new file
output_file_path_precise = "/home/marmot/dixiao/ME5413_2/Lidar_file/transformed_lego_tum.txt"
with open(output_file_path_precise, "w") as output_file:
    for line in transformed_lines_precise:
        output_file.write(line + "\n")

output_file_path_precise

