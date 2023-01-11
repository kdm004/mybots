
import time as t
import constants as c
import numpy as np
import random


# myMatrix = np.zeros((3,5))
# print(myMatrix)
# myMatrix[2][3] = 1
# print(myMatrix)


weights = np.random.rand(9+1, 8)                                                  
for i in range(8): # 7 to 8
    weights[9][i] = random.uniform(.5,1.5)
print(type(weights))


#-------------------------------------------------------------------
# zeroList = []
# for i in range(c.populationSize):
#     zeroList.append(0)

# swarmList = []
# for i in range(10):
#     swarmList.append(zeroList)

# myMatrices = []
# for i in range(c.numberOfSwarms):
#     myMatrices.append(swarmList)

# # print(myMatrices[0][8][4])
# print('------------------------------------')
# myMatrices[0][8][4][0] = 3 #weights
# print(myMatrices)
lattice = np.array((c.numberOfSwarms,10,c.populationSize))
#print(lattice)
matrix = np.empty(shape=(c.numberOfSwarms,10,c.populationSize), dtype='object')
print(matrix)
matrix[0][0][0] = weights
print(matrix)
# lattice[0][0][0] = 1
# print(lattice[0][0][0])


# print(lattice)
# print('---------------')
# lattice[0][0][0] = weights
# print(lattice)


#print(myMatrices[0 or 1][0 to 9][0 to 4]) # yes, yes, 

# print(myMatrices[swarm][bot][ID])


#matrixOfWeights[self.emptySwarmIndex*10+self.emptyBotIndex][int(self.myID)-(5*self.emptySwarmIndex)] = self.weights


