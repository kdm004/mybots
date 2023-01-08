import os
import time
import glob 
import constants as c
import nonChampDeleter as NCD
import sys


commandLineVar = sys.argv

for i in range(2): # let's test it with 2. So... Evolve 2 swarms for 5 generations. Playback the 2 swarms. Evolve the 2 swarms for 5 more generations.
    os.system('python3 search.py' + ' ' + str(i)) 


