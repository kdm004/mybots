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
        self.robot = p.loadURDF("body.urdf") #changed from robotId to robot
        pyrosim.Prepare_To_Simulate(self.robot) #changed from robotId to robot
        self.sensors = {}
        self.motors = {}
        self.values = {}  
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system("rm" +" "+ "brain" + str(solutionID) + ".nndf")




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
    
    def Act(self,neuronName): # took out t from Act()
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) *  c.motorJointRange # multiplied by  c.motorJointRange ... finishing quadruped
                self.motors[jointName].Set_Value(self.robot, desiredAngle) #step 71 neurons
        
        # applyExternalForce
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[100,0,0] , posObj=[0,0,1], flags=p.LINK_FRAME)



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