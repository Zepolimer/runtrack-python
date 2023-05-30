"""
    Créer un programme qui lit le contenu du fichier “output.txt” et qui l’affiche dans le terminal.
"""
from os.path import exists


def main():
    file_exists = exists('../job00/output.txt')

    if file_exists:
        with open('../job00/output.txt') as f:
            lines = f.readlines()

            print(lines)
    else:
        print('You should create a file, go to job00 : python3 main.py')


if __name__ == "__main__":
    main()
