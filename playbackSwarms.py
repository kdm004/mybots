import os
import sys
import constants as c
import swarmSimulation as SWARM_SIMULATION


# Playback swarm of robots
overallBot = 0
for swarm in range(c.numberOfSwarms):
    for bot in range(c.botsPerSwarm):
        botInSwarm = overallBot % 10
        swarmSim = SWARM_SIMULATION(overallBot)
        swarmSim.Run()
        swarmSim.Get_Fitness()
        overallBot += 1
