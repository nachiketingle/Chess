import pygame
import Board
from GameEvents import *
import numpy as np

pygame.init()

# Display Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Initialize Board
gameBoard = Board.init()
move_board = np.zeros((8, 8))
print(gameBoard)

# Initialize event objects
event_handler = MouseEvents(SCREEN_WIDTH, SCREEN_HEIGHT)

# Start game
running = True
while running:

    # Check for pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            move_board = event_handler.mouse_clicked(pygame.mouse.get_pos(), gameBoard, move_board)

    # Draw board and pieces
    Board.draw_background(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    Board.draw_pieces(screen, gameBoard, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Draw choices
    Board.draw_valid(screen, gameBoard, move_board, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Display on screen
    pygame.display.flip()

pygame.quit()
print("Quit game!")
quit()
