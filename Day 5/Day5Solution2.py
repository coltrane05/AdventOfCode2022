with open("Day 5/Procedure.txt", 'r') as procedure:
    stacks = []
    
    for i in range(8):
        stacks.append([])
        for j in range(0, 9*4, 4):
            interest = procedure.read(4).split()
            if len(interest) > 0:
                stacks[i].append(interest[0])
            else:
                stacks[i].append(None)

    tempStacks = []
    for j in range(9):
        tempStacks.append([])
        for i in range(7, -1, -1):
            if stacks[i][j] != None:
                tempStacks[j].append(stacks[i][j])
    stacks = tempStacks
    
    procedure.readline()
    procedure.readline()


    for line in procedure:
        splitLine = line.split()
        numToMove = int(splitLine[1])
        stackFrom = int(splitLine[3]) - 1
        stackTo = int(splitLine[5]) - 1
        subStackToMove = stacks[stackFrom][len(stacks[stackFrom]) - numToMove: len(stacks[stackFrom])]
        stacks[stackTo] = stacks[stackTo] + subStackToMove
        for i in range(numToMove):
            stacks[stackFrom].pop()
        
    for i in range(9):
        print(stacks[i][len(stacks[i]) - 1]) 