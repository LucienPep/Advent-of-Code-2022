#Advent Day 05
#Part 1
import copy
with open("CrateData.txt") as f:
    crateData = [i.strip() for i in f.readlines()]

stackData = [
    ["F", "D", "B", "Z", "T", "J", "R", "N"],
    ["R", "S", "N", "J", "H"],
    ["C", "R", "N", "J", "G", "Z", "F", "Q"],
    ["F", "V", "N", "G", "R", "T", "Q"],
    ["L", "T", "Q", "F"],
    ["Q", "C", "W", "Z", "B", "R", "G", "N"],
    ["F", "C", "L", "S", "N", "H", "M"],
    ["D", "N", "Q", "M", "T", "J"],
    ["P", "G", "S"]
]
stackDataCopy = copy.deepcopy(stackData)

def partOne(stacks):
    for line in range(10, 513):
        move, stack = crateData[line].split(" from ")
        stack = [int(i) for i in stack.split(" to ")]
        move = move.removeprefix("move ")

        for i in range(0, int(move)):
            x = stacks[int(stack[0]) - 1].pop()
            stacks[int(stack[1]) - 1].append(x)
    print("Part01")
    for line in stacks:
        print(line[-1])

#Part02
def partTwo(stacks):
    for line in range(10, 513):
        z = []
        move, stack = crateData[line].split(" from ")
        stack = [int(i) for i in stack.split(" to ")]
        move = move.removeprefix("move ")

        for i in range(0, int(move)):
            x = [stacks[int(stack[0]) - 1].pop()]
            z.append(x[0])

        for i in range(0, int(move)):
            x = z.pop()
            stacks[int(stack[1]) - 1].append(x)
    print("Part02")
    for line in stacks:
        print(line[-1])

partOne(stackData)
partTwo(stackDataCopy)