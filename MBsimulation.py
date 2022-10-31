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
    def __init__(self):
        self.directOrGUI = p.connect(p.GUI) #DIRECT or GUI

        fitnessFile = open('emptyEnv_fitnesses.txt','r')         # This block is to get the fitness values from emptyEnv_fitnesses.txt
        fitnessList = fitnessFile.readlines()
        fitnessFile.close()
        cleanFitnessList = []
        for entry in fitnessList:
            cleanFitnessList.append(entry.replace('\n',''))
        cleanFitnessList = list(map(float,cleanFitnessList))

        bestIDFile = open("bestBrains.txt","r")                  # This block is to get the IDs of the controllers from bestBrains.txt
        bestBrains = bestIDFile.readlines()
        bestIDFile.close()
        bestBrains = list(map(int, bestBrains))


        overallChampionIndex =  cleanFitnessList.index(min(cleanFitnessList))

        self.robot0 = ROBOT(bestBrains[overallChampionIndex],0,0)       # xi = 0, yi = 0
        #self.robot5 = ROBOT(bestBrains[1],5)                   
        #self.robot10 = ROBOT(bestBrains[2],10)                 



    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.obstacleWorld = OBSTACLE_WORLD()

        for i in range (c.loopLength):
            p.stepSimulation()
            self.robot0.Sense(i)
            self.robot0.Think()
            self.robot0.Act(i)  

            #self.robot5.Sense(i)
            #self.robot5.Think()
            #self.robot5.Act(i)  

            #self.robot10.Sense(i)
            #self.robot10.Think()
           # self.robot10.Act(i)  

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)


    def Get_Fitness(self):
        self.robot0.Get_Obstacle_Fitness()
        #self.robot0.Get_Fitness()

        #self.robot5.Get_Fitness()
        #self.robot10.Get_Fitness()


    def __del__(self):
        #self.robot.Save_Values()
        p.disconnect()

    
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





