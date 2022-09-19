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


#------------------------------------
for i in range(0,10,5):
    stagger = i
#------------------------------------

simulation = SIMULATION(directOrGUI, solutionID, stagger)
simulation.Run()

simulation.Get_Fitness()

while os.path.exists('fitness*.txt'):
    time.sleep(100)