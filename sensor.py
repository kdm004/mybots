import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self,linkName, linkNamesToIndices):
        self.values = np.zeros(c.loopLength) 
        self.linkName = linkName
        self.linkNamesToIndices = linkNamesToIndices

    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName, self.linkNamesToIndices) 

        # if self.linkName == 'Box':  
        #     print(f'{self.linkName} = {pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)}')
        # if self.linkName == 'RightLowerLeg':  
        #     print(f'{robot}_{self.linkName} = {pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)}')

        return self.values

    def Save_Values(self, robot):
        np.save(f"data/"+str(robot) + str(self.linkName)+"Sensor", self.values)