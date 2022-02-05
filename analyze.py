import matplotlib.pyplot
import numpy as numpy
#import matplotlib.pylab as plt

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

#matplotlib.pyplot.plot(backLegSensorValues, linewidth = 5, label = 'Back Leg')
#matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg')
#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()

motorCommand = numpy.load('data/motorCommand.npy')
#plt.plot(motorCommand, numpy.sin(motorCommand))
#plt.xlabel('Angle [rad]')
#plt.ylabel('sin(motorCommand)')
#plt.axis('tight')
#plt.show()
motorPlot = matplotlib.pyplot.plot(numpy.sin(motorCommand))
matplotlib.pyplot.show()
#





