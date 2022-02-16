import constants as c
import numpy as numpy
import pyrosim.pyrosim as pyrosim


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        self.BackLeg_motorCommand = self.amplitude * numpy.sin(self.frequency * c.targetAngles + self.offset)
        self.FrontLeg_motorCommand = self.amplitude * numpy.sin(self.frequency * c.targetAngles + self.offset) 

    def Set_Value(self, robot, t):
        pass
    
    