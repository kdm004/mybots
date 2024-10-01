def Get_Familiar_Fits():
    with open("familiarFits.txt", "r") as f:
        familiarFits = [float(line.strip()) for line in f]
    return familiarFits

test = Get_Familiar_Fits()
print(test)