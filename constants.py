import numpy as np

# Simulation Parameters
gravityConstant = -9.8 * 2.5 # delete * 2.5
loopLength = 5000
sleepRate = 1/5000 

# Robot Parameters
amplitude = np.pi /4
phaseOffset = np.pi/2
frequency = 10
legMaxForce = 120 
# targetAngles = np.linspace(-np.pi,np.pi, loopLength)
motorJointRange = 0.8 
numSensorNeurons = 9 
numMotorNeurons = 8

# Evolution Parameters
numberOfGenerations = 1 # change to 10 to complete quadruped #5 for manyBotsV2
populationSize = 1 # change to 10 to complete quadruped #5 for manyBotsV2


# environment = 'empty' 
environment = 'obstacles'
 