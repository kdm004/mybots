import os
import constants as c
from swarmSimulation import SWARM_SIMULATION
import random
import numpy as np
import pyrosim.pyrosim as pyrosim  # Ensure pyrosim is imported for cube generation

cubeLength = 0.2
cubeWidth = 0.2
cubeHeight = 0.2

overallBot = 0
currentSwarmNum = 0
currentBotNum = 0

# Determine the correct fitness file based on the environment and swarm type
if c.playbackEnvironment == 'foreign':
    filePath = 'foreignFits.txt'
elif c.playbackEnvironment == 'familiar' and (c.swarmType == 'case2' or c.swarmType == 'case3'):
    filePath = 'familiarFits.txt'
elif c.playbackEnvironment == 'familiar' and c.swarmType == 'case1':
    filePath = 'familiarFits_full.txt'

# Load the fitness file to determine how many robots have been simulated already
if os.path.exists(filePath):
    with open(filePath, 'r') as file:
        numPastBots = sum(1 for line in file if line.strip())
        overallBot = numPastBots
        currentSwarmNum = overallBot // c.botsPerSwarm
        currentBotNum = overallBot % c.botsPerSwarm

# Replay each swarm based on the swarm type
for swarmNumber in range(currentSwarmNum, c.numberOfSwarms):
    leg_positions_of_all_bots = []

    # for botNumber in range(currentBotNum, c.botsPerSwarm):
    if c.swarmType == 'case1':                                                             
        swarmNumber = overallBot // c.botsPerSwarm**2
        botNumber = (overallBot // c.botsPerSwarm) % c.botsPerSwarm
    else: 
        swarmNumber = overallBot // c.botsPerSwarm                                          # Added these two statements.
        botNumber = overallBot % c.botsPerSwarm
        print(f"\nReplaying swarm {swarmNumber}, bot {botNumber}, overall bot {overallBot}\n")

    # Collect leg positions for all bots in the swarm
    with open("bestBrains.txt", "r") as file:
        lines = file.readlines()
    botID = int(lines[overallBot].strip())

    if c.swarmType == 'case3':                                                  # case 3
        bodyFile = f"bodies/body_{swarmNumber}_{botNumber}_{botID}.urdf"            
    else:                                                                       # case 1 and case 2
        bodyFile = f"bodies/body_{botNumber}.urdf"

    with open(bodyFile, "r") as body_file:
        bodyLines = body_file.readlines()

    lowerLegXY = []
    for i, line in enumerate(bodyLines):
        if '<joint name=' and "LowerLeg" in line:
            for j in range(2):  # Assuming coordinates are in the next two lines
                lowerLegLine = bodyLines[i + j]
                if 'xyz=' in lowerLegLine:
                    coordsStr = lowerLegLine.split('xyz="')[1].split('"')[0]
                    coords = [float(coord) for coord in coordsStr.split()]
                    lowerLegXY.append(coords[:2])  # Extract XY coordinates only

    leg_positions_of_all_bots.extend(lowerLegXY)  # Collect leg positions from all bots

    # Initialize and run the swarm simulation
    swarmSim = SWARM_SIMULATION(c.playbackView, swarmNumber, botNumber, overallBot)
    swarmSim.Run()
    swarmSim.Get_Fitness()
    swarmSim.Cleanup()

    # Reset the bot number and update the overall bot index
    currentBotNum = 0
    overallBot += 1

    # Generate cubes, avoiding leg positions
    if c.swarmType == 'case1' or c.swarmType == 'case2':
        def is_valid_position(new_pos, positions, leg_positions, min_separation):
            for pos in positions:
                if np.linalg.norm(np.array(new_pos) - np.array(pos)) < min_separation:
                    return False
            for leg_pos in leg_positions:
                if np.linalg.norm(np.array(new_pos[:2]) - np.array(leg_pos)) < min_separation:
                    return False
            return True

        # Set random seed so that every robot gets a unique set of obstacles
        seed_value = overallBot
        random.seed(seed_value)
        np.random.seed(seed_value)

        # Generate random positions for obstacles
        x_range = (10, -14)
        y_range = (-8, 8)
        cube_size = 0.2
        min_separation = 0.5
        total_cubes = 117

        effective_separation = cube_size + min_separation
        positions = []
        while len(positions) < total_cubes:
            x = random.uniform(min(x_range), max(x_range))
            y = random.uniform(min(y_range), max(y_range))
            new_pos = (x, y, cube_size / 2)
            if is_valid_position(new_pos, positions, leg_positions_of_all_bots, effective_separation):
                positions.append(new_pos)

        # Generate cubes in the environment, avoiding leg positions
        pyrosim.Start_SDF("world.sdf")
        for i, pos in enumerate(positions):
            x, y, z = pos
            # pyrosim.Send_Cube(name=f"Box{x}{y}", pos=[x, y, z], size=[cube_size, cube_size, cube_size])
            pass
        pyrosim.End()
