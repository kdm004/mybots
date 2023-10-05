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
        numberOfBrainFiles = len(glob.glob("brainFiles/brain*.nndf"))

        if self.continueOrNone == 'none':
            self.record = numpy.zeros((c.numberOfGenerations+1,c.populationSize)) # LOOK hello data
        if self.continueOrNone == 'continue':
            self.record = numpy.zeros((c.numberOfGenerations,c.populationSize))   # purpose would be such that we don't want to rewrite the fitness of the loaded in weights, so size will only be g instead of g+1


        

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
            self.nextAvailableID = 0      # we should make it start at something that already exists so the code can iterate to an ID that doesn't exist yet.
            for i in range(numberOfBrainFiles): 
                if os.path.exists("brainFiles/brain"+ str(self.nextAvailableID) + ".nndf"):  
                    self.nextAvailableID += 1

        for i in range(c.populationSize): # this for loop says that there will be 1 file that will be overwritten/evolved per parent. This is the original for loop from parallelHC step #17
            self.parents[i] = SOLUTION(self.nextAvailableID, self.overallBot, self.continueOrNone, i) # i = populationID
            self.nextAvailableID = self.nextAvailableID + 1
    


    def Evolve(self): 
        self.Evaluate(self.parents)

        #----
        
        for p in self.parents:
            # initialFitness = self.parents.get(p).fitness # maybe put this above the for loop
            # self.record.itemset((1,p), initialFitness)
            if self.continueOrNone == 'none':
                initialFitness = self.parents[p].fitness
                self.record[0, p] = initialFitness  # Fill the first row            # if 'continue', then this shouldn't happen
        #----


        for g in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            for p in range(c.populationSize): 
                # lookFitness = self.parents.get(p).fitness 
                # self.record.itemset((g+1,p), lookFitness)       # +1
                lookFitness = self.parents[p].fitness

                if self.continueOrNone == 'none':
                    self.record[g+1,p] = lookFitness                                # if 'continue', then [g,p] not [g+1,p]
                if self.continueOrNone == 'continue':
                    self.record[g,p] = lookFitness



    def Evolve_For_One_Generation(self):
        self.Spawn()
        # headsOrTails = random.choice([0,1])
        # if headsOrTails == 1:
        self.Mutate()
        # else:
        #     self.Mutate_Body()

        self.Evaluate(self.children)
        self.Print() # uncommented call to parallelHC print method ... step 107 parallelHC
        self.Select()
        for p in self.parents:
            self.parents[p].Save_Weights()




    def Spawn(self):
        self.children = {}
        for i in range (len(self.parents)): 
            self.children[i] = copy.deepcopy(self.parents[i])
            self.nextAvailableID = self.nextAvailableID + 1
            


    def Mutate(self):
        for i in range(len(self.children)): # len(self.children) iterates through empty keys too?
            self.children[i].Mutate()
        


    def Mutate_Body(self):
        for i in range(len(self.children)): # len(self.children) iterates through empty keys too?
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
        self.parents[0].Start_Simulation("DIRECT", self.overallBot) # change this to GUI to actually see the best bot simulation



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
            solutions[i].Start_Simulation("DIRECT", self.overallBot) 
        for i in range(len(solutions)):       
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
            #print(cleanLines)
            print(self.overallBot)
            print('End Test1')
            numpy.savetxt('fitnessCurves/fitness_curve'+str(int(self.overallBot))+'.txt', self.record, delimiter=',') #LOOK

        else:
            itemset = []
            with open('fitnessCurves/fitness_curve'+str(int(self.overallBot))+'.txt', "r") as f:
                for line in f:
                    items = line.strip().split(",")
                    itemset.append(items)

            itemset.extend(self.record) # extend with self.record
            itemset = numpy.array(itemset, dtype=float) # convert to float
            print('itemset = ', itemset)
            numpy.savetxt('fitnessCurves/fitness_curve'+str(int(self.overallBot))+'.txt', itemset, delimiter=',')

            f.close()
