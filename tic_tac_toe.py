"""
Tic-Tac-Toe

Took a basic version of tic-tac-toe (The Perfect Crabs Intro's replit) and then added these features:
    
    Colors, user names, fonts, check for draws, typewriter font, 
    instructions, time, check if space was taken and a clear function.
    
C.Rin, April 2024
"""

import requests as r
import sys
import time
from time import sleep
import datetime
import os

PURPLE = "\033[1;35m"
GREEN = "\033[1;32m"
BGREEN = "\033[1;96m"
NC = "\033[0m"


def cleaner():
    return os.system("clear") and os.system("cls")


def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    return f"\t{BGREEN}***{NC}\n"


time.sleep(0.05)
cleaner()
welcome = f"\n\t\t{GREEN}Welcome to TIC-TAC-TOE{NC}\n"
typewriter(welcome)
time.sleep(2)
cleaner()


def print_board(board):
    formatted_rows = []
    for row in board:
        formatted_rows.append(" ".join(row))
    grid = "\n".join(formatted_rows)
    return grid


starter_board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

typewriter("Our starting board:\n")
print(print_board(starter_board))
time.sleep(2)
cleaner()
row_cells = "\nSpaces of the board go by Python logic.\n\nRow:\n\n0\n1\n2\n\n"
col_cells = "\nColumns: 0  1  2\n\n"
typewriter(row_cells)
time.sleep(1)
cleaner()
typewriter(col_cells)
time.sleep(2)
cleaner()
typewriter(
    "When you want to mark your space, think about the row and column it will fall on:\n"
)
board_example = f"\n\t{BGREEN}0,0  0,1  0,2\n\t1,0  1,1  1,2\n\t2,0  2,1  2,2{NC}\n"
typewriter(board_example)
time.sleep(3)
cleaner()


# make a move:
def make_move(board, row, column, player):
    board[row][column] = player
    return board


# instructions for move
typewriter("\nAfter a move:\n\n")
print(print_board(make_move(starter_board, 0, 0, "X")))
time.sleep(3)
cleaner()
# check if the game is over:

# get players
typewriter("\nReady Player One!\n")
player_one = input("Enter your name: ").capitalize()
typewriter(f"\n{PURPLE}{player_one}, you are Player 'X'!{NC}\n")
typewriter("\nReady Player Two!\n")
player_two = input("Enter your name: ").capitalize()
typewriter(f"\n{GREEN}{player_two}, you are Player 'O'!{NC}\n")
typewriter(f"\n{BGREEN}Let's play!{NC}\n")
time.sleep(2)
cleaner()
x_color = f"{PURPLE}X{NC}"
y_color = f"{GREEN}O{NC}"


# extract cells from the board
def get_cells(board, coord_1, coord_2, coord_3):
    return [
        board[coord_1[0]][coord_1[1]],
        board[coord_2[0]][coord_2[1]],
        board[coord_3[0]][coord_3[1]],
    ]


# check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, coord_1, coord_2, coord_3):
    cells = get_cells(board, coord_1, coord_2, coord_3)
    return "." not in cells


# check if X X X or O O O are next to each other
def are_all_cells_the_same(board, coord_1, coord_2, coord_3):
    cells = get_cells(board, coord_1, coord_2, coord_3)
    return cells[0] == cells[1] and cells[1] == cells[2]


# list of groups to check:

groups_to_check = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ".":
                return False
    print("No more moves!")
    return True


def is_game_over(board):
    for group in groups_to_check:
        if is_group_complete(board, group[0], group[1], group[2]):
            if are_all_cells_the_same(board, group[0], group[1], group[2]):
                print("Winner!")
                return True  # winning row!
    if check_draw(board):
        return True
    return False  # no winning row


def play_game():
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

    player = x_color
    while not is_game_over(board):
        time.sleep(0.05)
        cleaner()
        print(print_board(board))
        print("It's " + player + "'s turn.")
        row = int(input("Enter a row: "))
        column = int(input("Enter a column: "))
        if not is_move_valid(board, row, column):
            print("Invalid move!")
            continue
        board = make_move(board, row, column, player)
        if player == x_color:
            player = y_color
        else:
            player = x_color
        print(print_board(board), "\n")
    print("Game over!")


def is_move_valid(board, row, column):
    if board[row][column] == ".":
        return True
    else:
        return False


# start
print("LET'S START!")
play_game()
