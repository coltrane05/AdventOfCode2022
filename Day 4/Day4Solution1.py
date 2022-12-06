
import string


with open("Day 4/Assignments.txt", 'r') as assignments:
    finalScore = 0
    for line in assignments:
        line = line.replace('-', ' ')
        line = line.replace(',', ' ')
        numbers = [eval(i) for i in line.split()]
        print(numbers)
        same = False
        if numbers[0] == numbers[2] and numbers[1] == numbers[3]:
            same = True
        
        if (numbers[0] <= numbers[2] and numbers[1] >= numbers[3]) or (numbers[0] >= numbers[2] and numbers[1] <= numbers[3]):
            finalScore += 1

    print(finalScore)

        