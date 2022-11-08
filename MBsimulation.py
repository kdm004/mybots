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

        self.robots = ROBOT(*self.positions[self.botIndex])
        #self.robots(*self.positions[self.botIndex])


        # self.robot0 = ROBOT(bestBrains[overallChampionIndex],-8,0)       # xi = 0, yi = 0
        # self.robot1 = ROBOT(bestBrains[overallChampionIndex-2],-4,-4)       # xi = 0, yi = 0
        # self.robot2 = ROBOT(bestBrains[overallChampionIndex],-4,4)       # xi = 0, yi = 0
        # self.robot3 = ROBOT(bestBrains[overallChampionIndex],0,-8)       # xi = 0, yi = 0
        # self.robot4 = ROBOT(bestBrains[overallChampionIndex],0,0)       # xi = 0, yi = 0
        # self.robot5 = ROBOT(bestBrains[overallChampionIndex],0,8)       # xi = 0, yi = 0
        # self.robot6 = ROBOT(bestBrains[overallChampionIndex],4,-4)       # xi = 0, yi = 0
        # self.robot7 = ROBOT(bestBrains[overallChampionIndex],4,0)       # xi = 0, yi = 0
        # self.robot8 = ROBOT(bestBrains[overallChampionIndex],4,4)       # xi = 0, yi = 0
        # self.robot9 = ROBOT(bestBrains[overallChampionIndex],8,0)       # xi = 0, yi = 0

        #self.robot5 = ROBOT(bestBrains[1],5)                   
        #self.robot10 = ROBOT(bestBrains[2],10)                 



    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.obstacleWorld = OBSTACLE_WORLD()

        for timeStep in range (c.loopLength):
            p.stepSimulation()
            self.robots.Sense(timeStep)
            self.robots.Think()
            self.robots.Act(timeStep)  

            # self.robot1.Sense(i)
            # self.robot1.Think()
            # self.robot1.Act(i)  
            
            # self.robot2.Sense(i)
            # self.robot2.Think()
            # self.robot2.Act(i)  

            # self.robot3.Sense(i)
            # self.robot3.Think()
            # self.robot3.Act(i)  

            # self.robot4.Sense(i)
            # self.robot4.Think()
            # self.robot4.Act(i)  

            # self.robot5.Sense(i)
            # self.robot5.Think()
            # self.robot5.Act(i)  

            # self.robot6.Sense(i)
            # self.robot6.Think()
            # self.robot6.Act(i)  

            # self.robot7.Sense(i)
            # self.robot7.Think()
            # self.robot7.Act(i)  
        
            # self.robot8.Sense(i)
            # self.robot8.Think()
            # self.robot8.Act(i)  

            # self.robot9.Sense(i)
            # self.robot9.Think()
            # self.robot9.Act(i)  

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)


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


