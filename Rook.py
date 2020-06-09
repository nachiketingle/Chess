import pygame
from Piece import Piece

imagePathWhite = 'Assets/Chess_rlt60.png'
imagePathBlack = 'Assets/Chess_rdt60.png'


class Rook(Piece):
    def __init__(self, white, pos):
        image_path = imagePathWhite if white else imagePathBlack
        image = pygame.image.load(image_path)
        Piece.__init__(self, white, image_path, image, pos, 50)

    def talk(self):
        print('Rook')

    def draw_self(self, screen, row, col):
        Piece.draw_piece(self, screen, row, col)

    def indicate_valid(self, game_board, move_board):
        # Movement based on color
        i = self.pos[0]
        j = self.pos[1]

        # Check for valid movement
        self.rook_movement(game_board, move_board, i, j, 1, 0)
        self.rook_movement(game_board, move_board, i, j, -1, 0)
        self.rook_movement(game_board, move_board, i, j, 0, 1)
        self.rook_movement(game_board, move_board, i, j, 0, -1)

    def rook_movement(self, game_board, move_board, i, j, di, dj):
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
            return 'WR'
        else:
            return 'BR'

    def __repr__(self):
        if self.white:
            return 'WR'
        else:
            return 'BR'
