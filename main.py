# Main Tic Tac Toe file
#!/usr/bin/env python3

# Module imports
import algorithm
from startInput import startGame
import time

# Player Dictionaries and Global Variables
playerOne = {'name': '', 'piece': '', 'timesWon': 0}
playerTwo = {'name': '', 'piece': '', 'timesWon': 0}
board = []
width = height = 3

startGame(playerOne, playerTwo)

# Initialize empty 2-Dimensional Array
for x in range(width):
    row = []
    for y in range(height):
        row.append('_')
    board.append(row)

# Game loop
while True:
    # Draw the game board
    for x in range(width):
        for y in range(height):
            if (y < 2):
                print(board[x][y], end='|')
            else:
                print(board[x][y], end='')
        print("")
    nextMove = input("Player " + playerOne['name'] + ": Next move?")




