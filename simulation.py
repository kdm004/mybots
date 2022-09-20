# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data

class SIMULATION:
    def __init__(self,directOrGUI, solutionID, stagger):
        self.solutionID = solutionID
        self.directOrGUI = directOrGUI # step 86 hillclimber ... # make sure the if else statements are correct
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)


        #self.physicsClient = p.connect(p.DIRECT)   # should this be directorGUI? Maybe delete this line completely?
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.world = WORLD()







        self.stagger = 5 #right now, only works with 5
        #--------------------------------------------------------
        self.robot = ROBOT(self.solutionID,self.stagger)      
        #--------------------------------------------------------





    def Run(self):
        for i in range (c.loopLength):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)   

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)
            #print('For loop variable is',i)   # commented this out for step 74 hillclimber
        #    print(backLegSensorValues)
        #    print(frontLegSensorValues) #

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        #self.robot.Save_Values()
        p.disconnect()

 
    


     
