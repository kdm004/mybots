import numpy as np

# Simulation Parameters
gravityConstant = -9.8 * 2.5 
loopLength = 1000 # was evolved for 5000
sleepRate = 1/5000 

# Robot Parameters
amplitude = np.pi /4
phaseOffset = np.pi/2
frequency = 10
legMaxForce = 120 
motorJointRange = 0.8 
numSensorNeurons = 4 
numMotorNeurons = 8

# Evolution Parameters
numberOfGenerations = 3 # change to 10 to complete quadruped #5 for manyBotsV2
populationSize = 4 # change to 10 to complete quadruped #5 for manyBotsV2




 