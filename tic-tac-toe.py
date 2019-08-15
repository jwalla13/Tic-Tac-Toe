import random

def makeBoard():
    board = []
    for r in range(3):
        row = ['-'] * 3
        board.append(row)
    return board

def printBoard(board):
    print("Here is the current board: \n")
    rows, cols = len(board), len(board[0]) #form called parallel assignment
    for row in range(rows):
        for col in range(cols):
            print(board[row][col], end = " ") #no newline
        print() #newline
    print() #newline

def userMove(board):
    moveMade = False
    while(moveMade == False):
        printBoard(board)
        row = int(input("What row do you want place you move at: "))
        col = int(input("What column do you want place you move at: "))
        if(row < 3 and row >= 0 and col < 3 and col >= 0): #move is on board
            if(board[row][col] == '-'): #make sure cell is empty
                board[row][col] = 'X'
                moveMade = True
                print("\nYour move was recorded")
                printBoard(board)
            else: print("\nPlease choose an empty cell")
        else: print("\nPlease enter a valid coordinate")

def computerMove(board):
    moveMade = False
    while(moveMade == False):
        row = random.randint(0,2)
        col = random.randint(0,2)
        if(board[row][col] == '-'): #make sure cell is empty
            board[row][col] = 'O'
            moveMade = True
            print("\nThe computer moved at row: %d, col: %d" % (row, col))

def checkHorizontals(board):
    for row in board:
        if(row[0] == row[1] == row[2] and row[0] != '-'):
            return True
    return False

def checkVerticals(board):
    for col in range(3):
        if(board[0][col] == board[1][col] == board[2][col] and 
            board[0][col] != '-'):
            return True
    return False

def checkDiagonals(board):
    if(board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-'):
        return True
    elif(board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-'):
        return True
    return False



def checkForWin(board):
    return (checkHorizontals(board) or checkVerticals(board) or 
        checkDiagonals(board))


def playTicTacToe():
    board = makeBoard()
    winner = None
    moveCount = 0
    while(winner == None):
        userMove(board)
        moveCount += 1
        if(checkForWin(board)): winner = 'User'
        else:
            computerMove(board)
            moveCount += 1
            if(checkForWin(board)): winner = 'Computer'
        if(moveCount == 9 and winner = None): #tie
            print("The game is a tie...")
            break
    if(winner == 'User'): print("Congrats, you win!")
    else: print("better luck next time")

        

playTicTacToe()
