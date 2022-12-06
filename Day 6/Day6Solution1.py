

with open("Day 6/Datastream.txt", 'r') as datastream:
    dataString = datastream.read() 
    for i in range(len(dataString)):
        dataDict = {}
        for j in range(4):
            dataDict[dataString[i + j]] = "Value"
        if len(dataDict) == 4:
            print(dataDict)
            print("good")
            print(i + 4)
            break
        else:
            print("bad")    
        

            