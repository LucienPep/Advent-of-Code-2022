#Advent Day 05
#Part 1
with open("CrateData.txt") as f:
    crateData = [i.strip() for i in f.readlines()]

print(crateData)