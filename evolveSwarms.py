import os
import sys
import constants as c

# if len(sys.argv) > 0:
#    if sys.argv[1] == 'hey':
#       print('hello')

# assert len(sys.argv) == 3
# if sys.argv[0] == 'case1':
#     print('hello')



# To do:
'''
TO DO:
- Implement case1 by adding in a list of positions that the robot can take
- The position of the robot will be dictated by overallBotNumber
- Create a loop that iterates through 10 bots 3 times
- The resulting number from the loop will iterate from 0 to 29. This will represent bot number
- We will pass this bot number into the solution and perhaps parallelHillClimber
- We can probably have a variable in this file that updates called populationID. We can then reference this variable in other files for a cleaner way of keeping track which populationID we're on. 
   - The above is cleaner than having to keep a count going of the populationID within parallelHillClimber.py or solution.py
- one script for collecting foreign environment
- one script for collecting familiar environment
'''

# Evolve robots
overallBot = 0                                     # later, change this to the length of the bestBrains file
for swarm in range(c.numberOfSwarms):
    for bot in range(c.botsPerSwarm):
        os.system(f"python3 search.py {overallBot}")
        overallBot += 1

'''
TO DO:
- Pass in overallBot
- Make the naming scheme of the files like so --> brains/brain_overallBot_populationID
- nextAvailableID is populationID for our purposes, since nextAvailableID loops from 0 to c.populationSize
- Write out the ID of the bot? 
- Now, simply make the fileNames rely on overallBot
'''

'''
TO DO:

- It looks like we're collecting the data correctly. 
- Now push these changes as "collect in batches of 10"
- Now, we want to implement "continue" functionality
- Now, we want to change the position of each bot based on its NumberInSwarm = overallBot % 10

'''


# if collect.py evolve case1:
   # do this
# if collect.py continue case1:
   # do this
# if collect.py playback case1:
   # do this

# if collect.py evolve case2:
   # do this
# if collect.py continue case2:
   # do this
# if collect.py playback case2:
   # do this

# if collect.py evolve case3:
   # do this
# if collect.py continue case3:
   # do this
# if collect.py playback case3:
   # do this


'''
To do:
- Make a playback script, test it, push it
- Rename this branch to "quadruped_swarms"
- create a new branch called clean_case1
- implement case1 and case2
- 


'''



'''
To Do
- output the correct files for case1 such that playback simply needs to load them.

'''