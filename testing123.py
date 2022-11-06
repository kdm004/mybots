import os
import glob
from testing456 import NUMBERS as NUMBERS

myList = [(1,2,3),(4,5,6)]

class DISPLAY:
    def __init__(self,index):
        self.index = index
        self.numbers = [(1,2,3),(4,5,6),(7,8,9)]

        self.mySum = NUMBERS(*self.numbers[index])

    def Print(self):
        print(self.mySum.Add_Numbers())




