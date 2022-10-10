# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from world import WORLD 
from robot import ROBOT
import pybullet as p
import pybullet_data

class SIMULATION:
    def __init__(self,directOrGUI, solutionID):
        self.solutionID = solutionID
        self.directOrGUI = directOrGUI # step 86 hillclimber ... # make sure the if else statements are correct
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)


        #self.physicsClient = p.connect(p.DIRECT)   # should this be directorGUI? Maybe delete this line completely?
        
        #p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #p.setGravity(0,0,c.gravityConstant)
        #self.world = WORLD()







        #self.stagger = 5 #right now, only works with 0, 5,10
        #--------------------------------------------------------


        self.robot0 = ROBOT(self.solutionID,0)      
        self.robot5 = ROBOT(0,5)
        self.robot10 = ROBOT(1,10)          
        self.robot10 = ROBOT(2,15) 

        #--------------------------------------------------------

        




    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.world = WORLD()

        for i in range (c.loopLength):
            p.stepSimulation()
            self.robot0.Sense(i)
            self.robot0.Think()
            self.robot0.Act(i)  

            self.robot5.Sense(i)
            self.robot5.Think()
            self.robot5.Act(i)  

            self.robot10.Sense(i)
            self.robot10.Think()
            self.robot10.Act(i)  

            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)
            #print('For loop variable is',i)   # commented this out for step 74 hillclimber
        #    print(backLegSensorValues)
        #    print(frontLegSensorValues) #

    def Get_Fitness(self):
        self.robot0.Get_Fitness()
        self.robot5.Get_Fitness()
        self.robot10.Get_Fitness()


    def __del__(self):
        #self.robot.Save_Values()
        p.disconnect()

 
    


     
