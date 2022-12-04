
with open("Day 3/Rucksacks.txt", 'r') as rucksacks:
    finalScore = 0
    for line in rucksacks:
        first = line[0:len(line)//2]
        second = line[len(line)//2: len(line)]
        for letter in first:
            if second.find(letter) != -1:
                index = first.find(letter)
                if first[index].isupper():
                    finalScore += ord(letter) - ord('A') + 27
                else:
                    finalScore += ord(letter) - ord('a') + 1
                break

    print(finalScore)





