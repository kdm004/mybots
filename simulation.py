import time
import constants as c
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data

class SIMULATION:
    def __init__(self,directOrGUI, solutionID, swarmNumber, botNumber, overallBot):
        self.solutionID = solutionID
        self.directOrGUI = directOrGUI 
        self.swarmNumber = swarmNumber
        self.botNumber = botNumber
        self.overallBot = overallBot
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.robot = ROBOT(self.solutionID, self.swarmNumber, self.botNumber, self.overallBot)
        self.world = WORLD()


        
    def Run(self):
        for i in range (c.loopLength):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)   

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)
        self.robot.Save_Values()

    def Get_Fitness(self):
        self.robot.Get_Evolution_Fitness()

    def __del__(self):
        p.disconnect()

 
    


     
