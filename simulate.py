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

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()

simulation.Get_Fitness()

while os.path.exists('fitness*.txt'):
    time.sleep(100)