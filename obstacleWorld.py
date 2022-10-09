import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import os
import random
import time
import constants as c


def Create_World():
    #p.setGravity(0,0,c.gravityConstant)
    #p.loadURDF("plane.urdf")
    #p.loadSDF("world.sdf")
    pyrosim.Start_SDF("world.sdf")
   
    for x in range(-5, -15,-5):
        for y in range(-5, 15, 5):
            pyrosim.Send_Cube(name="Box", pos=[x,y,.5] , size=[1,1,1]) 

    pyrosim.End()

Create_World()


# Create a new file which starts up the virtual environment and generates some stuff in it. there should be one of the first things 
