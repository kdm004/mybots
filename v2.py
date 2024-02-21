import matplotlib.pyplot as plt
import glob

def plot_files_in_folder(folder, color, folder_index):
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

            if folder_index == 2 and i != 4:
                plt.plot(x_values, y_values, color=color, linestyle=':', alpha=0.5, label=f'Folder: {folder}')
            elif folder_index == 3 and i != 2:
                plt.plot(x_values, y_values, color=color, linestyle=':', alpha=0.5, label=f'Folder: {folder}')
            else:
                plt.plot(x_values, y_values, color=color, label=f'Folder: {folder}')

folders = ['case1_10x75_trajectories', 'case2_10x75_trajectories', 'case3_10x75_trajectories']  
colors = ['blue', 'red', 'green']

for i, (folder, color) in enumerate(zip(folders, colors), 1):
    plot_files_in_folder(folder, color, i)

plt.xlabel('y')  # Swap x and y labels
plt.ylabel('x')  # Swap x and y labels
plt.gca().invert_yaxis() # Invert y axis
plt.title('Plot of Trajectories')
# plt.legend()
plt.grid(True)
plt.show()



