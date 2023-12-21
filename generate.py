import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    # pyrosim.Send_Cube(name="Box", pos=[-20,16,.51] , size=[1,1,1])
    # pyrosim.Send_Cube(name="Box1", pos=[-20,14,.52] , size=[1,1,1])
    # pyrosim.Send_Cube(name="Box", pos=[-20,12,.53] , size=[1,1,1])
    # pyrosim.Send_Cube(name="Box", pos=[-20,10,.54] , size=[1,1,1])

    pyrosim.End()

def Create_Robot(xi, yi, zi):
    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name="Torso", pos=[xi, yi, zi], size=[1,1,1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[xi-0.5, yi,zi-0.5])

    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[xi+0.5, yi,zi-0.5])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])

    pyrosim.End()


Create_Robot(0, 0, 1.5)
Create_World()

