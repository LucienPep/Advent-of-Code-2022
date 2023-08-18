#Advent Day 05
import copy
with open("CrateData.txt") as f:
    crateData = [i.strip() for i in f.readlines()]

stackData = []
for i in range(1, 34, 4):
    try:
        dataTemp = []
        for x in range(7, -1, -1):
            if crateData[x][i] == ' ':
                break
            else:
                dataTemp.append(crateData[x][i])
        stackData.append(dataTemp)
    except:
        stackData.append(dataTemp)
        continue

stackDataCopy = copy.deepcopy(stackData)

def finalCrateStack(stacks, key):
    print("Part0" + str(key))
    finalOutput = ''

    for line in range(10, 513):
        move, stack = crateData[line].split(" from ")
        stack = [int(i) for i in stack.split(" to ")]
        move = move.removeprefix("move ")
    
        if key == 1:
            for _ in range(0, int(move)):
                x = stacks[int(stack[0]) - 1].pop()
                stacks[int(stack[1]) - 1].append(x)
        
        if key == 2:
            z = []
            for _ in range(0, int(move)):
                x = [stacks[int(stack[0]) - 1].pop()]
                z.append(x[0])

            for _ in range(0, int(move)):
                x = z.pop()
                stacks[int(stack[1]) - 1].append(x)

    for line in stacks:
        finalOutput += line[-1]
    print(finalOutput)

finalCrateStack(stackData, 1)
finalCrateStack(stackDataCopy, 2)