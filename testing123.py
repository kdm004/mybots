import os
import glob

numberOfFiles = 3
number = 1
for number in range(3,9+3,3):
    for i in range(number):
        if os.path.exists("brain"+ str(number) + ".nndf"): 
            number +=1

#print(number)



# we should count the number of files present.
# number of Files 
#if os.path.exists("brain"+(str(number))+".nndf"):


#fileList1 = os.listdir(path='brain*.nndf')
#print(fileList1)

filesList = len(glob.glob("brain*.nndf"))
print(filesList)
