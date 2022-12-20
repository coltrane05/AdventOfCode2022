

with open("Day 10/program.txt", 'r') as program:
    cycle = 1
    register = 1
    signalStrengthTotal = 0
    for line in program:
        command = line.split()
        if command[0] == "noop":
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                print(cycle, register)
                signalStrengthTotal += (cycle * register)
                print(signalStrengthTotal)
            cycle += 1
        else:
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                print(cycle, register)
                signalStrengthTotal += (cycle * register)
                print(signalStrengthTotal)
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                print(cycle, register)
                signalStrengthTotal += (cycle * register)
                print(signalStrengthTotal)
            cycle += 1
            register += int(command[1])
    
    print(cycle)
    print(signalStrengthTotal)