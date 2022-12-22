

# myList = []
# myList.append('a')
# myList.append('b')
# myList.append('c')
# myNewList = myList[1:2]
# print(myNewList)


import string
with open("Day 7/FileSystem.txt", 'r') as fileSystem:
    currentDirectory = "/"
    directoryStack = []
    currentDirSize = 0
    directoryDict = {"/": 0}
    finalTotal = 0
    finalTotal2 = 0
    duplicateDirCount = 1
    for line in fileSystem:
        if line[0] == "$":
            if line[2] == "c":
                if line[5:7] == "..":
                    directoryDict[currentDirectory] = currentDirSize
                    if currentDirSize <= 100000:
                        finalTotal += currentDirSize
                        # print("added ", currentDirectory, ": ", currentDirSize)
                    directoryStack.pop()
                    currentDirectory = directoryStack[len(directoryStack) - 1]
                    currentDirSize += directoryDict[currentDirectory]
                else:
                    directoryDict[currentDirectory] = currentDirSize
                    
                    currentDirectory = line[5:len(line)].split()[0]
                    if currentDirectory != "/" and currentDirectory in directoryDict:
                        currentDirectory = currentDirectory + str(duplicateDirCount)
                        duplicateDirCount += 1
                        directoryDict[currentDirectory] = 0
                    else:
                        directoryDict[currentDirectory] = 0
                    directoryStack.append(currentDirectory)
                    currentDirSize = directoryDict[currentDirectory]
        elif line[0:3] == "dir":
            print("new dir")
        else:
            parsed = line.split()
            currentDirSize += int(parsed[0])
    
    
    while len(directoryStack) > 1:
        directoryDict[currentDirectory] = currentDirSize
        if currentDirSize <= 100000:
            finalTotal += currentDirSize
        directoryStack.pop()
        currentDirectory = directoryStack[len(directoryStack) - 1]
        currentDirSize += directoryDict[currentDirectory]
    directoryDict[currentDirectory] = currentDirSize

    minSize = 70000000
    targetSize = directoryDict["/"] - 40000000 
    for key in directoryDict: 
        if directoryDict[key] >= targetSize and minSize > directoryDict[key]:
            minSize = directoryDict[key]

    print(directoryDict)
    print(duplicateDirCount)
    print(finalTotal)
    print(finalTotal2)
    print(minSize)