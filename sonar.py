import random
import os
import sys

NUMCHEST = 3
NUMDEVICE = 14


def drawBoard(sonar, chest):
    hline1 = '         '.join('1 2 3 4 5'.split())
    hline2 = '0123456789' * 6

    print('   ' + ' '*10 + hline1)
    print('   '+hline2)

    for i in range(15):
        if i<10:
            print(' ', end='')
        print(str(i)+' ', end='')
        for a in range(60):
            dist = 99
            if [str(a), str(i)] in sonar:
                for x in chest:
                    if (max(abs(a-int(x[0])), abs(i-int(x[1])))<dist):
                        dist = max(abs(a-int(x[0])), abs(i-int(x[1])))
                if dist >= 10:
                    dist = 0
                print(str(dist), end='')
            elif (random.randint(0,1) == 0):
                print('~', end='')
            else:
                print('`', end='')

        print(' '+str(i))

    print('   '+hline2)
    print('   ' + ' '*10 + hline1)

def showInstructions():
    print('Instructions: You are the captain of Simon, a treasure-hunting ship. Your current mission is to find the three')
    print('sunken treasure chests that are lurking in the part of the ocean you are in and collect them. To play, enter the')
    print('coordinates of the point in the ocean you wish to drop a solar device. The sonar can find out how far the closest')
    print('chest is to it. For example, the d below marks where the device was dropped, and the 2\'s represent distances of 2')
    print('away from the device. The 4\'s represent distances of 4 away from the device.')
    print('''
            444444444
            4       4
            4 22222 4
            4 2   2 4
            4 2 d 2 4
            4 2   2 4
            4 22222 4
            4       4
            444444444
            
        Press enter to continue...''')
    input()
    print('''For example, here is a treasure chest (the c) located a distance of 2 away from the sonar device (the d):
    
            22222
            c   2
            2 d 2
            2   2
            22222
            
The point where the device was dropped will be marked with a 2.
            
The treasure chests don't move around. Sonar devices can detect treasure chests up to a distance of 9. If all chests
are out of range, the point will be marked with 0
            
If a device is directly dropped on a treasure chest, you have discovered the location of the chest, and it will be
collected. The sonar device will remain there.

When you collect the chest, all sonar devices will update to locate the next closest sunken treasure chest.
            
Press enter to continue...''')
    input()
    print()


def again():
    print('Do you want to play again?')
    return input().lower().startswith('y')

def create_chest(num):
    ret = []
    for i in range(num):
        x = random.randint(0, 14)
        y = random.randint(0, 59)
        ret.append([str(y), str(x)])
    return ret
        
def checkGuess(guess, sonar):
    ans = guess.split()
    if len(ans) != 2:
        return False
    if isNum(ans[0]) == False or isNum(ans[1]) == False:
        return False
    if ans in sonar:
        return False
    if int(ans[0]) < 0 or int(ans[1]) < 0 or int(ans[0]) > 59 or int(ans[1]) > 14:
        return False
    return True

def isNum(num):
    if num =='':
        return False
    for i in num:
        if i not in '0123456789':
            return False
    return True

playAgain = True
while (playAgain==True):
    os.system('cls')
    print('S O N A R !')
    print()
    print('Would you like to see the instructions? (yes/no)')
    if input().lower().startswith('y'):
        showInstructions()
    dev_left = NUMDEVICE
    sonar = []
    chest = create_chest(NUMCHEST)
    if (len(chest)!=NUMCHEST):
        print('We have a problem with the number of chests')
    while (dev_left > 0 and len(chest) > 0):
        drawBoard(sonar, chest)
        print('You have %s sonar devices left. %s treasure chests remaining.'%(dev_left, len(chest)))
        print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
        guess = input()
        if (guess.lower() == 'quit'):
            break
        while checkGuess(guess, sonar) == False:
            print('Please enter 2 number (0-59 0-14) separated by a space as required in the rule and no repetition!')
            guess = input()

        sonar.append(guess.split())
        if (guess.split() in chest):
            chest.remove(guess.split())
            print('You have found a sunken treasure chest!')
        print()
        dev_left -=1
    
    if len(chest) == 0:
        print('Congrats! You win!')
    else:
        print('You lose')
    playAgain = again()