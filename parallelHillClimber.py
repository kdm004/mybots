from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np
#------------------------------------
class PARALLEL_HILL_CLIMBER:
    def __init__(self, swarmNumber, botNumber):
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
            if c.continueEvolution == False:               
                initialFitness = self.parents[p].fitness
                self.evolutionHistory[0, p] = initialFitness  

        for g in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            for p in range(c.populationSize): 
                lookFitness = self.parents[p].fitness
                if c.continueEvolution == True:
                    self.evolutionHistory[g,p] = lookFitness                               
                else:
                    self.evolutionHistory[g+1,p] = lookFitness

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        # self.Print() 
        self.Select()
        for p in self.parents:
            self.parents[p].Save_Weights()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
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
        self.sortedParents[0].Start_Simulation("DIRECT")                                    # start simulation uses Generate_Body()... so we want to change the position of each generated body in batches of 10. 

    def Write_Best(self):
        with open("bestBrains.txt", "a") as f:   
            f.write(str(self.sortedParents[0].myID))
            f.write('\n')
        with open("familiarFits.txt", "a") as f:
            f.write(str(self.sortedParents[0].fitness))
            f.write('\n')

    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT")                                         # start simulation uses Generate_Body()
        for i in range(len(solutions)):         
            solutions[i].Wait_For_Simulation_To_End()

    def Save_Evolution_History(self):
        if c.continueEvolution == True:
            itemset = []
            with open(f'fitnessCurves/fitnessCurve_{self.swarmNumber}_{self.botNumber}.txt', "r") as f:
                for line in f:
                    items = line.strip().split(",")
                    itemset.append(items)
            itemset.extend(self.evolutionHistory)     # extend with self.evolutionHistory
            itemset = np.array(itemset, dtype=float)  # convert to float
            # print('itemset = ', itemset)
            np.savetxt(f'fitnessCurves/fitnessCurve_{self.swarmNumber}_{self.botNumber}.txt', itemset, delimiter=',')
        else:
            np.savetxt(f'fitnessCurves/fitnessCurve_{self.swarmNumber}_{self.botNumber}.txt', self.evolutionHistory, delimiter=',') 
