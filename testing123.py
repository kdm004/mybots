import numpy as np
import random
import constants as c
import sys
import pickle
import os
import testing789 as TESTING789





if len(sys.argv) > 1:
    if sys.argv[1] == '-continue':
        with open('testing123.txt', 'rb') as pickledFile:
            loadedMatrixList = pickle.load(pickledFile)
            print(loadedMatrixList[1])
            print(sys.argv)


else:

    # if pickledFile doesn't exist, initialize empty weightsList
    weightsList = []

    # if pickledFile exists, open it and load weightsList
    if os.path.exists('testing123.txt'):
        with open("testing123.txt", "rb") as pickledFile:
            # Load weightsList from pickledFile
            weightsList = pickle.load(pickledFile)

    # If pickledFile is empty, initialize weightsList 
    if len(weightsList) == 0:
        weightsList = []

    # Add a new matrix to weightsList
    weights = np.random.rand(9+1, 8)                                                  
    for i in range(8): # 7 to 8
        weights[9][i] = random.uniform(.5,1.5)
    weightsList.append(weights)
    print(weights)
    print(sys.argv)

    # Overwrite pickledFile with new weightsList
    with open("testing123.txt", "wb") as pickledFile:       
        pickle.dump(weightsList, pickledFile) 













