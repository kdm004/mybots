import filecmp

def are_files_equal(file1, file2):
    return filecmp.cmp(file1, file2)

def compare_files(path1, path2):
    are_files_identical = are_files_equal(path1, path2)

    if are_files_identical:
        print("The files are identical.")
    else:
        print("The files are different.")

# compare_files('empty_motors_dict.txt', 'obstacles_motors_dict.txt')
compare_files('sensor_data_empty.txt', 'sensor_data_obstacles.txt')