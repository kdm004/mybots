import matplotlib.pyplot
import numpy as numpy


backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

matplotlib.pyplot.plot(backLegSensorValues, linewidth = 5, label = 'Back Leg')
matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()







