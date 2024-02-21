import matplotlib.pyplot as plt
import glob

def plot_files_in_folder(folder, color):
    for i in range(10):
        position_files = glob.glob(f"{folder}/*o{i}.txt")
        for position_file in position_files:
            x_values = []
            y_values = []

            with open(position_file, 'r') as file:
                for line in file:
                    x, y = map(float, line.split())
                    x_values.append(y)  # Swap x and y
                    y_values.append(x)  # Swap x and y

            plt.plot(x_values, y_values, color=color, label=f'Folder: {folder}')

folders = ['case1_10x75_trajectories', 'case2_10x75_trajectories', 'case3_10x75_trajectories']  
colors = ['blue', 'red', 'green']

for folder, color in zip(folders, colors):
    plot_files_in_folder(folder, color)

plt.xlabel('y')  # Swap x and y labels
plt.ylabel('x')  # Swap x and y labels
plt.title('Plot of Trajectories')
plt.gca().invert_yaxis()  # Invert y axis

# plt.legend()
plt.grid(True)
plt.show()






