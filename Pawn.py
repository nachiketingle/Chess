import pygame
from Piece import Piece

imagePathWhite = 'Assets/Chess_plt60.png'
imagePathBlack = 'Assets/Chess_pdt60.png'


class Pawn(Piece):
    def __init__(self, white, pos):
        image_path = imagePathWhite if white else imagePathBlack
        image = pygame.image.load(image_path)
        Piece.__init__(self, white, image_path, image, pos, 10)

    def talk(self):
        print('Pawn')

    def draw_self(self, screen, row, col):
        Piece.draw_piece(self, screen, row, col)

    def indicate_valid(self, game_board, move_board):
        # Movement based on color
        i = self.pos[0]
        j = self.pos[1]

        # Check for valid movement
        if self.white:
            # Check for piece in front
            if self.is_valid((i-1, j)) and not isinstance(game_board[i - 1][j], Piece):
                move_board[i - 1][j] = 1
                if i == 6 and not isinstance(game_board[i - 2][j], Piece):
                    move_board[i - 2][j] = 1

            # Check if can capture
            if self.is_valid((i-1, j+1)) and self.is_enemy(game_board, i-1, j+1):
                move_board[i-1][j+1] = game_board[i-1][j+1].get_points()
            if self.is_valid((i-1, j-1)) and self.is_enemy(game_board, i-1, j-1):
                move_board[i-1][j-1] = game_board[i-1][j-1].get_points()

        else:
            # Check for piece in front
            if self.is_valid((i+1, j)) and not isinstance(game_board[i + 1][j], Piece):
                move_board[i + 1][j] = 1
                if i == 1 and not isinstance(game_board[i + 2][j], Piece):
                    move_board[i + 2][j] = 1

            # Check if can capture
            if self.is_valid((i + 1, j + 1)) and self.is_enemy(game_board, i + 1, j + 1):
                move_board[i + 1][j + 1] = game_board[i+1][j+1].get_points()
            if self.is_valid((i + 1, j - 1)) and self.is_enemy(game_board, i + 1, j - 1):
                move_board[i + 1][j - 1] = game_board[i+1][j-1].get_points()

    def __str__(self):
        if self.white:
            return 'WP'
        else:
            return 'BP'

    def __repr__(self):
        if self.white:
            return 'WP'
        else:
            return 'BP'
