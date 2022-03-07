import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
#--------------------------------------------
#Cube size (length, width, height) and position (x,y,z)
length = 1
width = 1
height = 1

#we want the world block to be at (-3, 3, .5)
# Torso_FrontLeg joint has no upstream joint because we want Torso to be the parent link again. So we use abs coords for Torso_FrontLeg.
x = -3
y = 3
z = 0.5

#Torso position
x0 = 0 #x0 = 1.5 
y0 = 0 #y0 = 0
z0 = 1 #z0 = 1.5

#BackLeg Position
x1 = 0
y1 = -0.5
z1 = 0
#BackLeg Size (Dimensions)
l1 = 0.2
w1 = 1
h1 = 0.2

#FrontLeg Position
x2 = 0
y2 = 0.5
z2 = 0
#FrontLeg Size (Dimensions)
l2 = 0.2
w2 = 1
h2 = 0.2

#LeftLeg Position
x3 = -0.5
y3 = 0
z3 = 0
#LeftLeg Size (Dimensions)
l3 = 1
w3 = 0.2
h3 = 0.2
#--------------------------------------------

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

    def Evaluate(self,directOrGUI):
        pass


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()

    def Generate_Body(self): 
        pyrosim.Start_URDF("body.urdf")
        
        #Torso
        pyrosim.Send_Cube(name="Torso", pos=[x0,y0,z0] , size=[length,width,height])
        
        #Back Leg
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[x1,y1,z1] , size=[l1,w1,h1])

        #Frong Leg
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[x2,y2,z2] , size=[l2,w2,h2])

        #Left Leg
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[x3,y3,z3] , size=[l3,w3,h3])        




        pyrosim.End()
        #exit() # uncommenting this allows you to see effects of code on body.urdf

    def Generate_Brain(self): 

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf") #changed from brain.nndf

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
   
        for currentRow in range(c.numSensorNeurons):
 
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] ) #step 7 randomsearch

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons - 1) #(0,2) represents 0th, 1st, and 2nd rows
        randomColumn = random.randint(0,c.numMotorNeurons - 1) #(0,1) represents 0th and 1st column
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self):
        self.myID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &") # changed from "DIRECT" to directOrGUI... added " &"

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+ str(self.myID) + ".txt"):
            time.sleep(0.01)

        fitnessFile = open("fitness"+ str(self.myID) + ".txt","r")
        self.fitness = float(fitnessFile.read()) #Used fitnessFile, they normally use f
        #print("fitness"+str(self.myID)+"=", self.fitness) # commented out for step 75 parallelHC
        fitnessFile.close()
        os.system("rm fitness"+ str(self.myID) + ".txt")
        time.sleep(.1)



       
        while os.path.exists("rm fitness"+ str(self.myID) + ".txt"):
            time.sleep(.01)