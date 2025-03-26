def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for j in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ", board[j][0], "  |  ", board[j][1], "  |  ", board[j][2], "  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


#def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


#def draw_move(board):
    # The function draws the computer's move and updates the board.

#creazione tabella e aggiunta parametri
board = [["" for row in range(3)] for column in range(3)]

for i in range(3):
    board[0][i]=i+1
    board[1][i]=i+4
    board[2][i]=i+7
board[1][1]="X"

#stampa iniziale
display_board(board)