
import os
import time
import glob
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import nonChampDeleter as NCD
import sys
#------------------------- 

commandLineArg = sys.argv
continueOrNone = commandLineArg[1]
overallBot = commandLineArg[2]

NCD.NonChampDeleter()

phc1 = PARALLEL_HILL_CLIMBER(overallBot, continueOrNone)
time.sleep(1)
phc1.Evolve()
time.sleep(1)
phc1.Show_Best()
phc1.Write_Best_ID()
phc1.Write_Best_Fitness()

phc1.Results() #LOOK


NCD.NonChampDeleter()


# # Delete Non-Champion brain.nndf files
# fp = open('bestBrains.txt', 'r') 
# lines = fp.readlines()
# cleanLines = []
# for entry in lines:
#     cleanLines.append(entry.replace('\n',''))
# cleanLines = list(map(int, cleanLines))
# print('Here are bestBrains entries:',cleanLines)
# fp.close()

# numberOfBrainFiles = len(glob.glob("brainFiles/brain*.nndf")) 
# for i in range(c.populationSize*350): # changed from numberOfBrainFiles since some brains are out of that range. max(cleanLines) could be the first of a batch of populationSize.
#     if i not in cleanLines:
#         #print("Here is i:",i)
#         os.system('rm brainFiles/brain'+str(i)+'.nndf')
#         while os.path.exists('brainFiles/brain'+str(i)+'.nndf'):
#             os.system('rm brainFiles/brain' + str(i)+'.nndf')
#             time.sleep(0.1)




