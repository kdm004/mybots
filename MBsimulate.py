
# In this file, we want to run the simulation by generating several robot instances
#------------------------

#STEP 1
        # Run search.py in a loop for the number of evolved brains you want 


#STEP 2
        # Start Simulation for manyBots

        # Read bestBrains.txt and write the contents to a list

        # Use 3 Robot Instances with the format self.robot0 = ROBOT(self.bestBrainsList[i],0)



import time
import constants as c
from world import WORLD 
from robot import ROBOT
import pybullet as p
import pybullet_data
import os


# Overwrite world.sdf with obstacle world
os.system('python3 obstacleWorld.py')


# Run simulation in obstacleWorld



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
#pyrosim.Prepare_To_Simulate(robotId) #this is in ROBOT instance




for i in range (1000):
    p.stepSimulation()


  

    time.sleep(1/(240))

    

    

#numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
#numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
#numpy.save('data/targetAngles.npy', targetAngles)
#numpy.save('data/motorCommand.npy', motorCommand)
#exit()
p.disconnect()




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



directOrGUI = sys.argv[1]
#solutionID = sys.argv[2] #Where does this come from? Where is the os.system call? I want this for each instance of PHC.


#------------------------------------

#------------------------------------

manyBots_simulation = MB_SIMULATION(directOrGUI)
manyBots_simulation.Run()

#simulation.Get_Fitness()

#while os.path.exists('fitness*.txt'):
#    time.sleep(100)