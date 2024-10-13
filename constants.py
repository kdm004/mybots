import numpy as np

# Simulation Parameters         # Paper parameters:
gravityConstant = -9.8          # -9.8
loopLength = 1000               # 1000
sleepRate = 1/5000              # 1/5000
timeStepSize = 1/240            # 1/240
numSolverIterations = 500       # 500. Default is 50

# Robot Parameters
# amplitude = np.pi /4
# phaseOffset = np.pi/2
# frequency = 10
legMaxForce = 50                # 50
motorJointRange = 0.8           # 0.8
numSensorNeurons = 4            # 4
numMotorNeurons = 8             # 8
legLengthRange = (0.5, 1.5)     # Only used for case3

# Evolution Parameters
numberOfGenerations = 0         # 0 for random. 75 for evolved.
populationSize = 1              # 1 for random. 10 for evolved.

# Collection parameters
swarmType = 'case2'             # Choose swarmType:                [case1, case2, or case3]
playbackEnvironment = 'familiar' # Choose environment for playback: [foreign or familiar].  Under current codebase, case2 and case3 familiarFits.txt outputted during evolution implicitly results in fitness values from their deployment. This does not hold for case1 due to controller assignment requiring manipulation through max{f1,f2,...,fb}.
numberOfSwarms = 1             # 55 
botsPerSwarm = 2               # 10
continueEvolution = False       # if continueEvolution = True, add more generations to current data (assuming same number of parents). This will evolve new bots, this will just evolve current bots further.
stopStart = False               # if stopStart = True, you can continue collecting more data by evolving more controllers. This will pickup evolution or playback data collection where you left off. This will not evolve current bots further.

botPosition = [(0,-2), (0,2), (0,6), (0,10), (0,14), (0,18)]


playbackView = 'GUI'         # DIRECT or GUI. DIRECT collects data, while GUI collects data AND shows you the simulation on-screen (affects data collection speed).     
                                # Note: GUI mode automatically collects video
