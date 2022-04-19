import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy as numpy

class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf") #changed from robotId to robot
        pyrosim.Prepare_To_Simulate(self.robot) #changed from robotId to robot
        self.sensors = {}
        self.motors = {}
        self.values = {}  
        self.Prepare_To_Sense()
        self.Prepare_To_Act()


    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,t):
        for key in self.sensors:
            #print(self.sensors)
            #print('key is ', key)
            self.values[t] =self.sensors[key].Get_Value(t)
            if t == c.loopLength:
                print(self.values[key])

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self,t):
        for key in self.motors:
            self.motors[key].Set_Value(self.robot,t)
            #print(self.motors[key]) ... this prints out a bunch of stuff
                # applyExternalForce

        #Sphere1
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[10,1,10] , posObj=[0,0,1], flags=p.LINK_FRAME) # Rear thruster
        #sphere2
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[0,12,13] , posObj=[1 , 0 , 1], flags=p.LINK_FRAME)
        #sphere3
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[-10,15,8] , posObj=[1 , 0 , 2], flags=p.LINK_FRAME)
        #sphere4
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[4,12,-10] , posObj=[1 , 0 , 3], flags=p.LINK_FRAME)
        #Sphere5
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[4,12,-10] , posObj=[1 , 1 , 3], flags=p.LINK_FRAME)
        #Sphere6
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[4,-11,-7] , posObj=[2 , 1 , 4], flags=p.LINK_FRAME)
        #Sphere7
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[2,-8,-10] , posObj=[2 , 1 , 5], flags=p.LINK_FRAME)
        #Sphere8
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[10,8,-6] , posObj=[2 , 1 , 5], flags=p.LINK_FRAME)
        #Sphere9
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[10,8,-6] , posObj=[3 , 1 , 5], flags=p.LINK_FRAME)

        #Sphere10
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[10,8,-6] , posObj=[3 , 1 , 6], flags=p.LINK_FRAME)
        #Sphere11
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[10,-12,-10] , posObj=[3 , 2 , 6], flags=p.LINK_FRAME)
       
       
        #Sphere12
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[2,8,-6] , posObj=[4 , 2 , 6], flags=p.LINK_FRAME)
        #Sphere13
        p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[2,8,6] , posObj=[4 , 3 , 6], flags=p.LINK_FRAME)
        #Sphere14
        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[10,8,-6] , posObj=[4 , 4 , 6], flags=p.LINK_FRAME)
       #------
       #Sphere15
        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[5,-15,10] , posObj=[4 , 5 , 6], flags=p.LINK_FRAME)

#---------------------------------------------
        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[4,-8,-6] , posObj=[4 , 5 , 7], flags=p.LINK_FRAME)

        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[-2,4,10] , posObj=[4 , 5 , 8], flags=p.LINK_FRAME)

        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[10,-10,14] , posObj=[4 , 6 , 8], flags=p.LINK_FRAME)

        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[11,-8,-6] , posObj=[5 , 6 , 8], flags=p.LINK_FRAME)

        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[1,-10,2] , posObj=[5 , 7 , 8], flags=p.LINK_FRAME)

        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[13,1,4] , posObj=[5 , 8 , 8], flags=p.LINK_FRAME)

        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[10,8,-5] , posObj=[5 , 8 , 9], flags=p.LINK_FRAME)
        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[1,1,-6] , posObj=[6 , 8 , 9], flags=p.LINK_FRAME)

       
       
       
        #Sphere15
        #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[10,8,-6] , posObj=[4 , 4 , 7], flags=p.LINK_FRAME)


        #-----
   

        #while c.loopLength in range(1, 1000):
        
        #while 10 == c.loopLength:
            #p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[0,700,0] , posObj=[1.5/2,0,1.2], flags=p.LINK_FRAME)
           
           # p.applyExternalForce(objectUniqueId=self.robot, linkIndex=-1, forceObj=[1000,0,0] , posObj=[0,0,0], flags=p.LINK_FRAME)

    def Save_Values(self):
        for key in self.motors:
            self.motors[key].Save_Values()
        for key in self.sensors:
            self.sensors[key].Save_Values()