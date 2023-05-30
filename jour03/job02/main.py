"""
    Créer un programme qui demande à l’utilisateur de renseigner un nombre entier. Le
    programme devra alors parcourir le contenu du fichier “data.txt” compter le nombre de
    mots de la taille renseignée qui s’y trouvent.
"""
from os.path import exists


def extract_data():
    file_exists = exists('data.txt')

    value = int(input("Saississez un nombre entier (taille d'un mot) : "))

    if file_exists:
        counts = []

        with open('data.txt') as f:
            data = f.read()
            words = data.split()

            for i in words:
                if len(i) == value:
                    counts.append(i)

            print('- Le fichier data.txt contient %s mots contenant %s caractères.' % (len(counts), value))

    else:
        print('This file does not exist..')


if __name__ == "__main__":
    extract_data()
