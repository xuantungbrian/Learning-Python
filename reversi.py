import random 
import sys
def drawboard(board):
    Pline = '  '+ '+---'*8+'+'
    Sline = '  '+ '|   '*9+'|'
    print('  ', end='')
    for i in range (1,9):
        print('  i  ', end='')
    for y in range (1,9):
        print(Pline)
        print(Sline)
        print('1 ', end='')
        for x in range (1,9):
            print('|  '+board[x][y]+'  ')
        print(Sline)
    print(Pline)
            

board = []
for i in range
drawboard(board)
