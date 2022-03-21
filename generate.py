import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    #pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Sphere(name="Sphere1", pos=[0,0,1] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Sphere1_Sphere2" , parent= "Sphere1" , child = "Sphere2" , type = "fixed", position = [0,.5,.5])

    pyrosim.Send_Sphere(name="Sphere2", pos=[0,0.5,1] , size=[1,1,1])


    pyrosim.End()

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


Create_World()
Create_Robot()
