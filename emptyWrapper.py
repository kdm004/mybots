import os
import time
import glob 
import constants as c

zzz = 2

# Delete Non-Champion brain.nndf files
fp = open('bestBrains.txt', 'r') 
lines = fp.readlines()
cleanLines = []
for entry in lines:
    cleanLines.append(entry.replace('\n',''))
cleanLines = list(map(int, cleanLines))
print('Here are bestBrains entries:',cleanLines)
fp.close()

numberOfBrainFiles = len(glob.glob("brainFiles/brain*.nndf"))
for i in range(c.populationSize*350): # changed from numberOfBrainFiles since some brains are out of that range. max(cleanLines) could be the first of a batch of populationSize.
    if i not in cleanLines:
        #print("Here is i:",i)
        os.system('rm brainFiles/brain'+str(i)+'.nndf')
        while os.path.exists('brainFiles/brain'+str(i)+'.nndf'):
            os.system('rm brainFiles/brain' + str(i)+'.nndf')
            time.sleep(0.1)

#-------

# for i in range(20):
#     os.system('python3 search.py')

#     time.sleep(zzz)
#     #print("HELLO DATA",i)
#     time.sleep(zzz)


for i in range(350):
    os.system('python3 search.py')
    #time.sleep(zzz*2)







