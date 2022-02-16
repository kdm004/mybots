import constants as c
import numpy as numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self,linkName):
        self.values = numpy.zeros(c.loopLength) # maybe this should go in Get_Value(self,t) ???   
        self.linkName = linkName

    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName) #took out quotes from "self.linkName"       
        #return self.values     
        print(self.values[t])




