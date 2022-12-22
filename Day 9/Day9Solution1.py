from enum import Enum

class Motion(Enum):
    R = [0, 1]
    L = [0, -1]
    U = [1, 0]
    D = [-1, 0]

def moveRight(knot):
    knot[1] += 1
    return knot

def moveLeft(knot):
    knot[1] += -1
    return knot

def moveUp(knot):
    knot[0] += 1
    return knot

def moveDown(knot):
    knot[0] += -1
    return knot

def isTouching(head, tail):
    if abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1:
        return True

def moveTail(head, tail):
    if head[0] == tail[0] and head[1] == tail[1]:
        return tail
    if head[0] == tail[0] and head[1] - tail[1] > 1:
        tail = moveRight(tail)
        return tail
    if head[0] == tail[0] and head[1] - tail[1] < -1:
        tail = moveLeft(tail)
        return tail
    if head[1] == tail[1] and head[0] - tail[0] > 1:
        tail = moveUp(tail)
        return tail
    if head[1] == tail[1] and head[0] - tail[0] < -1:
        tail = moveDown(tail)
        return tail
    if (head[0] - tail[0] > 0 and head[1] - tail[1] > 0) and not isTouching(head, tail):
        tail = moveUp(tail)
        tail = moveRight(tail)
        return tail
    if (head[0] - tail[0] > 0 and head[1] - tail[1] < 0) and not isTouching(head, tail):
        tail = moveUp(tail)
        tail = moveLeft(tail)
        return tail
    if (head[0] - tail[0] < 0 and head[1] - tail[1] > 0) and not isTouching(head, tail):
        tail = moveDown(tail)
        tail = moveRight(tail)
        return tail
    if (head[0] - tail[0] < 0 and head[1] - tail[1] < 0) and not isTouching(head, tail):
        tail = moveDown(tail)
        tail = moveLeft(tail)
        return tail
    
    return tail

with open("Day 9/motions.txt") as motions:
    headIndex = [0, 0]
    tailIndex = [0, 0]
    headIndexDict = {str(headIndex) : 1}
    tailIndexDict = {str(tailIndex) : 1}
    for line in motions:
        motion = line.split()
        for i in range(int(motion[1])):
            headIndex[0] += Motion[motion[0]].value[0]
            headIndex[1] += Motion[motion[0]].value[1]
            if str(headIndex) in headIndexDict:
                headIndexDict[str(headIndex)] += 1
            else:
                headIndexDict[str(headIndex)] = 1

            tailIndex = moveTail(headIndex, tailIndex)
            if str(tailIndex) in tailIndexDict:
                tailIndexDict[str(tailIndex)] += 1
            else:
                tailIndexDict[str(tailIndex)] = 1
            #print(tailIndex)

    print(len(tailIndexDict))