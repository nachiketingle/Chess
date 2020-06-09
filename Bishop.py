import pygame
from Piece import Piece

imagePathWhite = 'Assets/Chess_blt60.png'
imagePathBlack = 'Assets/Chess_bdt60.png'


class Bishop(Piece):
    def __init__(self, white, pos):
        image_path = imagePathWhite if white else imagePathBlack
        image = pygame.image.load(image_path)
        Piece.__init__(self, white, image_path, image, pos, 30)

    def talk(self):
        print('Bishop')

    def draw_self(self, screen, row, col):
        Piece.draw_piece(self, screen, row, col)

    def indicate_valid(self, game_board, move_board):
        curr_i = self.pos[0]
        curr_j = self.pos[1]
        self.bishop_movement(game_board, move_board, curr_i, curr_j, 1, 1)
        self.bishop_movement(game_board, move_board, curr_i, curr_j, 1, -1)
        self.bishop_movement(game_board, move_board, curr_i, curr_j, -1, 1)
        self.bishop_movement(game_board, move_board, curr_i, curr_j, -1, -1)

    def bishop_movement(self, game_board, move_board, i, j, di, dj):
        while True:
            i = i + di
            j = j + dj
            if self.is_valid((i, j)):
                if not isinstance(game_board[i][j], Piece):
                    move_board[i][j] = 1
                elif self.is_enemy(game_board, i, j):
                    move_board[i][j] = game_board[i][j].get_points()
                    break
                else:
                    break
            else:
                break

    def __str__(self):
        if self.white:
            return 'WB'
        else:
            return 'BB'

    def __repr__(self):
        if self.white:
            return 'WB'
        else:
            return 'BB'
