import os
import sys
import constants as c
from swarmSimulation import SWARM_SIMULATION
import pybullet as p
import pyrosim.pyrosim as pyrosim
import math

# Generate world with obstacles ... you could put this in the inner loop, and shift the obstacles by some amount based on "bot" number.  Could do this for bots in diff pos or same pos. 
pyrosim.Start_SDF("world.sdf")

for x in range(8, -16-4, -4):
    for y in range(-12, 12+2, 2):  # Adjust the range to narrow the field

        # Calculate distance from the origin
        distance_from_origin = math.sqrt(x**2 + y**2)

        # Check if the distance is within a 6 unit radius
        if distance_from_origin >= 4:
            pyrosim.Send_Cube(name=f"Box{x}{y}", pos=[x, y, .5], size=[1/3, 1/3, 1/3])
pyrosim.End()



overallBot = 0                                    
currentSwarmNum = 0
currentBotNum = 0
filePath = 'foreignFits.txt'
if os.path.exists(filePath):
   with open(filePath, 'r') as file:
      numPastBots = sum(1 for line in file if line.strip())
      overallBot = numPastBots                                    # + 1
      currentSwarmNum = overallBot // c.botsPerSwarm
      currentBotNum = overallBot % c.botsPerSwarm



for swarmNumber in range(currentSwarmNum, c.numberOfSwarms):
    for botNumber in range(currentBotNum, c.botsPerSwarm):
        # initialPos = c.botPositions[overallBot % c.botsPerSwarm]      # bot position --> used to determine which part of a grid of obstacles to generate. Also used to keep obstacles closest to bot from generating

        if c.swarmType == 'case1':
            swarmNumber = overallBot // c.botsPerSwarm**2
            botNumber = ( overallBot // c.botsPerSwarm ) % c.botsPerSwarm

        print('\n')
        print(f"{swarmNumber} and {botNumber} and {overallBot}")
        print('\n')

        swarmSim = SWARM_SIMULATION(c.playbackView, swarmNumber, botNumber, overallBot)
        # swarmSim.Create_World(*initialPos)                                        Causes an error whenever it is called. Why?
        swarmSim.Run()
        swarmSim.Get_Fitness()
        swarmSim.Cleanup()
        currentBotNum = 0
        overallBot += 1





