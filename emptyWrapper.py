import os
import time
import glob 
import constants as c
# import nonChampDeleter as NCD
import sys


commandLineArg = sys.argv # [emptyWrapper.py, continue]

<<<<<<< HEAD
for i in range(70): # 35 for case1
    os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot
    #time.sleep(zzz*2)
=======
if commandLineArg[1] == 'none':
    if os.path.exists('bestBrains.txt'):
        fp = open('bestBrains.txt', 'r') 
        lines = fp.readlines()
        cleanLines = []
        for entry in lines:
            cleanLines.append(entry.replace('\n',''))
        cleanLines = list(map(int, cleanLines))
        fp.close()
        for i in range(len(cleanLines), 70): # 700 from 350
            os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot

    else:
        for i in range(70):
            os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot

>>>>>>> origin/case1_evolved

if commandLineArg[1] == 'continue':
    for i in range(70): # if interrupted, range should begin at the number we have yet to get to. Look at fitnessCurves for correct # of total gens
        os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot




