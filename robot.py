import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy as numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import math

class ROBOT:
    def __init__(self,solutionID, swarmNumber, botNumber, overallBot = None):
        self.solutionID = solutionID
        self.swarmNumber = int(swarmNumber)
        self.botNumber = int(botNumber)



        if c.swarmType == 'case1' or c.swarmType == 'case2':
            if overallBot is not None:
                self.overallBot = overallBot
                self.robot = p.loadURDF(f"bodies/body_{self.overallBot}.urdf") 
            else:
                self.robot = p.loadURDF(f"bodies/body_{self.botNumber}.urdf") 
        elif c.swarmType == 'case3':
            self.robot = p.loadURDF(f"bodies/body_{self.swarmNumber}_{self.botNumber}_{self.solutionID}.urdf")       # Give body unique ID depending on its position


        pyrosim.Prepare_To_Simulate(self.robot)
        self.sensors = {}
        self.motors = {}
        self.values = {}  
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK(f"brains/brain_{self.swarmNumber}_{self.botNumber}_{self.solutionID}.nndf")        
        print(f"brains/brain_{self.swarmNumber}_{self.botNumber}_{self.solutionID}.nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            # print('linkName = ', linkName)
            
    def Sense(self,t):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            # print('jointName = ', jointName)
    
    def Act(self,t): 
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

    def Get_Evolution_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        positionOfBase = basePositionAndOrientation[0]
        xCoordinateOfBase = positionOfBase[0]
        f = open("tmp" + str(self.swarmNumber) + "_" + str(self.botNumber) + "_" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfBase))
        f.close()
        os.system("mv" +" "+ "tmp"+ str(self.swarmNumber) + "_" + str(self.botNumber) + "_" + str(self.solutionID)+".txt" + " " + "fitness" + "_" + str(self.swarmNumber) + "_" + str(self.botNumber) + "_" + str(self.solutionID)+".txt")
        # print('fitness:', xCoordinateOfLinkZero)
        
    def Write_Playback_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        positionOfBase = basePositionAndOrientation[0]
        xCoordinateOfBase = positionOfBase[0]
        if c.playbackEnvironment == 'foreign':
            playbackFile = 'foreignFits.txt'
        elif c.playbackEnvironment == 'familiar' and (c.swarmType == 'case2' or c.swarmType=='case3'):
            playbackFile = 'familiarFits.txt' 
        elif c.playbackEnvironment == 'familiar' and (c.swarmType == 'case1'):
            playbackFile = 'familiarFits_full.txt'
        with open(playbackFile, "a") as f:
            f.write(str(xCoordinateOfBase))
            f.write("\n")
        # print(str(xCoordinateOfLinkZero))
            
    def Record_XY(self, swarm, bot, overall):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        positionOfBase = basePositionAndOrientation[0]
        xCoordinateOfBase = positionOfBase[0]
        yCoordinateOfBase = positionOfBase[1]
        if c.playbackEnvironment == 'familiar':
            trajectoryFolder = 'trajectoryFamiliar'
        elif c.playbackEnvironment == 'foreign':
            trajectoryFolder = 'trajectoryForeign'
        # Check the number of entries in the file
        trajectoryFile = f"{trajectoryFolder}/trajectory_s{swarm}_b{bot}_o{overall}.txt"
        if os.path.exists(trajectoryFile):
            with open(trajectoryFile, "r") as f:
                num_entries = sum(1 for _ in f)
            # If the number of entries exceeds 1001, do not write new entries
            if num_entries >= 1001:
                # print("Maximum number of entries reached. Not writing new entry.")
                return
            # Otherwise, write the new entry
        with open(trajectoryFile, "a") as f:
            f.write(f"{xCoordinateOfBase} {yCoordinateOfBase}\n")
