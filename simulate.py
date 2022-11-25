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


for botIndex in range(3):
    directOrGUI = sys.argv[1]
    solutionID = sys.argv[2] #Where does this come from? Where is the os.system call? I want this for each instance of PHC.

    simulation = SIMULATION(directOrGUI, botIndex, solutionID)
    simulation.Run()
    simulation.Get_Fitness()    # might need to move p.disconnect to the Get_Fitness() function.

#os.system('rm fitness*.txt')
#while os.path.exists('fitness*.txt'):
#    time.sleep(.1)      I think this was causing the simulation to sleep endlessly


# This is copied and pasted from MBsimulate.py in order to help you understand how to loop through self.positions in simulation.py.     Inner loop is bot index
# for innerLoopIndex in range(10):
#         MBSIM = MB_SIMULATION(innerLoopIndex, outerLoopIndex)
#         MBSIM.Run()
#         MBSIM.Get_Fitness()