# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from world import WORLD 
from robot import ROBOT
import pybullet as p
import pybullet_data
import os

class MANYBOTS_SIMULATION:
    def __init__(self):
        #self.solutionID = solutionID
       # self.directOrGUI = directOrGUI # step 86 hillclimber ... # make sure the if else statements are correct
        #os.system('python3 obstacleWorld.py')
        self.directOrGUI = p.connect(p.GUI)


        #self.physicsClient = p.connect(p.DIRECT)   # should this be directorGUI? Maybe delete this line completely?
        
        #p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #p.setGravity(0,0,c.gravityConstant)
        #self.world = WORLD()







        #self.stagger = 5 #right now, only works with 0, 5,10
        #--------------------------------------------------------

        # Writing self.solutionID to a file, which can be read to retrieve the best evolved brain from the sims with only 1 robot


        bestIDFile = open("bestBrains.txt","r")
        bestBrains = bestIDFile.readlines()
        bestIDFile.close()
        bestBrains = list(map(int, bestBrains))


        self.robot0 = ROBOT(bestBrains[0],0)       # THEORETICALLY, WE COULD USE bestBriansFrom1RobotSims[0] here, and we would get the ID for the best robot brain from 1 run.
        self.robot5 = ROBOT(bestBrains[1],5)                    # Now, we should be able to do 1 robot sims, and know what the IDs are of the best robots. 
        self.robot10 = ROBOT(bestBrains[2],10)                  # We should make it such that each time we run ROBOT, we run an individual instance of phc. 
        #self.robot10 = ROBOT(2,15)                  # We should be able to 

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
        #self.robot5.Get_Fitness()
        #self.robot10.Get_Fitness()


    def __del__(self):
        #self.robot.Save_Values()
        p.disconnect()

 
    

