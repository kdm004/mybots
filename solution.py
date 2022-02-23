import numpy
#--------------------------------------------
class SOLUTION:
    def __init__(self):
        self.weights = numpy.random.rand(3,2)
        print('before',self.weights)
        self.weights = self.weights * 2 - 1
        print('after',self.weights)