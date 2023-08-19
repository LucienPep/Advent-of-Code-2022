#Advent Day 06
with open("SignalInput.txt") as f:
    signalData = f.read()

for i in range(0, len(signalData)):
    tempList = []
    tempSet = set()
    for x in range(0, 4):
        tempList.append(signalData[i + x])
    answer = any(char in tempSet or tempSet.add(char) for char in tempList)
    
    if answer == False:
        print(tempList)
        print(i + 4)
        break

for i in range(0, len(signalData)):
    tempList = []
    tempSet = set()
    for x in range(0, 14):
        tempList.append(signalData[i + x])
    answer = any(char in tempSet or tempSet.add(char) for char in tempList)
    
    if answer == False:
        print(tempList)
        print(i + 14)
        break