"""
    Écrire un programme qui itère les nombres entiers de 1 à 100.
    - Pour les multiples de 3 afficher "Fizz" au lieu du nombre.
    - Pour les multiples de 3 afficher "Buzz" au lieu du nombre .
    - Pour les nombres qui sont des multiples de 3 et 5, afficher "FizzBuzz".
"""

for i in range(101):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
