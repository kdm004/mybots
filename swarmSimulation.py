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
    def __init__(self,directOrGUI, overallBot):
        self.directOrGUI = directOrGUI 
        self.overallBot = overallBot
        self.swarmNumber = math.floor(self.overallBot / c.botsPerSwarm)
        self.botNumber = self.overallBot % c.botsPerSwarm
        self.bestBrains = self.Get_Brain_IDs()


        # for case1:
        self.populationID = self.bestBrains[self.swarmNumber]
        self.initialPos = c.botPositions[self.botNumber]


        
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)



        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.robot = ROBOT(self.populationID, self.overallBot)
        self.world = WORLD()


    def Get_Brain_IDs(self):
        with open("bestBrains.txt", "r") as f:
            bestBrains = [int(line.strip()) for line in f]
        return bestBrains
    





