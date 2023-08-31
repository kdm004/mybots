import constants as c
import random as random
import numpy as numpy
import pyrosim.pyrosim as pyrosim 
import pybullet_data
import pybullet as p
import time
from MBsimulation import MANYBOTS_SIMULATION as MB_SIMULATION
import sys
import os




pyrosim.Start_SDF("obstacleWorld.sdf")
for x in range(10, -22-2,-2): # -4
       for y in range(-28, 28+2, 2): #-4
           pyrosim.Send_Cube(name="Box", pos=[x,y,.5] , size=[1/3,1/3,1/3]) 
pyrosim.End()
#---------------------------------------------------------------------------------------------------------------------


# MBSIM = MB_SIMULATION(1)
# while not os.path.exists("obstacleWorld.sdf"):
#         time.sleep(0.01)
# MBSIM.Run()
# #MBSIM.Shift_Lines() We comment this out for case1 because if the top line is deleted by Shift_Lines(), that would change the index of the overall champion of the 35 controllers
# MBSIM.Get_Fitness()





# MBSIM2 = MB_SIMULATION(2)
# while not os.path.exists("obstacleWorld.sdf"):
#         time.sleep(0.01)
# MBSIM2.Run()
# #MBSIM.Shift_Lines() We comment this out for case1 because if the top line is deleted by Shift_Lines(), that would change the index of the overall champion of the 35 controllers
# MBSIM2.Get_Fitness()

for outerLoopIndex in range(70): # 34 because we want the final line number to be 350, which will be swarmIndex + 10
        for innerLoopIndex in range(10):
                MBSIM = MB_SIMULATION(innerLoopIndex, outerLoopIndex)
                MBSIM.Run()
                MBSIM.Get_Fitness()
