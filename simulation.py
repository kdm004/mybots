# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from world import WORLD 
from robot import ROBOT
import pybullet as p
import pybullet_data

class SIMULATION:
    def __init__(self,directOrGUI, solutionID, overallBot, continueOrNone, populationID):
        self.solutionID = solutionID
        self.directOrGUI = directOrGUI # step 86 hillclimber ... # make sure the if else statements are correct
        self.overallBot = overallBot
        self.continueOrNone = continueOrNone
        self.populationID = populationID
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)
            
        self.robot0 = ROBOT(self.solutionID,0,0, self.overallBot, self.continueOrNone, self.populationID)       # ROBOT(self.solutionID, xi, yi) where xi = 0, yi = 0 # we evolve the robot in an empty environment, so position doesn't matter.

    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.world = WORLD()

        for i in range (c.loopLength):
            p.stepSimulation()
            self.robot0.Sense(i)
            self.robot0.Think()
            self.robot0.Act(i)  

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)
            #print('For loop variable is',i)   # commented this out for step 74 hillclimber
        #    print(backLegSensorValues)
        #    print(frontLegSensorValues) #

    def Get_Fitness(self):
        self.robot0.Get_Fitness()

    def __del__(self):
        #self.robot.Save_Values()
        p.disconnect()

 
    


     