import numpy as numpy
#------------------------------------------


loopLength = 1000 #change back to 1000

amplitude = numpy.pi/4
frequency = 10
phaseOffset = numpy.pi/2
legMaxForce = 120 # change back to 20

targetAngles = numpy.linspace(-numpy.pi,numpy.pi, loopLength)

sleepRate = 1/1000 #changed from 1/260

gravityConstant = -9.8 * 2.5 # delete * 2.5

numberOfGenerations = 10 #initially was 2, changed to 10 for step 75 hillclimber

populationSize = 2




