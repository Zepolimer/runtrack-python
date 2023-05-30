import random


class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = [['O' for _ in range(j)] for _ in range(i)]

    @staticmethod
    def __check_color(color):
        if color == "rouge":
            return "R"
        elif color == "jaune":
            return "J"
        else:
            raise ValueError("La couleur doit être rouge ou jaune.")

    def play(self, col, color):
        jeton = self.__check_color(color)

        for i in range(self.i-1, -1, -1):
            if self.board[i][col] == "O":
                self.board[i][col] = jeton
                return
        raise ValueError("Colonne pleine.")

    def print_board(self):
        print("  " + "   ".join([str(x) for x in range(self.j)]))
        print("- " * (self.j * 2 + 1))

        for i in range(self.i):
            print("| " + " | ".join(self.board[i]) + " | ")

        print("- "*(self.j*2+1))

    def is_valid(self, col):
        return 0 <= col < self.j and self.board[0][col] == 'O'

    def check_win(self, color):
        jeton = self.__check_color(color)

        # Vérification des lignes
        for i in range(self.i):
            for j in range(self.j-3):
                if self.board[i][j] == jeton and self.board[i][j+1] == jeton and self.board[i][j+2] == jeton and self.board[i][j+3] == jeton:
                    return True

        # Vérification des colonnes
        for i in range(self.i-3):
            for j in range(self.j):
                if self.board[i][j] == jeton and self.board[i+1][j] == jeton and self.board[i+2][j] == jeton and self.board[i+3][j] == jeton:
                    return True

        # Vérification des diagonales
        for i in range(3, self.i):
            for j in range(self.j-3):
                if self.board[i][j] == jeton and self.board[i-1][j+1] == jeton and self.board[i-2][j+2] == jeton and self.board[i-3][j+3] == jeton:
                    return True

        for i in range(self.i-3):
            for j in range(self.j-3):
                if self.board[i][j] == jeton and self.board[i+1][j+1] == jeton and self.board[i+2][j+2] == jeton and self.board[i+3][j+3] == jeton:
                    return True
        return False


class AIOne:
    def __init__(self, name):
        self.name = name
        self.color = "jaune"

    @staticmethod
    def think(board):
        valid_cols = [col for col in range(board.j) if board.is_valid(col)]
        return random.choice(valid_cols)


class AITwo:
    def __init__(self, name):
        self.name = name
        self.color = "rouge"

    @staticmethod
    def think(board):
        valid_cols = [col for col in range(board.j) if board.is_valid(col)]
        return random.choice(valid_cols)


def play_game_vs_ai():
    i = int(input("Nombre de lignes : "))
    j = int(input("Nombre de colonnes : "))
    board = Board(i, j)

    ai_one = AIOne("AI_ONE")
    ai_two = AITwo("AI_TWO")

    players = [ai_one.name, ai_two.name]
    random.shuffle(players)
    current_player = players[0]

    while True:
        board.print_board()

        if current_player == ai_one:
            col = ai_one.think(board)

            print("\n %s a jouée son coup dans la colonne : %s !" % (ai_one.name, col))
            board.play(col, ai_one.color)
        else:
            col = ai_two.think(board)

            print("\n %s a jouée son coup dans la colonne : %s !" % (ai_two.name, col))
            board.play(col, ai_two.color)

        if board.check_win(ai_one.color):
            if current_player == ai_one:
                print("\n %s A GAGNÉ !" % ai_one.name)
            else:
                print("\n %s A GAGNÉ !" % ai_two.name)
            break

        if current_player == ai_one:
            current_player = ai_two
        else:
            current_player = ai_one


play_game_vs_ai()
