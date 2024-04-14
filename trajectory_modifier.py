import os
import shutil
import random

# Function to process each file
def process_file(file_path):
    # Determine random modification values
    x_modification = random.uniform(-5, 5)
    y_modification = random.uniform(-5, 5)

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
            # Process the copied file
            process_file(dest_file_path)

print("Processing complete.")

