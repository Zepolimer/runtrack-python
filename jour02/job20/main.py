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
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @staticmethod
    def think(board):
        valid_cols = [col for col in range(board.j) if board.is_valid(col)]
        return random.choice(valid_cols)


def play_game_vs_ai():
    i = int(input("Nombre de lignes : "))
    j = int(input("Nombre de colonnes : "))
    board = Board(i, j)

    joueur = input("Nom du joueur : ")

    while True:
        color = input("Voulez-vous jouer en rouge ou en jaune ? ")
        if color in ["rouge", "jaune"]:
            if color == "rouge":
                ai_color = "jaune"
            else:
                ai_color = "rouge"

            j_color = color
            break
        print("Couleur invalide. Veuillez choisir entre rouge et jaune.")

    ai = AIOne("AI", ai_color)

    players = [joueur, ai.name]
    random.shuffle(players)
    current_player = players[0]

    while True:
        board.print_board()

        if current_player == joueur:
            while True:
                col = int(input("%s - Dans quelle colonne voulez-vous jouer ? [0, %s] : " % (current_player, j - 1)))

                if board.is_valid(col):
                    board.play(col, j_color)
                    break
        else:
            col = ai.think(board)

            print("\n L'IA a jouée son coup dans la colonne : %s !" % col)
            board.play(col, ai.color)

        if board.check_win(color):
            if current_player == joueur:
                print("\n %s a gagné ! Félicitations, vous avez remporté 100 000 euros !" % current_player)
            else:
                print("Dommage, vous avez perdu contre l'IA.")
            break

        if current_player == joueur:
            current_player = ai.name
        else:
            current_player = joueur


play_game_vs_ai()
