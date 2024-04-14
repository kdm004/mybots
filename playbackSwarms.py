import os
import sys
import constants as c
from swarmSimulation import SWARM_SIMULATION
import pybullet as p
import pyrosim.pyrosim as pyrosim
import math
import numpy as np

cubeLength = 0.2
cubeWidth = 0.2
cubeHeight = 0.2


# pyrosim.Start_SDF("world.sdf")
# for x in range(8 - 30, -12 - 30 - 2, -2):
#     for y in range(-6, 6 + 2, 2):  # Adjust the range to narrow the field                                       # cube field very far away
#         pyrosim.Send_Cube(name=f"Box{x}{y}", pos=[x, y, (0.3)/2], size=[0.3, 0.3, 0.3])
# # pyrosim.Send_Cube(name=f"Box", pos=[0, 0, .01], size=[10, 10, 0.3])           # sdf plane
# pyrosim.End()


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
        if c.swarmType == 'case1':
            swarmNumber = overallBot // c.botsPerSwarm**2
            botNumber = ( overallBot // c.botsPerSwarm ) % c.botsPerSwarm
        print('\n')
        print(f"{swarmNumber} and {botNumber} and {overallBot}")
        print('\n')


#-----------------Generate the cluttered environment. Skip cubes if they are close enough to a leg that its corner can touch the leg's corner
        

        

        if c.swarmType == 'case1' or c.swarmType == 'case2':
            pyrosim.Start_SDF("world.sdf")
            for x in range(10, -14 - 2, -2):
                for y in range(-8, 8 + 2, 2):
                    # pass
                    pyrosim.Send_Cube(name=f"Box{x}{y}", pos=[x,y, cubeHeight/2], size=[cubeLength, cubeWidth, cubeHeight])
            pyrosim.End()

        
        else:
            with open("bestBrains.txt", "r") as file:
                lines = file.readlines()
            botID = int(lines[overallBot].strip())

            # open body file
            if c.swarmType == 'case3':
                bodyFile = f"bodies/body_{swarmNumber}_{botNumber}_{botID}.urdf"
            else:
                bodyFile = "bodies/body.urdf"
            with open(bodyFile, "r") as body_file:
                bodyLines = body_file.readlines()
                
            # get x and y coordinates
            lowerLegXY = []
            for i, line in enumerate(bodyLines):
                if '<joint name=' and "LowerLeg"in line:
                    for j in range(2):
                        lowerLegLine = bodyLines[i + j]
                        if 'xyz=' in lowerLegLine:
                            coordsStr = lowerLegLine.split('xyz="')[1].split('"')[0]
                            coords = [float(coord) for coord in coordsStr.split()]
                            lowerLegXY.append(coords[:2])
                            print(coords)
            print('relative coords:',lowerLegXY)

            # translate from x and y relative coordinates to absolute coordinates
            for i in range(len(lowerLegXY)):
                for j in range(len(lowerLegXY[i])):
                    if lowerLegXY[i][j] > 0:
                        lowerLegXY[i][j] += 0.5
                    elif lowerLegXY[i][j] <0:
                        lowerLegXY[i][j] += -0.5
            print('absolute coords:', lowerLegXY)

            # get z coords
            lowerLegs = []
            for i, line in enumerate(bodyLines):
                if '<link name=' and "LowerLeg"in line:
                    lowerLegLine = bodyLines[i + 9]          # 9th line below
                    if 'box size=' in lowerLegLine:
                        legsStr = lowerLegLine.split('box size="')[1].split('"')[0]
                        print("leg string",legsStr)
                        legs = [float(coord) for coord in legsStr.split()]
                        lowerLegs.append(legs[2])

            # Get lower most positions of the legs in absolute coordinates        
            longestLeg = np.max(lowerLegs)
            lowerLegZ = []
            for leg in lowerLegs:
                lowerLegZ.append(longestLeg - leg)      # calculate the distance of the leg's lowest point from the ground for each leg


            # Put together x,y,z of lowermost leg position
            lowerLegCoords = [[x, y, z] for [x, y], z in zip(lowerLegXY, lowerLegZ)]   # this is the lowermost location of each of the lower legs

            print(lowerLegCoords)



            legLength = 0.2
            legWidth = 0.2
            legSafetyDistance = 0.02    # issue might arise since initial height of cubes are 0.01. This is to stop those issues. added another 0.01 here for redundancy

            pyrosim.Start_SDF("world.sdf")

            for x in range(10, -14 - 2, -2):
                for y in range(-8, 8 + 2, 2):
                    cubePosition = np.array([x, y, (cubeHeight) / 2])            

                    # check if the cube is too close to any lower leg
                    tooClose = False
                    for legCoord in lowerLegCoords:
                        legX, legY, legZ = legCoord
                        if (abs(x - legX) < cubeLength / 2 + legLength / 2 + legSafetyDistance and
                                abs(y - legY) < cubeWidth / 2 + legWidth / 2 + legSafetyDistance and
                                abs(cubePosition[2] - legZ) < (cubeHeight) / 2 + legSafetyDistance):
                            tooClose = True
                            break

                    # gen cube only if not too close to any lower leg
                    if not tooClose:
                        pyrosim.Send_Cube(name=f"Box{x}{y}", pos=cubePosition, size=[cubeLength, cubeWidth, cubeHeight])

            pyrosim.End()

        

#-----------------

        swarmSim = SWARM_SIMULATION(c.playbackView, swarmNumber, botNumber, overallBot)
        # swarmSim.Create_World(*initialPos)                                        Causes an error whenever it is called. Why?
        swarmSim.Run()
        swarmSim.Get_Fitness()
        swarmSim.Cleanup()
        currentBotNum = 0
        overallBot += 1





