import os

folder_path = 'fitnessCurves/'  

# Generate a list of expected file names
expected_files = [f'fitness_curve{i}.txt' for i in range(700)]

# Get the list of files in the folder
actual_files = os.listdir(folder_path)

# Find missing files
missing_files = set(expected_files) - set(actual_files)

# Print the missing files
if missing_files:
    print("Missing files:")
    for file in missing_files:
        print(file)
else:
    print("All files are present.")