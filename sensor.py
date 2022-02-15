import constants as c
import numpy as numpy


class SENSOR:
    def __init__(self,linkName):
        self.values = numpy.zeros(c.loopLength)
        print(self.values)
        self.linkName = linkName
