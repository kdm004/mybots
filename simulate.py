import constants as c
import random as random
import numpy as numpy
import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
import time
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()

#numpy.save('data/motorCommand.npy', motorCommand)
#exit()

#-----    

#numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
#numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
#numpy.save('data/targetAngles.npy', targetAngles)

