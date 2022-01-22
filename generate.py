import pyrosim.pyrosim as pyrosim
length = 1
width = 2
height = 3

pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[length,width,height])

pyrosim.End()


