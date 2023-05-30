"""
    Écrire un programme qui affiche dans le terminal un triangle avec des ‘_’, des ‘\’ et des ‘/’
    en fonction des paramètres d’entrées, (height)
"""


def draw_triangle(n):
    slash = '/'
    underscore = '_'
    space = "  "
    backslash = '\\'

    for i in range(n):
        if i == n-1:
            print(slash + (underscore * (2*n-2)) + backslash)
        else:
            print(' ' * (n-i-1), end='')
            print(slash + space*i + backslash)


draw_triangle(4)
