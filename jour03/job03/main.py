"""
    Écrire un programme qui parcourt le fichier “data.txt” et qui compte le nombre
    d'occurrence de chaque lettre (Minuscules et Capitales comptent pour la même lettre).
    A l’aide du module MatPlotLib, générer un histogramme représentant le pourcentage
    d’apparition de chaque lettre.
"""
from os.path import exists
import re
import matplotlib.pyplot as plt


def main():
    file_exists = exists('data.txt')

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if file_exists:
        counts = {}

        with open('data.txt') as f:
            data = f.read()
            words = data.split()

            words_str = str(words)

            for letter in alphabet:
                count = len(re.findall(letter, words_str.lower()))
                counts[letter] = count

            print(counts)

            names = list(counts.keys())
            values = list(counts.values())
            fig, axs = plt.subplots(1, 1, figsize=(9, 3), sharey=True)
            axs.bar(names, values)

            plt.show()
    else:
        print('This file does not exist..')


if __name__ == "__main__":
    main()
