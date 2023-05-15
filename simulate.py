import constants as c
import random as random
import numpy as numpy
import pyrosim.pyrosim as pyrosim 
import pybullet_data
import pybullet as p
import time
from simulation import SIMULATION
import sys
import os


#for botIndex in range(3):
directOrGUI = sys.argv[1]
solutionID = sys.argv[2] #Where does this come from? Where is the os.system call? I want this for each instance of PHC.
botIndex = int(sys.argv[3]) # THIS IS NEW. THIS SHOULD BE GETTING RECEIVED FROM THE OS.SYSTEM CALL IN SOLUTION.PY.... it receives the botIndex as a string, and we convert it into an int.
#swarmIndex = int(sys.argv[4])
continueOrNone = sys.argv[4]
populationID = int(sys.argv[5])

simulation = SIMULATION(directOrGUI, solutionID, botIndex, continueOrNone, populationID)
simulation.Run()
simulation.Get_Fitness()    # might need to move p.disconnect to the Get_Fitness() function.

