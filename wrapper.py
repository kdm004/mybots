import os
import time
import parallelHillClimber as phc


zzz = 1


for fileNumber in range(50):
    os.system("python3 search.py")
    time.sleep(zzz)
    print("HELLO DATA",fileNumber)
    time.sleep(zzz)

phc.Results()




