import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5 * height

a = 1
b = 0
c = (.5 * height) + height  #Multiplied height by 2 to increase box starting height by 1 box
pyrosim.Start_SDF("boxes.sdf")

pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
pyrosim.Send_Cube(name="Box2", pos=[a,b,c] , size=[length,width,height])

pyrosim.End()


