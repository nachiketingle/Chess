import pygame
import numpy as np


class Piece:
    IMAGE_WIDTH = 60
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800

    def __init__(self, white, image_path, image, pos, points):
        self.white = white
        self.image_path = image_path
        self.image = image
        self.pos = pos
        self.points = points

    def __str__(self):
        print('Piece')

    def talk(self):
        print('Piece')

    def draw_self(self, surface, row, col):
        print('General piece')

    def draw_piece(self, screen, row, col):
        screen.blit(self.image, (row * self.SCREEN_WIDTH // 8 + (self.SCREEN_WIDTH // 8 - self.IMAGE_WIDTH) // 2,
                                 col * self.SCREEN_HEIGHT // 8 + (self.SCREEN_HEIGHT // 8 - self.IMAGE_WIDTH) // 2))

    def indicate_valid(self, game_board, move_board):
        print("Checking valid squares")

    def move(self, game_board, move_board, new_pos):
        (i, j) = new_pos
        (curr_i, curr_j) = self.pos
        if move_board[i][j] > 0 and not self.causes_check(game_board, new_pos):
            game_board[i][j] = self
            game_board[curr_i][curr_j] = None
            self.pos = new_pos
            return True

        return False

    def causes_check(self, game_board, new_pos):
        i, j = new_pos
        curr_i, curr_j = self.pos
        temp = game_board[i][j]
        game_board[curr_i][curr_j] = None
        game_board[i][j] = self
        # Go through all enemy pieces
        copy_board = np.zeros((8, 8))
        for row in range(0, len(game_board)):
            for col in range(0, len(game_board[row])):
                if isinstance(game_board[row][col], Piece) and self.is_enemy(game_board, row, col):
                    piece = game_board[row][col]

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

        game_board[i][j] = temp
        game_board[curr_i][curr_j] = self
        return False

    def valid_turn(self, white_turn):
        return self.white == white_turn

    def is_white(self):
        return self.white

    def is_enemy(self, game_board, row, col):
        return isinstance(game_board[row][col], Piece) and (game_board[row][col].is_white() != self.white)

    def get_points(self):
        return self.points

    @staticmethod
    def is_valid(pos):
        (i, j) = pos
        if i < 0 or i >= 8 or j < 0 or j >= 8:
            return False
        return True
