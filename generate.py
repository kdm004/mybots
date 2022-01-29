import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x1,y1,z1] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [.5,0,1])
    pyrosim.Send_Cube(name="Leg", pos=[x2,y2,z2] , size=[length,width,height])
    pyrosim.End()

#Cube size (length, width, height) and position (x,y,z)
length = 1
width = 1
height = 1

#we want the world block to be at (-3, 3, .5)

x = -3
y = 3
z = .5

x1 = 0
y1 = 0
z1 = .5

x2 = .5
y2 = 0
z2 = .5

Create_World()
Create_Robot()
