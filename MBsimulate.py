import constants as c
import random as random
import numpy as numpy
import pyrosim.pyrosim as pyrosim 
import pybullet_data
import pybullet as p
import time
from MBsimulation import MANYBOTS_SIMULATION as MB_SIMULATION
import sys
import os




pyrosim.Start_SDF("obstacleWorld.sdf")
for x in range(10, -22-2,-2): 
       for y in range(-28, 28+2, 2): 
           pyrosim.Send_Cube(name="Box", pos=[x,y,.5] , size=[1/3,1/3,1/3]) 
pyrosim.End()


def Get_Current_Bot_Number():
        currentBot = 0
        currentSwarm = 0
        if os.path.exists('obstacleEnv_fitnesses.txt'):
                fp = open('obstacleEnv_fitnesses.txt', 'r') 
                lines = fp.readlines()
                cleanLines = []
                for entry in lines:
                        cleanLines.append(entry.replace('\n',''))
                cleanLines = list(map(float, cleanLines))
                fp.close()
                
                currentBot = len(cleanLines) % 10
                currentSwarm = int((len(cleanLines)-1 - currentBot) / 10)

        return currentBot, currentSwarm


currentBot, currentSwarm = Get_Current_Bot_Number()
for swarmIndex in range(35):
        for botIndex in range(currentBot, 10):
                MBSIM = MB_SIMULATION(botIndex, swarmIndex)
                MBSIM.Run()
                MBSIM.Get_Fitness()
