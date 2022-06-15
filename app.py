import csv
from os import name, system

def main():
    yearSubjectCount = {
            1400: 4,
            1399: 5,
            1398: 5,
            1397: 4,
    }
    csvHeader = [["Vorudi","Class Variance" ,"Class Average", "First Student", "Second Student", "Third Student", "Failed"]]
    inputCount = 4
    studentData = {}
    for i in range(1, inputCount + 1):
        inputTitle = int(input("Enter input title: ")) # 1400, 1397
        studentData[inputTitle] = []
        studentCount = int(input("Enter student count for the {}: ".format(inputTitle)))
        for p in range(1, studentCount + 1):
            scores = [] # [ "13:3", [20, 3] ]
            studentNumber = int(input("Enter student number #{}: ".format(p)))
            sex = input("Enter {}'s gender: ".format(studentNumber)) 

            for z in range(1, yearSubjectCount[inputTitle] + 1):
                factor = int(input("Enter subject #{}'s factor: ".format(z)))
                score = float(input("Enter subject #{}'s score: ".format(z)))
                scores.append(str(score) + ":" + str(factor)) 

            studentData[inputTitle].append([studentNumber, sex, scores])
        clearScreen()
            
def saveArray(data):
    with open('database.csv', 'w+') as fh:
        csv.writer(fh, delimiter=",").writerows(data)

def clearScreen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
        
if __name__ == '__main__': main()
