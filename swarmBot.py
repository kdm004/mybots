
import pyrosim.pyrosim as pyrosim 
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy as numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
from solution import SOLUTION
import time


class SWARMBOT:                          
    def __init__(self,solutionID,xi,yi):
        self.solutionID = solutionID
        self.xi = xi
        self.yi = yi

        time.sleep(2)
        self.swarmBot = p.loadURDF("bodyFiles/body"+str(self.xi)+str(self.yi)+str(self.solutionID)+".urdf") 
        pyrosim.Prepare_To_Simulate(self.swarmBot) 

        self.sensors = {}
        self.motors = {}
        self.values = {}  
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brainFiles/brain" + str(self.solutionID)+ ".nndf")



    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)



    def Sense(self,t):
        for key in self.sensors:
            self.values[t] =self.sensors[key].Get_Value(t)
            if t == c.loopLength:
                print(self.values[key])



    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    


    def Act(self,neuronName): 
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) *  c.motorJointRange 
                self.motors[jointName].Set_Value(self.swarmBot, desiredAngle) 



    def Save_Values(self):
        for key in self.motors:
            self.motors[key].Save_Values()
        for key in self.sensors:
            self.sensors[key].Save_Values()



    def Think(self):
        self.nn.Update()
        self.nn.Print()



    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.swarmBot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close
        os.system("mv" +" "+ "tmp"+str(self.solutionID)+".txt" + " " + "fitness"+str(self.solutionID)+".txt")



    def Get_Obstacle_Fitness(self):                
        self.stateOfLinkZero = p.getLinkState(self.swarmBot,0)
        self.positionOfLinkZero = self.stateOfLinkZero[0]
        self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]
        
        # Write fitness to txt file
        f = open('cluttered_fitnesses.txt','a')
        f.write(str(self.xCoordinateOfLinkZero-self.xi)) # displacement from origin, not distance
        f.write('\n')
        f.close


