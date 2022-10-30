import os
import glob





listOfBrains = glob.glob('brain*.nndf')
#print(type(listOfBrains))
#print(listOfBrains)
brainNumbers = []
for entry in listOfBrains:
    brainNumbers.append(int(entry.strip('brain.nndf')))

print(brainNumbers)
print(max(brainNumbers))
#print(number)


