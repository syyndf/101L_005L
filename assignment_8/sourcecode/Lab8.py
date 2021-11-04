import math
Tests = []
Assignments = []

def score_Calc():
        sum1 = 0
        sum2 = 0
        stdSum1 = 0
        stdSum2 = 0
        if len(Tests) > 0:
            for score in Tests:
                sum1 += score
            Testmean = sum1 / len(Tests)
            for score in Tests:
                stdSum1 += (score - Testmean)**2
            TestStd = math.sqrt(stdSum1 / len(Tests))
            maxTestscore = max(Tests)
            minTestscore = min(Tests)
        else:
            Testmean = 'n/a'
            TestStd = 'n/a'
            maxTestscore = 'n/a'
            minTestscore = 'n/a'
        if len(Assignments) > 0:
            for score in Assignments:
                sum2 += score
            AssignAvg = sum2 / len(Assignments)
            for score in Assignments:
                stdSum2 += (score - AssignAvg)**2
            AssignStd = math.sqrt(stdSum2 / len(Assignments))
            maxAssignscr = max(Assignments)
            minAssignscr = min(Assignments)
        else:
            AssignAvg = 'n/a'
            AssignStd = 'n/a'
            maxAssignscr = 'n/a'
            minAssignscr = 'n/a'
        PrintScore(minTestscore, maxTestscore, Testmean, TestStd, minAssignscr, maxAssignscr, AssignAvg, AssignStd)
       
def PrintScore(minTestscore, maxTestscore, Testmean, TestStd, minAssignscr, maxAssignscr, AssignAvg, AssignStd):
        if len(Assignments) > 0 and len(Tests) > 0:
                WeightedScore = (Testmean * 0.6) + (AssignAvg * 0.4)
        else:
                WeightedScore = 0
        if len(Assignments) > 0 and len(Tests) > 0:
                print('{:<25}{:<10}{:<10}{:<10}{:<10}{}\n{}'.format('Type', '#', 'Min', 'Max', "Avg", 'STD', ('='*68)))
                print('{:<25}{:<10}{:<10}{:<10}{:<10.2f}{:.2f}'.format('Tests', len(Tests), minTestscore, maxTestscore, Testmean, TestStd))
                print('{:<25}{:<10}{:<10}{:<10}{:<10.2f}{:.2f}'.format('Programs', len(Assignments), minAssignscr, maxAssignscr, AssignAvg, AssignStd))
                print("\nThe weighted score is ==> {:.2f}".format(WeightedScore))
        else:
                print('{:<25}{:<10}{:<10}{:<10}{:<10}{}\n{}'.format('Type', '#', 'Min', 'Max', "Avg", 'STD', ('='*68)))
                print('{:<25}{:<10}{:<10}{:<10}{:<10}{}'.format('Tests', len(Tests), minTestscore, maxTestscore, Testmean, TestStd))
                print('{:<25}{:<10}{:<10}{:<10}{:<10}{}'.format('Programs', len(Assignments), minAssignscr, maxAssignscr, AssignAvg, AssignStd))
                print("\nThe weighted score is ==> {:.2f}".format(WeightedScore))

def AppendTestScore():
    try:
        userInput = float(input("Enter Test score 0 - 100 ==> "))
        if userInput > 0:
            Tests.append(userInput)
        else:
            print("Test score can't be lower than 0")
    except:
        print('Input error')
def DelTestScore():
        try:
            delChoice = float(input('Enter Test score to delete ==> '))
            if delChoice in Tests:
                Tests.remove(delChoice)
            else:
                print("Test score {} not found".format(delChoice))
        except:
            print('Input error')
def AppendAssignScore():
        try:
            userInput = float(input("Enter Assignment score 0 - 100 ==> "))
            if userInput > 0:
                Assignments.append(userInput)
            else:
                print("Assignment score can't be lower than 0")
        except:
            print('Input error')
def DelAssignScore():
        try:
            delChoice = float(input('Enter Assignment score to delete ==> '))
            if delChoice in Assignments:
                Assignments.remove(delChoice)
            else:
                print("Test score not found")
        except:
            print('Input error')

while True:
    print('{:^50}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format('Grade Menu', '1 - Add Test', '2 - Remove Test', '3 - Clear Tests', '4 - Add Assignment', '5 - Remove Assignment', '6 - Clear Assignments', 'D - Display Scores', 'Q - Quit\n'))
    Choice = input('\n==> ')
    if Choice == '1':
        AppendTestScore()
    elif Choice == '2':
        DelTestScore()
    elif Choice == '3':
        Tests.clear()
    elif Choice == '4':
        AppendAssignScore()
    elif Choice == '5':
        DelAssignScore()
    elif Choice == '6':
        Assignments.clear()      
    elif Choice == 'Q' or Choice == 'q':
        break              
    elif Choice == 'D' or Choice == 'd':
        score_Calc()
    else:
        print('Error')