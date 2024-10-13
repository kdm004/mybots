import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import math
#-----------------------------------------------------------------------------------------


class SOLUTION:
    def __init__(self, nextAvailableID, swarmNumber, botNumber):
        self.myID = nextAvailableID
        self.swarmNumber = int(swarmNumber)
        self.botNumber = int(botNumber)

        # Create array of weights and leg lengths
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        if c.swarmType == 'case1' or c.swarmType == 'case2':
        # First 4 legLengths are for upper legs. Second 4 legLengths are for lower legs
            self.legLengths = np.ones(c.numMotorNeurons)
        elif c.swarmType == 'case3':
            self.legLengths = np.random.uniform(*c.legLengthRange, c.numMotorNeurons)
        self.weights = np.vstack([self.weights, self.legLengths])


        # Load weights from disk if continuing evolution 
        if c.continueEvolution == True: 
            with open(f'weights/weights_{self.swarmNumber}_{self.botNumber}_{self.myID}.txt', 'r') as f:
                self.weights = np.loadtxt(f)

        if c.numberOfGenerations == 0:
            if c.continueEvolution == True:
                ValueError("numberOfGenerations must be an integer greater than 0 when continuing evolution.")
            else:
                self.Save_Weights()                                                                   # If gens = 0, then we never used to save weights. This saves the weights in that case.

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="Box", pos=[-10,5,.5] , size=[1,1,1])  # Empty world for evolution
        pyrosim.End()

    def Generate_Body(self, xi, yi, zi):
        if c.swarmType == 'case1' or c.swarmType == 'case2':
            pyrosim.Start_URDF(f"bodies/body_{self.botNumber}.urdf")                                                   # All bodies are identical
        elif c.swarmType == 'case3':
            pyrosim.Start_URDF(f"bodies/body_{self.swarmNumber}_{self.botNumber}_{self.myID}.urdf")   # Differentiate body files for case3. Differentiate files by their evolution traits ie swarmNumber, botNumber, myID

        # Root link
        pyrosim.Send_Cube(name=f"Torso{self.botNumber}", pos=[xi, yi, zi], size=[1,1,1])
        print(f"Torso{self.botNumber}")

        # Upper joints (from root link)
        pyrosim.Send_Joint(name=f"Torso_FrontLeg{self.botNumber}", parent=f"Torso{self.botNumber}", child=f"FrontLeg{self.botNumber}", type="revolute", position=[xi, yi+0.5,zi], jointAxis="1 0 1")
        pyrosim.Send_Joint(name=f"Torso_BackLeg{self.botNumber}", parent=f"Torso{self.botNumber}", child=f"BackLeg{self.botNumber}", type="revolute", position=[xi, yi-0.5,zi], jointAxis="1 0 1")
        pyrosim.Send_Joint(name=f"Torso_LeftLeg{self.botNumber}", parent=f"Torso{self.botNumber}", child=f"LeftLeg{self.botNumber}", type="revolute", position=[xi-0.5, yi, zi], jointAxis="0 1 1")
        pyrosim.Send_Joint(name=f"Torso_RightLeg{self.botNumber}", parent=f"Torso{self.botNumber}", child=f"RightLeg{self.botNumber}", type="revolute", position=[xi+0.5, yi, zi], jointAxis="0 1 1")

        # LowerLeg joints
        pyrosim.Send_Joint(name=f"FrontLeg{self.botNumber}_FrontLowerLeg{self.botNumber}", parent=f"FrontLeg{self.botNumber}", child=f"FrontLowerLeg{self.botNumber}", type="revolute", position=[0,self.weights[-1][0],0], jointAxis="1 0 1")
        pyrosim.Send_Joint(name=f"BackLeg{self.botNumber}_BackLowerLeg{self.botNumber}", parent=f"BackLeg{self.botNumber}", child=f"BackLowerLeg{self.botNumber}", type="revolute", position=[0,-self.weights[-1][1],0], jointAxis="1 0 1")
        pyrosim.Send_Joint(name=f"LeftLeg{self.botNumber}_LeftLowerLeg{self.botNumber}", parent=f"LeftLeg{self.botNumber}", child=f"LeftLowerLeg{self.botNumber}", type="revolute", position=[-self.weights[-1][2],0,0], jointAxis="0 1 1")
        pyrosim.Send_Joint(name=f"RightLeg{self.botNumber}_RightLowerLeg{self.botNumber}", parent=f"RightLeg{self.botNumber}", child=f"RightLowerLeg{self.botNumber}", type="revolute", position=[self.weights[-1][3],0,0], jointAxis="0 1 1")

        # Upper legs
        pyrosim.Send_Cube(name=f"FrontLeg{self.botNumber}", pos=[0, 0.5*self.weights[-1][0], 0], size=[0.2, self.weights[-1][0], 0.2])
        pyrosim.Send_Cube(name=f"BackLeg{self.botNumber}", pos=[0, -0.5*self.weights[-1][1], 0], size=[0.2, self.weights[-1][1], 0.2])
        pyrosim.Send_Cube(name=f"LeftLeg{self.botNumber}", pos=[-0.5*self.weights[-1][2],0, 0], size=[self.weights[-1][2], 0.2, 0.2])
        pyrosim.Send_Cube(name=f"RightLeg{self.botNumber}", pos=[0.5*self.weights[-1][3], 0, 0], size=[self.weights[-1][3], 0.2, 0.2])

        # LowerLeg legs
        pyrosim.Send_Cube(name=f"FrontLowerLeg{self.botNumber}", pos=[0, 0, -0.5*self.weights[-1][4]], size=[0.2, 0.2, self.weights[-1][4]])
        pyrosim.Send_Cube(name=f"BackLowerLeg{self.botNumber}", pos=[0, 0, -0.5*self.weights[-1][5]], size=[0.2, 0.2, self.weights[-1][5]])
        pyrosim.Send_Cube(name=f"LeftLowerLeg{self.botNumber}", pos=[0, 0, -0.5*self.weights[-1][6]], size=[0.2, 0.2, self.weights[-1][6]])
        pyrosim.Send_Cube(name=f"RightLowerLeg{self.botNumber}", pos=[0, 0, -0.5*self.weights[-1][7]], size=[0.2, 0.2, self.weights[-1][7]])

        pyrosim.End()
        #exit() # uncommenting this allows you to see effects of code on body.urdf

    def Generate_Brain(self): 
        pyrosim.Start_NeuralNetwork(f"brains/brain_{self.swarmNumber}_{self.botNumber}_{self.myID}.nndf") 

        # Note: Do not add neuron for Torso. Root links have the same index as SDF links. Pyrosim processes sensory based on link index, so links of same index will have their touchValues will be conflated. 

        # Sensor neurons (only lower legs)
        pyrosim.Send_Sensor_Neuron(name=0, linkName=f"FrontLowerLeg{self.botNumber}")
        pyrosim.Send_Sensor_Neuron(name=1, linkName=f"BackLowerLeg{self.botNumber}")
        pyrosim.Send_Sensor_Neuron(name=2, linkName=f"LeftLowerLeg{self.botNumber}")
        pyrosim.Send_Sensor_Neuron(name=3, linkName=f"RightLowerLeg{self.botNumber}")

        # Upper motor neurons
        pyrosim.Send_Motor_Neuron(name=4, jointName=f"Torso_FrontLeg{self.botNumber}")
        pyrosim.Send_Motor_Neuron(name=5, jointName=f"Torso_BackLeg{self.botNumber}")
        pyrosim.Send_Motor_Neuron(name=6, jointName=f"Torso_LeftLeg{self.botNumber}")
        pyrosim.Send_Motor_Neuron(name=7, jointName=f"Torso_RightLeg{self.botNumber}")

        # Lower motor neurons
        pyrosim.Send_Motor_Neuron(name=8, jointName=f"FrontLeg{self.botNumber}_FrontLowerLeg{self.botNumber}")
        pyrosim.Send_Motor_Neuron(name=9, jointName=f"BackLeg{self.botNumber}_BackLowerLeg{self.botNumber}")
        pyrosim.Send_Motor_Neuron(name=10, jointName=f"LeftLeg{self.botNumber}_LeftLowerLeg{self.botNumber}")
        pyrosim.Send_Motor_Neuron(name=11, jointName=f"RightLeg{self.botNumber}_RightLowerLeg{self.botNumber}")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self):
        if c.swarmType == 'case1' or c.swarmType == 'case2':
            randomWeightsRow = random.randint(0,c.numSensorNeurons - 1) 
            randomWeightsColumn = random.randint(0,c.numMotorNeurons - 1)
            self.weights[randomWeightsRow, randomWeightsColumn] = random.random() * 2 - 1

        elif c.swarmType == 'case3':
            headsOrTails = random.choice([1,0])
            if headsOrTails == 1:
                randomWeightsRow = random.randint(0,c.numSensorNeurons - 1) 
                randomWeightsColumn = random.randint(0,c.numMotorNeurons - 1)
                self.weights[randomWeightsRow, randomWeightsColumn] = random.random() * 2 - 1      
            elif headsOrTails == 0:
                legToMutate = random.randint(0,7)
                self.weights[-1][legToMutate] = random.uniform(*c.legLengthRange)


    def Save_Weights(self):
        file_path = f'weights/weights_{self.swarmNumber}_{self.botNumber}_{self.myID}.txt'
        with open(file_path, 'w') as f: 
            np.savetxt(f,self.weights)
                      

    def Start_Simulation(self, directOrGUI):
        self.Generate_Body(*c.botPosition[self.botNumber], np.max(self.weights[-1, -4:]))   # (0,0, z-spawnPoint based on longest lower leg section) ... added self.overallBot % c.botsPerSwarm as index of which bot position for current bot
        self.Generate_Brain()
        self.Create_World()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(self.swarmNumber) + " " + str(self.botNumber) + " &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness_{self.swarmNumber}_{self.botNumber}_{self.myID}.txt"):
            time.sleep(0.01)
        f = open(f"fitness_{self.swarmNumber}_{self.botNumber}_{self.myID}.txt","r")
        time.sleep(0.1)
        lines = f.read()
        time.sleep(0.1)
        self.fitness = float(lines)
        f.close()

        os.system(f"rm fitness_{self.swarmNumber}_{self.botNumber}_{self.myID}.txt")
        while os.path.exists(f"fitness_{self.swarmNumber}_{self.botNumber}_{self.myID}.txt"):       
            os.system(f"rm fitness_{self.swarmNumber}_{self.botNumber}_{self.myID}.txt")
