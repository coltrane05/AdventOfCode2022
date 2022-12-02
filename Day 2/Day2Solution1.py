from enum import Enum

class RockPaperScissors(Enum):
    X = 1
    Y = 2
    Z = 3
    A = 1
    B = 2
    C = 3

    def __gt__(self, other):
        if (self == self.X or self == self.A) and (other == other.C or other == other.Z):
            return True
        elif (self == self.Z or self == self.C) and (other == other.Y or other == other.B):
            return True
        elif (self == self.B or self == self.Y) and (other == other.A or other == other.X):
            return True
        else:
            return False
        
    #def __lt__(self, other):


with open("StrategyGuide.txt", 'r') as strategyGuide:
    finalScore = 0
    for line in strategyGuide:
        finalScore += RockPaperScissors[line[2]].value
        isGreater = RockPaperScissors[line[0]] > RockPaperScissors[line[2]]
        print(isGreater)
        


