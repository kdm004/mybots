import os
import sys
import constants as c
from swarmSimulation import SWARM_SIMULATION
import pybullet as p

# Playback swarm of robots
overallBot = 0
for swarm in range(c.numberOfSwarms):
    for bot in range(c.botsPerSwarm):
        swarmSim = SWARM_SIMULATION('GUI', swarm, bot)
        swarmSim.Run()
        swarmSim.Get_Fitness()
        swarmSim.Cleanup()
        # p.disconnect()                  # the error that was occuring was a result of the p.disconnect() being in the wrong place.
        overallBot += 1



