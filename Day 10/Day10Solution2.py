
with open("Day 10/program.txt", 'r') as program:
    cycle = 1
    pixelPosition = 0
    register = 1
    signalStrengthTotal = 0
    currentLine = ""
    for line in program:
        command = line.split()
        if command[0] == "noop":
            if register - 1 <= pixelPosition <= register + 1:
                currentLine = currentLine + "#"
            else:
                currentLine = currentLine + "."
            cycle += 1
            pixelPosition += 1
            if len(currentLine) == 40:
                print(currentLine)
                currentLine = ""
                pixelPosition = 0
        else:
            if register - 1 <= pixelPosition <= register + 1:
                currentLine = currentLine + "#"
            else:
                currentLine = currentLine + "."
            cycle += 1
            pixelPosition += 1
            if len(currentLine) == 40:
                print(currentLine)
                currentLine = ""
                pixelPosition = 0

            if register - 1 <= pixelPosition <= register + 1:
                currentLine = currentLine + "#"
            else:
                currentLine = currentLine + "."
            cycle += 1
            pixelPosition += 1
            if len(currentLine) == 40:
                print(currentLine)
                currentLine = ""
                pixelPosition = 0
            register += int(command[1])
    
    print(cycle)
    print(signalStrengthTotal)