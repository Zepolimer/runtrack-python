"""
    Créez un programme qui demande 5 fois à l’utilisateur de renseigner un nombre entier.
    Stockez ces nombres entiers dans une liste puis triez-les par ordre croissant avant de
    les afficher, dans l’ordre, dans le terminal.
"""

print('Entrez un nombre entier :')
array = []

while len(array) < 5:
    number = input()
    array.append(number)

array.sort()
print(array)
