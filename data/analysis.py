import numpy as np

# Load the data from the .npy file
motor_values = np.load('data/BackLeg_BackLowerLegmotorValues.npy')
sensor_values = np.load('data/BackLowerLegsensorValues.npy')
print(motor_values[0:100])
print(sensor_values[0:10])


