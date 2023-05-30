from os.path import exists


def read_txt(file):
    file_exists = exists(file)

    if file_exists:
        with open(file) as f:

            data = f.read()
            return data.split()
    else:
        print('This file does not exist..')


if __name__ == "__main__":
    occurrences = {}
    txt = read_txt('data.txt')
    pokemon = read_txt('pokemon.txt')

    for p in pokemon:
        for t in txt:
            if p == t:
                print('Pokemon "%s" founded' % p)
                break

