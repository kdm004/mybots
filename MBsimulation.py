# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from obstacleWorld import OBSTACLE_WORLD 
from swarmBot import SWARMBOT
import pybullet as p
import pybullet_data
import os
import pyrosim.pyrosim as pyrosim


class MANYBOTS_SIMULATION:
    def __init__(self,botIndex, swarmIndex): # swarmIndex is the outer loop. So we want 35 total swarms of 10 swarmBots. 
        self.botIndex = botIndex
        self.swarmIndex = swarmIndex
        self.directOrGUI = p.connect(p.DIRECT) #DIRECT or GUI

        #bestBrains, overallChampionIndex = self.Get_Champ()
        bestBrains = self.Get_Champ()

        self.positions = [
            (bestBrains[0+self.swarmIndex*10],0,-18),
            (bestBrains[1+self.swarmIndex*10],0,-14),
            (bestBrains[2+self.swarmIndex*10],0,-10),
            (bestBrains[3+self.swarmIndex*10],0,-6),
            (bestBrains[4+self.swarmIndex*10],0,-2),
            (bestBrains[5+self.swarmIndex*10],0,2),
            (bestBrains[6+self.swarmIndex*10],0,6),
            (bestBrains[7+self.swarmIndex*10],0,10),
            (bestBrains[8+self.swarmIndex*10],0,14),
            (bestBrains[9+self.swarmIndex*10],0,18)
        ]

        self.swarmBots = SWARMBOT(*self.positions[self.botIndex])


    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.obstacleWorld = OBSTACLE_WORLD()

        for timeStep in range (c.loopLength):
            p.stepSimulation()
            self.swarmBots.Sense(timeStep)
            self.swarmBots.Think()
            self.swarmBots.Act(timeStep)  

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)


    def Get_Fitness(self):
        self.swarmBots.Get_Obstacle_Fitness()

        p.disconnect()


    # def __del__(self):
    #     #self.swarmBot.Save_Values()
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

    # #Get the fitness of the champion
        # fitnessFile = open('emptyEnv_fitnesses.txt','r')         # This block is to get the fitness values from emptyEnv_fitnesses.txt
        # fitnessList = fitnessFile.readlines()
        # fitnessFile.close()
        # # fitnessList = fitnessList[self.swarmIndex*10:(self.swarmIndex*10)+10] LOOK : only required for case1
        # cleanFitnessList = []
        # for entry in fitnessList:
        #     cleanFitnessList.append(entry.replace('\n',''))
        # cleanFitnessList = list(map(float,cleanFitnessList))
        # overallChampionIndex =  cleanFitnessList.index(min(cleanFitnessList))

        bestIDFile = open("bestBrains.txt","r")                  # This block is to get the IDs of the controllers from bestBrains.txt
        bestBrains = bestIDFile.readlines()
        bestIDFile.close()
        # bestBrains = bestBrains[self.swarmIndex*10:(self.swarmIndex*10)+10] LOOK : only required for case1
        bestBrains = list(map(int, bestBrains))



        # return bestBrains, overallChampionIndex
        return bestBrains

        # I also commented out #bestBrains, overallChampionIndex = self.Get_Champ() at the top of the file