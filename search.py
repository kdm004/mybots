
import os
import time
import glob
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import nonChampDeleter as NCD
import sys
#------------------------- 

commandLineArg = sys.argv
continueOrNone = commandLineArg[1]
overallBot = commandLineArg[2]

NCD.NonChampDeleter()

phc1 = PARALLEL_HILL_CLIMBER(overallBot, continueOrNone)
time.sleep(1)
phc1.Evolve()
time.sleep(1)

phc1.Show_Best()
phc1.Write_Best_ID()
phc1.Write_Best_Fitness()


phc1.Results() 

NCD.NonChampDeleter()




