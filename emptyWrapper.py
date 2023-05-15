import os
import time
import glob 
import constants as c
import nonChampDeleter as NCD
import sys


commandLineArg = sys.argv # [emptyWrapper.py, continue]

if os.path.exists('bestBrains.txt'):
    fp = open('bestBrains.txt', 'r') 
    lines = fp.readlines()
    cleanLines = []
    for entry in lines:
        cleanLines.append(entry.replace('\n',''))
    cleanLines = list(map(int, cleanLines))
    fp.close()
    for i in range(len(cleanLines) ,350):
        os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot
else:
    for i in range(350):
        os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot
