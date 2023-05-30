"""
    Créer un programme qui demandera à l’utilisateur de renseigner un mot et un seul, sans
    espace ni aucun autre caractère que les 26 lettres de l’alphabet (sans accent ni
    majuscule).

    Votre programme devra modifier ce mot, en y changeant de place certains caractères
    (ou tous) afin de donner un mot plus “loin” dans l’ordre alphabétique que le mot
    renseigné par l'utilisateur.

    Attention: Le nouveau mot doit être le mot le plus proche possible, dans l’ordre
    alphabétique, du mot original !
    Par exemple, “abcde” donnerait “abced”. “acedb” est aussi “valide” mais n’est PAS le
    plus proche du mot original dans l’ordre alphabétique.
"""


def verify_word(word):
    word.replace(" ", "")
    letters = list(word.lower())

    for i in range(len(letters)):
        if letters[i] == 'é' or letters[i] == 'è' or letters[i] == 'ê' or letters[i] == 'ê':
            letters[i] = 'e'
        if letters[i] == 'à' or letters[i] == 'ä' or letters[i] == 'â':
            letters[i] = 'a'
        if letters[i] == 'ù' or letters[i] == 'û' or letters[i] == 'ü':
            letters[i] = 'u'
        if letters[i] == 'î' or letters[i] == 'ï' or letters[i] == 'ì':
            letters[i] = 'i'

    return letters


def modify_word(value):
    word = verify_word(value)
    letters = list(word)
    n = len(letters)

    for i in range(n - 2, -1, -1):
        if letters[i] < letters[i + 1]:
            next_letter = i + 1

            for j in range(i + 2, n):
                if letters[i] < letters[j] < letters[next_letter]:
                    next_letter = j

            letters[i], letters[next_letter] = letters[next_letter], letters[i]

            letters[i + 1:] = sorted(letters[i + 1:])
            return ''.join(letters)

    return value


input_word = input("Entrez un mot sans espace ni caractère autre que les 26 lettres de l'alphabet : ")

new_word = modify_word(input_word)
print("Le mot modifié est :", new_word)
