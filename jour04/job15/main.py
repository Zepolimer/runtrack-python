

def inputs():
    a = str(input("Saisir une 1ere chaine de caractères : ").lower())
    b = str(input("Saisir une 2eme chaine de caractères : ").lower())

    if a != '' and b != '':
        if '*' in a:
            print('La première chaine de caratères ne peut contenir de *')
            inputs()
        else:
            compare_str(a, b)


def str_to_arr(string: str):
    nw = []

    for s in string:
        nw.append(s)

    return nw


def compare_str(str1: str, str2: str):
    str1_arr = str_to_arr(str1)
    str2_arr = str_to_arr(str2)

    for x, y in zip(str1_arr, str2_arr):
        if x == y:
            res = True
            break
        else:
            if y == '*' and str2.index(y) + 1 == len(str2):
                res = True
                break
            elif y == '*' and str2.index(y) + 1 != len(str2):
                new_list = []
                [new_list.append(item) for item in str2 if item != '*']
                compare_str(str1, ''.join(new_list))
                break

            res = False
            break

    print(res)


if __name__ == "__main__":
    inputs()
