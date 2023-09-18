
import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import pickle
#--------------------------------------------





class SOLUTION:
    def __init__(self, nextAvailableID, overallBot, continueOrNone, populationID):
        self.myID = nextAvailableID
        self.overallBot = int(overallBot)
        self.continueOrNone = continueOrNone
        self.populationID = int(populationID) # obtained from parallelHillClimber constructor



        if self.continueOrNone == 'continue': 
            with open('weightsFiles/weights' + str(self.overallBot) + '_' + str(self.populationID) + '.txt', 'r') as pickleFile: # use botNumber
                self.weights = np.loadtxt(pickleFile)
                pickleFile.close()
        
        else:
            self.weights = np.random.rand(c.numSensorNeurons+1,c.numMotorNeurons)   
            self.weights = self.weights * 2 - 1    
            for i in range(8):
                self.weights[9][i] = random.uniform(.5,1.5)

        self.initial_weights = self.weights.copy()

    # def Evaluate(self,directOrGUI):
    #     pass


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] , size=[1,1,1]) 
        pyrosim.End()

    def Generate_Body(self, xi,yi): 

        initial_height = max(self.weights[9]) + 1 # initial height of torso (measured from origin of torso)
 
        pyrosim.Start_URDF("bodyFiles/body"+str(xi)+str(yi)+str(self.myID)+".urdf") # LOOK here, we create the body with position and ID
        
        #Torso
        pyrosim.Send_Cube(name="Torso", pos=[0+xi,0+yi,initial_height] , size=[1,1,1])
            
    # Upper Extremities
        #Back Leg
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0+xi,-0.5+yi,initial_height], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-(self.weights[9][0]/2),0] , size=[0.2,self.weights[9][0],0.2])

        #Front Leg
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0+xi,0.5+yi,initial_height], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,(self.weights[9][1]/2),0] , size=[0.2,self.weights[9][1],0.2])

        #Left Leg
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5+xi,0+yi,initial_height], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-(self.weights[9][2]/2),0,0] , size=[self.weights[9][2],0.2,0.2])        

        #Right Leg
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5+xi,0+yi,initial_height], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[(self.weights[9][3]/2),0,0] , size=[self.weights[9][3],0.2,0.2])   

    # Lower Extremities
        #Back Lower Leg
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg", child = "BackLowerLeg", type = "revolute", position = [0, -self.weights[9][0], 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -(self.weights[9][4]/2)] , size=[0.2, 0.2, self.weights[9][4]])
            
        #Front Lower Leg
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg", child = "FrontLowerLeg", type = "revolute", position = [0, self.weights[9][1], 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -(self.weights[9][5]/2)] , size=[0.2, 0.2, self.weights[9][5]])

        #Left Lower Leg
        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg", child = "LeftLowerLeg", type = "revolute", position = [-self.weights[9][2], 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -(self.weights[9][6]/2)] , size=[0.2, 0.2, self.weights[9][6]])

        #Right Lower Leg
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg", parent= "RightLeg", child = "RightLowerLeg", type = "revolute", position = [self.weights[9][3], 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -(self.weights[9][7]/2)] , size=[0.2, 0.2, self.weights[9][7]])

        pyrosim.End()
        #exit() # uncommenting this allows you to see effects of code on body.urdf

    def Generate_Brain(self):  #ADDED TO ROBOT_BRAIN
        pyrosim.Start_NeuralNetwork("brainFiles/brain" + str(self.myID) + ".nndf") #changed from brain.nndf

# Upper Extremity Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")

# Lower Extremity Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")

# Upper Extremity Motor Neurons
        pyrosim.Send_Motor_Neuron( name = 9, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 10, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 12, jointName = "Torso_RightLeg")

# Lower Extremity Motor Neurons
        pyrosim.Send_Motor_Neuron( name = 13, jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 14, jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15, jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 16, jointName = "RightLeg_RightLowerLeg")
   
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] ) #step 7 randomsearch

        pyrosim.End()

    def Mutate(self): #ADDED TO ROBOT_BRAIN
        headsOrTails = random.choice([0,1])
        if headsOrTails == 1:

            # randomly select an entry in the synaptic weights, and change it
            randomRow = random.randint(0,c.numSensorNeurons - 1) #(0,2) represents 0th, 1st, and 2nd rows
            randomColumn = random.randint(0,c.numMotorNeurons - 1) #(0,1) represents 0th and 1st column
            self.weights[randomRow, randomColumn] = random.random() * 2 - 1


        else:

            # randomly select a leg part and change it
            randomLegPart = random.randint(0,7)
            self.weights[9][randomLegPart] = random.uniform(0.5,1.5)


    def Save_Weights(self):
        if self.continueOrNone == 'continue': # if 'continue', we've already loaded from this file. Edit the constructor to include this.
            with open('weightsFiles/weights' + str(self.overallBot) + '_' + str(self.populationID) + '.txt', 'w') as pickleFile: #let's use botNumber
                np.savetxt(pickleFile,self.weights)
                pickleFile.close()
            

        else:
            with open('weightsFiles/weights' + str(self.overallBot) + '_' + str(self.populationID) + '.txt', 'w') as pickleFile: # let's use botNumber, not botIndex swarmID*10+botIndex
                np.savetxt(pickleFile,self.weights)
                pickleFile.close()

        tempfile = open('WeightsTemp.txt','a')
        tempfile.write(str(self.weights))
        tempfile.write('---------------'+str(self.overallBot) + '_' + str(self.populationID)+'----------------')
        tempfile.write('\n')
        tempfile.write('\n')
        tempfile.close  

        # yep, looks like the weights and leg lengths are being changed correctly. We inspected testingBoth.txt, and we can see the 5 parent matrices evolving with every iteration. 
        # so, we will write out the matrices to their own files using this method, and load them using the constructor.

    # def Mutate_Body(self): #ADDED TO ROBOT_BRAIN
    #     pass


    
    def Set_ID(self): #ADDED TO ROBOT_BRAIN
        self.myID

    def Start_Simulation(self, directOrGUI, overallBot):

        botIndex = self.overallBot % 10


        self.Create_World()
        self.Generate_Brain() #ADDED TO ROBOT_BRAIN

        positions = [
            (0,-18),
            (0,-14),
            (0,-10),
            (0,-6),
            (0,-2),
            (0,2),
            (0,6),
            (0,10),
            (0,14),
            (0,18)
        ]

        self.Generate_Body(*positions[botIndex]) #... I just put this in 11-22-2022... will putting this here allow me to evolve the body? 
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID)+ ' ' + str(botIndex) + ' ' + str(self.continueOrNone) + ' ' + str(self.populationID) +" &") # changed from "DIRECT" to directOrGUI... added " &"

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+ str(self.myID) + ".txt"):
            time.sleep(0.01)

        fitnessFile = open("fitness"+ str(self.myID) + ".txt","r")
        time.sleep(0.1)
        lines = fitnessFile.read()
        time.sleep(0.1)
        self.fitness = float(lines)

        fitnessFile.close()
        os.system("rm fitness"+ str(self.myID) + ".txt")
        while os.path.exists("fitness"+str(self.myID)+".txt"):
            os.system("rm fitness"+ str(self.myID) + ".txt")
