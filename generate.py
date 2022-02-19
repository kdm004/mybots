import pyrosim.pyrosim as pyrosim
#-------------------------------------------------------------
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pass
    #pyrosim.Start_URDF("body.urdf")
    #pyrosim.Send_Cube(name="Torso", pos=[x0,y0,z0] , size=[length,width,height])
    #pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    #pyrosim.Send_Cube(name="BackLeg", pos=[x1,y1,z1] , size=[length,width,height])

    #pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    #pyrosim.Send_Cube(name="FrontLeg", pos=[x2,y2,z2] , size=[length,width,height])

    #pyrosim.End()

def Generate_Body(): 
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x0,y0,z0] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[x1,y1,z1] , size=[length,width,height])

    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[x2,y2,z2] , size=[length,width,height])

    pyrosim.End()

def Generate_Brain(): 
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    pyrosim.End()
#-------------------------------------------------------------
#Cube size (length, width, height) and position (x,y,z)
length = 1
width = 1
height = 1

#we want the world block to be at (-3, 3, .5)
# Torso_FrontLeg joint has no upstream joint because we want Torso to be the parent link again. So we use abs coords for Torso_FrontLeg.
x = -3
y = 3
z = .5

x0 = 1.5
y0 = 0
z0 = 1.5

x1 = -.5
y1 = 0
z1 = -.5

x2 = .5
y2 = 0
z2 = -.5
#-------------------------------------------------------------

Create_World()
Create_Robot() # this one is commented out. Only has pass in it.

Generate_Body() 
Generate_Brain()