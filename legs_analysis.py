import numpy as np

with open('bestBrains.txt', 'r') as best_brains_file:
    best_brains = [int(line.strip()) for line in best_brains_file]

average_matrix = []  # To store the matrix of averages
row = []  # To store the current row

upper_average_matrix = []  # To store the matrix of upper averages
upper_row = []  # To store the current row

lower_average_matrix = []  # To store the matrix of lower averages
lower_row = []  # To store the current row

for i in range(700):
    for j in range(5):
        filename = f'weightsFiles/weights{i}_{j}.txt'
        
        if i + j in best_brains:
            # Read the file and calculate the average of the last line
            with open(filename, 'r') as weights_file:
                lines = weights_file.readlines()
                if lines:
                    last_line = lines[-1].strip().split()
                    
                    values = [float(val) for val in last_line]
                    average = sum(values) / len(values)
                    row.append(average)
                    if len(row) == 10:
                        average_matrix.append(row)
                        row = []  # Reset the row

                    # average of first 4 entries in last line (upper legs)
                    upper_values = [float(val) for val in last_line[:4]]
                    upper_average = sum(upper_values) / len(upper_values)
                    upper_row.append(upper_average)
                    if len(upper_row) == 10:
                        upper_average_matrix.append(upper_row)
                        upper_row = []  # Reset the row

                    # average of first 4 entries in last line (lower legs)
                    lower_values = [float(val) for val in last_line[-4:]]
                    lower_average = sum(lower_values) / len(lower_values)
                    lower_row.append(lower_average)
                    if len(lower_row) == 10:
                        lower_average_matrix.append(lower_row)
                        lower_row = []  # Reset the row




# Write the matrix to a file called 'avg_lengths.txt'
with open('legs_array.txt', 'w') as array_file:
    for row in average_matrix:
        array_file.write(' '.join(map(str, row)) + '\n')

# Write the matrix to a file called 'upper_avg_lengths.txt'
with open('upper_legs_array.txt', 'w') as array_file:
    for upper_row in upper_average_matrix:
        array_file.write(' '.join(map(str, upper_row)) + '\n')

# Write the matrix to a file called 'lower_avg_lengths.txt'
with open('lower_legs_array.txt', 'w') as array_file:
    for lower_row in upper_average_matrix:
        array_file.write(' '.join(map(str, lower_row)) + '\n')


matrix_array = np.array(average_matrix)
average_of_matrix = np.mean(matrix_array)
std_deviation = np.std(matrix_array)

upper_matrix_array = np.array(upper_average_matrix)
upper_average_of_matrix = np.mean(upper_matrix_array)
upper_std_deviation = np.std(upper_matrix_array)

lower_matrix_array = np.array(lower_average_matrix)
lower_average_of_matrix = np.mean(lower_matrix_array)
lower_std_deviation = np.std(lower_matrix_array)



# Write the average leg length to a file
with open('all_legs_avgs.txt', 'w') as output_file:
    output_file.write(f"Average leg length: {average_of_matrix}" + '\n')
    output_file.write(f"Standard Deviation: {std_deviation}" + '\n' + '\n')

    output_file.write(f"Average upper leg length: {upper_average_of_matrix}" + '\n')
    output_file.write(f"Standard Deviation: {upper_std_deviation}" + '\n' + '\n')

    output_file.write(f"Average lower leg length: {lower_average_of_matrix}" + '\n')
    output_file.write(f"Standard Deviation: {lower_std_deviation}")


