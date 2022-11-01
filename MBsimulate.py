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
#for x in range(34, -34-2,-2): # -4
#        for y in range(-34, 34+2, 2): #-4
#            pyrosim.Send_Cube(name="Box", pos=[x,y,.5] , size=[1/3,1/3,1/3]) 
pyrosim.End()

manyBots_simulation = MB_SIMULATION()


while not os.path.exists("obstacleWorld.sdf"):
        time.sleep(0.01)
manyBots_simulation.Run()

#manyBots_simulation.Shift_Lines() We comment this out for case1 because if the top line is deleted by Shift_Lines(), that would change the index of the overall champion of the 35 controllers



manyBots_simulation.Get_Fitness()
