import os
import time
import glob 
import constants as c
import nonChampDeleter as NCD
import sys

commandLineArg = sys.argv # [emptyWrapper.py, continue]


for i in range(3):
    os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = swarmIndex
