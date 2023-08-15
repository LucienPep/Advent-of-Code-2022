#Advent Day 03
#Part 1
with open("RucksackData.txt", "r") as rucksackData:
    sackData = rucksackData.readlines()
    finalDataList = []

    for line in sackData:
        lineLength = len(line)
        first = slice(0,lineLength//2)      
        second = slice(lineLength//2, lineLength)
        firstHalf = line[first]
        secondHalf = line[second]
        firstSet = set()

        for char in firstHalf:
            firstSet.add(char)
        
        for char in secondHalf:
            if char in firstSet:
                finalDataList.append(char)
                break
    
    totalValue = 0

    characterDictionary = {}
    charInput = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charList = list(charInput)

    for char in finalDataList:
        charValue = (charList.index(char) + 1)
        totalValue += charValue
    
    print(totalValue)
    print("banana")
            
    
            

