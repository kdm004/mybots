import os
import sys
import constants as c
from swarmSimulation import SWARM_SIMULATION
import pybullet as p

# Playback swarm of robots
overallBot = 0
for swarm in range(c.numberOfSwarms):
    for bot in range(c.botsPerSwarm):
        swarmSim = SWARM_SIMULATION('DIRECT', swarm, bot, overallBot)
        swarmSim.Run()
        swarmSim.Get_Fitness()
        swarmSim.Cleanup()
        # p.disconnect()                  # the error that was occuring was a result of the p.disconnect() being in the wrong place.
        overallBot += 1



if c.swarmType == 'case1':  
    swarmIndices = [j for j in range(c.numberOfSwarms)]                                         # seems correct
    botIndices = [j for j in range(c.numberOfSwarms) for i in range(c.botsPerSwarm)]            # seems correct                                    

if c.swarmType == 'case2' or 'case3':
    swarmIndices = list(range(c.numberOfSwarms))
    botIndices = list(range(c.botsPerSwarm))


for swarm in swarmIndices:
    for bot in botIndices:
        swarmSim = SWARM_SIMULATION('DIRECT', swarm, bot)
        swarmSim.Run()
        swarmSim.Get_Fitness()
        swarmSim.Cleanup()




