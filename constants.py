import numpy as numpy
#------------------------------------------
gravityConstant = -9.8 * 2.5 # delete * 2.5

loopLength = 5000 #change back to 1000
sleepRate = 1/5000 #changed from 1/260 ... throughout parallelHC it was set to 1/5000

amplitude = numpy.pi /4
frequency = 10
phaseOffset = numpy.pi/2
legMaxForce = 120 # change back to 20 #was at 120 at beginning of quadruped
targetAngles = numpy.linspace(-numpy.pi,numpy.pi, loopLength)


numberOfGenerations = 0  # change to 10 to complete quadruped #5 for manyBotsV2
populationSize = 1 # change to 10 to complete quadruped #5 for manyBotsV2

motorJointRange = .8 # set to .2 for oscillatory motion ... step 55 quadruped


numSensorNeurons = 9 # Edit these two statements to set the correct number of sensor and motor neurons. Don't forget the 0th sensor neuron!
numMotorNeurons = 8

#-----------------
numberOfBots = 2 # not currently used anywhere.
numberOfSwarms = 2 # used in emptyWrapper.py
 

runs = 700