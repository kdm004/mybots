
import numpy as np
import random
import constants as c
import sys
# weights = np.random.rand(c.numSensorNeurons+1,c.numMotorNeurons)    # +1 row for the extra vector of leg parts                                                  
# weights = weights * 2 - 1   
# weights[9] = 1                                      # Assign value of 1 to every cell in last row

# print(weights)

argLength = len(sys.argv)
print(argLength)

if sys.argv[1] == '-continue':
    # use weights from file
    inputMatrix = np.loadtxt("testing789.txt", dtype = 'f' , delimiter=' ')               # This code block will read in the matrix from a file. 
    print(inputMatrix)

else:
    weights = np.random.rand(c.numSensorNeurons+1,c.numMotorNeurons)    # +1 row for the extra vector of leg parts                                                  
    for i in range(7):
        weights[9][i] = random.uniform(.5,1.5)
    print(weights)

    # write out weights to file
    someFile = open('testing789.txt', 'w')
    np.savetxt('testing789.txt',weights)
    someFile.close()
