import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem, t


def read_fitness_curves(folder_path):
    # Get a list of all files in the folder
    file_list = [f for f in os.listdir(folder_path) if f.startswith("fitnessCurve_") and f.endswith(".txt")]
    
    # Sort the file list to ensure the order
    file_list.sort()

    # Initialize an empty list to store the fitness curves
    fitness_curves = []

    # Read each file and append its content to the list
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            curve = [float(line.strip()) for line in file]
            fitness_curves.append(curve)

    # Convert the list of lists into a numpy array
    fitness_array = np.array(fitness_curves)

    # Calculate the average row and return it as a list
    average_row = np.mean(fitness_array, axis=0).tolist()
    confidence_interval = t.interval(0.95, len(fitness_array)-1, loc=np.mean(fitness_array, axis=0), scale=sem(fitness_array, axis=0))

    # Plot the average fitness curve with a 95% confidence interval
    plt.plot(average_row, label='Case #')
    plt.fill_between(range(len(average_row)), confidence_interval[0], confidence_interval[1], alpha=0.3, label=None)
    plt.title('Average Fitness Curve with 95% Confidence Interval')
    plt.xlabel('Iteration')
    plt.ylabel('Fitness Value')
    plt.legend()
    plt.show()
    return average_row

# Example usage:
folder_path = "fitnessCurves"
result = read_fitness_curves(folder_path)
print(result)


'''
TO DO:
Enable this function to plot fitness curve of each case

Take out legend for confidence interval
'''