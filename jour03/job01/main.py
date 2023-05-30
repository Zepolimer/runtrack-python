"""
    Créer un programme qui parcourt le contenu du fichier “domains.xml” et qui compte le
    nombre d’extension de domaines qui s’y trouvent (.com, .net, etc …).
"""
from os.path import exists
import re


def extract_domains():
    file_exists = exists('domains.xml')

    if file_exists:
        with open('domains.xml') as f:
            lines = f.readlines()

            extensions = []
            unique_extensions = []

            for l_no, line in enumerate(lines):
                if 'domain' in line:
                    isolate_domain = re.split('\.', line)[1:]
                    extracted_domain = re.split('<', str(isolate_domain))[:1]

                    domain = ''.join(str(extracted_domain[:2]))
                    extension = ''.join([str(item) for item in domain])[2:]

                    extensions.append(extension)

            for extension in extensions:
                if extension not in unique_extensions:
                    unique_extensions.append(extension)

            print('- Le fichier domain.xml contient %s extension de domaines différentes' % len(unique_extensions))

    else:
        print('This file does not exist..')


"""
    Créer un programme qui parcourt le contenu du fichier “data.txt” et qui compte le
    nombre de mots (sans caractère spéciaux) qui s’y trouvent.
"""
def extract_data():
    file_exists = exists('data.txt')

    if file_exists:
        with open('data.txt') as f:
            data = f.read()
            words = data.split()

            print('- Le fichier data.txt contient %s mots' % len(words))

    else:
        print('This file does not exist..')


if __name__ == "__main__":
    extract_domains()
    extract_data()
