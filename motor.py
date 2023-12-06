import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.values = np.zeros(c.loopLength) #moved to SENSOR's Prepare_To_Sense()
        self.jointName = jointName
        
    
    def Set_Value(self, robot, desiredAngle, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.legMaxForce)
        self.values[t] = desiredAngle
        
    def Save_Values(self):
        # numpy.save('data/sensorValues.npy', self.values)
        np.save(f'data/obstacles/{self.jointName}motorValues.npy', self.values)



    
