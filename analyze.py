import matplotlib.pyplot
import numpy as numpy
import matplotlib.pylab as plt

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

#matplotlib.pyplot.plot(backLegSensorValues, linewidth = 5, label = 'Back Leg')
#matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg')
#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()
#--------------------------------------
BackLeg_motorCommand = numpy.load('data/BackLeg_motorCommand.npy')
#plt.plot(BackLeg_motorCommand, numpy.sin(BackLeg_motorCommand))
#plt.xlabel('Angle [rad]')
#plt.ylabel('sin(BackLeg_motorCommand)')
#plt.axis('tight')
#plt.show()


motorPlot = matplotlib.pyplot.plot(numpy.sin(BackLeg_motorCommand))
matplotlib.pyplot.show()
#--------------------------------------
#matplotlib.pyplot.plot(BackLeg_motorCommand)
#matplotlib.pyplot.show()
#



