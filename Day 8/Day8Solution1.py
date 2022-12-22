
with open("Day 8/Grid.txt", 'r') as data:
    grid = []
    lineIndex = 0
    for line in data:
        grid.append([])
        line = line.split()[0]
        for number in line:
            grid[lineIndex].append(int(number))
        lineIndex += 1
    
    visibleTrees = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            visibleLeft = True
            visibleRight = True
            visibleUp = True
            visibleDown = True
            for k in range(j - 1, -1, -1):
                # if i == 1 and j == 2:
                #     print(grid[i][k])
                if grid[i][k] >= grid[i][j]:
                    visibleLeft = False
            for k in range(j + 1, len(grid[i])):
                if i == 1 and j == 1:
                    print(grid[i][k])
                if grid[i][k] >= grid[i][j]:
                    visibleRight = False
            for k in range(i - 1, -1, -1):
                # if i == len(grid) - 2 and j == 1:
                #     print(grid[k][j])
                if grid[k][j] >= grid[i][j]:
                    visibleUp = False
            for k in range(i + 1, len(grid)):
                # if i == 1 and j == 1:
                #     print(grid[k][j])
                if grid[k][j] >= grid[i][j]:
                    visibleDown = False
            
            if visibleLeft or visibleRight or visibleUp or visibleDown:
                visibleTrees += 1
            

    visibleTrees += (len(grid) - 1) * 2 + (len(grid[0]) - 1) * 2
            
    print(visibleTrees)

