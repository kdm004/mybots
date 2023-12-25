from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np
#------------------------------------
class PARALLEL_HILL_CLIMBER:
    def __init__(self, swarmNumber, botNumber):
        # os.system("rm brains/brain*.nndf") # step 82 parallelHC
        os.system("rm fitness*.txt") 
        self.parents = {}
        self.swarmNumber = int(swarmNumber)
        self.botNumber = int(botNumber)


        if c.continueEvolution == True:
            self.evolutionHistory = np.zeros((c.numberOfGenerations,c.populationSize))  
        else: 
            self.evolutionHistory = np.zeros((c.numberOfGenerations+1,c.populationSize))  

        self.nextAvailableID = 0
        for i in range(c.populationSize): 
            self.parents[i] = SOLUTION(self.nextAvailableID, self.swarmNumber, self.botNumber) 
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self): 
        self.Evaluate(self.parents)
        for p in self.parents:
            if c.continueEvolution == False:                # maybe put this above its for loop?
                initialFitness = self.parents[p].fitness
                self.evolutionHistory[0, p] = initialFitness  # Fill the first row            # if 'continue', then this shouldn't happen

        for g in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            for p in range(c.populationSize): 
                lookFitness = self.parents[p].fitness
                if c.continueEvolution == True:
                    self.evolutionHistory[g,p] = lookFitness                                # if 'continue', then [g,p] not [g+1,p]
                else:
                    self.evolutionHistory[g+1,p] = lookFitness

    # def Evolve(self):
    #     '''TO DO: Figure out why the first row in fitnessCurves is not being written'''


    # def Evolve(self):
    #     self.Evaluate(self.parents)
    #     for currentGeneration in range(c.numberOfGenerations):
    #         self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print() 
        self.Select()
        for p in self.parents:
            self.parents[p].Save_Weights()

    def Spawn(self):
        self.children = {}

        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            #self.children[i].Set_ID()
            self.nextAvailableID = self.nextAvailableID + 1
            
    def Mutate(self):
        for i in self.children: 
            self.children[i].Mutate()

    def Print(self): 
        print('\n')
        for key in self.parents:
            print('parents fitness =',self.parents[key].fitness, 'children fitness=',self.children[key].fitness)
        print('\n')

    def Select(self): 
        for i in self.parents:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]
        
    def Show_Best(self):
        self.sortedParents = sorted(self.parents.values(), key=lambda x: x.fitness)           
        self.sortedParents[0].Start_Simulation("DIRECT")   

    def Write_Best(self):
        with open("bestBrains.txt", "a") as f:                                   # Write the best brain file ID to bestBrains.txt
            f.write(str(self.sortedParents[0].myID))
            f.write('\n')
        if c.continueEvolution == True:
            with open("familiarFitsContinued.txt", "a") as f:
                f.write(str(self.sortedParents[0].fitness))
                f.write('\n')
        else:
            with open("familiarFits.txt", "a") as f:
                f.write(str(self.sortedParents[0].fitness))
                f.write('\n')

    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT") 
        for i in range(len(solutions)):         
            solutions[i].Wait_For_Simulation_To_End()

    def Save_Evolution_History(self):
        if c.continueEvolution == True:
            itemset = []
            with open(f'fitnessCurves/fitnessCurve_{self.swarmNumber}_{self.botNumber}.txt', "r") as f:
                for line in f:
                    items = line.strip().split(",")
                    itemset.append(items)
            itemset.extend(self.evolutionHistory)  # extend with self.evolutionHistor
            itemset = np.array(itemset, dtype=float)  # convert to float
            # print('itemset = ', itemset)
            np.savetxt(f'fitnessCurves/fitnessCurve_{self.swarmNumber}_{self.botNumber}.txt', itemset, delimiter=',')
        else:
            np.savetxt(f'fitnessCurves/fitnessCurve_{self.swarmNumber}_{self.botNumber}.txt', self.evolutionHistory, delimiter=',') 
