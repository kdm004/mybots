from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np
#------------------------------------
class PARALLEL_HILL_CLIMBER:
    def __init__(self, overallBot):
        # os.system("rm brains/brain*.nndf") # step 82 parallelHC
        os.system("rm fitness*.txt") 
        self.parents = {}
        self.overallBot = overallBot
        self.nextAvailableID = 0
        self.evolutionHistory = np.zeros((c.numberOfGenerations+1,c.populationSize))

        for i in range(c.populationSize): 
            self.parents[i] = SOLUTION(self.nextAvailableID, self.overallBot) 
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self): 
        self.Evaluate(self.parents)
        for p in self.parents:
            initialFitness = self.parents[p].fitness
            self.evolutionHistory[0,p] = initialFitness
        for g in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            for p in range(c.populationSize):
                fitness = self.parents[p].fitness
                self.evolutionHistory[g+1, p] = fitness

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
        sortedParents = sorted(self.parents.values(), key=lambda x: x.fitness)           
        sortedParents[0].Start_Simulation("DIRECT")   

    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT") 
        for i in range(len(solutions)):         
            solutions[i].Wait_For_Simulation_To_End()

    def Save_Evolution_History(self):
                np.savetxt(f'fitnessCurves/fitnessCurve_{self.overallBot}.txt', self.evolutionHistory, delimiter=',') 