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
#------------------------------------------------------------




#-------------------------------------------------------------
## Vectors for sensor values  (moving sensor values to sensor.py) #####
#backLegSensorValues = numpy.zeros(c.loopLength)
#frontLegSensorValues = numpy.zeros(c.loopLength)

## Vector for target angles
#targetAngles = numpy.linspace(-numpy.pi,numpy.pi, c.loopLength)

## Defining leg motor commands
#BackLeg_motorCommand = c.BackLeg_amplitude * numpy.sin(c.BackLeg_frequency * targetAngles + c.BackLeg_phaseOffset)
#FrontLeg_motorCommand = c.FrontLeg_amplitude * numpy.sin(c.FrontLeg_frequency * targetAngles + c.FrontLeg_phaseOffset)
#--------------------------------------------------------------



#numpy.save('data/motorCommand.npy', motorCommand)
#exit()

#-----    

#numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
#numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
#numpy.save('data/targetAngles.npy', targetAngles)

