
import os
import time
import glob 
import constants as c
import nonChampDeleter as NCD
import sys

commandLineArg = sys.argv # sys.argv = ['emptyWrapper.py', '-continue']         # should probably be using the -c way
for emptySwarmIndex in range(c.numberOfSwarms): # numberOfSwarms defined in constants.py
    os.system('python3' + ' ' + 'search.py' + '  ' + str(commandLineArg[1]) + ' ' + str(emptySwarmIndex))


    # so -c way doesn't work because -c is considered to be a part of python3, so it is not in the sys.argv list.
   # change to continue instead of c