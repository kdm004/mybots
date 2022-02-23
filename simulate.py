import constants as c
import random as random
import numpy as numpy
import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
import time
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]

simulation = SIMULATION(directOrGUI)
simulation.Run()

simulation.Get_Fitness()




