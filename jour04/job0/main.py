

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    i = int(input("Saisir un nombre entier : "))

    print(factorial(i))
