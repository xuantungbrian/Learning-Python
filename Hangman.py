import os
import random
import time

playAgain = True
while (playAgain == True):
    wordList = 'each one of us was harmed by being brought into existence that harm is not negligible because the quality of even the best lives is very bad'.split()

    chosenWord = wordList[random.randint(0, 26)]
    count = 0
    guessing ='_' * len(chosenWord)

    guessMem = ''
    count = 0
    while (count < 8):
        
        os.system('cls')
        print('H A N G M A N\n')
        print('The word is ' +guessing+ '\n')
        print('    +---+')
        if (count>0):
            print('    |   |')
        else:
            print('        |')  
        if (count>1):
            print('    O   |')  
        else:
            print('        |')  
        if (count==3):
            print('    |   |')  
        elif (count==4):
            print('   /|   |')  
        elif (count>=5):
            print('   /|\\  |') 
        else:
            print('        |')   
        if (count==6):
            print('   /    |')  
        elif (count>=7):
            print('   / \\ |') 
            print('========')
            break
        else:
            print('        |')  
        print('==========')
        print('Please guess a character:')
        guessChar = input()
        guessChar = guessChar.lower()
        if (len(guessChar) != 1):
            print('Please enter only a character')
            time.sleep(2)
        elif (guessChar not in 'abcdefghijklmnopqrstuvwxyz'):
            print('Please enter a character in the alphabet')
            time.sleep(2)
        elif (guessChar in guessMem):
            print('You have guessed this char')
            time.sleep(2)
            continue
        guessMem = guessMem + guessChar
        
        if guessChar in chosenWord:
            for i in range(len(chosenWord)):
                if guessChar == chosenWord[i]:
                    guessing = guessing[:i] + guessChar +guessing[i+1:]
            if guessing == chosenWord:
                break
        else:
            count += 1

    if count == 7:
        os.system('cls')
        print('You lose! The word is "'+chosenWord +'"!')
    else:
        os.system('cls')
        print('Congrats! You win in ' + str(len(guessMem)) + ' tries!')
    playAgain = False
    print('Do you want to play again?')
    ans = input()
    if (ans.lower().startswith('y')):
        playAgain = True
    else:
        playAgain = False
