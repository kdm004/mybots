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
        for i in range(len(cleanLines), 70): # 700 from 350
            os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot

    else:
        for i in range(70):
            os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot


if commandLineArg[1] == 'continue':
    if os.path.exists('emptyEnv_fitnesses.txt'):
        fp = open('emptyEnv_fitnesses.txt', 'r') 
        lines = fp.readlines()
        cleanLines = []
        for entry in lines:
            cleanLines.append(entry.replace('\n',''))
        cleanLines = list(map(str, cleanLines))
        fp.close()
        for i in range(len(cleanLines), 70): # 700 from 350
            os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot

    else: 
        for i in range(70): # 700 from 350
                    os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot