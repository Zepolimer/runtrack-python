
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


def play_game():
    i = int(input("Nombre de lignes : "))
    j = int(input("Nombre de colonnes : "))
    board = Board(i, j)

    joueur1 = input("Nom du joueur 1 : ")
    joueur2 = input("Nom du joueur 2 : ")

    current_player = joueur1
    current_color = "rouge"

    while True:
        print("\n")

        board.print_board()
        col = int(input("%s - Dans quelle colonne voulez-vous jouer ? [0, %s] : " % (current_player, j - 1)))

        if col >= j:
            col = int(input("%s - Votre colonne n'existe pas, veuillez réessayer ? [0, %s] : " % (current_player, j - 1)))

        try:
            board.play(col, current_color)
        except ValueError:
            print("Cette colonne est pleine. Veuillez en choisir une autre.")
            continue

        if board.check_win(current_color):
            print("\n %s a gagné ! Félicitations, vous avez remporté 100 000 euros !" % current_player)
            break

        if current_player == joueur1:
            current_player = joueur2
            current_color = "jaune"
        else:
            current_player = joueur1
            current_color = "rouge"


play_game()
