import os
import sys
import constants as c



# Evolve robots
overallBot = 0                                     # later, change this to the length of the bestBrains file
for swarm in range(c.numberOfSwarms):
    for bot in range(c.botsPerSwarm):
      os.system(f"python3 search.py {swarm} {bot} {overallBot}")
      print(f'overallBot = {overallBot}')
      overallBot += 1
      
      if c.swarmType == 'case1':
          if overallBot == (c.numberOfSwarms):
             exit()


