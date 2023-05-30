"""
    Luke Skywalker, un professeur de Math, fait passer un test et décide de noter ses élèves
    sur une échelle allant de 0 à 100 inclus.
    - Si un étudiant obtient moins de 40 sur 100, il échoue au test.
    - S'il a plus de 40, il réussit le test.

    Luke décide donc d’arrondir à la hausse les notes des étudiants ayant réussi le test.
    Mais Luke n’est quand même pas trop gentil. Cet arrondi à la hausse ne bénéficiera qu’aux étudiants
    remplissant certains critères.
    - Si un étudiant a eu une note de moins de strictement 3 points de son prochain multiple de 5,
    alors sa note est arrondie à ce multiple de 5.
    Par exemple, un 83 sera arrondi à 85 alors qu’un 82 restera un 82.

    Pour simplifier le travail de Luke, écrivez une fonction qui prend en paramètre une liste
    de notes et qui renvoie une liste de notes, arrondies comme il se doit, quand cela est nécessaire.
"""

import math


def notation(results):
    array = []
    for note in results:
        if note < 40:
            array.append(note)
        elif note >= 40 and note % 5 >= 3:
            array.append(math.ceil(note/5) * 5)
        else:
            array.append(note)
    print(array)


results = [33, 62, 55, 83, 43, 77, 38, 49, 88, 93, 24, 78]
notation(results)
