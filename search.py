import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import sys

swarm = sys.argv[1]
bot = sys.argv[2]
overallBot = sys.argv[3]                                            # add overallBot as a sys.argv[3] which is incoming from evolveSwarms.py. --> PARALLEL_HILL_CLIMBERS --> SOLUTION --> I think we're good here but idk where else it needs to be passed to. Pretty sure solution is where the body is generated? Maybe I only need to go to PHC becuase that's were the body is geenerated. 

phc = PARALLEL_HILL_CLIMBER(swarm, bot, overallBot)
phc.Evolve()
phc.Show_Best()
phc.Write_Best()
phc.Save_Evolution_History()

