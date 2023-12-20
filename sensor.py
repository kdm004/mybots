import constants as c
import numpy as numpy
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self,linkName):
        self.values = numpy.zeros(c.loopLength) 
        self.linkName = linkName

    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName) 

        # if self.linkName == 'Box':  
        #     print(f'{self.linkName} = {pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)}')
        # if self.linkName == 'Torso':  
        #     print(f'{self.linkName} = {pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)}')

        return self.values

    def Save_Value(self):
        numpy.save('data/sensorValues.npy', self.values)