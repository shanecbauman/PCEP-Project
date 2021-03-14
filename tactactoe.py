import random
import re

board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9]
]
victory = False
p = re.compile(r"\d")



def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    board_template = [
        "+-------+-------+-------+",
        "|       |       |       |",
        f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |",
        "|       |       |       |",
        "+-------+-------+-------+",
        "|       |       |       |",
        f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |",
        "|       |       |       |",
        "+-------+-------+-------+",
        "|       |       |       |",
        f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |",
        "|       |       |       |",
        "+-------+-------+-------+"
        ]
    for row in board_template:
        print(row)


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    move = 0
    while move not in range(1, 10):
        move = int(input("Enter your move (1-9): "))
        for row in board:
            if move in row:
                break
        else:
            move = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move:
                board[i][j] = "O"
                return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    possible_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if p.match(str(board[i][j])):
                possible_moves.append((i, j))

    random.shuffle(possible_moves)
    return possible_moves[0]


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    winning_lines = [
        # Winning rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Winning cols
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Winning diags
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]

    # Check if there are atleast 3 moves
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == sign:
                moves.append((i, j))
    if len(moves) < 3:
        return False

    # Check if any of the previous moves contain any of the winning lines
    for lines in winning_lines:
        for i, spot in enumerate(lines):
            if spot not in moves:
                break
            elif spot in moves and i == len(lines) - 1:
                print(f"Player {sign} wins!")
                return True
    
    # Check if all moves are taken, if so, finish game
    open_spots = 0
    for row in board:
        for col in row:
            if p.match(str(col)):
                open_spots += 1
    if open_spots == 0:
        print("Draw Game.")
        return True
    else:
        return False
    

def draw_move(board):
    # The function draws the computer's move and updates the board.
    move = make_list_of_free_fields(board)
    board[move[0]][move[1]] = "X"
    return board


print("Computer's turn:")
display_board(board)
while not victory:
    # Player turn
    board = enter_move(board)
    display_board(board)
    victory = victory_for(board, "O")
    if victory:
        break

    # Computer turn
    print("Computer's turn:")
    draw_move(board)
    display_board(board)
    victory = victory_for(board, "X")