########################################################################
##
## CS 101 Lab
## Flarsheim Guesser
## Samuel Yohannes
## syyndf@umkc.edu
##
## PROBLEM : trying to guess the number knowing mod3, mod5, and mod7
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
def game():
    mod3, mod5, mod7 = 'NULL', 'NULL', 'NULL'
    print('Welcome to the Flarsheim Guesser!\n')
    print('Please think of a number betweem and including 1 and 100.\n')
    while mod3 == 'NULL':
        mod3 = int(input('What is the remainder when your number is divided by 3 ?'))
        if mod3 > 3:
            print('The value entered must be less than 3')
            mod3 = 'NULL'
        elif mod3 < 0:
            print('The value entered must be more than 0')
            mod3 = 'NULL'
    while mod5 == 'NULL':
        mod5 =  int(input('What is the remainder when your number is divided by 5 ?'))
        if mod5 > 5:
            print('The value entered must be less than 3')
            mod5 = 'NULL'
        elif mod5 < 0:
            print('The value entered must be more than 0')
            mod5 = 'NULL'
    while mod7 == 'NULL':
        mod7 = int(input('What is the remainder when your number is divided by 7 ?'))
        if mod7 > 7:
            print('The value entered must be less than 3')
            mod7 = 'NULL'
        elif mod7 < 0:
            print('The value entered must be more than 0')
            mod7 = 'NULL'

    for i in range(101):
        if i%3 == mod3:
            if i%5 == mod5:
                if i%7 == mod7:
                    return i


cont = 'Y'
while cont == 'Y':
    print(f'Your number was {game()}')
    cont = input('How amazing is that?\n\nDo you want to play again?Y to continue, N to quit  ==>')
