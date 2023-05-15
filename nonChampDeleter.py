import os
import time
import glob
import constants as c


def NonChampDeleter():
    if os.path.exists('bestBrains.txt'):
        # Delete Non-Champion brain.nndf files
        fp = open('bestBrains.txt', 'r') 
        lines = fp.readlines()
        cleanLines = []
        for entry in lines:
            cleanLines.append(entry.replace('\n',''))
        cleanLines = list(map(int, cleanLines))
        print('Here are bestBrains entries:',cleanLines)
        fp.close()


        # We are removing any file with an ID that is not a champion between (current ID + populationSize) to 0. 
        lastInBestBrains = cleanLines[-1:][0]
        allIDs = list(range(lastInBestBrains+c.populationSize))
        nonChamps = list(set(allIDs).difference(set(cleanLines)))                                                                         


        bestBrainsList = cleanLines
        currentChamp = int(bestBrainsList[len(bestBrainsList)-1])
        previousChamp = int(bestBrainsList[len(bestBrainsList)-2])
        if len(bestBrainsList) > 0:
            for entry in nonChamps:
                if previousChamp < entry < currentChamp:
                    for i in range(previousChamp+1, currentChamp): # numbers that are between previousChamp and currentChamp, excluding previousChamp and currentChamp
                        if i not in bestBrainsList:
                            os.system('rm brainFiles/brain'+str(i)+'.nndf')
                            os.system('rm bodyFiles/body0-18'+str(i)+'.urdf')
                            os.system('rm bodyFiles/body0-14'+str(i)+'.urdf')
                            os.system('rm bodyFiles/body0-10'+str(i)+'.urdf')
                            os.system('rm bodyFiles/body0-6'+str(i)+'.urdf')
                            os.system('rm bodyFiles/body0-2'+str(i)+'.urdf')
                            os.system('rm bodyFiles/body02'+str(i)+'.urdf')
                            os.system('rm bodyFiles/body06'+str(i)+'.urdf')
                            os.system('rm bodyFiles/body010'+str(i)+'.urdf')
                            os.system('rm bodyFiles/body014'+str(i)+'.urdf')
                            os.system('rm bodyFiles/body018'+str(i)+'.urdf')
                            os.system('rm fitness_curve'+str(i)+'.urdf')
