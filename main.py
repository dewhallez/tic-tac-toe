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
width = height = 3

startGame(playerOne, playerTwo)

# Initialize empty 2-Dimensional Array
for x in range(width):

    row = []

    for y in range(height):
        row.append('_')

    board.append(row)

# Game loop
#test comment
while True:

    printGrid(board, width, height);

    nextMove = input("Player " + playerOne['name'] + ": Next move?")
