import constants as c

# print(c.botPositions[0])

# def dummy_func(x, y, z=1):
#     print(x)
#     print(y)
#     print(z)

# test1 = dummy_func(*c.botPositions[0])


# swarmIndices = [j for j in range(c.numberOfSwarms) for i in range(c.botsPerSwarm)]
# botIndices = [j for j in range(c.botsPerSwarm) for i in range(c.botsPerSwarm)]

# print(swarmIndices)
# print(botIndices)


# if c.swarmType == 'case2' or 'case3':
#     swarmIndices = list(range(c.numberOfSwarms))
#     botIndices = list(range(c.botsPerSwarm))


# swarmIndices = [j for j in range(c.numberOfSwarms) for i in range(c.numberOfSwarms)]
# botIndices = [i for i in range(c.numberOfSwarms)]
# print(swarmIndices)
# print(botIndices)



# ACTUAL:
# swarmIndices=[]
# botIndices = []
# for swarm in range(c.numberOfSwarms):
#     swarmIndices.append(swarm)
#     for bot in range(c.botsPerSwarm):
#         botIndices.append(bot)
#         # print(f"{swarm}:{bot}")
# print(swarmIndices)
# print(botIndices)


numberOfSwarms = 10
botsPerSwarm = 10


# MODIFIED
swarmIndices = [j for j in range(numberOfSwarms)]      #    this actually makes sense. Presumably correct.
botIndices = [j for j in range(numberOfSwarms) for i in range(botsPerSwarm)]                                          #   this also seems to make sense. 
for swarm in swarmIndices:
    for bot in botIndices:
        print(f"{swarm}:{bot}")





'''
TO DO:

- Figure out swarm and bot numbers to pass in for case1, case2, case3
X How will the program know which position to run? We need to pass in overallBot using sys.argv and have the position rely on this. We can call overallBot % 10 the "position ID"
X Now, pass in overallBot using the playbackSwarms.py so we can play back bots with correct positions. 



I want to pass in the correct number and whatnot, but then I need a way to decide specifically which bo

'''
