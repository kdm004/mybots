
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


class ROBOT:
    def __init__(self,solutionID,xi,yi):
        self.solutionID = solutionID
        self.xi = xi
        self.yi = yi
        SOLUTION(solutionID).Generate_Body(xi,yi) # I think this needs to be before loadURDF

        time.sleep(2)
        self.robot = p.loadURDF("body"+str(xi)+str(yi)+str(solutionID)+".urdf")  # LOOK : 11-23-2022 : added str(solutionID)
        pyrosim.Prepare_To_Simulate(self.robot) 

        self.sensors = {}
        self.motors = {}
        self.values = {}  
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brainFiles/brain" + str(solutionID)+ ".nndf")
        #self.nn = NEURAL_NETWORK("brain" + str(solutionID)+ ".nndf")    Josh said you might need to make multiple instances of NEURAL_NETWORK inside ROBOT?
       # self.nn = NEURAL_NETWORK("brain" + str(solutionID)+ ".nndf")
        #os.system("rm" +" "+ "brain" + str(solutionID) + ".nndf")




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
                desiredAngle = self.nn.Get_Value_Of(neuronName) *  c.motorJointRange 
                self.motors[jointName].Set_Value(self.robot, desiredAngle) 



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


    def Get_Obstacle_Fitness(self):                    # do I need to specify what xi is for each instance of Get_Obstacle_Fitness? can I just say self.robot.xi?
        self.stateOfLinkZero = p.getLinkState(self.robot,0)
        self.positionOfLinkZero = self.stateOfLinkZero[0]
        self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]
        
        # Write fitness to txt file
        f = open('obstacleEnv_fitnesses.txt','a')
        f.write(str(self.xCoordinateOfLinkZero-self.xi)) # we want str(xCoordinateOfLinkZero - initialxcoord)
        f.write('\n')
        f.close

 # This function is to return the fitness of an obstacle sim fitness. The func for empty env sim fitness is in parallelHC under show_best. 
 # The reason it is there is because it needs to distinguish between all robots to see which is the best, whereas for the MB sims, there's 
 # only 1 robotBrian controller, which is already the best.



 



 






