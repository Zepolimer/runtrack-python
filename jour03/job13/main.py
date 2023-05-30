"""
    Écrire un programme qui parcourt le fichier “data.txt” et qui, pour chaque lettre, compte
    le nombre d'occurrence de la lettre suivante. Générer, ensuite, un graphique de courbes
    superposées, une courbe par lettre, montrant le pourcentage d’apparition de chaque lettre la suivant.

    Par exemple, pour le a: a(2%), b(5%), c(2.3%) …. pour le b: a(3%), b(0%), c(1%), …
"""
from os.path import exists
import matplotlib.pyplot as plt


def main():
    file_exists = exists('data.txt')

    if file_exists:
        with open('data.txt') as f:
            data = f.read()
            data_str = str(data).lower()

            for suffix in (',', '.', ':', ';', '!', '?', '"', '+', '/', '(', ')', '*', '§', '-', ' ', '\n'):
                data_str = [d.removesuffix(suffix) for d in data_str]

            occurrences = {}
            for i in range(len(data_str) - 1):
                letter = data_str[i]
                next_letter = data_str[i + 1]

                if letter in occurrences:
                    if next_letter in occurrences[letter]:
                        occurrences[letter][next_letter] += 1
                    else:
                        occurrences[letter][next_letter] = 1
                else:
                    occurrences[letter] = {next_letter: 1}

            for letter in occurrences:
                total_occurrences = sum(occurrences[letter].values())
                percentages = [occurrences[letter][next_letter] / total_occurrences * 100 for next_letter in
                               occurrences[letter]]
                plt.plot(list(occurrences[letter].keys()), percentages, label=letter)

            plt.xlabel("Lettre suivante")
            plt.ylabel("% d'apparition")
            plt.title("Pourcentage d'apparition de chaque lettre suivante")
            plt.legend()
            plt.show()
            return
    else:
        print('This file does not exist..')


if __name__ == "__main__":
    main()
