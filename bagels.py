import random
import os

NUMDIGITS = 3
MAXGUESSES = 10

def randnum():
    li = '0 1 2 3 4 5 6 7 8 9'.split()
    abc = ''
    random.shuffle(li)
    for i in range(NUMDIGITS):
        abc += li[i] 
    return abc

def isNum(num):
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

def getClue(pguess, unum):
    clue = []
    for i in range(len(pguess)):
        for a in range(len(unum)):
            if (pguess[i]==unum[a]):
                if i != a:
                    clue.append('Pico ')
                else:
                    clue.append('Fermi ')
    if len(clue) == 0:
        return 'Bagels'
    clue.sort()
    ans = str(clue[0])
    for i in range(1, len(clue)):
        ans = ans + ' ' +clue[i]
    return ans
    
def again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

#guess = 0
#unum = randnum()
#print(unum)
#"""
playAgain = True
while playAgain == True:
    os.system('cls')
    print('I am thinking of a %s-digit number. Try to guess what it is.'%NUMDIGITS)
    print('Here are some clues:')
    print('When I say:    That means:')
    print('  Pico         One digit is correct but in the wrong position.')
    print('  Fermi        One digit is correct and in the right position.')
    print('  Bagels       No digit is correct.')
    print('I have thought up a number. You have %s guesses to get it'%MAXGUESSES)

    guess = 0
    unum = randnum()
    
    while (guess<MAXGUESSES):
        print('Guess #' + str(guess+1) + ':')
        pguess = input()
        while (isNum(pguess) == False):
            print('Please enter a number')
            pguess = input()
        if pguess == unum:
            break
        clue = getClue(pguess, unum)
        print(clue)
        guess += 1

    if guess == MAXGUESSES:
        print('You lose! The number is ' + str(unum))
    else:
        print('Congrats! You win')
    playAgain = again()
#"""

