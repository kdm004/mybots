import random as random
import numpy as numpy
import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
import time
physicsClient = p.connect(p.DIRECT)     # DIRECT or GUI
robotId = p.loadURDF("body.urdf")
pyrosim.Prepare_To_Simulate(robotId)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)


planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

# Vectors for sensor values
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

# Target Angles Vector and scale factor mapping function
targetAngles = numpy.linspace(0,2*numpy.pi, 1000)
scaleFactor = float(numpy.pi/2) / float(2)
newTargetAngles = -numpy.pi/4 + (numpy.sin(targetAngles) - (-1))*scaleFactor

BackLeg_amplitude = numpy.pi/4
BackLeg_frequency = 1
BackLeg_phaseOffset = 0
    
FrontLeg_amplitude = numpy.pi/4
FrontLeg_frequency = 20
FrontLeg_phaseOffset = 0

BackLeg_motorCommand = BackLeg_amplitude * numpy.sin(BackLeg_frequency * targetAngles + BackLeg_phaseOffset)
FrontLeg_motorCommand = FrontLeg_amplitude * numpy.sin(FrontLeg_frequency * targetAngles + FrontLeg_phaseOffset)

#numpy.save('data/BackLeg_motorCommand.npy', BackLeg_motorCommand)
#exit()

for i in range (1000):
    p.stepSimulation()

    # Sensor values
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = BackLeg_motorCommand[i],
    maxForce = 20)  

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = FrontLeg_motorCommand[i],
    maxForce = 20)
  
    time.sleep(1/(2400))
    # print('For loop variable is',i)

    if i == 999:
        stateOfLinkZero = p.getLinkState(robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoord = positionOfLinkZero[0]
        print(xCoord)

# print(backLegSensorValues)
# print(frontLegSensorValues)

print(len(backLegSensorValues))
print(len(frontLegSensorValues))

file_path = 'sensor_data_obstacles.txt'
with open(file_path, 'w') as f:
    f.write(str(backLegSensorValues.tolist()))
    f.write('\n')
    f.write(str(frontLegSensorValues.tolist()))
    f.write('\n')

    
p.disconnect()
