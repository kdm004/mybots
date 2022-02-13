import pyrosim.pyrosim as pyrosim
import pybullet as p



class ROBOT:
    def __init__(self):
#        self.sensors = {}    #I'm moving this to def Prepare_To_Sense(self):
        self.motors = {}

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)






