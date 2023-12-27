import constants as c
import numpy as np

def dummy_func(x, y, z):
    print(x)
    print(y)
    print(z)

test1 = dummy_func(*c.botPositions[0], 1.5)


swarmType = 'case3'
weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
weights = weights * 2 - 1
if swarmType == 'case1' or swarmType == 'case2':
    legLengths = np.ones(c.numMotorNeurons)
elif swarmType == 'case3':
    legLengths = np.random.uniform(0.5, 1.5, c.numMotorNeurons)
weights = np.vstack([weights, legLengths])
print(weights)
print(np.max(weights[-1]))