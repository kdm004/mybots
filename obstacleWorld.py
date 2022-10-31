import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import os
import random
import time
import constants as c





# Create a new file which starts up the virtual environment and generates some stuff in it. there should be one of the first things 
class OBSTACLE_WORLD:
    def __init__(self):        
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("obstacleWorld.sdf")


