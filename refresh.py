import os

# Write 'python3 refresh.py' in terminal to delete the following files:


os.system("rm brainFiles/brain*.nndf")
os.system("rm bodyFiles/body*.urdf")
os.system("rm bestBrains.txt")
#os.system("rm allIDs.txt")


os.system("rm emptyEnv_fitnesses.txt")
os.system("rm obstacleEnv_fitnesses.txt")


os.system("rm fitness*.txt")
os.system("rm LegSizesTemp.txt")
os.system("rm WeightsTemp.txt")

os.system("rm weightsAndLegs.txt")
os.system("rm weightsFiles/weights*.txt")

os.system("rm testingBoth.txt")



# should this also refresh the pickled file?


