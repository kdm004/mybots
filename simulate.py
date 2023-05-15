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



directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
botIndex = int(sys.argv[3])
continueOrNone = sys.argv[4]
populationID = int(sys.argv[5])

simulation = SIMULATION(directOrGUI, solutionID, botIndex, continueOrNone, populationID)
simulation.Run()
simulation.Get_Fitness()    # might need to move p.disconnect to the Get_Fitness() function.
#simulation.__del__()
