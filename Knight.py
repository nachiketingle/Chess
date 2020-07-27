import pygame
from Piece import Piece

imagePathWhite = 'Assets/Chess_nlt60.png'
imagePathBlack = 'Assets/Chess_ndt60.png'


class Knight(Piece):
    def __init__(self, white, pos):
        image_path = imagePathWhite if white else imagePathBlack
        image = pygame.image.load(image_path)
        Piece.__init__(self, white, image_path, image, pos, 30)

    def talk(self):
        print('Knight')

    def draw_self(self, screen, row, col):
        Piece.draw_piece(self, screen, row, col)

    # Update move board with locations that the piece can go to
    def indicate_valid(self, game_board, move_board):
        curr_i = self.pos[0]
        curr_j = self.pos[1]

        self.knight_movement(game_board, move_board, curr_i, curr_j, 1, 2)
        self.knight_movement(game_board, move_board, curr_i, curr_j, -1, 2)
        self.knight_movement(game_board, move_board, curr_i, curr_j, 2, 1)
        self.knight_movement(game_board, move_board, curr_i, curr_j, -2, 1)
        self.knight_movement(game_board, move_board, curr_i, curr_j, 2, -1)
        self.knight_movement(game_board, move_board, curr_i, curr_j, -2, -1)
        self.knight_movement(game_board, move_board, curr_i, curr_j, 1, -2)
        self.knight_movement(game_board, move_board, curr_i, curr_j, -1, -2)

    def knight_movement(self, game_board, move_board, i, j, di, dj):
        i = i + di
        j = j + dj
        if self.is_valid((i, j)):
            if not isinstance(game_board[i][j], Piece):
                move_board[i][j] = 1
            elif self.is_enemy(game_board, i, j):
                move_board[i][j] = game_board[i][j].get_points()

    def __str__(self):
        if self.white:
            return 'WN'
        else:
            return 'BN'

    def __repr__(self):
        if self.white:
            return 'WN'
        else:
            return 'BN'
