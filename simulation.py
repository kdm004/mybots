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
        #self.robot5 = ROBOT(5,5)                    
        #self.robot10 = ROBOT(8,10)                  


    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.world = WORLD()

        for i in range (c.loopLength):
            p.stepSimulation()
            self.robot0.Sense(i)
            self.robot0.Think()
            self.robot0.Act(i)  

            #self.robot5.Sense(i)
            #self.robot5.Think()
            #self.robot5.Act(i)  

            #self.robot10.Sense(i)
            #self.robot10.Think()
            #self.robot10.Act(i)  

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)
            #print('For loop variable is',i)   # commented this out for step 74 hillclimber
        #    print(backLegSensorValues)
        #    print(frontLegSensorValues) #

    def Get_Fitness(self):
        self.robot0.Get_Fitness()
        #self.robot5.Get_Fitness()
        #self.robot10.Get_Fitness()


    def __del__(self):
        #self.robot.Save_Values()
        p.disconnect()

 
    


     
