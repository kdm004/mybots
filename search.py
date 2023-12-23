import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import sys

overallBot = sys.argv[1]


phc = PARALLEL_HILL_CLIMBER(overallBot)
phc.Evolve()
phc.Show_Best()
phc.Save_Evolution_History()

#for i in range(2): #this is number of simulation windows that will pop up. 3 are currently popping
    # up because there's another "simulate.py" call in SOLUTION's Evaluate(self)
#    os.system("python3 generate.py")
#    os.system("python3 simulate.py")