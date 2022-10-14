# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from world import WORLD 
from robot import ROBOT
import pybullet as p
import pybullet_data

class MANYBOTS_SIMULATION:
    def __init__(self,directOrGUI):
        self.directOrGUI = directOrGUI # step 86 hillclimber ... # make sure the if else statements are correct
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)




    def Run(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravityConstant)
        self.world = WORLD()



        bestIDFile = open("bestBrains.txt","r")
        bestBrains = int(bestIDFile.readlines())
        bestIDFile.close()

    
        self.robot0 = ROBOT(bestBrains[0],0)       # THEORETICALLY, WE COULD USE bestBriansFrom1RobotSims[0] here, and we would get the ID for the best robot brain from 1 run.
        self.robot5 = ROBOT(bestBrains[1],5)                    # Now, we should be able to do 1 robot sims, and know what the IDs are of the best robots. 
        self.robot10 = ROBOT(bestBrains[2],10)                  # We should make it such that each time we run ROBOT, we run an individual instance of phc. 
        #self.robot10 = ROBOT(2,15)                  # We should be able to 


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



    def Get_Fitness(self):
        self.robot0.Get_Fitness()
        #self.robot5.Get_Fitness()
        #self.robot10.Get_Fitness()


    def __del__(self):
        #self.robot.Save_Values()
        p.disconnect()