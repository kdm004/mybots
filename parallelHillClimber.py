
from solution import SOLUTION 
import constants as c
import copy
import os
import glob
import pybullet as p
import random 
import numpy
#------------------------------------
class PARALLEL_HILL_CLIMBER:
    def __init__(self, overallBot, continueOrNone):
        self.overallBot = overallBot
        self.continueOrNone = continueOrNone
        self.parents = {}
        self.record = numpy.zeros((c.numberOfGenerations,c.populationSize)) 
        numberOfBrainFiles = len(glob.glob("brainFiles/brain*.nndf"))

        if os.path.exists('bestBrains.txt'):
            fp = open('bestBrains.txt', 'r') 
            lines = fp.readlines()
            cleanLines = []
            for entry in lines:
                cleanLines.append(entry.replace('\n',''))
            cleanLines = list(map(int, cleanLines))
            print('Here are bestBrains entries:',cleanLines)
            fp.close()
            self.nextAvailableID = max(cleanLines) + 1
            for i in range(numberOfBrainFiles):
                if os.path.exists('brainFiles/brain'+str(self.nextAvailableID)+'.nndf'):
                    self.nextAvailableID += 1

        else:
            self.nextAvailableID = 0    
            for i in range(numberOfBrainFiles): 
                if os.path.exists("brainFiles/brain"+ str(self.nextAvailableID) + ".nndf"):  
                    self.nextAvailableID += 1

        for i in range(c.populationSize): 
            self.parents[i] = SOLUTION(self.nextAvailableID, self.overallBot, self.continueOrNone, i) # i is the populationID
            self.nextAvailableID = self.nextAvailableID + 1
    


    def Evolve(self): 
        self.Evaluate(self.parents)
        for g in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            for p in range(c.populationSize): 
                lookFitness = self.parents.get(p).fitness 
                self.record.itemset((g,p), lookFitness) 



    def Evolve_For_One_Generation(self):
        self.Spawn()
        # headsOrTails = random.choice([0,1])
        # if headsOrTails == 1:
        self.Mutate()
        # else:
        #     self.Mutate_Body()

        self.Evaluate(self.children)
        self.Print() 
        self.Select()



    def Spawn(self):
        self.children = {}
        for i in range (len(self.parents)): 
            self.children[i] = copy.deepcopy(self.parents[i])
            self.nextAvailableID = self.nextAvailableID + 1
            


    def Mutate(self):
        for i in range(len(self.children)):
            self.children[i].Mutate()
        


    def Mutate_Body(self):
        for i in range(len(self.children)): 
            self.children[i].Mutate_Body()



    def Print(self): 
        print('\n')
        for key in range(len(self.parents)):
            print('parents fitness =',self.parents[key].fitness, 'children fitness=',self.children[key].fitness)
        print('\n')



    def Select(self): 
        for key in range(len(self.parents)):
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]
        


    def Show_Best(self):
        self.parents = sorted(self.parents.values(), key = lambda x: x.fitness, reverse = True)
        print("Best fitness = ", self.parents[0].fitness)
        self.parents[0].Start_Simulation("DIRECT")



    def Write_Best_ID(self):
        # Write best brain file ID to bestBrains.txt
        bestIDFile = open("bestBrains.txt", "a") 
        bestIDFile.write(str(self.parents[0].myID))       
        bestIDFile.write('\n')                             
        bestIDFile.close
        


    def Write_Best_Fitness(self):
        noObstacleFile = open("emptyEnv_fitnesses.txt", "a")      # Use this one if empty environment.
        noObstacleFile.write(str(self.parents[0].fitness))
        noObstacleFile.write('\n')
        noObstacleFile.close



    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT", self.overallBot) #step 69 parallelHC -- GUI -> DIRECT
        for i in range(len(solutions)):            #step 72 parallelHC... uncomment to activate Parallelism, comment to deactivate Parallelism
            solutions[i].Wait_For_Simulation_To_End()



    def Results(self):
        if os.path.exists('bestBrains.txt'):
            fp = open('bestBrains.txt', 'r') 
            lines = fp.readlines()
            cleanLines = []
            for entry in lines:
                cleanLines.append(entry.replace('\n',''))
            cleanLines = list(map(int, cleanLines))
            fp.close()

        # make sure that file will be overwritten if we decide to use "python3 emptyWrapper.py -continue"
        if self.continueOrNone == 'none':
            print('Start Test1')
            print(cleanLines)
            print(self.overallBot)
            print('End Test1')
            numpy.savetxt('fitnessCurves/fitness_curve'+str(cleanLines[int(self.overallBot)])+'.txt', self.record, delimiter=',') #LOOK

        else:
            itemset = []
            with open('fitnessCurves/fitness_curve'+str(cleanLines[int(self.overallBot)])+'.txt', "r") as f:
                for line in f:
                    items = line.strip().split(",")
                    itemset.append(items)
            itemset.extend(self.record) # extend with self.record
            itemset = numpy.array(itemset, dtype=float) # convert to float
            print('itemset = ', itemset)
            numpy.savetxt('fitnessCurves/fitness_curve'+str(cleanLines[int(self.overallBot)])+'.txt', itemset, delimiter=',')
            f.close()

            