import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1
x = 0
y = 0
z = .5 * height

for k in range(10):
    length *= .9
    width *= .9
    height *= .9
    pyrosim.Send_Cube(name="Box", pos=[x,y,z+k] , size=[length,width,height])

pyrosim.End()


