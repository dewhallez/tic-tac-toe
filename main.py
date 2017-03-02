# Main Tic Tac Toe file
#!/usr/bin/env python3

# Module imports
import algorithm
from print_grid import printGrid
from start_input import startGame
import time

# Player Dictionaries and Global Variables
playerOne = {'name': '', 'piece': '', 'timesWon': 0}
playerTwo = {'name': '', 'piece': '', 'timesWon': 0}
board = []
WIDTH = HEIGHT = 3
turn = ''
x = 0
y = 0

def setCoordinate(turn):
    x = int(input('Player ' + turn['name'] + ': x coordinate?'))
    while ((x < 0) or (x > HEIGHT)):
        print('Out of range, this is a ' + str(WIDTH) + ' x ' + str(HEIGHT) + ' board.')
        x = int(input('Player ' + turn['name'] + ': x coordinate?'))

    y = int(input('Player ' + turn['name'] + ': y coordinate?'))
    print(y)
    while ((y < 0) or (y > HEIGHT)):
        print('Out of range, this is a ' + str(WIDTH) + ' x ' + str(HEIGHT) + ' board.')
        y = int(input('Player ' + turn['name'] + ': y coordinate?'))

# This function gets the user input before starting the game
startGame(playerOne, playerTwo)

if (playerOne['piece'] == 'X'):
    turn = playerOne
else:
    turn = playerTwo

# Initialize empty 2-Dimensional Array
for x in range(WIDTH):

    row = []

    for y in range(HEIGHT):
        row.append('_')

    board.append(row)

# Game loop
while True:

    printGrid(board, WIDTH, HEIGHT);

    setCoordinate(turn)

    coord = board[x][y]

    while (coord != '_'):
        print("There's a piece already there!")
        setCoordinate(turn)
        coord = board[x][y]

    board[x][y] = turn['piece']

    if (turn == playerOne):
        turn = playerTwo
    else:
        turn = playerOne
