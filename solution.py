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

#RightLeg Position
x4 = 0.5
y4 = 0
z4 = 0
#RightLeg Size (Dimensions)
l4 = 1
w4 = 0.2
h4 = 0.2
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
        
# Upper Extremities 
        
        # -----------All Back Legs (Upper) ----------------


        #BackLeg0 (Forward)
        pyrosim.Send_Joint( name = "Torso_BackLeg0" , parent= "Torso" , child = "BackLeg0" , type = "revolute", position = [-.4,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg0", pos=[-.4,-.5,0] , size=[.2,1,.2])
        
        #BackLeg 1 (Middle)
        pyrosim.Send_Joint( name = "Torso_BackLeg1" , parent= "Torso" , child = "BackLeg1" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg1", pos=[0,-.5,0] , size=[.2,1,.2])

        #BackLeg 2 (Rear)
        pyrosim.Send_Joint( name = "Torso_BackLeg2" , parent= "Torso" , child = "BackLeg2" , type = "revolute", position = [.4,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[.4,-.5,0] , size=[.2,1,.2])

        # -----------All Front Legs (Upper) --------------------


        #FrontLeg 0 (Forward)
        pyrosim.Send_Joint( name = "Torso_FrontLeg0" , parent= "Torso" , child = "FrontLeg0" , type = "revolute", position = [-.4,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg0", pos=[-.4,.5,0] , size=[.2,1,.2])

        #FrontLeg 1 (Middle)
        pyrosim.Send_Joint( name = "Torso_FrontLeg1" , parent= "Torso" , child = "FrontLeg1" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg1", pos=[0,.5,0] , size=[.2,1,.2])

        #FrontLeg 2 (Rear)
        pyrosim.Send_Joint( name = "Torso_FrontLeg2" , parent= "Torso" , child = "FrontLeg2" , type = "revolute", position = [.4,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[.4,.5,0] , size=[.2,1,.2])


# Lower Extremities
        
        # -----------All Back Legs (Lower) ----------------

        
        #Back Lower Leg
        pyrosim.Send_Joint( name = "BackLeg0_BackLowerLeg0" , parent= "BackLeg0" , child = "BackLowerLeg0" , type = "revolute", position = [0, -1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg0", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

        #Back Lower Leg
        pyrosim.Send_Joint( name = "BackLeg1_BackLowerLeg1" , parent= "BackLeg1" , child = "BackLowerLeg1" , type = "revolute", position = [0, -1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg1", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

        #Back Lower Leg
        pyrosim.Send_Joint( name = "BackLeg2_BackLowerLeg2" , parent= "BackLeg2" , child = "BackLowerLeg2" , type = "revolute", position = [0, -1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg2", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])




        # -----------All Front Legs (Lower) ----------------


        #Front Lower Leg
        pyrosim.Send_Joint( name = "FrontLeg0_FrontLowerLeg0" , parent= "FrontLeg0" , child = "FrontLowerLeg0" , type = "revolute", position = [0, 1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg0", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

        #Front Lower Leg
        pyrosim.Send_Joint( name = "FrontLeg1_FrontLowerLeg1" , parent= "FrontLeg1" , child = "FrontLowerLeg1" , type = "revolute", position = [0, 1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg1", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

        #Front Lower Leg
        pyrosim.Send_Joint( name = "FrontLeg2_FrontLowerLeg2" , parent= "FrontLeg2" , child = "FrontLowerLeg2" , type = "revolute", position = [0, 1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg2", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])



        pyrosim.End()
        #exit() # uncommenting this allows you to see effects of code on body.urdf

    def Generate_Brain(self): 

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf") #changed from brain.nndf


# Upper Extremity Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg0") #Forward
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "BackLeg1") #Middle
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "BackLeg2") #Rear


        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FrontLeg0") #Forward
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLeg1") #Middle
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLeg2") #Rear


# Lower Extremity Sensor Neurons

        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "BackLowerLeg0") #Forward
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "BackLowerLeg1") #Middle
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "BackLowerLeg2") #Rear


        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "FrontLowerLeg0") #Forward
        pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "FrontLowerLeg1") #Middle
        pyrosim.Send_Sensor_Neuron(name = 12 , linkName = "FrontLowerLeg2") #Rear

# Upper Extremity Motor Neurons

        pyrosim.Send_Motor_Neuron( name = 13, jointName = "Torso_BackLeg0") #Forward
        pyrosim.Send_Motor_Neuron( name = 14, jointName = "Torso_BackLeg1") #Middle 
        pyrosim.Send_Motor_Neuron( name = 15, jointName = "Torso_BackLeg2") #Rear


        pyrosim.Send_Motor_Neuron( name = 16, jointName = "Torso_FrontLeg0") #Forward
        pyrosim.Send_Motor_Neuron( name = 17, jointName = "Torso_FrontLeg1") #Middle
        pyrosim.Send_Motor_Neuron( name = 18, jointName = "Torso_FrontLeg2") #Rear


# Lower Extremity Motor Neurons

        pyrosim.Send_Motor_Neuron( name = 19, jointName = "BackLeg0_BackLowerLeg0") #Forward
        pyrosim.Send_Motor_Neuron( name = 20, jointName = "BackLeg1_BackLowerLeg1") #Middle
        pyrosim.Send_Motor_Neuron( name = 21, jointName = "BackLeg2_BackLowerLeg2") #Rear


        pyrosim.Send_Motor_Neuron( name = 22, jointName = "FrontLeg0_FrontLowerLeg0") #Forward
        pyrosim.Send_Motor_Neuron( name = 23, jointName = "FrontLeg1_FrontLowerLeg1") #Middle
        pyrosim.Send_Motor_Neuron( name = 24, jointName = "FrontLeg2_FrontLowerLeg2") #Rear



   
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