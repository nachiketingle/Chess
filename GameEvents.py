import pygame
from Piece import *
import numpy as np


class MouseEvents:
    piece_selected = False
    piece = None
    i = 0
    j = 0
    white_turn = True

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square_width = self.width // 8
        self.square_height = self.height // 8

    def mouse_clicked(self, pos, game_board, move_board):
        # Get index of square clicked
        x = pos[0]
        y = pos[1]
        j = x // self.square_width
        i = y // self.square_height

        # If a piece has been selected, move it if possible
        if self.piece_selected:
            success = self.piece.move(game_board, move_board, (i, j))
            move_board = np.zeros((8, 8))
            if success:
                self.white_turn = not self.white_turn
                # Determine checkmate
                if (self.checkmate(game_board, self.white_turn)):
                    move_board -= 1
                    print(move_board)

            self.piece_selected = False
            return move_board

        self.piece = game_board[i][j]

        # Initialize the move board
        move_board = np.zeros((8, 8))

        # If selected piece is our piece, and it is player's turn, update the move board
        if isinstance(self.piece, Piece) and self.piece.valid_turn(self.white_turn):
            self.piece_selected = True
            move_board[i][j] = -1
            self.piece.indicate_valid(game_board, move_board)
            print(move_board)
        else:
            self.piece_selected = False

        # Return the move board
        return move_board

    # See if King is in checkmate
    def checkmate(self, game_board, white_turn):
        # Create own move_board
        move_board = np.zeros((8,8))

        # See if king is in check
        inCheck = False
        for i in range(0, 8, 1):
            for j in range(0, 8, 1):
                self.piece = game_board[i][j]
                move_board[i][j] = -1
                if isinstance(self.piece, Piece) and self.piece.valid_turn(not self.white_turn):
                    self.piece.indicate_valid(game_board, move_board)
                    if self.max_value(move_board) == 999:
                        inCheck = True
                        break
                    move_board = np.zeros((8, 8))
            if inCheck:
                break
        
        # Stop if not in check
        if not inCheck:
            return False

        # TODO: See if any move gets you out of check
        

        return inCheck

    def max_value(self, move_board):
        max_value = -1
        for row in move_board:
            if max_value < max(row):
                max_value = max(row)
            
        print(max_value)
        return max_value