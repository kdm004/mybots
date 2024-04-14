import os
import sys
import constants as c


overallBot = 0                                    
currentSwarmNum = 0
currentBotNum = 0


if c.continueEvolution == False and c.stopStart == False:
   pass

if c.continueEvolution == False and c.stopStart == True:
   filePath = 'familiarFits.txt'                                                             # use most recent familiar fits?
   if os.path.exists(filePath):
      with open(filePath, 'r') as file:
         numPastBots = sum(1 for line in file if line.strip())
         overallBot = numPastBots                                    # + 1
         currentSwarmNum = overallBot // c.botsPerSwarm
         currentBotNum = overallBot % c.botsPerSwarm
   else:
      raise ValueError("There is no data to pick up collection.")

if c.continueEvolution == True and c.stopStart == False:
      os.system("rm bestBrains.txt")                     # these 3 files are contain the information that corresponds to the previously evolved best controller. After continuing evolution, this information is irrelevant
      os.system("rm familiarFits.txt")                   # and will be overwritten with the information for the controllers as they are evolved for more generations (given that stopStart == False)
      os.system("rm foreignFits.txt")
      os.system("rm trajectories/trajectory*.txt")


if c.continueEvolution == True and c.stopStart == True:
   filePath = 'familiarFits.txt'                                                             # use most recent familiar fits?
   if os.path.exists(filePath):
      with open(filePath, 'r') as file:
         numPastBots = sum(1 for line in file if line.strip())
         overallBot = numPastBots                                    # + 1
         currentSwarmNum = overallBot // c.botsPerSwarm
         currentBotNum = overallBot % c.botsPerSwarm
   else:
      raise ValueError("There is no data to pick up collection AND evolution.")






















for swarm in range(currentSwarmNum, c.numberOfSwarms):
    for bot in range(currentBotNum, c.botsPerSwarm):
      os.system(f"python3 search.py {swarm} {bot} {overallBot}")
      print(f'overallBot = {overallBot}')
      if c.stopStart == True:
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