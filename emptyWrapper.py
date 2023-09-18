import os
import time
import glob 
import constants as c
# import nonChampDeleter as NCD
import sys


commandLineArg = sys.argv # [emptyWrapper.py, continue]

if commandLineArg[1] == 'none':
    if os.path.exists('bestBrains.txt'):
        fp = open('bestBrains.txt', 'r') 
        lines = fp.readlines()
        cleanLines = []
        for entry in lines:
            cleanLines.append(entry.replace('\n',''))
        cleanLines = list(map(int, cleanLines))
        fp.close()
        for i in range(len(cleanLines), 700): # 700 from 350
            os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot

    else:
        for i in range(700):
            os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot


if commandLineArg[1] == 'continue':
    for i in range(700): # if interrupted, range should begin at the number we have yet to get to. Look at fitnessCurves for correct # of total gens
        os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot