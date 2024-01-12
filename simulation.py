import time
import constants as c
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data

class SIMULATION:
    def __init__(self,directOrGUI, solutionID, swarmNumber, botNumber):
        self.solutionID = solutionID
        self.directOrGUI = directOrGUI 
        self.swarmNumber = swarmNumber
        self.botNumber = botNumber
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)

        p.setPhysicsEngineParameter(fixedTimeStep=c.timeStepSize)      # 1/1400   #default value = 1/240
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        currentParams = p.getPhysicsEngineParameters()
        print(currentParams)
        self.robot = ROBOT(self.solutionID, self.swarmNumber, self.botNumber)
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

 
    


     
