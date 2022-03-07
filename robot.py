import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy as numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os


class ROBOT:
    def __init__(self,solutionID):
        self.solutionID = solutionID
        self.robot = p.loadURDF("body.urdf") 
        pyrosim.Prepare_To_Simulate(self.robot)
        self.sensors = {}
        self.motors = {}
        self.values = {}  
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        # os.system("rm" +" "+ "brain" + str(solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        # print('linkNamesToIndices from robot.py = ', pyrosim.linkNamesToIndices)
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    def Sense(self,t):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self,t): # took out t from Act()
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) *  c.motorJointRange 
                self.motors[jointName].Set_Value(self.robot, desiredAngle, t) 

    def Save_Values(self):
        for key in self.motors:
            self.motors[key].Save_Values()
        for key in self.sensors:
            self.sensors[key].Save_Values()

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close
        os.system("mv" +" "+ "tmp"+str(self.solutionID)+".txt" + " " + "fitness"+str(self.solutionID)+".txt")
        print('fitness:', xCoordinateOfLinkZero)