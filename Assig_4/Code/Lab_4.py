


#import random to simulate dice rolling
import random
def game():
    chips, chipsw = 'NULL', 'NULL'
    while chips == 'NULL':
        chips = int(input('How many chips do you want to start with? ==> '))
        if chips <= 1:
            print('Too low a value, you can only choose 1 - 100 chips')
            chips = 'NULL'
        elif chips > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
            chips = 'NULL'
    while chipsw == 'NULL':
        chipsw =  int(input('How many chips do you want to wager? ==> '))
        if chipsw <= 0:
            print('The wager amount must be greater than 0.\nPlease enter again.')
            chipsw = 'NULL'
        elif chipsw > chips:
            print(f'The wager amount cannot be greater than how much you have.  {chips}')
            chipsw = 'NULL'
    chips -= chipsw
#
    s1 = random.randint(1,10)
    s2 = random.randint(1,10)
    s3 = random.randint(1,10)
    h1 = random.randint(1,10)
    h2 = random.randint(1,10)
    h3 = random.randint(1,10)
    cnt = 0
    if s1 == h1:cnt += 1
    if s1 == h2:cnt += 1
    if s1 == h3:cnt += 1
    if s2 == h1:cnt += 1
    if s2 == h2:cnt += 1
    if s2 == h3:cnt += 1
    if s3 == h1:cnt += 1
    if s3 == h2:cnt += 1
    if s3 == h3:cnt += 1
    print(f'Your spin {s1} {s2} {s3}\nYou matched {cnt} reels\nYou won/lost {cnt}\nCurrent bank {chips}')
    

cont = 'Y'
while cont != 'n' and 'N' and 'NO':
    game()
    cont = input('Do you want to play again? ==> ')
    while cont != 'y' and 'Y' and 'Yes' and 'n' and 'N' and 'NO':
        if cont == 'n' or 'N' or 'NO':
            break
        print('You must enter y/Y/YES/n/N/NO to continue. Please try again')
        cont = input('Do you want to play again? ==> ')