# import os
# import time
# import glob 
# import constants as c
# import nonChampDeleter as NCD
# import sys

# commandLineArg = sys.argv # [emptyWrapper.py, continue]

# for i in range(350):
#     os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot
#     #time.sleep(zzz*2)


# NCD.Delete_Remaining()





import os
import time
import glob 
import constants as c
import nonChampDeleter as NCD
import sys


commandLineArg = sys.argv # [emptyWrapper.py, continue]



if commandLineArg[1] == 'none':
    if os.path.exists('bestBrains.txt'):
        fp = open('bestBrains.txt', 'r') 
        lines = fp.readlines()
        cleanLines = []
        for entry in lines:
            cleanLines.append(entry.replace('\n',''))
        cleanLines = list(map(int, cleanLines))
        fp.close()

        for i in range(len(cleanLines) ,700):
            os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot
            #time.sleep(zzz*2)


    else:
        for i in range(700):
            os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot
            #time.sleep(zzz*2)
            print('hello world')



if commandLineArg[1] == 'continue':
    for i in range(700):
        os.system('python3 search.py' + ' ' + str(commandLineArg[1]) + ' ' + str(i)) # i = overallBot
        #time.sleep(zzz*2)


