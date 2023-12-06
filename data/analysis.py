import numpy as np


# Empty
# \n
# Obstacles:
#--------------------------------------------------------------------------------------------------------------------------


# Front Leg
print('--- Front Leg ---')
motor_empty = np.load('data/empty/FrontLeg_FrontLowerLegmotorValues.npy')
sensor_empty = np.load('data/empty/FrontLowerLegsensorValues.npy')
print(motor_empty[0:10])
print(sensor_empty[0:10])
print('\n')
motor_obstacles = np.load('data/obstacles/FrontLeg_FrontLowerLegmotorValues.npy')
sensor_obstacles = np.load('data/obstacles/FrontLowerLegsensorValues.npy')
print(motor_obstacles[0:10])
print(sensor_obstacles[0:10])

print('\n')

# Back Leg
print('--- Back Leg ---')
motor_empty = np.load('data/empty/BackLeg_BackLowerLegmotorValues.npy')
sensor_empty = np.load('data/empty/BackLowerLegsensorValues.npy')
print(motor_empty[0:10])
print(sensor_empty[0:10])
print('\n')
motor_obstacles = np.load('data/obstacles/BackLeg_BackLowerLegmotorValues.npy')
sensor_obstacles = np.load('data/obstacles/BackLowerLegsensorValues.npy')
print(motor_obstacles[0:10])
print(sensor_obstacles[0:10])

print('\n')

# Left Leg
print('--- Left Leg ---')
motor_empty = np.load('data/empty/LeftLeg_LeftLowerLegmotorValues.npy')
sensor_empty = np.load('data/empty/LeftLowerLegsensorValues.npy')
print(motor_empty[0:10])
print(sensor_empty[0:10])
print('\n')
motor_obstacles = np.load('data/obstacles/LeftLeg_LeftLowerLegmotorValues.npy')
sensor_obstacles = np.load('data/obstacles/LeftLowerLegsensorValues.npy')
print(motor_obstacles[0:10])
print(sensor_obstacles[0:10])

print('\n')

# Right Leg
print(' --- Right Leg ---')
motor_empty = np.load('data/empty/RightLeg_RightLowerLegmotorValues.npy')
sensor_empty = np.load('data/empty/RightLowerLegsensorValues.npy')
print(motor_empty[0:10])
print(sensor_empty[0:10])
print('\n')
motor_obstacles = np.load('data/obstacles/RightLeg_RightLowerLegmotorValues.npy')
sensor_obstacles = np.load('data/obstacles/RightLowerLegsensorValues.npy')
print(motor_obstacles[0:10])
print(sensor_obstacles[0:10])