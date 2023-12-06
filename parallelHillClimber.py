from solution import SOLUTION 
import constants as c
import copy
import os
import glob
import pybullet as p
import numpy as np
#------------------------------------
class PARALLEL_HILL_CLIMBER:
    def __init__(self, overallBot, continueOrNone):
        self.overallBot = overallBot
        self.continueOrNone = continueOrNone
       # os.system("rm brain*.nndf") # step 82 parallelHC
        #os.system("rm fitness*.txt") # step 83 parallelHC
        self.parents = {}

        if self.continueOrNone == 'none':
            self.record = np.zeros((c.numberOfGenerations+1,c.populationSize)) # LOOK hello data
        if self.continueOrNone == 'continue':
            self.record = np.zeros((c.numberOfGenerations,c.populationSize))   # purpose would be such that we don't want to rewrite the fitness of the loaded in weights, so size will only be g instead of g+1

        # This block is for manyBots
        # Start with ID of 0, and check if a brain.nndf file has already occurred. Purpose of this code block is to determine the initial ID after possible prev ParallelHC
        brain_files = glob.glob("brainFiles/brain*.nndf")
        numberOfBrainFiles = len(brain_files)
        if os.path.exists('bestBrains.txt'):
            with open('bestBrains.txt', 'r') as fp:
                cleanLines = [int(entry.strip()) for entry in fp]
            print('Here are bestBrains entries:', cleanLines)
            
            self.nextAvailableID = max(cleanLines) + 1
            for i in range(numberOfBrainFiles):
                if os.path.exists('brainFiles/brain'+str(self.nextAvailableID)+'.nndf'):
                    self.nextAvailableID += 1
        else:
            self.nextAvailableID = 0      # we should make it start at something that already exists so the code can iterate to an ID that doesn't exist yet.
            for i in range(numberOfBrainFiles): 
                if os.path.exists("brainFiles/brain"+ str(self.nextAvailableID) + ".nndf"):  
                    self.nextAvailableID += 1

        # For each parent, a single file is going to be overwritten/evolved
        for i in range(c.populationSize): 
            self.parents[i] = SOLUTION(self.nextAvailableID, self.overallBot, self.continueOrNone, i) # i = populationID
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self): 
        self.Evaluate(self.parents)
        for p in self.parents:
            if self.continueOrNone == 'none':
                initialFitness = self.parents[p].fitness
                self.record[0, p] = initialFitness  # Fill the first row            # if 'continue', then this shouldn't happen
        for g in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            for p in range(c.populationSize): 
                lookFitness = self.parents[p].fitness
                if self.continueOrNone == 'none':
                    self.record[g+1,p] = lookFitness                                # if 'continue', then [g,p] not [g+1,p]
                if self.continueOrNone == 'continue':
                    self.record[g,p] = lookFitness

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
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
        for i in range(len(self.children)):
            self.children[i].Mutate()

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
        sorted_parents = sorted(self.parents.values(), key=lambda x: x.fitness)             # Sort parents by fitness
        sorted_parents[0].Start_Simulation("DIRECT")                                        # Start simulation with the best parent using "DIRECT" method
        with open("bestBrains.txt", "a") as best_id_file:                                   # Write the best brain file ID to bestBrains.txt
            best_id_file.write(str(sorted_parents[0].myID))
            best_id_file.write('\n')
        with open("emptyEnv_fitnesses.txt", "a") as no_obstacle_file:                       # Write the fitness to emptyEnv_fitnesses.txt
            no_obstacle_file.write(str(sorted_parents[0].fitness))
            no_obstacle_file.write('\n')

    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT")                                         #step 69 parallelHC
        for i in range(len(solutions)):                                                     #step 72 parallelHC... uncomment to activate Parallelism, comment to deactivate Parallelism
            solutions[i].Wait_For_Simulation_To_End()



    def Results(self):        
        if os.path.exists('bestBrains.txt'):
            with open('bestBrains.txt', 'r') as fp:
                clean_lines = [int(entry.strip()) for entry in fp]

            # make sure that the file will be overwritten if we decide to use "python3 emptyWrapper.py -continue"
            if self.continueOrNone == 'none':
                print('Start Test1')
                print(clean_lines)
                print(self.overallBot)
                print('End Test1')
                np.savetxt(f'fitnessCurves/fitness_curve{int(self.overallBot)}.txt', self.record, delimiter=',')  # LOOK
            else:
                itemset = []
                with open(f'fitnessCurves/fitness_curve{int(self.overallBot)}.txt', "r") as f:
                    for line in f:
                        items = line.strip().split(",")
                        itemset.append(items)
                itemset.extend(self.record)  # extend with self.record
                itemset = np.array(itemset, dtype=float)  # convert to float
                print('itemset = ', itemset)
                np.savetxt(f'fitnessCurves/fitness_curve{int(self.overallBot)}.txt', itemset, delimiter=',')


