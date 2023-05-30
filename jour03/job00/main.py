"""
    Créer un programme qui demande à l'utilisateur de renseigner une chaîne de caractères
    et qui écrit cette chaine de caractère dans un fichier “output.txt”
"""


def main():
    string = input("Saississez une chaine de caractères : ")

    string = str(string)
    f = open('output.txt', 'w+')
    f.write(string)
    f.close()


if __name__ == "__main__":
    main()
