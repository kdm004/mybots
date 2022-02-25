from solution import SOLUTION
import constants as c
import copy
#------------------------------------
class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
        self.child = SOLUTION()

    def Evolve(self): # how to edit this to just show parent???
        self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations): # to get just the first gen, set c.numberOfGenerations = 1
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Print(self):
        print('parent fitness =',self.parent.fitness, 'child fitness=',self.child.fitness)

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
        
    def Show_Best(self):
        self.parent.Evaluate("GUI") #why isn't this showing?




