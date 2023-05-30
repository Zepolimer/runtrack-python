"""
    Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’
    en fonction des paramètres d’entrées (width, height)
"""


def draw_rectangle(width, height):
    for i in range(1, height + 1):
        for j in range(1, width):
            if j == 1 or j == width - 1:
                print("|", end="")

            if (i == 1 or i == height) and j != width - 1:
                print("-", end=" ")
            else:
                print(" ", end=" ")

        print()


draw_rectangle(10, 4)
