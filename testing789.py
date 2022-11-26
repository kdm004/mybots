
import numpy as np
import random
import constants as c

# weights = np.random.rand(c.numSensorNeurons+1,c.numMotorNeurons)    # +1 row for the extra vector of leg parts                                                  
# weights = weights * 2 - 1   
# weights[9] = 1                                      # Assign value of 1 to every cell in last row

# print(weights)



weights = np.random.rand(c.numSensorNeurons+1,c.numMotorNeurons)    # +1 row for the extra vector of leg parts                                                  

weights[0][1] = 1
#print(weights)
for i in range(7):
    weights[9][i] = random.uniform(.5,1.5)


print(weights[9])