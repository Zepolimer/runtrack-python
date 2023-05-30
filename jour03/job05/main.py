"""
    Écrire un programme qui parcourt le fichier “data.txt” et qui compte le nombre de mots
    de chaque taille. A l’aide du module MatPlotLib, générer un histogramme représentant
    le pourcentage d’apparition de chaque taille de mot.

    cd jour03/job05
"""
from os.path import exists
import matplotlib.pyplot as plt


def main():
    file_exists = exists('data.txt')

    if file_exists:
        with open('data.txt') as f:
            data = f.read()
            words = data.split()

            for suffix in (',', '.', ':', ';', '!', '?', '"'):
                words = [w.removesuffix(suffix) for w in words]

            words = [w.removeprefix('"') for w in words]

            values = {}
            for w in words:
                length = len(w)
                values[length] = values.get(length, 0) + 1

            lengths, counts = zip(*values.items())

            fig, axs = plt.subplots(1, 1, figsize=(9, 3), sharey=True)
            axs.bar(lengths, counts)

            plt.show()
            return
    else:
        print('This file does not exist..')


if __name__ == "__main__":
    main()
