# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from world import WORLD 
from robot import ROBOT
import pybullet as p
import pybullet_data

class SIMULATION:
    def __init__(self,directOrGUI, solutionID, botIndex, swarmIndex, continueOrNone, populationID):
        self.solutionID = solutionID
        self.botIndex = botIndex
        self.swarmIndex = swarmIndex
        self.continueOrNone = continueOrNone
        self.populationID = populationID
    
        self.directOrGUI = directOrGUI # step 86 hillclimber ... # make sure the if else statements are correct
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)
              

        self.positions = [
            (self.solutionID,0,-18),
            (self.solutionID,0,-14),
            (self.solutionID,0,-10),
            (self.solutionID,0,-6),
            (self.solutionID,0,-2),
            (self.solutionID,0,2),
            (self.solutionID,0,6),
            (self.solutionID,0,10),
            (self.solutionID,0,14),
            (self.solutionID,0,18)
        ]

        self.robots = ROBOT(*self.positions[self.botIndex], self.botIndex, self.swarmIndex, self.continueOrNone, self.populationID)


    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.world = WORLD()

        for i in range (c.loopLength):
            p.stepSimulation()
            self.robots.Sense(i)
            self.robots.Think()
            self.robots.Act(i)  


            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)
            #print('For loop variable is',i)   # commented this out for step 74 hillclimber
        #    print(backLegSensorValues)
        #    print(frontLegSensorValues) #

    def Get_Fitness(self):
        self.robots.Get_Fitness()
        p.disconnect()


    # def __del__(self):
    #     p.disconnect()

 
    


     