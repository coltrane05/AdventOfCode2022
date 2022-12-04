with open("Day 3/Rucksacks.txt", 'r') as rucksacks:
    finalScore = 0
    line1 = "0"
    line2 = "0"
    line3 = "0"

    while line1 != "":
        line1 = rucksacks.readline()
        line2 = rucksacks.readline()
        line3 = rucksacks.readline()
        for letter in line1:
            if line2.find(letter) != -1:
                if line3.find(letter) != -1:
                    index = line1.find(letter)
                    if line1[index].isupper():
                        finalScore += ord(letter) - ord('A') + 27
                    else:
                        finalScore += ord(letter) - ord('a') + 1
                    break

    print(finalScore)            
    

        

    # for line in rucksacks:
    #     first = line[0:len(line)//2]
    #     second = line[len(line)//2: len(line)]
    #     for letter in first:
    #         if second.find(letter) != -1:
    #             index = first.find(letter)
    #             if first[index].isupper():
    #                 finalScore += ord(letter) - ord('A') + 27
    #             else:
    #                 finalScore += ord(letter) - ord('a') + 1
    #             break

    print(finalScore)