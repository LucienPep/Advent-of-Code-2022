#Advent Day 06
with open("SignalInput.txt") as f:
    signalData = f.read()

def signalDecipher(x):
    for i in range(len(signalData)):
        tempList, tempSet = [], set()
        for z in range(x):
            tempList.append(signalData[i + z])

        answer = any(char in tempSet or tempSet.add(char) for char in tempList)
        if answer == False:
            print(i + x)
            break

print("Part01")
signalDecipher(4)
print("Part02")
signalDecipher(14)