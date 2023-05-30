import pygame as pg


CASE_SIZE = 200
GRAY_BG = (223, 223, 223)
GRAY_BORDER = (210, 210, 210)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 255, 0)
COULEUR_GAGNANT = (255, 255, 0)

# Initialiser Pygame
pg.init()

window = pg.display.set_mode((600, 600))
pg.display.set_caption("Tic Tac Toe")


class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = None

    def draw(self):
        if self.state == "X":
            pg.draw.line(window, X_COLOR, (self.x + 50, self.y + 50), (self.x + 150, self.y + 150), 4)
            pg.draw.line(window, X_COLOR, (self.x + 150, self.y + 50), (self.x + 50, self.y + 150), 4)
        elif self.state == "O":
            pg.draw.circle(window, O_COLOR, (self.x + 100, self.y + 100), 50, 4)

    def selected(self, x, y):
        return self.x <= x <= self.x + CASE_SIZE and self.y <= y <= self.y + CASE_SIZE

    def is_empty(self):
        return self.state is None


# Définir la classe Tableau
class Board:
    def __init__(self):
        self.cases = [[Case(x * CASE_SIZE, y * CASE_SIZE) for x in range(3)] for y in range(3)]

    def draw(self):
        for line in self.cases:
            for case in line:
                case.draw()

    def set_case(self, line, column, player):
        self.cases[line][column].state = player

    def get_case(self, line, column):
        return self.cases[line][column]

    def is_full(self):
        for line in self.cases:
            for case in line:
                if case.is_empty():
                    return False
        return True

    def is_winner(self, player):
        # Vérifier les lignes
        for line in self.cases:
            if all([case.state == player for case in line]):
                return True

        # Vérifier les colonnes
        for column in range(3):
            if all([self.cases[line][column].state == player for line in range(3)]):
                return True

        # Vérifier les diagonales
        if self.cases[0][0].state == self.cases[1][1].state == self.cases[2][2].state == player:
            return True
        if self.cases[0][2].state == self.cases[1][1].state == self.cases[2][0].state == player:
            return True

        return False


# Définir la classe Jeu
class Game:
    def __init__(self):
        self.board = Board()
        self.current = "X"
        self.winner = None

    def draw(self):
        self.board.draw()

        if self.winner:
            return True
            # pg.draw.line(window, COULEUR_GAGNANT, (0, CASE_SIZE // 2), (600, CASE_SIZE // 2), 5)
        elif self.board.is_full():
            return True
            # pg.draw.line(window, GRAY_BORDER, (0, CASE_SIZE // 2), (600, CASE_SIZE // 2), 5)

        pg.display.update()

    def clic(self, x, y):
        if not self.winner:
            for line in self.board.cases:
                for case in line:
                    if case.selected(x, y) and case.is_empty():
                        case.state = self.current
                        if self.board.is_winner(self.current):
                            self.winner = self.current
                        elif self.board.is_full():
                            self.winner = "Personne"
                        else:
                            self.current = "O" if self.current == "X" else "X"
                        return True
        return False


game = Game()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.MOUSEBUTTONUP:
            if game.clic(*pg.mouse.get_pos()):
                game.draw()

    window.fill(GRAY_BG)
    pg.draw.line(window, GRAY_BORDER, (CASE_SIZE, 0), (CASE_SIZE, 600), 5)
    pg.draw.line(window, GRAY_BORDER, (2 * CASE_SIZE, 0), (2 * CASE_SIZE, 600), 5)
    pg.draw.line(window, GRAY_BORDER, (0, CASE_SIZE), (600, CASE_SIZE), 5)
    pg.draw.line(window, GRAY_BORDER, (0, 2 * CASE_SIZE), (600, 2 * CASE_SIZE), 5)

    if game.draw():
        game = Game()

    pg.display.update()

