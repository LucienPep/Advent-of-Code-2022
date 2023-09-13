#Advent Day 07
with open("SpaceInput.txt") as f:
    driveData = [i.strip() for i in f.readlines()]

drive = {}
folderName = ''
folderValue = 0
for line in driveData:
    lineValues = line.split(' ')
    if lineValues[1] == 'cd' and lineValues[2] != '..':
        drive[folderName] = folderValue
        folderValue = 0
        folderName = lineValues[2]
        drive[folderName] = {}
    elif lineValues[0] not in ['$', 'dir']:
        folderValue += int(lineValues[0])   

drive[folderName] = folderValue
#print(drive['wzvvggdp'])   

totals = {}
tempTotal = 0
for line in driveData:
    lineValues = line.split(' ')
    if lineValues[1] == 'cd' and lineValues[2] != '..':
        folderName = lineValues[2]
        totals[folderName] = {tempTotal}
        tempTotal = 0
    elif lineValues[0] == 'dir':
        tempTotal += int(drive[lineValues[1]])

print(totals)