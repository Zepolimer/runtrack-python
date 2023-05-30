from os.path import exists
import random


def read_txt():
    file_exists = exists('data.txt')

    if file_exists:
        with open('data.txt') as f:

            data = f.read()
            data_str = str(data).lower()

            for suffix in (':', ';', '!', '?', '"', '+', '/', '(', ')', '*', '§', '\n'):
                data_str = [d.removesuffix(suffix) for d in data_str]

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

            return occurrences
    else:
        print('This file does not exist..')


def generate_word():
    # Choisir une longueur de mot au hasard, en se basant sur les longueurs observées dans le texte
    lengths = list(occurrences.keys())
    length = random.choice(lengths)

    # Choisir une première lettre au hasard, en se basant sur les lettres observées en début de mot dans le texte
    first_letters = list(occurrences[length].keys())
    first_letter = random.choice(first_letters)

    word = length + first_letter

    for c in list(occurrences[length].items()):
        letter_keys = list(occurrences[length].keys())
        letter_values = list(occurrences[length].values())

        total_occurrences = sum(letter_values)
        percentages = [value / total_occurrences for value in letter_values]
        next_letter = random.choices(letter_keys, weights=percentages)[0]
        word += next_letter

    return word


if __name__ == "__main__":
    occurrences = {}
    read_txt()

    for i in range(7):
        word = generate_word()
        print(word)
