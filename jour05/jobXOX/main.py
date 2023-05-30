import pygame as pg
from pygame.locals import *


GRAY_BG = (223, 223, 223)
GRAY_BORDER = (210, 210, 210)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (25, 25, 25)
BLUE = (0, 0, 255)

WINDOW_SIZE = (600, 600)
WINDOW_TITLE = 'TicTacToe1337'

CASE_SIZE = 200

pg.init()
POLICE = pg.font.SysFont('Calibri', 50, True, False)

game_window = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption(WINDOW_TITLE)


class Current:
    def __init__(self, player):
        self.player = player

    def handle_player(self):
        if self.player == 'X':
            return 'O'
        else:
            return 'X'


class Case:
    def __init__(self, size):
        self.size = size


class Board:
    def __init__(self):
        self.board = [[None] * 3, [None] * 3, [None] * 3]

    def player_click(self, row, col, player):
        if self.board[row][col] is None:
            self.board[row][col] = player

            return player


class GameHandler:
    def __init__(self, case, current):
        self.game_window = game_window
        self.board = Board().board
        self.case = case
        self.current = current

    def initialize_window(self):
        for row in range(3):
            for col in range(3):
                x = col * self.case
                y = row * self.case

                rectangle = pg.Rect(x, y, self.case, self.case)
                pg.draw.rect(self.game_window, (210, 210, 210), rectangle, 3)

                value = self.board[row][col]
                if value is not None:
                    text = POLICE.render(value, True, BLACK)
                    text_rect = text.get_rect(center=rectangle.center)
                    game_window.blit(text, text_rect)

    def check_win(self):
        for r in range(3):
            if self.board[r][0] == self.board[r][1] == self.board[r][2] != None:
                pg.draw.line(
                    self.game_window,
                    (255, 0, 0),
                    (0, (r + 1) * self.case),
                    (self.game_window, (r + 1) * self.case),
                    4
                )
                return True
            if self.board[0][r] == self.board[1][r] == self.board[2][r] != None:
                pg.draw.line(
                    self.game_window,
                    (255, 0, 0),
                    (0, (r + 1) * self.case),
                    (self.game_window, (r + 1) * self.case),
                    4
                )
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            pg.draw.line(game_window, (255, 0, 0), (50, 50), (550, 550), 4)
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            pg.draw.line(game_window, (255, 0, 0), (50, 50), (550, 550), 4)
            return True
        if all([all(r) for r in self.board]):
            return True

        return False

    def player_click(self, row, col, player):
        if self.board[row][col] is None:
            self.board[row][col] = player

            self.current = player.handle_player()

    @staticmethod
    def reset_game(case, player):
        new_handler = GameHandler(case, player)
        new_handler.initialize_window()
        return new_handler


"""
PLAY GAME HERE
"""
pg.init()

case = Case(200)
current_player = Current('X')

handler = GameHandler(case.size, current_player)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos

            row = y // case.size
            col = x // case.size

            handler.player_click(row, col, current_player)

    game_window.fill((223, 223, 223))
    handler.initialize_window()

    if handler.check_win():
        pg.time.wait(1000)
        handler = handler.reset_game(case.size, current_player)

    pg.display.update()
