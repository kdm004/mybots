# class NUMBERS:
#     def __init__(self,num1, num2, num3):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3

#     def Add_Numbers(self):
#         self.sumNum = self.num1 + self.num2 + self.num3
#         return self.sumNum
import numpy as numpy

bestBrains = [1,3,5,7]
lastBrain = bestBrains[-1:][0]
allIDs = list(range(lastBrain+4))

diffs = list(set(allIDs).difference(set(bestBrains)))

print(diffs)




