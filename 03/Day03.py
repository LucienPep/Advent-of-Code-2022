#Advent Day 03
#Part 1
with open("RucksackData.txt", "r") as f:
    sackData = f.readlines()
    commonElements = []

    for line in sackData:
        first = line[: len(line) // 2]
        second = line[len(line) // 2 :]
        commonElements += set(first).intersection(second)
    
totalValue = 0
for letter in commonElements:
    totalValue += ord(letter) - (96 if letter.islower() else 38)

print(totalValue)

#Part 2
commonElements = []
for line in sackData:
    i = sackData.index(line) - 1
    if i % 3 == 0:
        commonElements += set(sackData[i]).intersection(sackData[i + 1], sackData[i + 2])
        
totalValue = 0
for letter in commonElements:
    i = ord(letter)
    if i != 10:
        totalValue += i - (96 if letter.islower() else 38)
        
print(totalValue)
            
            
    
            

