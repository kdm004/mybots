import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[x0,y0,z0] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link1", pos=[x1,y1,z1] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link2", pos=[x2,y2,z2] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,.5,.5])
    pyrosim.Send_Cube(name="Link3", pos=[x3,y3,z3] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0,.5,0])
    pyrosim.Send_Cube(name="Link4", pos=[x4,y4,z4] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute", position = [0,.5,-.5])
    pyrosim.Send_Cube(name="Link5", pos=[x5,y5,z5] , size=[length,width,height])  
    pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute", position = [0,0,-1])
    pyrosim.Send_Cube(name="Link6", pos=[x6,y6,z6] , size=[length,width,height])

    pyrosim.End()

#Cube size (length, width, height) and position (x,y,z)
length = 1
width = 1
height = 1

#we want the world block to be at (-3, 3, .5)

x = -3
y = 3
z = .5

x0 = 0
y0 = 0
z0 = .5

x1 = 0
y1 = 0
z1 = .5

x2 = 0
y2 = 0
z2 = .5

x3 = 0
y3 = .5
z3 = 0

x4 = 0
y4 = 1
z4 = 0

x5 = 0
y5 = .5
z5 = -.5

x6 = 0
y6 = .5
z6 = -.5

Create_World()
Create_Robot()
