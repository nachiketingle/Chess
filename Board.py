import pygame

from Piece import Piece
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King


def draw_background(screen, width, height):
    screen.fill((255, 255, 255))
    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if i % 2 != j % 2:
                pygame.draw.rect(screen, (74, 42, 42),
                                 pygame.Rect(i * width // 8, j * height // 8, width // 8, height // 8))


def draw_pieces(screen, game_board, width, height):
    row = 0
    for row_arr in game_board:
        col = 0
        for space in row_arr:
            if isinstance(space, Piece):
                space.draw_self(screen, col, row)
            col += 1
        row += 1


def draw_valid(screen, game_board, move_board, width, height):
    square_width = width // 8
    square_height = height // 8

    for i in range(0, 8):
        for j in range(0, 8):
            if move_board[i][j] != 0:
                pixel_row = j * square_width
                pixel_col = i * square_height

                if move_board[i][j] == -1:
                    pygame.draw.rect(screen, (255, 0, 0), (pixel_row, pixel_col, square_width, square_height), 1)

                s = pygame.Surface((square_width, square_height))
                s.set_alpha(128)
                s.fill((128, 128, 128))
                screen.blit(s, (pixel_row, pixel_col))


def init():
    game_board = []

    # Generate all the rows in the board
    for i in range(0, 8):
        game_board.append([])

    # Add all the black pieces
    game_board[0].append(Rook(False, (0, 0)))
    game_board[0].append(Knight(False, (0, 1)))
    game_board[0].append(Bishop(False, (0, 2)))
    game_board[0].append(Queen(False, (0, 3)))
    game_board[0].append(King(False, (0, 4)))
    game_board[0].append(Bishop(False, (0, 5)))
    game_board[0].append(Knight(False, (0, 6)))
    game_board[0].append(Rook(False, (0, 7)))
    for i in range(8):
        game_board[1].append(Pawn(False, (1, i)))

    # Add the empty spaces
    for i in range(2, 6):
        for j in range(8):
            game_board[i].append(None)

    # Add all the white pieces
    for i in range(8):
        game_board[6].append(Pawn(True, (6, i)))
    game_board[7].append(Rook(True, (7, 0)))
    game_board[7].append(Knight(True, (7, 1)))
    game_board[7].append(Bishop(True, (7, 2)))
    game_board[7].append(Queen(True, (7, 3)))
    game_board[7].append(King(True, (7, 4)))
    game_board[7].append(Bishop(True, (7, 5)))
    game_board[7].append(Knight(True, (7, 6)))
    game_board[7].append(Rook(True, (7, 7)))

    return game_board
