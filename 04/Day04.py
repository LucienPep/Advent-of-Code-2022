#Advent Day 04
#Part 1
with open("cleaningInput.txt") as f:
    cleaningData = [i.strip() for i in f.readlines()]
    
totalScore = 0
for line in cleaningData:
    left, right = line.split(",")
    left = [int(i) for i in left.split("-")]
    right = [int(i) for i in right.split("-")]

    leftRange = [i for i in range(left[0], left[1] + 1)]
    rightRange = [i for i in range(right[0], right[1] + 1)]

    if left[0] in rightRange and left[1] in rightRange:
        totalScore += 1
    elif right[0] in leftRange and right[1] in leftRange:
        totalScore += 1
        
print(totalScore)

#Part 02
totalScore = 0
for line in cleaningData:
    left, right = line.split(",")
    left = [int(i) for i in left.split("-")]
    right = [int(i) for i in right.split("-")]

    leftRange = [i for i in range(left[0], left[1] + 1)]
    rightRange = [i for i in range(right[0], right[1] + 1)]

    if left[0] in rightRange or left[1] in rightRange:
        totalScore += 1
    elif right[0] in leftRange or right[1] in leftRange:
        totalScore += 1
        
print(totalScore)