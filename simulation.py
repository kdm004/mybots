# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data

class SIMULATION:
    def __init__(self,mode):
        self.directOrGUI = mode # step 86 hillclimber
        if mode == 'DIRECT':
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)


        #self.physicsClient = p.connect(p.DIRECT)   # should this be directorGUI? Maybe delete this line completely?
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.world = WORLD()
        self.robot = ROBOT()
        
    def Run(self):
        for i in range (c.loopLength):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)   


            time.sleep(c.sleepRate)
            #print('For loop variable is',i)   # commented this out for step 74 hillclimber
        #    print(backLegSensorValues)
        #    print(frontLegSensorValues) #

    def __del__(self):
        #self.robot.Save_Values()
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()
    


     
