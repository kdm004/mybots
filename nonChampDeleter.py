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



        lastInBestBrains = cleanLines[-1:][0]
        allIDs = list(range(lastInBestBrains+c.populationSize)) # add population size just in case the last ID in bestBrains is the first of that 5 members of a population. 
        nonChamps = list(set(allIDs).difference(set(cleanLines)))             # maybe we should change the name of cleanLines to something like bestBrains?                                                                        #.
        for entry in nonChamps:
            os.system('rm brainFiles/brain'+str(entry)+'.nndf')
            os.system('rm bodyFiles/body0-18'+str(entry)+'.urdf')
            os.system('rm bodyFiles/body0-14'+str(entry)+'.urdf')
            os.system('rm bodyFiles/body0-10'+str(entry)+'.urdf')
            os.system('rm bodyFiles/body0-6'+str(entry)+'.urdf')
            os.system('rm bodyFiles/body0-2'+str(entry)+'.urdf')
            os.system('rm bodyFiles/body02'+str(entry)+'.urdf')
            os.system('rm bodyFiles/body06'+str(entry)+'.urdf')
            os.system('rm bodyFiles/body010'+str(entry)+'.urdf')
            os.system('rm bodyFiles/body014'+str(entry)+'.urdf')
            os.system('rm bodyFiles/body018'+str(entry)+'.urdf')


#----------------------------------------------------------------------------------------------------------------
        # for entry in nonChamps:
        #     os.system('rm brainFiles/brain'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body0-18'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body0-14'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body0-10'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body0-6'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body0-2'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body02'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body06'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body010'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body014'+str(entry)+'.txt')
        #     os.system('rm bodyFiles/body018'+str(entry)+'.txt')


        #     # If there's a glitch and a file isn't deleted, wait until it's deleted
        #     while os.path.exists('brainFiles/brain'+str(entry)+'.txt'):
        #         os.system('rm brainFiles/brain'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body0-18'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body0-18'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body0-14'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body0-14'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body0-10'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body0-10'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body0-6'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body0-6'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body0-2'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body0-2'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body02'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body02'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body06'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body06'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body010'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body010'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body014'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body014'+str(entry)+'.txt')
        #         time.sleep(0.1)
        #     while os.path.exists('bodyFiles/body018'+str(entry)+'.txt'):
        #         os.system('rm bodyFiles/body018'+str(entry)+'.txt')
        #         time.sleep(0.1)

        









        # numberOfBrainFiles = len(glob.glob("brainFiles/brain*.nndf"))
        # for i in range(c.populationSize*350): # changed from numberOfBrainFiles since some brains are out of that range. max(cleanLines) could be the first of a batch of populationSize.
        #     if i not in cleanLines:
        #         #print("Here is i:",i)
        #         os.system('rm brainFiles/brain'+str(i)+'.nndf')           # remove non-champ brains
        #         os.system('rm bodyFiles/body*'+str(i)+'.urdf')           # remove non-champ bodies
        #         while os.path.exists('brainFiles/brain'+str(i)+'.nndf'):
        #             os.system('rm brainFiles/brain' + str(i)+'.nndf')        # remove non-champ brains
        #             os.system('rm bodyFiles/body*'+str(i)+'.urdf')          # remove non-champ bodies

        #             time.sleep(0.1)


    