#Advent Day 04
#Part 1
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "cleaningInput.txt") as f:
#with open("cleaningInput.txt", "r") as f:
    cleaningData = f.readlines()
    
totalScore = 0
for line in cleaningData: 
    lineRange = []
    i = line.split(",")
    firstValue = i[0].split("-")[0]
    secondValue = i[0].split("-")[1]
    thirdValue = i[1].split("-")[0]
    fourthValue = i[1].split("-")[1]
    
    for x in range(int(firstValue), int(secondValue) + 1):
        lineRange.append(x)

    if int(thirdValue) in lineRange and int(fourthValue) in lineRange:
        totalScore += 1
    else:
        lineRange = []
        for x in range(int(thirdValue), int(fourthValue) + 1):
            lineRange.append(x)

        if int(firstValue) in lineRange and int(secondValue) in lineRange:
            totalScore += 1
        
print(totalScore)

#Part 02

totalScore = 0
for line in cleaningData: 
    lineRange = []
    i = line.split(",")
    firstValue = i[0].split("-")[0]
    secondValue = i[0].split("-")[1]
    thirdValue = i[1].split("-")[0]
    fourthValue = i[1].split("-")[1]
    
    for x in range(int(firstValue), int(secondValue) + 1):
        lineRange.append(x)

    if int(thirdValue) in lineRange or int(fourthValue) in lineRange:
        totalScore += 1
    else:
        lineRange = []
        for x in range(int(thirdValue), int(fourthValue) + 1):
            lineRange.append(x)

        if int(firstValue) in lineRange or int(secondValue) in lineRange:
            totalScore += 1
        
print(totalScore)