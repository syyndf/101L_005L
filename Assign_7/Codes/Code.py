from os.path import exists

def InputFile():
    flag = 0
    while flag == 0:
        try:
            getInputFile = input("Enter the name of the input file ==> ")
            if exists(getInputFile):
                return getInputFile
            else:
                print("Could not find file", getInputFile)
                continue
        except:
            print("Invalid input")
            continue

def MPG():
    flag = 0
    while flag == 0:
        try:
            mpg = float(input("Enter the minimum mpg ==> "))
            if mpg < 0 or mpg > 100:
                print("Please enter a number more than 0 or more than 100")
                continue
            flag = 1
            return mpg

        except:
            print("Enter a number only")
            continue


def OutputFile():
    flag = 0
    while flag == 0:
        try:
            getOutputFile = input("Enter the name of the output file ==> ")
            if exists(getOutputFile):
                return getOutputFile

            else:
                print("Could not find file", getOutputFile)
                continue
        except:
            print("Invalid input")
            continue


def read_File(txt, mpg):
    data = []
    processedData = []
    processedCars = []
    ErrorValue = []
    ErrorCar = []
    finalList = []
    Errors = []
    with open(txt, 'r') as file:
        placeholder = file.readline()
        data = file.readlines()

    for info in data:
        processedData.append(info.strip().split('\t'))

    for info in range(len(processedData)):
        try:
            if float(processedData[info][7]) > float(mpg):
                processedCars.append(processedData[info])
        except ValueError:
            ErrorValue.append(processedData[info][7])
            ErrorCar.append(processedData[info])

    if ErrorValue:
        print('')
        for cars in range(len(ErrorValue)):
            Errors.append(("Could not convert value {} for vehicle {} {} {}".format(ErrorValue[cars], ErrorCar[cars][0], ErrorCar[cars][1], ErrorCar[cars][2], ErrorCar[cars][7])))

    for cars in range(len(processedCars)):
        finalList.append(("{} {:<20}{:<40}{:>10.2f}".format(processedCars[cars][0], processedCars[cars][1], processedCars[cars][2], float(processedCars[cars][7]))))

    return finalList, Errors

def output(txt, car, error):
  if errors:
    print('')
    for error in errors:
        print(error)

  with open(txt, 'w') as file:
    for car in cars:
        file.write(car)
        file.write('\n')

mpg = MPG()
file = InputFile()
outputFile = OutputFile()
cars, errors = read_File(file, mpg)

output(outputFile, cars, errors)
