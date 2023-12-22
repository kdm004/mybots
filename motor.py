import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.values = np.zeros(c.loopLength)
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
        np.save(f'data//{self.jointName}motorValues.npy', self.values)