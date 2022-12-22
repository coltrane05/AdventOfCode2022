with open("Day 8/Grid.txt", 'r') as data:
    grid = []
    lineIndex = 0
    for line in data:
        grid.append([])
        line = line.split()[0]
        for number in line:
            grid[lineIndex].append(int(number))
        lineIndex += 1

    maxViewScore = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            viewScoreLeft = 0
            viewScoreRight = 0
            viewScoreUp = 0
            viewScoreDown = 0
            for k in range(j - 1, -1, -1):
                viewScoreLeft += 1
                if grid[i][k] >= grid[i][j]:
                    break
            for k in range(j + 1, len(grid[i])):
                viewScoreRight += 1
                if grid[i][k] >= grid[i][j]:
                    break
            for k in range(i - 1, -1, -1):
                viewScoreUp += 1
                if grid[k][j] >= grid[i][j]:
                    break
            for k in range(i + 1, len(grid)):
                viewScoreDown += 1
                if grid[k][j] >= grid[i][j]:
                    break
            
            totalViewScore = viewScoreLeft * viewScoreRight * viewScoreUp * viewScoreDown
            
            
            if totalViewScore > maxViewScore:
                maxViewScore = totalViewScore
                
    print(maxViewScore)