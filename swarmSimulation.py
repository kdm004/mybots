import time
import constants as c
from robot import ROBOT
import pybullet as p
import pybullet_data
import os
import pyrosim.pyrosim as pyrosim
from world import WORLD
import math


class SWARM_SIMULATION:
    def __init__(self,directOrGUI, swarmNumber, botNumber, overallBot):

        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            p.connect(p.DIRECT) 
        elif self.directOrGUI == 'GUI':
            p.connect(p.GUI) 


        self.swarmNumber = swarmNumber
        self.botNumber = botNumber
        self.overallBot = overallBot


        self.bestBrains = self.Get_Brain_IDs()  # list

        # self.initialPos = c.botPositions[self.botNumber]

        if c.swarmType == 'case1':
            self.brainID = self.bestBrains[self.botNumber]  # is this going to actually be the bestBrain for case1 or for everything?

        if c.swarmType == 'case2' or c.swarmType == 'case3':
            self.brainID = self.bestBrains[self.overallBot]  # is this going to actually be the bestBrain for case1 or for everything?
            
        self.robot = ROBOT(self.brainID, self.swarmNumber, self.botNumber) # fix this for case1. overallBot isn't the correct number to pass in here. We want them to be 0 for the first 10, 1 for the next 10, etc...


    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.world = WORLD()

        for i in range (c.loopLength):

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)   

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)
        # self.robot.Save_Values()

    def Get_Fitness(self):
        self.robot.Write_Playback_Fitness()
        

    def Get_Brain_IDs(self):
        with open("bestBrains.txt", "r") as f:
            bestBrains = [int(line.strip()) for line in f]
        return bestBrains
    
    # def Create_World(self):
    #     pyrosim.Start_SDF("world.sdf")
    #     # pyrosim.Send_Cube(name="Box", pos=[-10,5,.5] , size=[1,1,1])            this does not work when called in playbackSwarms.py
    #     pyrosim.End()
    
    def Cleanup(self):
        p.disconnect()



