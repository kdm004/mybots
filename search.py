import os
from hillclimber import HILL_CLIMBER
#-------------------------

hc = HILL_CLIMBER()

hc.Evolve()

#for i in range(2): #this is number of simulation windows that will pop up. 3 are currently popping
    # up because there's another "simulate.py" call in SOLUTION's Evaluate(self)
#    os.system("python3 generate.py")
#    os.system("python3 simulate.py")