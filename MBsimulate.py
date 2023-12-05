import constants as c
import random as random
import numpy as numpy
import pyrosim.pyrosim as pyrosim 
import pybullet_data
import pybullet as p
import time
from MBsimulation import MANYBOTS_SIMULATION as MB_SIMULATION
import sys
import os
import math


# List of robot x,y positions
positions = [
    (0, -18),
    (0, -14),
    (0, -10),
    (0, -6),
    (0, -2),
    (0, 2),
    (0, 6),
    (0, 10),
    (0, 14),
    (0, 18)
]

# calculate distance between two points (coordinates)
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Determine currentBot
def Get_Current_Bot_Number():
    currentBot = 0
    currentSwarm = 0
    file_path = 'obstacleEnv_fitnesses.txt'
    if os.path.exists(file_path):
        fp = open(file_path, 'r') 
        lines = fp.readlines()
        clean_lines = []
        for entry in lines:
            clean_lines.append(entry.replace('\n',''))
        clean_lines = list(map(float, clean_lines))
        fp.close()
        currentBot = len(clean_lines) % 10
        currentSwarm = int((len(clean_lines) - 1 - currentBot) / 10)
    return currentBot, currentSwarm


currentBot, currentSwarm = Get_Current_Bot_Number()
num_coordinates_to_skip = 0

# Generate SDF file for unfamiliar environment
pyrosim.Start_SDF("obstacleWorld.sdf")
# for x in range(6, -22-4, -4): 
#     for y in range(-28, 28+2, 2): 
#         current_coordinate = (x, y)
#         current_position = positions[currentBot]
            
#         # Check if the y-coordinate is within 10 units of the current position's y-coordinate
#         if abs(current_coordinate[1] - current_position[1]) > 10:                                 # removes blocks in the y direction (perpendicular to robot motion)
#             continue  # Skip this coordinate
#         if abs(current_coordinate[0] - current_position[0]) < 22:                                 # removes blocks in the x direction (parallel to robot motion)
#             continue  # Skip this coordinate

#         distances = [(distance(current_position, (x, y)), (x, y)) for x in range(6, -22-4, -4) for y in range(-28, 28+2, 2)]
#         distances.sort(key=lambda x: x[0])
#         coordinates_to_skip = [coord for _, coord in distances[:num_coordinates_to_skip]]
#         if current_coordinate in coordinates_to_skip:
#             continue  # Skip this coordinate
#         pyrosim.Send_Cube(name="Box", pos=[x, y, .5], size=[1, 1, 1]) # formula: [x,y,z]
pyrosim.End()

# for swarmIndex in range(int(700/10)):
#     for botIndex in range(10):
#         print(f'currentSwarm, currentBot = {swarmIndex}, {botIndex}')
#         MBSIM = MB_SIMULATION(botIndex, swarmIndex)
#         MBSIM.Run()
#         MBSIM.Get_Fitness()

# Only simulate the first bot
for swarmIndex in range(1):
    for botIndex in range(1):
        print(f'currentSwarm, currentBot = {swarmIndex}, {botIndex}')
        MBSIM = MB_SIMULATION(botIndex, swarmIndex)
        MBSIM.Run()
        MBSIM.Get_Fitness()