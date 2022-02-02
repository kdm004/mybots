import random as random
import numpy as numpy
import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

# Vectors for sensor values
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

# Target Angles Vector
targetAngles = numpy.linspace(-numpy.pi,numpy.pi, 1000)

BackLeg_amplitude = numpy.pi/4
BackLeg_frequency = 10
BackLeg_phaseOffset = numpy.pi/2
    
FrontLeg_amplitude = numpy.pi/4
FrontLeg_frequency = 20
FrontLeg_phaseOffset = 0


BackLeg_motorCommand = BackLeg_amplitude * numpy.sin(BackLeg_frequency * targetAngles + BackLeg_phaseOffset)
FrontLeg_motorCommand = FrontLeg_amplitude * numpy.sin(FrontLeg_frequency * targetAngles + FrontLeg_phaseOffset)

#numpy.save('data/motorCommand.npy', motorCommand)
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
  

    time.sleep(1/(240))
    print('For loop variable is',i)
    print(backLegSensorValues)
    print(frontLegSensorValues)
    

numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
#numpy.save('data/targetAngles.npy', targetAngles)
p.disconnect()
