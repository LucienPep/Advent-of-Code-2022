#Advent Day 01
with open("elfInput.txt", "r") as elfCalorieFile:
    calorieData = elfCalorieFile.readlines()
    newCalorieData = []
    tempTotal = 0
    
    for line in calorieData:
        if line.isspace():
            newCalorieData.append(tempTotal)
            tempTotal = 0    
        else:
            tempTotal += int(line)        
    
    tempMax = 0
    newCalorieData.sort()
    
    for number in range(-3, 0):
        print(newCalorieData[number])
        tempMax += newCalorieData[number]
        
    print(tempMax)