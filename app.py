import csv

def test():
    data = [["Taha", "Haxa"]]
    saveArray(data)
    print("Finished")

def saveArray(data):
    with open('database.csv', 'w+') as fh:
        csv.writer(fh, delimiter=",").writerows(data)

def main():
    inputCount = 4
    for i in range(1, inputCount + 1):
        inputTitle = int(input("Enter input title: ")) # 1400, 1397
        studentCount = int(input("Enter student count for the {}".format(inputTitle)))
        for p in range(1, studentCount + 1):
            name = input("Enter stduent #{}'s name: ".format(p))
            sex = input("Enter {}'s gender: ".format(name)) 
            studentNumber = int(input("Enter student number for {}".format(name)))

if __name__ == '__main__': test()
