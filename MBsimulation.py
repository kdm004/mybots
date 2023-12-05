# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from obstacleWorld import OBSTACLE_WORLD 
from robot import ROBOT
import pybullet as p
import pybullet_data
import os
import pyrosim.pyrosim as pyrosim


class MANYBOTS_SIMULATION:
    def __init__(self,botIndex, swarmIndex): # swarmIndex is the outer loop. So we want 35 total swarms of 10 robots. 
        self.botIndex = botIndex
        self.swarmIndex = swarmIndex
        self.directOrGUI = p.connect(p.DIRECT) #DIRECT or GUI

        bestBrains, overallChampionIndex = self.Get_Champ()

        self.positions = [
            (bestBrains[self.swarmIndex],0,-18),
            (bestBrains[self.swarmIndex],0,-14),
            (bestBrains[self.swarmIndex],0,-10),
            (bestBrains[self.swarmIndex],0,-6),
            (bestBrains[self.swarmIndex],0,-2),
            (bestBrains[self.swarmIndex],0,2),
            (bestBrains[self.swarmIndex],0,6),
            (bestBrains[self.swarmIndex],0,10),
            (bestBrains[self.swarmIndex],0,14),
            (bestBrains[self.swarmIndex],0,18)
        ]

        self.robots = ROBOT(*self.positions[self.botIndex], '999', 'none', '999')

    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.obstacleWorld = OBSTACLE_WORLD()

        for timeStep in range (c.loopLength):
            p.stepSimulation()
            self.robots.Sense(timeStep)
            self.robots.Think()
            self.robots.Act(timeStep)  

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)

        self.robots.Save_Values()


    def Get_Fitness(self):
        self.robots.Get_Obstacle_Fitness()
        #self.robot0.Get_Fitness()

        p.disconnect()


    # def __del__(self):
    #     #self.robot.Save_Values()
    #     p.disconnect()

    
    def Shift_Lines(self):
        #bestIDFile = open("bestBrains.txt","w")
        #bestBrains = bestIDFile.readlines()
        #bestIDFile.close()
        #bestBrains = list(map(int, bestBrains))
      
        lines = []
        # read file
        with open('bestBrains.txt', 'r') as fp:
            # read an store all lines into list
            lines = fp.readlines()

        # Write file
        with open('bestBrains.txt', 'w') as fp:
            # iterate each line
            for number, line in enumerate(lines):
                # delete line 5 and 8. or pass any Nth line you want to remove
                # note list index starts from 0
                if number not in [0]:
                    fp.write(line)


    def Get_Champ(self):
        fitnessFile = open('emptyEnv_fitnesses.txt','r')         # This block is to get the fitness values from emptyEnv_fitnesses.txt
        fitnessList = fitnessFile.readlines()
        fitnessFile.close()
        # fitnessList = fitnessList[self.swarmIndex*10:(self.swarmIndex*10)+10] LOOK : only required for case1
        cleanFitnessList = []
        for entry in fitnessList:
            cleanFitnessList.append(entry.replace('\n',''))
        cleanFitnessList = list(map(float,cleanFitnessList))

        bestIDFile = open("bestBrains.txt","r")                  # This block is to get the IDs of the controllers from bestBrains.txt
        bestBrains = bestIDFile.readlines()
        bestIDFile.close()
        # bestBrains = bestBrains[self.swarmIndex*10:(self.swarmIndex*10)+10] LOOK : only required for case1
        bestBrains = list(map(int, bestBrains))

        overallChampionIndex =  cleanFitnessList.index(min(cleanFitnessList))

        return bestBrains, overallChampionIndex

