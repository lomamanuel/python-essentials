from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ", board[i][0], "  |  ", board[i][1], "  |  ", board[i][2], "  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move=int(input("Enter your move: "))
    #controllo parametro
    while move<1 or move>9:
        print("Move not allowed!")
        move=int(input("Enter your move: "))
    #ricerca casella corrispondente
    for j in range(3):
        for i in range(3):
            if board[i][j]==move:
                board[i][j]="O"
    display_board(board)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields=[]
    for j in range(3):
        for i in range(3):
            if board[i][j] in range(1,10):
                free_fields.append(board[i][j])
    return free_fields


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board, free_fields):
    # The function draws the computer's move and updates the board.
    computer_move=randrange(free_fields)
    #modifica tabella
    for j in range(3):
        for i in range(3):
            if board[i][j]==computer_move:
                board[i][j]="X"
    display_board(board)

#creazione tabella e aggiunta parametri
board = [["" for row in range(3)] for column in range(3)]

for j in range(3):
    board[0][j]=j+1
    board[1][j]=j+4
    board[2][j]=j+7
board[1][1]="X"

#stampa iniziale
display_board(board)

#mossa iniziale
enter_move(board)

#lista caselle libere
free_fields=make_list_of_free_fields(board)
if free_fields==[]:
    victory_for()
else:
    draw_move(board, free_fields)