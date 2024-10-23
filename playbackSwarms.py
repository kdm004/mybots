import os
import constants as c
from swarmSimulation import SWARM_SIMULATION
import random
import numpy as np
import pyrosim.pyrosim as pyrosim  # Ensure pyrosim is imported for cube generation
import argparse

cubeLength = 0.2
cubeWidth = 0.2
cubeHeight = 0.2

def is_valid_position(new_pos, positions, leg_positions, min_separation):
    for pos in positions:
        if np.linalg.norm(np.array(new_pos) - np.array(pos)) < min_separation:
            return False
    for leg_pos in leg_positions:
        if np.linalg.norm(np.array(new_pos[:2]) - np.array(leg_pos)) < min_separation:
            return False
    return True

def Create_Familiar_Environment():
     pyrosim.Start_SDF("world.sdf")
     pyrosim.End()

def Create_Foreign_Environment(bodyFiles, swarmSeed):
    leg_positions_of_all_bots = []
    
    # Iterate over each robot body file in the list
    for bodyFile in bodyFiles:
        with open(bodyFile, "r") as body_file:
            bodyLines = body_file.readlines()

        # Extract leg positions from each file
        lowerLegXY = []
        for i, line in enumerate(bodyLines):
            if '<joint name=' and "LowerLeg" in line:
                for j in range(2):  # Assuming coordinates are in the next two lines
                    lowerLegLine = bodyLines[i + j]
                    if 'xyz=' in lowerLegLine:
                        coordsStr = lowerLegLine.split('xyz="')[1].split('"')[0]
                        coords = [float(coord) for coord in coordsStr.split()]
                        lowerLegXY.append(coords[:2])  # Extract XY coordinates only
        leg_positions_of_all_bots.extend(lowerLegXY)  # Collect leg positions from all robots

    # Set random seed so that every robot gets a unique set of obstacles
    seed_value = swarmSeed
    random.seed(seed_value)
    np.random.seed(seed_value)

    # Generate random positions for obstacles
    x_range = (10, -14) # (10, -14)
    y_range = (-26, 26) # (-8, 8) --> (-26, 26)
    cube_size = 0.2
    leg_size = 0.2
    min_separation = 0.5 # 0.5
    effective_separation = (cube_size/2) + (leg_size/2) + min_separation

    positions = []
    # Keep trying random cube positions until we get <total_cube> number of cubes
    while len(positions) < c.total_cubes:
        x = random.uniform(min(x_range), max(x_range))
        y = random.uniform(min(y_range), max(y_range))
        new_pos = (x, y, cube_size / 2)
        
        # Check if the new cube position is valid (no overlap with other cubes or robot legs)
        if is_valid_position(new_pos, positions, leg_positions_of_all_bots, effective_separation):
            positions.append(new_pos)

    # Generate cubes in the environment, avoiding leg positions
    pyrosim.Start_SDF("world.sdf")
    for i, pos in enumerate(positions):
        x, y, z = pos
        # pyrosim.Send_Cube(name=f"Box{x}{y}", pos=[x, y, z], size=[cube_size, cube_size, cube_size])
        pass
    pyrosim.End()


# Determine the correct fitness file based on the environment and swarm type
if c.playbackEnvironment == 'foreign':
    filePath = 'foreignFits.txt'
elif c.playbackEnvironment == 'familiar' and (c.swarmType == 'case1' or c.swarmType == 'case2' or c.swarmType == 'case3'):
    filePath = 'familiarFits_playback.txt'

# Load the fitness file to determine how many robots have been simulated already
if os.path.exists(filePath):
    with open(filePath, 'r') as file:
        numPastBots = sum(1 for line in file if line.strip())
        overallBot = numPastBots   
        print(overallBot)        
else:
    numPastBots = 0
    overallBot = 0           
# currentSwarmNum = 0
currentBotNum = 0                         
currentSwarmNum = overallBot // c.botsPerSwarm

#########################################################################################################
if c.swarmType == 'case1':
    # swarmNumber = overallBot // c.botsPerSwarm  ############## is this necessary? ##############
    # botNumber = overallBot % c.botsPerSwarm

    bodyFiles = []

    # currentBotNum = overallBot % c.botsPerSwarm
    for bot in range(c.botsPerSwarm):     # We don't want every single body file. We just want the 10 files
        bodyFile = f"bodies/body_{bot}.urdf"  # Define body file
        bodyFiles.append(bodyFile)

    for swarmNumber in range(currentSwarmNum, c.numberOfSwarms):

        if c.playbackEnvironment == 'foreign':      # If foreign environment, create foreign environment
            Create_Foreign_Environment(bodyFiles, swarmNumber)
        elif c.playbackEnvironment == 'familiar':   # If familiar environment, create familiar environment
            Create_Familiar_Environment()

        # swarmNumber = overallBot // c.botsPerSwarm  ############## is this necessary? ##############
        botNumber = overallBot % c.botsPerSwarm
        # Initialize and run the swarm simulation
        swarmSim = SWARM_SIMULATION(c.playbackView, swarmNumber, botNumber, overallBot)
        swarmSim.Run()
        swarmSim.Get_Fitness()
        swarmSim.Cleanup()

#########################################################################################################
elif c.swarmType == 'case2':
    
    bodyFiles = []
    # currentBotNum = overallBot % c.botsPerSwarm
    for bot in range(c.botsPerSwarm):     # We don't want every single body file. We just want the 10 files
        bodyFile = f"bodies/body_{bot}.urdf"  # Define body file
        bodyFiles.append(bodyFile)

    for swarmNumber in range(currentSwarmNum, c.numberOfSwarms):
        # Create environment with different swarm seed
        if c.playbackEnvironment == 'foreign':      # If foreign environment, create foreign environment
            Create_Foreign_Environment(bodyFiles, swarmNumber)
        elif c.playbackEnvironment == 'familiar':   # If familiar environment, create familiar environment
            Create_Familiar_Environment()

        botNumber = overallBot % c.botsPerSwarm
        swarmSim = SWARM_SIMULATION(c.playbackView, swarmNumber, botNumber, overallBot)
        swarmSim.Run()
        swarmSim.Get_Fitness()
        swarmSim.Cleanup()
        # overallBot += 1

#########################################################################################################
elif c.swarmType == 'case3':
    # overallBot = 0
    # swarmNumber = overallBot // c.botsPerSwarm
    botNumber = overallBot % c.botsPerSwarm
    for swarmNumber in range(currentSwarmNum, c.numberOfSwarms):   

        # For every c.botsPerSwarm bot in swarm, append the bodyFile to a list.  
        botNumbers = [x for x in range(c.botsPerSwarm)]
        bodyFiles = []
        for botNumber in botNumbers:
            with open("bestBrains.txt", "r") as file:
                lines = file.readlines()
                botID = int(lines[overallBot].strip())
                bodyFile = f"bodies/body_{swarmNumber}_{botNumber}_{botID}.urdf"  
                print(bodyFile)
                bodyFiles.append(bodyFile)

                # For every bodyFile in the list, create the foreign environment avoiding those body positions.
                if c.playbackEnvironment == 'foreign':      # If foreign environment, create foreign environment
                    Create_Foreign_Environment(bodyFiles)
                elif c.playbackEnvironment == 'familiar':   # If familiar environment, create familiar environment
                    Create_Familiar_Environment()


        print(swarmNumber, botNumber)
        swarmSim = SWARM_SIMULATION(c.playbackView, swarmNumber, botNumber, overallBot)
        swarmSim.Run()
        swarmSim.Get_Fitness()
        swarmSim.Cleanup()
        overallBot += 1
#########################################################################################################