from solution import SOLUTION 
import constants as c
import copy
import os
import glob
#------------------------------------
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
       # os.system("rm brain*.nndf") # step 82 parallelHC
        #os.system("rm fitness*.txt") # step 83 parallelHC
        self.parents = {}

        # Start with ID of 0, and check if a brain.nndf file has already occurred. Purpose of this code block is to determine the initial ID after possible prev ParallelHC
        numberOfBrainFiles = len(glob.glob("brain*.nndf"))
        self.nextAvailableID = 0 #instead of 0, we want this to start at the ID number of the last brainID.nndf file, or else it will make it 0 every time initially?
        for i in range(numberOfBrainFiles): # range(number of brain.nndf files)
            if os.path.exists("brain"+ str(self.nextAvailableID) + ".nndf"): 
                self.nextAvailableID += 1

        #self.child = SOLUTION() #might need to pass in self.nextAvailableID to SOLUTION()
        for i in range(c.populationSize): # this for loop says that there will be 1 file that will be overwritten/evolved per parent. 
            self.parents[i] = SOLUTION(self.nextAvailableID) 
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self): 
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations): # to get just the first gen, set c.numberOfGenerations = 1
            self.Evolve_For_One_Generation()

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
        overKey = 0                             # I think this 0 should actually start with the first of the next group of brain files that is being produced. 
        bestFitness = self.parents[0].fitness   # So it should be 0 for 012, 3 for 345, and 6 for 678. Will it keep showing 3 as well?
        for i in range(len(self.parents)):
            if self.parents[i].fitness < bestFitness:
                bestFitness = self.parents[i].fitness
                overKey = i
        self.parents[overKey].Start_Simulation("GUI") #Shows best single robot sim in GUI
        
        bestIDFile = open("bestBrains.txt", "a") # should it be 'w' or 'a'? write or append? 
        bestIDFile.write(str(self.parents[overKey].myID)) #        bestIDFile.write(str(self.parents[overKey].fitness))
        bestIDFile.write('\n') #       Write delimiter after brain ID


        bestIDFile.close
        


    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT") #step 69 parallelHC -- GUI -> DIRECT
        for i in range(len(solutions)):            #step 72 parallelHC... uncomment to activate Parallelism, comment to deactivate Parallelism
            solutions[i].Wait_For_Simulation_To_End()