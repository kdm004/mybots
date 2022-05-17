# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import numpy

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.world = WORLD()
        self.robot = ROBOT()
        self.xRecord = numpy.zeros((1, c.loopLength)) 


        
    def Run(self):
        for i in range (c.loopLength):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            self.robot.Get_Fitness()


            time.sleep(c.sleepRate)
            #print('For loop variable is',i)
        #    print(backLegSensorValues)
        #    print(frontLegSensorValues) #

    #def Get_Fitness(self):
    #    self.robot.Get_Fitness()

    def __del__(self):
        #self.robot.Save_Values()
        p.disconnect()




     
