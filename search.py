import os
import time
import glob
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER
# import nonChampDeleter as NCD
import sys
#------------------------- 

commandLineArg = sys.argv
continueOrNone = commandLineArg[1]
overallBot = commandLineArg[2]

# NCD.NonChampDeleter()

phc1 = PARALLEL_HILL_CLIMBER(overallBot, continueOrNone)
time.sleep(1)
phc1.Evolve()
time.sleep(1)
phc1.Show_Best()

phc1.Results() #LOOK


# NCD.NonChampDeleter()


