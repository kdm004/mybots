
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



#-------------------------------------------------------------------
zeroList = []
for i in range(c.populationSize):
    zeroList.append(0)

swarmList = []
for i in range(10):
    swarmList.append(zeroList)

myMatrices = []
for i in range(c.numberOfSwarms):
    myMatrices.append(swarmList)

# print(myMatrices[0][8][4])
print('------------------------------------')
myMatrices[0][8][4] = 3 #weights



print(myMatrices)

#print(myMatrices[0 or 1][0 to 9][0 to 4]) # yes, yes, 

# print(myMatrices[swarm][bot][ID])


#matrixOfWeights[self.emptySwarmIndex*10+self.emptyBotIndex][int(self.myID)-(5*self.emptySwarmIndex)] = self.weights


