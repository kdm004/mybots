
# In this file, we want to run the simulation by generating several robot instances
#------------------------

#STEP 1
        # Run search.py in a loop for the number of evolved brains you want 


#STEP 2
        # Start Simulation for manyBots

        # Read bestBrains.txt and write the contents to a list

        # Use 3 Robot Instances with the format self.robot0 = ROBOT(self.bestBrainsList[i],0)



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


# Overwrite world.sdf with obstacle world
#os.system('python3 obstacleWorld.py')


#directOrGUI = sys.argv[1]
#solutionID = sys.argv[2] #Where does this come from? Where is the os.system call? I want this for each instance of PHC.


#------------------------------------

#------------------------------------
pyrosim.Start_SDF("obstacleWorld.sdf")
pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] , size=[1,1,1]) 
pyrosim.End()

manyBots_simulation = MB_SIMULATION()

#manyBots_simulation.Create_World()
while not os.path.exists("obstacleWorld.sdf"):
        time.sleep(0.01)
manyBots_simulation.Run()

#simulation.Get_Fitness()

#while os.path.exists('fitness*.txt'):
#    time.sleep(100)