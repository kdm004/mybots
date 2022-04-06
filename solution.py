from operator import length_hint
import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
#--------------------------------------------
# Cube size (length, width, height) and position (x,y,z)
length = 1
width = 1
height = 1

#we want the world block to be at (-3, 3, .5)
# Torso_FrontLeg joint has no upstream joint because we want Torso to be the parent link again. So we use abs coords for Torso_FrontLeg.
# Worldcube dimensions
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
        #pyrosim.Send_Sphere(name="Box", pos=[7, .5, 1] , size=[.5,.5,.5])

        pyrosim.End()

    def Generate_Body(self): 
        pyrosim.Start_URDF("body.urdf")
        
        #Torso
        pyrosim.Send_Sphere(name="Torso", pos=[0,0,1.5] , size=[1.5, 1.5, 1.5])
    
        #Right Leg
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "fixed", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Sphere(name="RightLeg", pos=[1,0,.5] , size=[1.5])

        pyrosim.Send_Joint( name = "RightLeg_RightLeg2" , parent= "RightLeg" , child = "RightLeg2" , type = "fixed", position = [1.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Sphere(name="RightLeg2", pos=[1,0,-.5] , size=[1.5])
#-----------------
        pyrosim.Send_Joint( name = "RightLeg2_RightLeg3" , parent= "RightLeg2" , child = "RightLeg3" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Sphere(name="RightLeg3", pos=[1,0,-.5] , size=[1.5])
#------------------------
        pyrosim.Send_Joint( name = "RightLeg3_RightLeg4" , parent= "RightLeg3" , child = "RightLeg4" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Sphere(name="RightLeg4", pos=[1,0,-.5] , size=[1.5])

        pyrosim.Send_Joint( name = "RightLeg4_RightLeg5" , parent= "RightLeg4" , child = "RightLeg5" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Sphere(name="RightLeg5", pos=[1,0,-.5] , size=[1.5])

        pyrosim.Send_Joint( name = "RightLeg5_RightLeg6" , parent= "RightLeg5" , child = "RightLeg6" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Sphere(name="RightLeg6", pos=[1,0,-.5] , size=[1.5])

        pyrosim.Send_Joint( name = "RightLeg6_RightLeg7" , parent= "RightLeg6" , child = "RightLeg7" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Sphere(name="RightLeg7", pos=[1,0,-.5] , size=[1.5])

        pyrosim.Send_Joint( name = "RightLeg7_RightLeg8" , parent= "RightLeg7" , child = "RightLeg8" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Sphere(name="RightLeg8", pos=[1,0,-.5] , size=[1.5])


        pyrosim.End()
        #exit() # uncommenting this allows you to see effects of code on body.urdf

    def Generate_Brain(self): 

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf") #changed from brain.nndf



        pyrosim.End()

    def Mutate(self):
        pass
        #randomRow = random.randint(0,c.numSensorNeurons - 1) #(0,2) represents 0th, 1st, and 2nd rows
        #randomColumn = random.randint(0,c.numMotorNeurons - 1) #(0,1) represents 0th and 1st column
        #self.weights[randomRow, randomColumn] = random.random() * 2 - 1

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