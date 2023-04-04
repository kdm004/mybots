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

phc1.Results() #LOOK


NCD.NonChampDeleter()









#phc2 = PARALLEL_HILL_CLIMBER()
#phc2.Evolve()
#phc2.Show_Best()

#phc3 = PARALLEL_HILL_CLIMBER()
#phc3.Evolve()
#phc3.Show_Best()



#--------------------------

#for i in range(2): #this is number of simulation windows that will pop up. 3 are currently popping
    # up because there's another "simulate.py" call in SOLUTION's Evaluate(self)
#    os.system("python3 generate.py")
#    os.system("python3 simulate.py")




# Initially, we had 1 instance called phc. Now, we have phc1, phc2, and phc3
# So now, we should only need to run search.py once to get brain0,brain1,brain2 | brain3, brain4, brain5 | brain6, brain7, brain8.