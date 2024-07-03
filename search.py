import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import sys

swarm = sys.argv[1]
bot = sys.argv[2]


phc = PARALLEL_HILL_CLIMBER(swarm, bot)
phc.Evolve()
phc.Show_Best()
phc.Write_Best()
phc.Save_Evolution_History()

