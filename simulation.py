# This is the new simulation file that was created in the refactoring branch
import time
import constants as c
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        
    def Run(self):
        for i in range (c.loopLength):
            p.stepSimulation()

        #    # Sensor values
        #    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        #    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


        #    pyrosim.Set_Motor_For_Joint(
        #    bodyIndex = robotId,
        #    jointName = "Torso_BackLeg",
        #    controlMode = p.POSITION_CONTROL,
        #    targetPosition = BackLeg_motorCommand[i],
        #    maxForce = 20)

        #    pyrosim.Set_Motor_For_Joint(
        #    bodyIndex = robotId,
        #    jointName = "Torso_FrontLeg",
        #    controlMode = p.POSITION_CONTROL,
        #    targetPosition = FrontLeg_motorCommand[i],
        #    maxForce = 20)


            time.sleep(1/(240))
            print('For loop variable is',i)
        #    print(backLegSensorValues)
        #    print(frontLegSensorValues)

    def __del__(self):
        p.disconnect()




     
