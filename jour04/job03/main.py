def place_piece(board, i, j):
    for k in range(i):
        if (board[k] == j) or (board[k] - j == i - k) or (board[k] - j == k - i):
            return True
    return False


def checkers_game(tab, i):
    if i == value:
        return True
    else:
        for j in range(value):
            if not place_piece(tab, i, j):
                tab[i] = j

                if checkers_game(tab, i + 1):
                    return True

        return False


def play(n):
    board = [['O' for x in range(n)] for y in range(n)]

    tab = [-1 for i in range(n)]

    checkers_game(tab, 0)

    for i in range(n):
        board[i][tab[i]] = 'X'

    for j in range(n):
        print(" ".join(board[j]))

    return board


if __name__ == "__main__":
    value = int(input("Saisir un nombre entier : "))

    play(value)
