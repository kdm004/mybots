
from solution import SOLUTION
import constants as c
import copy
import os
import numpy
import random
#------------------------------------
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf") # step 82 parallelHC
        os.system("rm fitness*.txt") # step 83 parallelHC
        self.parents = {}
        self.nextAvailableID = 0

        self.record = numpy.zeros((c.populationSize, c.numberOfGenerations)) # LOOK hello data

        #self.child = SOLUTION() #might need to pass in self.nextAvailableID to SOLUTION()
        for i in range(c.populationSize): # why isn't this len(self.nextAvailableID)?
            self.parents[i] = SOLUTION(self.nextAvailableID) 
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self): 
        self.Evaluate(self.parents)
        for g in range(c.numberOfGenerations): # to get just the first gen, set c.numberOfGenerations = 1 LOOK Changed currentGeneration to g
            self.Evolve_For_One_Generation()
            for p in range(c.populationSize): #LOOK
                lookFitness = self.parents.get(p).fitness #LOOK
                self.record.itemset((p,g), lookFitness) #LOOK

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print() # uncommented call to parallelHC print method ... step 107 parallelHC
        self.Select()

    def Spawn(self):
        self.children = {}
        #self.parents = {}
        #self.child = copy.deepcopy(self.parent)
        for i in range (len(self.parents)): #changed from i in range (len(self.parents))
            #self.children[i].Set_ID()
            self.children[i] = copy.deepcopy(self.parents[i])
            self.nextAvailableID = self.nextAvailableID + 1
            


    def Mutate(self):
        for i in range(len(self.children)): # len(self.children) iterates through empty keys too
            self.children[i].Mutate()

    def Print(self): # modified according to step 108
        print('\n')
        for key in range(len(self.parents)):
            print('parents fitness =',self.parents[key].fitness, 'children fitness=',self.children[key].fitness)
        print('\n')

    def Select(self): # modified for step 112
        for key in range(len(self.parents)):
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]
        
    def Show_Best(self):
        overKey = 0
        bestFitness = self.parents[0].fitness
        for i in range(len(self.parents)):
            if self.parents[i].fitness < bestFitness:
                bestFitness = self.parents[i].fitness
                overKey = i
        self.parents[overKey].Start_Simulation("GUI")


    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT") #step 69 parallelHC -- GUI -> DIRECT
        for i in range(len(solutions)):            #step 72 parallelHC... uncomment to activate Parallelism, comment to deactivate Parallelism
            solutions[i].Wait_For_Simulation_To_End()

    def Results(self):
        numpy.savetxt('resultsPentapod2.out', self.record, delimiter=',', fmt='%.4f') #LOOK
        #numpy.save('resultsPentapod2'+'.npy', self.record) #LOOK
        numpy.savetxt('resultsPentapod2_'+str(random.randint(3,99999))+'.csv', self.record, delimiter=',', fmt='%.4f') #LOOK