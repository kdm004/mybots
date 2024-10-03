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
        self.bestBrains = self.Get_Brain_IDs()
        self.familiarFits = self.Get_Familiar_Fits()

        # Logic for case1: select the best brain for the entire swarm ###############                                     # THIS IS WHAT NEEDS TO BE EDITED (I THINK)
        if c.swarmType == 'case1':
            # Read the number of populated lines in foreignFits.txt
            foreignFitsPath = "foreignFits.txt"
            if os.path.exists(foreignFitsPath):
                with open(foreignFitsPath, "r") as f:
                    foreignFits = [line.strip() for line in f if line.strip()]  # Remove empty lines
            else:
                foreignFits = []

            num_populated_lines_in_foreign = len(foreignFits)

            # Determine the range in familiarFits.txt to observe
            if num_populated_lines_in_foreign == 0 or not os.path.exists("foreignFits.txt"):
                range_start = 0
            else:
                range_start = num_populated_lines_in_foreign
            range_end = range_start + (c.botsPerSwarm - 1)

            # Get the sublist from familiarFits.txt for this range
            sublist = self.familiarFits[range_start:range_end + 1]
            max_value = min(sublist)                                     # Find the robot with the lowest fitness in the familiar environment...Lower fitnesses are better
            print(f"Range: {range_start}, {range_end}")
            print("here's max value:", max_value)
            max_index = self.familiarFits.index(max_value)
            best_brain_for_swarm = self.bestBrains[max_index]
            best_ID = best_brain_for_swarm # Assign the best brain and set the botNumber to the best one in the sublist
            self.botNumber = max_index  # Set botNumber to correspond to the best fitness in familiarFits

        # # Logic for case2 and case3: each robot has its own brain
        # elif c.swarmType == 'case2' or c.swarmType == 'case3':
        #     best_ID = self.bestBrains[overallBot + botNumber]  # We need to figure out how to give each bot the appropriate best_ID. Currently, we're just setting a best_ID? Idk, we'll have to test it. Maybe we can move this inside of the for loop below to use the overallBot from the loop instead of self.overallBot?

        if c.swarmType == 'case1':
            # Initialize swarm of robots
            self.robots = []
            for overallBot in range(c.botsPerSwarm):
                self.robots.append(ROBOT(best_ID, swarmNumber, botNumber, overallBot))
                # print(f"best_ID={best_ID}, swarm#={swarmNumber}, botNumber={botNumber}, overallBot={overallBot} ")
        
        if c.swarmType == 'case2' or c.swarmType == 'case3':
            # Initialize swarm of robots
            self.robots = []
            for botNumber in range(c.botsPerSwarm):
                best_ID = self.bestBrains[botNumber + self.swarmNumber*10]
                self.robots.append(ROBOT(best_ID, swarmNumber, botNumber))
                print(f"best_ID={best_ID}, swarm#={swarmNumber}, botNumber={botNumber}, overallBot={botNumber + self.swarmNumber*10} ")






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
                    time.sleep(1/5000)     # c.sleepRate

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
