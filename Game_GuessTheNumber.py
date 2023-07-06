#Guess the number
#Rules: You have to guess a number between -1000 to 1000. The entered number will be
#evaluated as higher or smaller than the number.

import random
import os

def Compare(gnum,num):
    if (gnum<num):
        return 0
    if (gnum>num):
        return 1
    
answer='y'
while (answer=='y'):
    os.system('cls')
    
    num=random.randint(-1000,1000)

    print('Enter the number you guess')
    gnum=int(input())

    result=Compare(gnum,num)

    if (result==1): print('Higher')
    else: print('Lower')
    
    trials=0
    
    while (gnum!=num and trials<=11):
        print('Guess again?')
        gnum=int(input())
        result=Compare(gnum,num)
        if (result==1): print('Higher')
        else: print('Lower')
        trials=trials+1
        if (gnum==num):
            break

    if (trials<=11):
        print('You have won!')
    else:
        print('The answer is:',+num)
        print('Do you wanna try again?')
        print('y/n')
        answer=input()
