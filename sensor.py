import constants as c
import numpy as numpy


class SENSOR:
    def __init__(self,linkName):
        self.values = numpy.zeros(c.loopLength)   
        self.linkName = linkName

    def Get_Value():
        backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")        
     





