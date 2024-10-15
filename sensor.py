import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self,bodyID, linkName, linkNamesToIndices):
        self.values = np.zeros(c.loopLength) 
        self.bodyID = bodyID
        self.linkName = linkName
        self.linkNamesToIndices = linkNamesToIndices

    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.bodyID, self.linkName, self.linkNamesToIndices) 
        if t == 10:
            print(self.values[t])

        # if self.linkName == 'Box':  
        #     print(f'{self.linkName} = {pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)}')

        if self.linkName == 'RightLowerLeg0':  
            print(f'{self.linkName} = {pyrosim.Get_Touch_Sensor_Value_For_Link(self.bodyID, self.linkName, self.linkNamesToIndices)}')
            # print(f'Look here: {self.linkNamesToIndices}')
        if self.linkName == 'RightLowerLeg1':  
            print(f'{self.linkName} = {pyrosim.Get_Touch_Sensor_Value_For_Link(self.bodyID, self.linkName, self.linkNamesToIndices)}')
            # print(f'Look here: {self.linkNamesToIndices}')

        return self.values

    def Save_Values(self, robot):
        np.save(f"data/" + str(self.linkName)+"Sensor", self.values)