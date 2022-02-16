import constants as c
import numpy as numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = numpy.zeros(c.loopLength)
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset

        for i in range(c.loopLength):
            self.motorValues = self.amplitude * numpy.sin(self.frequency * c.targetAngles + self.offset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = 20)

    def Save_Values(self):
        numpy.save('data/motorValues.npy', self.motorValues)
    
