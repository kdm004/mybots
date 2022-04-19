import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    #pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
        
        #Torso
    pyrosim.Send_Sphere(name="Torso", pos=[0,0,1] , size=[1])

#-------------------------
        #Right Leg
    pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "fixed", position = [1,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg", pos=[0,0,0] , size=[1])

    pyrosim.Send_Joint( name = "RightLeg_RightLeg2" , parent= "RightLeg" , child = "RightLeg2" , type = "fixed", position = [0,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg2", pos=[0,0,0] , size=[1])

    pyrosim.Send_Joint( name = "RightLeg2_RightLeg3" , parent= "RightLeg2" , child = "RightLeg3" , type = "fixed", position = [0,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg3", pos=[0,0,0] , size=[1])

    pyrosim.Send_Joint( name = "RightLeg3_RightLeg4" , parent= "RightLeg3" , child = "RightLeg4" , type = "fixed", position = [0,1,0], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg4", pos=[0,0,0] , size=[1])

    pyrosim.Send_Joint( name = "RightLeg4_RightLeg5" , parent= "RightLeg4" , child = "RightLeg5" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0") #for original sim, put pos[0,0,1]
    pyrosim.Send_Sphere(name="RightLeg5", pos=[0,0,0] , size=[1])
#---------------
    pyrosim.Send_Joint( name = "RightLeg5_RightLeg6" , parent= "RightLeg5" , child = "RightLeg6" , type = "fixed", position = [0,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg6", pos=[0,0,0] , size=[1])

    pyrosim.Send_Joint( name = "RightLeg6_RightLeg7" , parent= "RightLeg6" , child = "RightLeg7" , type = "fixed", position = [0,1,0], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg7", pos=[0,0,0] , size=[1])
    
    pyrosim.Send_Joint( name = "RightLeg7_RightLeg8" , parent= "RightLeg7" , child = "RightLeg8" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg8", pos=[0,0,0] , size=[1])
#--------------

    pyrosim.Send_Joint( name = "RightLeg8_RightLeg9" , parent= "RightLeg8" , child = "RightLeg9" , type = "fixed", position = [0,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg9", pos=[0,0,0] , size=[1])

    pyrosim.Send_Joint( name = "RightLeg9_RightLeg10" , parent= "RightLeg9" , child = "RightLeg10" , type = "fixed", position = [0,1,0], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg10", pos=[0,0,0] , size=[1])
    
    pyrosim.Send_Joint( name = "RightLeg10_RightLeg11" , parent= "RightLeg10" , child = "RightLeg11" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg11", pos=[0,0,0] , size=[1])

    pyrosim.Send_Joint( name = "RightLeg11_RightLeg12" , parent= "RightLeg11" , child = "RightLeg12" , type = "fixed", position = [0,1,0], jointAxis = "0 1 0")
    pyrosim.Send_Sphere(name="RightLeg12", pos=[0,0,0] , size=[1])

    #pyrosim.Send_Joint( name = "RightLeg12_RightLeg13" , parent= "RightLeg12" , child = "RightLeg13" , type = "fixed", position = [0,1,0], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg13", pos=[0,0,0] , size=[1])
#-----------
    #pyrosim.Send_Joint( name = "RightLeg13_RightLeg14" , parent= "RightLeg13" , child = "RightLeg14" , type = "fixed", position = [0,1,0], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg14", pos=[0,0,0] , size=[1])

    #pyrosim.Send_Joint( name = "RightLeg14_RightLeg15" , parent= "RightLeg14" , child = "RightLeg15" , type = "fixed", position = [0,0,1], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg15", pos=[0,0,0] , size=[1])

    #------
#17
    #pyrosim.Send_Joint( name = "RightLeg15_RightLeg16" , parent= "RightLeg15" , child = "RightLeg16" , type = "fixed", position = [0,0,1], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg16", pos=[0,0,0] , size=[1])

    #pyrosim.Send_Joint( name = "RightLeg16_RightLeg17" , parent= "RightLeg16" , child = "RightLeg17" , type = "fixed", position = [0,1,0], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg17", pos=[0,0,0] , size=[1])

    #pyrosim.Send_Joint( name = "RightLeg17_RightLeg18" , parent= "RightLeg17" , child = "RightLeg18" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg18", pos=[0,0,0] , size=[1])

    #pyrosim.Send_Joint( name = "RightLeg18_RightLeg19" , parent= "RightLeg18" , child = "RightLeg19" , type = "fixed", position = [0,1,0], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg19", pos=[0,0,0] , size=[1])

    #pyrosim.Send_Joint( name = "RightLeg19_RightLeg20" , parent= "RightLeg19" , child = "RightLeg20" , type = "fixed", position = [0,1,0], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg20", pos=[0,0,0] , size=[1])

    #pyrosim.Send_Joint( name = "RightLeg20_RightLeg21" , parent= "RightLeg20" , child = "RightLeg21" , type = "fixed", position = [0,0,1], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg21", pos=[0,0,0] , size=[1])

    #pyrosim.Send_Joint( name = "RightLeg21_RightLeg22" , parent= "RightLeg21" , child = "RightLeg22" , type = "fixed", position = [1,0,0], jointAxis = "0 1 0")
    #pyrosim.Send_Sphere(name="RightLeg22", pos=[0,0,0] , size=[1])


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
