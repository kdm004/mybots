
import os
import time
import glob 
import constants as c
import nonChampDeleter as NCD
import sys

commandLineArg = sys.argv # sys.argv = ['-c', '-emptyWrapper.py']         # should probably be using the -c way
for emptySwarmIndex in range(2):
    os.system('python3' + str(commandLineArg[0]) + 'search.py' + ' ' + str(emptySwarmIndex))


    # so -c way doesn't work because -c is considered to be a part of python3, so it is not in the sys.argv list.