import os
import sys
import constants as c
from swarmSimulation import SWARM_SIMULATION
import pybullet as p


if c.swarmType == 'case1':
    overallBot = 0
    for swarm in range(c.numberOfSwarms):
        for bot in range(c.botsPerSwarm):

            # Get correct swarm and bot number for case1
            swarmNumber = overallBot // c.botsPerSwarm**2
            botNumber = ( overallBot // c.botsPerSwarm ) % c.botsPerSwarm

            # Print numbers
            print('\n')
            print(f"{swarmNumber} and {botNumber} and {overallBot}")
            print('\n')

            swarmSim = SWARM_SIMULATION('DIRECT', swarmNumber, botNumber, overallBot)
            swarmSim.Run()
            swarmSim.Get_Fitness()
            swarmSim.Cleanup()
            overallBot += 1


elif c.swarmType == 'case2' or c.SwarmType == 'case3':
    overallBot = 0
    for swarmNumber in range(c.numberOfSwarms):
        for botNumber in range(c.botsPerSwarm):

            # Print numbers
            print('\n')
            print(f"{swarmNumber} and {botNumber} and {overallBot}")
            print('\n')

            swarmSim = SWARM_SIMULATION('DIRECT', swarmNumber, botNumber, overallBot)
            swarmSim.Run()
            swarmSim.Get_Fitness()
            swarmSim.Cleanup()
            overallBot += 1




