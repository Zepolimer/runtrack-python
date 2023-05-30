from os.path import exists
import random


def read_txt():
    file_exists = exists('data.txt')

    if file_exists:
        with open('data.txt') as f:

            data = f.read()
            data_str = str(data).lower()

            for suffix in (':', ';', '!', '?', '"', '+', '/', '(', ')', '*', '§', '\n', '-'):
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
    lengths = list(occurrences.keys())
    length = random.choice(lengths)

    letter_keys = list(occurrences[length].keys())
    letter_values = list(occurrences[length].values())

    first_letter = random.choice(letter_keys)

    if content == '':
        word = length.upper() + first_letter
    else:
        word = length + first_letter

    for c in list(occurrences[length].items()):
        last_letter = word[-1]
        total_occurrences = sum(letter_values)
        percentages = [value / total_occurrences for value in letter_values]
        next_letter = random.choices(letter_keys, weights=percentages)[0]

        if last_letter == next_letter:
            next_letter = random.choices(letter_keys, weights=percentages)[0]
        elif last_letter == ',':
            next_letter = ' ' + random.choices(letter_keys, weights=percentages)[0]
        elif last_letter == '-':
            next_letter = random.choices(letter_keys, weights=percentages)[0]
        elif last_letter == '.':
            next_letter = random.choices(letter_keys, weights=percentages)[0]
            if next_letter == ' ':
                next_letter = str(next_letter.upper())
            else:
                next_letter = ' ' + str(next_letter.upper())
        elif last_letter == ' ' and last_letter == next_letter:
            next_letter = random.choices(letter_keys, weights=percentages)[0]

        word += next_letter

    return word


if __name__ == "__main__":
    occurrences = {}
    read_txt()

    content = ''

    random_words = random.randrange(4, 12)

    for s in range(5):
        for i in range(random_words):
            word = generate_word()

            if content == '':
                if word[0] == ' ':
                    word.replace(" ", "", 1)
                elif word[0] == ',':
                    word.replace(",", "", 1)
                elif word[0] == '.':
                    word.replace(".", "", 1)

            content += word

    print(content)

