import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem, t
from itertools import islice
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu



def Plot_Fitness_Curves(folder_paths, labels):
    '''
    Description: 
        - Plots fitness curve for each robot with a 95% confidence interval based on swarm type

    Parameters:
        - folder_paths: folder of .txt files 
        - labels: list of strings

    Returns:
        - None
    '''

    if len(folder_paths) != len(labels):
        raise ValueError("Number of folders and labels must be the same.")

    # Initialize an empty list to store fitness data for each folder
    all_fitness_data = []

    # Iterate over each folder
    for folder_path in folder_paths:
        file_list = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

        # Initialize an empty list to store fitness values for each generation
        fitness_data = []

        # Read fitness values from each file
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                # Extract fitness values from the file and convert to floats
                fitness_matrix = np.array([list(map(float, line.split(','))) for line in file.readlines()])

                # Calculate average fitness for each generation
                average_fitness = np.mean(fitness_matrix, axis=1)
                fitness_data.append(average_fitness)

        # Stack the fitness data for each generation vertically
        fitness_data = np.vstack(fitness_data)

        # Append fitness data for this folder to the overall list
        all_fitness_data.append(fitness_data)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Iterate over each folder's fitness data and label
    for fitness_data, label in zip(all_fitness_data, labels):
        mean_fitness = np.mean(fitness_data, axis=0)
        confidence_interval = t.interval(0.95, len(fitness_data) - 1, loc=np.mean(fitness_data, axis=0), scale=sem(fitness_data, axis=0))
        generations = np.arange(len(mean_fitness))
        plt.plot(generations, mean_fitness, label=f'{label} - Average Fitness')
        plt.fill_between(generations, confidence_interval[0], confidence_interval[1], alpha=0.3, label=None)

    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.title('Average Fitness Curve with 95% Confidence Interval')
    plt.legend()
    plt.show()


def Get_Swarm_Fits(fitnessFile, botsPerSwarm, numLinesToRead=None):
    '''
    Description:
        - Gets the fitness of a swarm by finding the maximum inter-bot fitness

    Parameters:
        - fitnessFile: txt file where each line is a number
        - botsPerSwarm: integer number of bots in each swarm
        - numLinesToRead: optional parameter specifying the number of lines to read from the file

    Returns:
        - None
    '''

    # Read nums from the file
    with open(fitnessFile, 'r') as file:
        lines_to_read = file if numLinesToRead is None else islice(file, numLinesToRead)
        numbers = [float(line.strip()) for line in lines_to_read]   

    # transform data from (-)=more fit to (+)=more fit
    numbers = [num*-1 for num in numbers]

    # check if the length of the list is divisible by botsPerSwarm
    if len(numbers) % botsPerSwarm != 0:
        raise ValueError("Length of the list is not divisible by botsPerSwarm")

    # compute avg of every <botsPerSwarm> lines
    bestOfEachSwarm = [np.max(numbers[i:i+botsPerSwarm]) for i in range(0, len(numbers), botsPerSwarm)]

    return bestOfEachSwarm




def Check_Normal_Distribution(data):
    '''
    Description:
    - Prints the result of a shapiro-wilk test to determine if data is normally distributed

    Parameters:
    - data: list

    Returns:
    - None

    '''
    # Perform Shapiro-Wilk test
    stat, p_value = shapiro(data)
    
    # Check the p-value
    alpha = 0.05                        # significance level
    if p_value > alpha:
        print("The data is normally distributed")
    else:
        print("The data is not normally distributed")


def mann_whitney_u_test(list1, list2, alpha=0.05):
    '''    
    Description:
        - Perform Mann-Whitney U test to determine if there is a significant difference between two lists.

    Parameters:
        - list1: First list of values
        - list2: Second list of values
        - alpha: Significance level for the test (default is 0.05)

    Returns:
        - None
   '''

    # Perform Mann-Whitney U test
    statistic, p_value = mannwhitneyu(list1, list2)

    # Check if the result is significant
    is_significant = p_value < alpha

    # Print information
    print(f"t statistic: {statistic:.5f}, p-value: {p_value},  alpha: {alpha}, {'significant' if is_significant else 'not significant'}")



import matplotlib.pyplot as plt

def side_by_side_box_plots(*lists, labels=None):
    '''    
    Desription:
        - Generate side-by-side box plots

    Parameters:
        - *lists: variable number of lists to plot.
        - labels: pptional list of labels for each box plot.

    Returns:
        - None 
    '''


    # Check if labels are provided, otherwise use default labels
    if labels is None:
        labels = [f'Case {i+1}' for i in range(len(lists))]

    # Create side-by-side box plots
    plt.boxplot(lists, labels=labels)

    # Add labels and title
    plt.ylim(-4, 12)
    plt.xlabel('')
    plt.ylabel('Swarm Fitness')
    plt.title('')

    # Show the plot
    plt.show()


    