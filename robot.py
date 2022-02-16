import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy as numpy

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.values = {}     # are you sure? why not just put the numpy.zeros thing as the first line in Sense() down here?

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,t):
        for key in self.sensors:
            print(self.sensors)
            print('key is ', key)
            self.values[t] =self.sensors[key].Get_Value(t)
 



