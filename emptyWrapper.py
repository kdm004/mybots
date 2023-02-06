import os
import time
import glob 
import constants as c
import nonChampDeleter as NCD
import sys

commandLineArg = sys.argv # [emptyWrapper.py, continue]

for i in range(35): # 35 for case1
    os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot
    #time.sleep(zzz*2)


NCD.Delete_Remaining()



