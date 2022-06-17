import csv
from os import name, system

def main():
    allowedInputTitles = range(1397, 1401)
    yearSubjectCount = {
            1400: 4,
            1399: 5,
            1398: 5,
            1397: 4,
    }
    csvHeader = [["Entrance","Class Variance" ,"Class Average", "First Student", "Second Student", "Third Student", "Failed"]]
    inputCount = 4
    studentData = {}
    for i in range(1, inputCount + 1):
        inputTitle = None

        while True:
            inputTitle = int(input("Enter input title: ")) 
            if inputTitle in allowedInputTitles: break

        studentData[inputTitle] = []
        studentCount = int(input("Enter student count for the {}: ".format(inputTitle)))

        for p in range(1, studentCount + 1):
            scores = []
            studentNumber = int(input("\tEnter student number #{}: ".format(p)))
            sex = input("\tEnter {}'s gender: ".format(studentNumber)) 

            for z in range(1, yearSubjectCount[inputTitle] + 1):
                factor = int(input("\t\tEnter subject #{}'s factor: ".format(z)))
                score = float(input("\t\tEnter subject #{}'s score: ".format(z)))
                scores.append(str(score) + ":" + str(factor)) 
            average = calculateAverageOfStudent(scores)
            studentData[inputTitle].append([studentNumber, sex, scores, average])
            sorted(studentData[inputTitle], key=lambda x: x[3], reverse=True)
        clearScreen()
        print(studentData)

def saveArray(data):
    with open('database.csv', 'w+') as fh:
        csv.writer(fh, delimiter=",").writerows(data)

def clearScreen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def calculateAverageOfStudent(scoresAndFactors):
    scoreSum = 0
    factorSum = 0
    for scoreString in scoresAndFactors:
        scoreString = scoreString.split(":")
        score = float(scoreString[0])
        factor = int(scoreString[1])
        scoreSum += score * factor
        factorSum += factor
    return scoreSum / factorSum 

if __name__ == '__main__': main()
