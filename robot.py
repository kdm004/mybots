import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy as numpy

class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf") #changed from robotId to robot
        pyrosim.Prepare_To_Simulate(self.robot) #changed from robotId to robot
        self.sensors = {}
        self.motors = {}
        self.values = {}  
        self.Prepare_To_Sense()
        self.Prepare_To_Act()


    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,t):
        for key in self.sensors:
            #print(self.sensors)
            #print('key is ', key)
            self.values[t] =self.sensors[key].Get_Value(t)
            if t == c.loopLength:
                print(self.values[key])

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self,t):
        for key in self.motors:
            self.motors[key].Set_Value(self.robot,t)
            #print(self.motors[key]) ... this prints out a bunch of stuff


    def Save_Values(self):
        for key in self.motors:
            self.motors[key].Save_Values()
        for key in self.sensors:
            self.sensors[key].Save_Values()

    def Think(self):
        pass