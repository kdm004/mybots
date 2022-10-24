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


# Overwrite world.sdf with obstacle world
#os.system('python3 obstacleWorld.py')


pyrosim.Start_SDF("obstacleWorld.sdf")
#for x in range(-5, -15-5,-5):
#        for y in range(0, 15, 5):
#            pyrosim.Send_Cube(name="Box", pos=[x,y,.5] , size=[1/3,1/3,1/3]) 
pyrosim.End()

manyBots_simulation = MB_SIMULATION()

#manyBots_simulation.Create_World()
while not os.path.exists("obstacleWorld.sdf"):
        time.sleep(0.01)
manyBots_simulation.Run()

manyBots_simulation.Shift_Lines()

f = open('testfile.txt','a')
f.write('testing hello hello')
f.close()

manyBots_simulation.Get_Fitness()