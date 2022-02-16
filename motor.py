import constants as c
import numpy as numpy
import pyrosim.pyrosim as pyrosim


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        pass
        #BackLeg_motorCommand = c.BackLeg_amplitude * numpy.sin(c.BackLeg_frequency * targetAngles + c.BackLeg_phaseOffset)
        #FrontLeg_motorCommand = c.FrontLeg_amplitude * numpy.sin(c.FrontLeg_frequency * targetAngles + c.FrontLeg_phaseOffset)        
