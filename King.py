import pygame
from Piece import Piece
import numpy as np

imagePathWhite = 'Assets/Chess_klt60.png'
imagePathBlack = 'Assets/Chess_kdt60.png'


class King(Piece):
    def __init__(self, white, pos):
        image_path = imagePathWhite if white else imagePathBlack
        image = pygame.image.load(image_path)
        Piece.__init__(self, white, image_path, image, pos, 999)

    def talk(self):
        print('King')

    def draw_self(self, screen, row, col):
        Piece.draw_piece(self, screen, row, col)

    def indicate_valid(self, game_board, move_board):
        curr_i = self.pos[0]
        curr_j = self.pos[1]
        self.king_movement(game_board, move_board, curr_i, curr_j, 1, 1)
        self.king_movement(game_board, move_board, curr_i, curr_j, 1, -1)
        self.king_movement(game_board, move_board, curr_i, curr_j, -1, 1)
        self.king_movement(game_board, move_board, curr_i, curr_j, -1, -1)
        self.king_movement(game_board, move_board, curr_i, curr_j, 0, -1)
        self.king_movement(game_board, move_board, curr_i, curr_j, -1, 0)
        self.king_movement(game_board, move_board, curr_i, curr_j, 0, 1)
        self.king_movement(game_board, move_board, curr_i, curr_j, 1, 0)

    def king_movement(self, game_board, move_board, curr_i, curr_j, di, dj):
        i = curr_i + di
        j = curr_j + dj
        if self.is_valid((i, j)) and not self.adj_king(game_board, i, j) and not self.move_in_check(game_board, curr_i, curr_j, i, j):
            if not isinstance(game_board[i][j], Piece):
                move_board[i][j] = 1
            elif self.is_enemy(game_board, i, j):
                move_board[i][j] = game_board[i][j].get_points()

    def adj_king(self, game_board, i, j):

        # Check below
        for x in range(-1, 2):
            row = i-1
            col = j+x
            if self.is_valid((row, col)) and self.is_enemy(game_board, row, col) and isinstance(game_board[row][col], King):
                return True

        # Check top
        for x in range(-1, 2):
            row = i + 1
            col = j + x
            if self.is_valid((row, col)) and self.is_enemy(game_board, row, col) and isinstance(game_board[row][col], King):
                return True

        # Check sides
        row = i
        col = j + 1
        if self.is_valid((row, col)) and self.is_enemy(game_board, row, col) and isinstance(game_board[row][col], King):
            return True

        # Check sides
        row = i
        col = j - 1
        if self.is_valid((row, col)) and self.is_enemy(game_board, row, col) and isinstance(game_board[row][col], King):
            return True

        return False

    def move_in_check(self, game_board, curr_i, curr_j, i, j):
        # Do not ues original move_board
        copy_board = np.zeros((8, 8))

        # Temp move king to see if they would be in check
        game_board[curr_i][curr_j] = None
        temp = game_board[i][j]
        game_board[i][j] = self

        # Simulate all potential threats
        for row in range(0, len(game_board)):
            for col in range(0, len(game_board[row])):
                if isinstance(game_board[row][col], Piece) and self.is_enemy(game_board, row, col) :
                    piece = game_board[row][col]
                    if isinstance(piece, King):
                        continue

                    # Check if piece is a threat
                    piece.indicate_valid(game_board, copy_board)
                    for game_row in copy_board:
                        max_val = max(game_row)
                        # Reset board if it is
                        if max_val == 999:
                            game_board[i][j] = temp
                            game_board[curr_i][curr_j] = self
                            return True
                    copy_board = np.zeros((8, 8))

        # Reset board
        game_board[i][j] = temp
        game_board[curr_i][curr_j] = self
        return False

    def __str__(self):
        if self.white:
            return 'WK'
        else:
            return 'BK'

    def __repr__(self):
        if self.white:
            return 'WK'
        else:
            return 'BK'
