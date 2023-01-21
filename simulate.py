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
solutionID = sys.argv[2] #Where does this come from? Where is the os.system call? I want this for each instance of PHC.
overallBot = sys.argv[3]
continueOrNone = sys.argv[4]
populationID = sys.argv[5]


simulation = SIMULATION(directOrGUI, solutionID, overallBot, continueOrNone, populationID)
simulation.Run()

simulation.Get_Fitness()

#os.system('rm fitness*.txt')
#while os.path.exists('fitness*.txt'):
#    time.sleep(.1)      I think this was causing the simulation to sleep endlessly

