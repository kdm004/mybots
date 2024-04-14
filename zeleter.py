import os

folder_path = "case1_10x75_trajectories/"

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Iterate over each file in the folder
for file_name in files:
    if file_name.endswith('.txt'): 
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Truncate the file after the 1001st line
        with open(file_path, 'w') as file:
            file.writelines(lines[:1001])
