import constants as c

# print(c.botPositions[0])

# def dummy_func(x, y, z=1):
#     print(x)
#     print(y)
#     print(z)

# test1 = dummy_func(*c.botPositions[0])

numberOfSwarms = 20
botsPerSwarm = 10
# swarmType = 'case1'
# if c.swarmType == 'case1':  
#     swarmIndices = [j for j in range(numberOfSwarms)]                                         # seems correct
#     botIndices = [j for j in range(numberOfSwarms) for i in range(botsPerSwarm)]            # seems correct    
#     print(botIndices)



# for i in range(numberOfSwarms):         # seems correct but we would need to use "break" at some point
#     batch_number = i // botsPerSwarm
#     print(batch_number)

# for i in range(numberOfSwarms):
#     swarm_number = i % botsPerSwarm
#     print(swarm_number)


# for batch_number in range(numberOfSwarms):  # Outer loop for batches
#     for _ in range(botsPerSwarm):  # Inner loop for each number in the batch
#         print(batch_number)









# for i in range(numberOfSwarms * botsPerSwarm):
#     batch_number = i // botsPerSwarm
#     result = batch_number % botsPerSwarm
#     print(result)


def Get_Bot_Numbers(numberOfBots):
    for i in range(numberOfBots):
        batch_number = i // botsPerSwarm
        result = batch_number % botsPerSwarm
        return result
    






    
def Get_Bot_Number(overallBot):
    batch_number = overallBot // botsPerSwarm
    result = batch_number % botsPerSwarm
    return result


def Get_Swarm_Number(overallBot):
    batch_size = botsPerSwarm**2
    result = overallBot // batch_size
    return result


overallBot = 0
for swarm in range(numberOfSwarms):
    for bot in range(botsPerSwarm):
        botNumber = Get_Bot_Number(overallBot)
        swarmNumber = Get_Swarm_Number(overallBot)
        print(f"swarm {swarmNumber} bot {botNumber}")
        overallBot += 1



        # if overallBot == numberOfSwarms * botsPerSwarm:
        #     break


# for i in range(numberOfSwarms*botsPerSwarm):
#     batch_number = i // botsPerSwarm
#     result = batch_number % botsPerSwarm
#     print(result)