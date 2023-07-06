import time
import random

#Player is 1, computer is 0
#Player is X, computer is O

board = [3]*9

def getFirst():
    first = random.randint(0,1)
    if first == 0:
        return "computer"
    else:
        return "player"
    
def getPlayer(board):
    print('What is your next move?')
    inp = input()
    if inp not in '123456789':
        print('Please enter a number from 1 to 9 (I mean it\'s tictactoe)')
        time.sleep(2)
    elif board[inp] != 3:
        print('This place has been taken')
    else:
        board[inp] = 1

def getComputer(board):
    if (board[0] == board[1] and board[1] == board[2]):
        win = board[0]
    elif (board[3] == board[4] and board[4] == board[5]):
        win = board[3]
    elif (board[6] == board[7] and board[7] == board[8]):
        win = board[6]
    elif (board[0] == board[3] and board[3] == board[6]):
        win = board[0]
    elif (board[1] == board[4] and board[4] == board[7]):
        win = board[1]
    elif (board[2] == board[5] and board[5] == board[8]):
        win = board[2]
    elif (board[0] == board[4] and board[4] == board[8]):
        win = board[0]
    elif (board[2] == board[4] or board[4] == board[6] or board[2] == board[6]):
        win = board[2]
        

def showBoard():
    for x in range(3):
        for i in range(3):
            print(transform(board[3*x+i]), end=' ')
        print()

def transform(number):
    if number == 0:
        return 'X'
    elif number == 1:
        return 'O'
    else:
        return ' '
    
def checkWin():
    win = 3
    if (board[0] == board[1] and board[1] == board[2]):
        win = board[0]
    elif (board[3] == board[4] and board[4] == board[5]):
        win = board[3]
    elif (board[6] == board[7] and board[7] == board[8]):
        win = board[6]
    elif (board[0] == board[3] and board[3] == board[6]):
        win = board[0]
    elif (board[1] == board[4] and board[4] == board[7]):
        win = board[1]
    elif (board[2] == board[5] and board[5] == board[8]):
        win = board[2]
    elif (board[0] == board[4] and board[4] == board[8]):
        win = board[0]
    elif (board[2] == board[4] and board[4] == board[6]):
        win = board[2]
    elif (board != [3]*9):
        win = 2
    if win == 1:
        return 'player'
    elif win == 0:
        return 'computer'
    elif win == 2:
        return 'noone'
    
playAgain = True
while (playAgain == True):
    while (True):
        first = getFirst()
        if (first == 'computer'):
            getComputer(board)
        else:
            getPlayer(board)
        win = checkWin()
        if (win == 'computer'):
            print('U lose')
            break
        elif (win == 'player'):
            print('U win')
            break
        elif (win == 'noone'):
            print('It is a draw!')
            break    
    print('Do you want to play again?')
    playAgain = input().lower().startswith('y')

print('Bye bye, see ya again')    
