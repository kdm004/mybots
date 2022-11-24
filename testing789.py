
import numpy as np
import random
import constants as c

weights = np.random.rand(c.numSensorNeurons+1,c.numMotorNeurons)    # +1 row for the extra vector of leg parts
weights[9] = 1                                                      # Assign value of 1 to every cell in last row
weights[0:8] = weights[0:8] * 2 - 1   

print(weights)
#print(weights *2-1)

# We want to add another ro







# l1 = 1
# l2 = 1
# l3 = 1
# l4 = 1
# l5 = 1
# l6 = 1
# l7 = 1
# l8 = 1

# legPartList = ['l1','l2','l3','l4','l5','l6','l7','l8']
# randomIndex = random.choice([0,1,2,3,4,5,6,7])
# legParts = [l1, l2, l3, l4, l5, l6, l7, l8]
# print(legParts)
# if legPartList[randomIndex] == 'l1':
#     legParts[0] = np.random.uniform(0,2)
# if legPartList[randomIndex] == 'l2':
#     legParts[1] = np.random.uniform(0,2)
# if legPartList[randomIndex] == 'l3':
#     legParts[2] = np.random.uniform(0,2)
# if legPartList[randomIndex] == 'l4':
#     legParts[3] = np.random.uniform(0,2)
# if legPartList[randomIndex] == 'l5':
#     legParts[4] = np.random.uniform(0,2)
# if legPartList[randomIndex] == 'l6':
#     legParts[5] = np.random.uniform(0,2)
# if legPartList[randomIndex] == 'l7':
#     legParts[6] = np.random.uniform(0,2)
# if legPartList[randomIndex] == 'l8':
#     legParts[7] = np.random.uniform(0,2)
# print(legParts)

