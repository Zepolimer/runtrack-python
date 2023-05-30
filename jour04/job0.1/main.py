

def recursive(x, n):
    if n == 0:
        return 1
    else:
        return x * recursive(x, n-1)


if __name__ == "__main__":
    i_x = int(input("Entrez un 1er nombre entier : "))
    i_n = int(input("Entrez un 2nd nombre entier : "))

    result = recursive(i_x, i_n)
    print(f"{i_x}^{i_n} = {result}")