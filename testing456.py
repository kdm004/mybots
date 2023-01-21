
import time as t
import constants as c
import numpy as np
import random


class Greeting:
    def __init__(self, greeting1, greeting2 = None, greeting3 = None):
        self.greeting1 = greeting1
        self.greeting2 = greeting2
        self.greeting3 = greeting3


    def speak1(self):
        print(str(self.greeting1))

    def speak2(self):
        print(str(self.greeting2))
    
    def speak3(self):
        print(str(self.greeting3))


classInstance1 = Greeting('Hey there!', 'Yo!')

classInstance1.speak3()