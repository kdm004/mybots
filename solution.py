import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
#--------------------------------------------
#Cube size (length, width, height) and position (x,y,z)
length = 1
width = 1
height = 1

#we want the world block to be at (-3, 3, .5)
# Torso_FrontLeg joint has no upstream joint because we want Torso to be the parent link again. So we use abs coords for Torso_FrontLeg.
x = -3
y = 3
z = .5

x0 = 1.5
y0 = 0
z0 = 1.5

x1 = -.5
y1 = 0
z1 = -.5

x2 = .5
y2 = 0
z2 = -.5
#--------------------------------------------

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1

    def Evaluate(self,directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &") # changed from "DIRECT" to directOrGUI
        fitnessFile = open("fitness.txt","r")
        self.fitness = float(fitnessFile.read()) #Used fitnessFile, they normally use f
        fitnessFile.close()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()

    def Generate_Body(self): 
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[x0,y0,z0] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[x1,y1,z1] , size=[length,width,height])

        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[x2,y2,z2] , size=[length,width,height])

        pyrosim.End()

    def Generate_Brain(self): 

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf") #changed from brain.nndf

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
   
        for currentRow in range(3):
 
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] ) #step 7 randomsearch

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,2) #(0,2) represents 0th, 1st, and 2nd rows
        randomColumn = random.randint(0,1) #(0,1) represents 0th and 1st column
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self):
        self.myID