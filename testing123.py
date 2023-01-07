import numpy as np
import random
import constants as c
import sys
import pickle
import os






if sys.argv[1] == '-continue':
    with open('testing123.txt', 'rb') as pickledFile:
        loadedMatrixList = pickle.load(pickledFile)
        print(loadedMatrixList[1])


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
    for i in range(7):
        weights[9][i] = random.uniform(.5,1.5)
    weightsList.append(weights)
    print(weights)

    # Overwrite pickledFile with new weightsList
    with open("testing123.txt", "wb") as pickledFile:       
        pickle.dump(weightsList, pickledFile) 













