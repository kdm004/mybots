import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1
x = 0
y = 0
z = .5 * height

for i in range(10):
    x += i
    for j in range (10):
        y += 1
        new_length *= .9
        new_width *= .9
        new_height *= .9

        for k in range(10):
            new_length *= .9
            new_width *= .9
            new_height *= .9
            pyrosim.Send_Cube(name="Box2", pos=[a,b,c] , size=[length,width,height])

pyrosim.End()


