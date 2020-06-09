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

        x = pos[0]
        y = pos[1]

        j = x // self.square_width
        i = y // self.square_height

        if self.piece_selected:
            success = self.piece.move(game_board, move_board, (i, j))
            if success:
                self.white_turn = not self.white_turn
            self.piece_selected = False
            move_board = np.zeros((8, 8))
            return move_board

        self.piece = game_board[i][j]

        move_board = np.zeros((8, 8))

        if isinstance(self.piece, Piece) and self.piece.valid_turn(self.white_turn):
            self.piece_selected = True
            move_board[i][j] = -1
            self.piece.indicate_valid(game_board, move_board)
            print(move_board)
        else:
            self.piece_selected = False

        return move_board
