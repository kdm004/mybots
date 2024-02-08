import numpy as np

# Simulation Parameters
gravityConstant = -9.8 
loopLength = 1000 # was evolved for 5000
sleepRate = 1/5000 
timeStepSize = 1/240 #1/3800
numSolverIterations = 500 # default is 50

# Robot Parameters
amplitude = np.pi /4
phaseOffset = np.pi/2
frequency = 10
legMaxForce = 50
motorJointRange = 0.8 
numSensorNeurons = 4 
numMotorNeurons = 8
legLengthRange = (0.5, 1.5) # only used for case3

# Evolution Parameters
numberOfGenerations = 25 # 50 # 100
populationSize = 10 # 10 # 20

# collection parameters
swarmType = 'case1'  # Choose swarmType: case1, case2, case3
numberOfSwarms = 30
botsPerSwarm = 10
continueEvolution = False  # if continueEvolution = True, add more generations (assuming same number of parents)
stopStart = False           # if stopStart = True, you can continue collecting more data by evolving more controllers. This will pickup where you left off.
# continueCollection = False # currently not implemented completely. Might appear in codebase occasionally.

# playback parameters
botPosition = (0,0)
playbackView = 'DIRECT'

# Assertions
# assert len(botPositions) == botsPerSwarm    # kind of unecessary      Not needed if all bots have a (0,0) position


