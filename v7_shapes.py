import matplotlib.pyplot as plt
import numpy as np
import glob

case_numbers = ['1', '2', '3']
swarm_name = ['\nNo Diversity', '\nNeurological Diversity', '\nNeurological-Morphological Diversity']
colors = ['blue', 'red', 'green']

def plot_files_in_folder(case_number):
    for i in range(10):
        position_files = glob.glob(f"mod_case{case_number}_10x75_trajectories/*o{i}.txt")
        for position_file in position_files:
            x_values = []
            y_values = []

            with open(position_file, 'r') as file:
                for line in file:
                    x, y = map(float, line.split())
                    x_values.append(y)  # Swap x and y because our x is vertical direction        
                    y_values.append(-x)  # Swap x and y                                                  # only flip the y-axis, not the x-axis or else it'll be reflected

            if case_number == '2' and i != 4 or case_number == '3' and i != 2:
                plt.plot(x_values, y_values, color=colors[int(case_number)-1], linestyle=':', alpha=1)  # alpha is opacity
                plt.plot(x_values[-1], y_values[-1], color=colors[int(case_number)-1], marker='s', fillstyle = 'none')  # Square at the end
                plt.plot(x_values[0], y_values[0], color=colors[int(case_number)-1], marker='o') # circle at start
            else:
                plt.plot(x_values, y_values, color=colors[int(case_number)-1], linestyle='-', alpha=1) # alpha is opacity
                plt.plot(x_values[-1], y_values[-1], color=colors[int(case_number)-1], marker='s', fillstyle = 'none')  # Square at the end
                plt.plot(x_values[0], y_values[0], color=colors[int(case_number)-1], marker='o') # circle at start

def setup_plot(case_number):
    fig, ax = plt.subplots(figsize=(5, 8.8))

    # color gradient
    gradient = np.linspace(0, 1, 100).reshape(-1, 1)
    ax.imshow(gradient, aspect='auto', cmap=plt.cm.RdYlGn, extent=(-10, 10, 8, -4), alpha=0.3)

    plot_files_in_folder(case_number)

    plt.xlabel('X (m)', fontsize='17')
    plt.ylabel('Y (m)', fontsize='17')
    plt.xticks(fontsize='17') ; plt.gca().xaxis.set_major_locator(plt.MultipleLocator(4))   # space out x-ticks more
    plt.yticks(fontsize='17')

    plt.xlim(-10, 10)
    plt.ylim(-4, 8)
    # plt.gca().invert_yaxis()
    plt.title(f'Case {case_number}: {swarm_name[int(case_number)-1]} ', fontsize = '16')

    # legend w/ labels for solid and dotted lines
    solid_patch = plt.Line2D([], [], color=colors[int(case_number)-1], label='Best')

    # if case_number == '2' or case_number == '3':
    dotted_patch = plt.Line2D([], [], color=colors[int(case_number)-1], linestyle=':', label='Not Best')
    end_marker = plt.Line2D([], [], color=colors[int(case_number)-1], marker='s', linestyle='', fillstyle='none', label='End')
    start_marker = plt.Line2D([], [], color=colors[int(case_number)-1], marker='o', linestyle='', label='Start')
    plt.legend(handles=[solid_patch, dotted_patch, end_marker, start_marker], loc='upper right', fontsize = '13')
    # else:
    #     end_marker = plt.Line2D([], [], color=colors[int(case_number)-1], marker='s', linestyle='', label='End')
    #     plt.legend(handles=[solid_patch, end_marker], loc='upper right')

    plt.tight_layout()
    plt.grid(True)
    plt.savefig(f"case{case_number}_trajectories.png")
    plt.show()

setup_plot('1')
setup_plot('2')
setup_plot('3')
