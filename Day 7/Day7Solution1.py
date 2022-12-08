

# myList = []
# myList.append('a')
# myList.append('b')
# myList.append('c')
# myNewList = myList[1:2]
# print(myNewList)


with open("Day 7/FileSystem.txt", 'r') as fileSystem:
    currentDirectory = ""
    directoryStack = []
    currentDirSize = 0
    directoryDict = {"/": 0}
    for line in fileSystem:
        if line[0] == "$":
            if line[2] == "c":
                if line[5] == ".":
                    directoryDict[currentDirectory] = currentDirSize
                    directoryStack.pop()
                    currentDirectory = directoryStack[len(directoryStack) - 1]
                    currentDirSize = directoryDict[currentDirectory] + currentDirSize
                else:
                    currentDirectory = line[5:len(line)].split()[0]
                    directoryStack.append(currentDirectory)
                    # TODO: add Dictionary to Dictionary
        elif line[0:3] == "dir":
            directoryDict[line[4: len(line)].split()[0]] = 0
            print(line[4: len(line)])
        else:
            parsed = line.split()
            print(int(parsed[0]))