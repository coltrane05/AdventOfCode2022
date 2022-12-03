from enum import Enum

class RockPaperScissors(Enum):
    X = 0
    Y = 3
    Z = 6
    AX = 3
    BX = 1
    CX = 2
    AY = 1
    BY = 2
    CY = 3
    AZ = 2
    BZ = 3
    CZ = 1
        


with open("Day 2/StrategyGuide.txt", 'r') as strategyGuide:
    finalScore = 0
    currentMatchup = ""
    for line in strategyGuide:
        currentMatchup = line[0] + line[2]
        finalScore += RockPaperScissors[currentMatchup].value + RockPaperScissors[line[2]].value
    print(finalScore)