import os
import glob





listOfBrains = glob.glob('brain*.nndf')
#print(type(listOfBrains))
#print(listOfBrains)
brainNumbers = []
for entry in listOfBrains:
    brainNumbers.append(int(entry.strip('brain.nndf')))

#print(brainNumbers)
#print(max(brainNumbers))
#print(number)


myList2=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
#print(min(myList2))



fitnessFile = open('emptyEnv_fitnesses.txt','r')
fitnessList = fitnessFile.readlines()
fitnessFile.close()

cleanFitnessList = []
for entry in fitnessList:
    cleanFitnessList.append(entry.replace('\n',''))
cleanFitnessList = list(map(float,cleanFitnessList))


bestIDFile = open("bestBrains.txt","r")
bestBrains = bestIDFile.readlines()
bestIDFile.close()

bestBrains = list(map(int, bestBrains))


overallChampionIndex =  cleanFitnessList.index(min(cleanFitnessList))



print(overallChampionIndex)

print(bestBrains[overallChampionIndex])