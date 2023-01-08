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
import pickle



pyrosim.Start_SDF("obstacleWorld.sdf")
for x in range(10, -22-2,-2): # -4
       for y in range(-28, 28+2, 2): #-4
           pyrosim.Send_Cube(name="Box", pos=[x,y,.5] , size=[1/3,1/3,1/3]) 
pyrosim.End()
#---------------------------------------------------------------------------------------------------------------------


for swarmIndex in range(34): # 34 because we want the final line number to be 350, which will be swarmIndex + 10
        for botIndex in range(10):
                MBSIM = MB_SIMULATION(botIndex, swarmIndex)
                MBSIM.Run()
                MBSIM.Get_Fitness()

#------




'''
So, Synaptic Weights will be in the matrix for that bot, and will be in its NNDF file. 

So, leg lengths will be in the matrix for that bot, and will be in its URDF file. 

2 Options:
       Option1: Get synaptic Weights + leg lengths from matrix, use that matrix as the starting point for next 5 gens
       Option2: Get Synaptic Weights from NNDF, Get Leg Lengths from URDF, put into a matrix, use matrix as starting point for next 5 gens

Let's do Option1... So let's first try this all with 3 swarms instead of 34.
Let's write out the synapticWeight + legLength matrix to a file that ends with 1 matrix for each bot, and updates itself. 
Then, let's use this matrix as the starting matrix (instead of a random matrix) for when we continue our program. 
This means that we will be opening this file of all these matrices for fpBrain and fpBody!!!
'''


# open entire folder or every file in the folder for URDF and NNDF files
# For the correct bot in the swarm, open that URDF and NNDf               
# Evolve that URDF and NNDF for 5 Generations



# if len(argv) > 2:   # if the command line input is more than just < python3 arbitraryName.py >, 




