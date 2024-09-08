import time
import constants as c
from robot import ROBOT
import pybullet as p
import pybullet_data
import os
import pyrosim.pyrosim as pyrosim
from world import WORLD
import math
import numpy as np
import time

class SWARM_SIMULATION:
    def __init__(self, directOrGUI, swarmNumber, botNumber, overallBot): 
        self.directOrGUI = directOrGUI
        self.swarmNumber = swarmNumber
        self.botNumber = botNumber
        self.overallBot = overallBot
        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        elif self.directOrGUI == 'GUI':
            p.connect(p.GUI) 
        
        # Set up world and physics parameters
        p.setPhysicsEngineParameter(fixedTimeStep=c.timeStepSize,
                                    numSolverIterations=c.numSolverIterations)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, c.gravityConstant)

        self.world = WORLD()
        bestBrains = self.Get_Brain_IDs()
        familiarFits = self.Get_Familiar_Fits()

        # Logic for case1: select the best brain for the entire swarm                                       # THIS IS WHAT NEEDS TO BE EDITED (I THINK)
        if c.swarmType == 'case1':
            range_start = (overallBot // c.botsPerSwarm) * c.botsPerSwarm
            range_end = range_start + (c.botsPerSwarm - 1)
            sublist = familiarFits[range_start:range_end + 1]
            max_value = min(sublist)  # Lower fitnesses are better, so we find the lowest-fitness-robot in the swarm
            print(max_value)
            max_index = familiarFits.index(max_value)
            best_brain_for_swarm = bestBrains[max_index]

            best_ID = best_brain_for_swarm  # Assign the best brain to all bots in the swarm
            self.botNumber = max_index # Use the botNumber that corresponds to the best fitness of c.botsPerSwarm robots from the familiar environment

        # Logic for case2 and case3: each robot has its own brain
        elif c.swarmType == 'case2' or c.swarmType == 'case3':
            best_ID = bestBrains[overallBot + botNumber]  # We need to figure out how to give each bot the appropriate best_ID. Currently, we're just setting a best_ID? Idk, we'll have to test it. Maybe we can move this inside of the for loop below to use the overallBot from the loop instead of self.overallBot?

        # Initialize swarm of robots
        self.robots = []
        for overallBot in range(c.botsPerSwarm):
            self.robots.append(ROBOT(best_ID, swarmNumber, botNumber, overallBot))
            print(f"best_ID={best_ID}, swarm#={swarmNumber}, botNumber={botNumber}, overallBot={overallBot} ")

    def Run(self):
        # Run simulation for all robots
        for i in range(c.loopLength):
            p.stepSimulation()

            for robot in self.robots:
                robot.Sense(i)
                robot.Think()
                robot.Act(i)

                # Record positions of each robot
                robot.Record_XY(self.swarmNumber, self.botNumber, self.overallBot)

                if self.directOrGUI == "GUI":
                    time.sleep(1/200)     # c.sleepRate

    def Get_Fitness(self):
        for robot in self.robots:
            robot.Write_Playback_Fitness()

    def Get_Brain_IDs(self):
        with open("bestBrains.txt", "r") as f:
            bestBrains = [int(line.strip()) for line in f]
        return bestBrains

    def Get_Familiar_Fits(self):
        with open("familiarFits.txt", "r") as f:
            familiarFits = [float(line.strip()) for line in f]
        return familiarFits

    def Cleanup(self):
        p.disconnect()
