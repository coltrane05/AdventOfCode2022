

with open("ElfBags.txt", "r") as elfBagsFile:
    elfTotal = 0
    maxCalories = 0
    elfList = []
    for line in elfBagsFile:
        if line == "\n":
            elfList.append(elfTotal)
            if elfTotal > maxCalories:
                maxCalories = elfTotal
            elfTotal = 0
        else:
            elfTotal += int(line)
    
    finalSum = 0
    for i in range(3):
        finalSum += elfList.pop(elfList.index(max(elfList)))

    print(finalSum)


