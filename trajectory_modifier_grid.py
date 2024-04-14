import os
import shutil
import random

# Function to process each file
def process_file(file_path, x_modification, y_modification):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            x, y = map(float, line.split())
            x += x_modification
            y += y_modification
            file.write(f"{x} {y}\n")

# Source and destination directories
source_dirs = ["mod_case1_10x75_trajectories", "mod_case2_10x75_trajectories", "mod_case3_10x75_trajectories"]
dest_dirs = ["edit_mod_case1_10x75_trajectories", "edit_mod_case2_10x75_trajectories", "edit_mod_case3_10x75_trajectories"]

# Dictionary to map file endings to initial x and y coordinates
file_endings_coordinates = {
    "o0": (5, -4),
    "o1": (5, -2),
    "o2": (5, 0),
    "o3": (5, 2),
    "o4": (5, 4),
    "o5": (0, -4),
    "o6": (0, -2),
    "o7": (0, 0),
    "o8": (0, 2),
    "o9": (0, 4)
}

# Iterate over each source and destination directory pair
for source_dir, dest_dir in zip(source_dirs, dest_dirs):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over files in source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.txt'):  
            source_file_path = os.path.join(source_dir, filename)
            dest_file_path = os.path.join(dest_dir, filename)
            # Copy the file
            shutil.copy(source_file_path, dest_file_path)
            # Get file ending
            file_ending = filename.split('_')[-1].split('.')[0]
            # Get initial x and y coordinates for this file ending
            x_modification, y_modification = file_endings_coordinates.get(file_ending, (0, 0))
            # Process the copied file
            process_file(dest_file_path, x_modification, y_modification)

print("Processing complete.")
