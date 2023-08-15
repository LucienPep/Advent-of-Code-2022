#Advent Day 02
#Part 1
with open("RockPaperScissorsInput.txt", "r") as rockPaperScissorsFile:
    gameData = rockPaperScissorsFile.readlines()
    totalScore = 0

    configurations = {
        "A" : {
            "X": 4,
            "Y": 8,
            "Z": 3
        },
        "B" : {
            "X": 1,
            "Y": 5,
            "Z": 9
        },
        "C" : {
            "X": 7,
            "Y": 2,
            "Z": 6
        }
    }

    for line in gameData:
        totalScore += configurations[line[0]][line[2]]

    print(totalScore)

    #Part 2
    TotalScore = 0

    Configurations = {
        "A" : {
            "X": 3,
            "Y": 4,
            "Z": 8
        },
        "B" : {
            "X": 1,
            "Y": 5,
            "Z": 9
        },
        "C" : {
            "X": 2,
            "Y": 6,
            "Z": 7
        }
    }
    for line in gameData:
        TotalScore += Configurations[line[0]][line[2]]

    print(TotalScore)