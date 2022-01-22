import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

length = 1/.9
width = 1/.9
height = 1/.9
x = 0
y = 0
z = .5

for i in range(6):
    x=i
    for j in range(6):
        y=j
        new_length = length
        new_width = width
        new_height = height
        for k in range(10):
            new_length *= .9
            new_width *= .9
            new_height *= .9
            pyrosim.Send_Cube(name="Box", pos=[x,y,z+k] , size=[new_length,new_width,new_height])

pyrosim.End() #Flat base, correctly positioned, and correct tower.


