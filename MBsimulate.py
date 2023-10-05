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



# Your list of positions
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

# Function to calculate the Euclidean distance between two points (coordinates)
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Your code to determine currentBot
def Get_Current_Bot_Number():
    currentBot = 0
    currentSwarm = 0
    if os.path.exists('obstacleEnv_fitnesses.txt'):
        fp = open('obstacleEnv_fitnesses.txt', 'r') 
        lines = fp.readlines()
        cleanLines = []
        for entry in lines:
            cleanLines.append(entry.replace('\n',''))
        cleanLines = list(map(float, cleanLines))
        fp.close()
        
        currentBot = len(cleanLines) % 10
        currentSwarm = int((len(cleanLines)-1 - currentBot) / 10)

    return currentBot, currentSwarm

# Define the number of closest coordinates to skip
num_coordinates_to_skip = 5

currentBot, currentSwarm = Get_Current_Bot_Number()

# Your Pyrosim SDF setup code here
pyrosim.Start_SDF("obstacleWorld.sdf")
for x in range(10, -22-2, -2): 
    for y in range(-28, 28+2, 2): 
        current_coordinate = (x, y)
        current_position = positions[currentBot]
        distances = [(distance(current_position, (x, y)), (x, y)) for x in range(10, -22-2, -2) for y in range(-28, 28+2, 2)]
        distances.sort(key=lambda x: x[0])
        coordinates_to_skip = [coord for _, coord in distances[:num_coordinates_to_skip]]
        if current_coordinate in coordinates_to_skip:
            continue  # Skip this coordinate
        pyrosim.Send_Cube(name="Box", pos=[x, y, .5], size=[1/3, 1/3, 1/3]) 

pyrosim.End()



for swarmIndex in range(int(700/10)):
    for botIndex in range(currentBot, 10):
        MBSIM = MB_SIMULATION(botIndex, swarmIndex)
        MBSIM.Run()
        MBSIM.Get_Fitness()
