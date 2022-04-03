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
       
        # -----------All Left Legs (Upper) ----------------


       #Left Leg1
        pyrosim.Send_Joint( name = "Torso_LeftLeg1" , parent= "Torso" , child = "LeftLeg1" , type = "revolute", position = [-0.5,-.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg1", pos=[-.5,-.2,0] , size=[1,.2,.2])   
     

       #Left Leg2
        pyrosim.Send_Joint( name = "Torso_LeftLeg2" , parent= "Torso" , child = "LeftLeg2" , type = "revolute", position = [-0.5,.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg2", pos=[-.5,.2,0] , size=[1,.2,.2])   

        
        
        # -----------All Right Legs (Upper) ----------------

        #Right Leg1
        pyrosim.Send_Joint( name = "Torso_RightLeg1" , parent= "Torso" , child = "RightLeg1" , type = "revolute", position = [0.5,-.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg1", pos=[.5,-.2,0] , size=[1,.2,.2])  


        #Right Leg2
        pyrosim.Send_Joint( name = "Torso_RightLeg2" , parent= "Torso" , child = "RightLeg2" , type = "revolute", position = [0.5,.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg2", pos=[.5,.2,0] , size=[1,.2,.2])  


        
        # -----------All Back Legs (Upper) ----------------


        #BackLeg 1 (Middle)
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5,0] , size=[.2,1,.2])


        # -----------All Front Legs (Upper) --------------------

        #FrontLeg 1 (Middle)
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,.5,0] , size=[.2,1,.2])

# Lower Extremities
        


        # -----------All Left Legs (Lower) ----------------

        #Left Lower Leg
        pyrosim.Send_Joint( name = "LeftLeg1_LeftLowerLeg1" , parent= "LeftLeg1" , child = "LeftLowerLeg1" , type = "revolute", position = [-1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg1", pos=[0, -.2, -0.5] , size=[0.2, 0.2, 1])
        
        #Left Lower Leg
        pyrosim.Send_Joint( name = "LeftLeg2_LeftLowerLeg2" , parent= "LeftLeg2" , child = "LeftLowerLeg2" , type = "revolute", position = [-1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg2", pos=[0, .2, -0.5] , size=[0.2, 0.2, 1])

        # -----------All Right Legs (Lower) ----------------

        #Right Lower Leg
        pyrosim.Send_Joint( name = "RightLeg1_RightLowerLeg1" , parent= "RightLeg1" , child = "RightLowerLeg1" , type = "revolute", position = [1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg1", pos=[0, -.2, -0.5] , size=[0.2, 0.2, 1])
        
        #Right Lower Leg
        pyrosim.Send_Joint( name = "RightLeg2_RightLowerLeg2" , parent= "RightLeg2" , child = "RightLowerLeg2" , type = "revolute", position = [1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg2", pos=[0, .2, -0.5] , size=[0.2, 0.2, 1])

        # -----------All Back Legs (Lower) ----------------

        #Back Lower Leg
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0, -1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

        # -----------All Front Legs (Lower) ----------------

        #Front Lower Leg
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0, 1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

     

        pyrosim.End()
        #exit() # uncommenting this allows you to see effects of code on body.urdf

    def Generate_Brain(self): 

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf") #changed from brain.nndf


# Upper Extremity Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftLeg1") 
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLeg2") 

        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLeg1")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg2") 


        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLeg") 

        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLeg") 


# Lower Extremity Sensor Neurons

        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg1") #Forward
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LeftLowerLeg2") #Forward

        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "RightLowerLeg1") #Forward
        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "RightLowerLeg2") #Forward


        pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "BackLowerLeg") #Middle


        pyrosim.Send_Sensor_Neuron(name = 12 , linkName = "FrontLowerLeg") #Middle

# Upper Extremity Motor Neurons
        
        pyrosim.Send_Motor_Neuron(name = 13 , jointName = "Torso_LeftLeg1") 
        pyrosim.Send_Motor_Neuron(name = 14 , jointName = "Torso_LeftLeg2") 

        pyrosim.Send_Motor_Neuron(name = 15 , jointName = "Torso_RightLeg1")
        pyrosim.Send_Motor_Neuron(name = 16 , jointName = "Torso_RightLeg2") 


        pyrosim.Send_Motor_Neuron(name = 17 , jointName = "Torso_BackLeg") 

        pyrosim.Send_Motor_Neuron(name = 18 , jointName = "Torso_FrontLeg") 



# Lower Extremity Motor Neurons
        pyrosim.Send_Motor_Neuron(name = 19 , jointName = "LeftLeg1_LeftLowerLeg1") #Forward
        pyrosim.Send_Motor_Neuron(name = 20 , jointName = "LeftLeg2_LeftLowerLeg2") #Forward

        pyrosim.Send_Motor_Neuron(name = 21 , jointName = "RightLeg1_RightLowerLeg1") #Forward
        pyrosim.Send_Motor_Neuron(name = 22 , jointName = "RightLeg2_RightLowerLeg2") #Forward


        pyrosim.Send_Motor_Neuron(name = 23 , jointName = "BackLeg_BackLowerLeg") #Middle


        pyrosim.Send_Motor_Neuron(name = 24 , jointName = "FrontLeg_FrontLowerLeg") #Middle



   
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