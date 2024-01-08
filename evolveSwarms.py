import os
import sys
import constants as c



# Evolve robots
overallBot = 0                                    
currentSwarmNum = 0
currentBotNum = 0
filePath = 'familiarFits.txt'
if os.path.exists(filePath):
   with open(filePath, 'r') as file:
      numPastBots = sum(1 for line in file if line.strip())
      overallBot = numPastBots                                    # + 1
      currentSwarmNum = overallBot // c.botsPerSwarm
      currentBotNum = overallBot % c.botsPerSwarm




for swarm in range(currentSwarmNum, c.numberOfSwarms):
    for bot in range(currentBotNum, c.botsPerSwarm):
      os.system(f"python3 search.py {swarm} {bot} {overallBot}")
      print(f'overallBot = {overallBot}')
      if bot == c.botsPerSwarm - 1:                               # currentBotNum starts where simulation interrupted. We reset currentBotNum to 0 after we complete the interrupted swarm so that the next swarm doesn't start on the interrupted bot number.
         currentBotNum = 0
      overallBot += 1

      if c.swarmType == 'case1':
          if overallBot == (c.numberOfSwarms):
             exit()


'''
To do:
Test this. If successful, push it.
Test with case1
Test with case1 continue
Test with case2
Test with case2 continue
Test with case3
Test with case3 continue

Make sure fitnessTemp are deleted between runs so that the sim doesn't 
get hung up.


pop = 20
gens = 100




We have said that now, each time we run evolveSwarms.py, our first swarm starts on the "currentBotNum" for the botNumber

'''