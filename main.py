def read_list():
    lst = []
    n = int(input("Introduceti numarul de elemente din lista"))
    for i in range(n):
        x = int(input("a[{}]=". format(i+1)))
        lst.append(x)
    return lst

def get_longest_all_even(lst):
    '''
    10.Toate numerele sunt pare.
    :param lst: lista de numere intregi
    :return: rez ce reprezinta cea mai lunga subsecventa in care toate numerele sunt pare
    '''

    rez = []
    temp = []
    for x in lst:
        if x % 2 == 0:
            temp.append(x)
        else:
            if (len(temp)>len(rez)):
                rez = temp[:]
            temp.clear()
    if (len(temp) > len(rez)):
        rez = temp[:]
    return rez



def test_get_longest_all_even():
    assert get_longest_all_even([1, 3, 2, 16, 18, 5]) == [2, 16, 18]
    assert get_longest_all_even([20, 6, 15, 12]) == [20, 6]

test_get_longest_all_even()

def progresie_aritmetica(lst):
    '''
    Verifica daca o lista are elementele in progreie aritmetica
    :param lst: lista de numere intregi
    :return: True daca elementele din lista sunt in progresie aritmetica, False in caz contrar
    '''

    if len(lst)<3:
        return True
    for x in range(2, len(lst)):
        if lst[x]-lst[x-1] != lst[1]-lst[0]:
            return False
    return True


def get_longest_arithmetic_progression(lst):
    '''
    16. Toate numerele sunt în progresie aritmetică.
    :param lst: lista de numere intregi
    :return: rez ce reprezinta cea mai lunga subsecventa in care toate numerele sunt in progresie aritmetica
    '''

    rez = []
    lungime_rez = 0
    for x in range(len(lst)):
        for y in range(x, len(lst)):
            if progresie_aritmetica(lst[x:y+1]) and len(lst[x:y+1]) > lungime_rez:
                rez = lst[x:y+1]
                lungime_rez = len(lst[x:y+1])
    return rez

def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([3, 6, 9, 7, 12]) == [3, 6, 9]
    assert get_longest_arithmetic_progression([45, 6, 15, 20, 25, 14]) == [15, 20, 25]

test_get_longest_arithmetic_progression()

import math
def get_longest_all_perfect_squares(lst):
    '''
    1. Toate numerele sunt patrate perfecte.
    :param lst: lista de numere intregi
    :return: rez ce reprezinta cea mai lunga subsecventa in care toate numerele sunt patrate perfecte
    '''

    rez = []
    temp = []
    for x in lst:
        if math.sqrt(x) == int(math.sqrt(x)):
            temp.append(x)
        else:
            if (len(temp) > len(rez)):
                rez = temp[:]
            temp.clear()
    if (len(temp) > len(rez)):
        rez = temp[:]
    return rez

def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([16, 4, 36, 21, 57]) == [16, 4, 36]
    assert get_longest_all_perfect_squares([74, 48, 81, 9, 64, 49]) == [81, 9, 64, 49]

test_get_longest_all_perfect_squares()


def show_menu():
    '''
    Print menu
    :return:
    '''
    print('''
    1. Citire date.
    2. Determinare cea mai lungă subsecvență cu proprietatea 1: Toate numerele sunt pare.
    3. Determinare cea mai lungă subsecvență cu proprietatea 2: Toate numerele sunt în progresie aritmetică.
    4. Determinare cea mai lungă subsecvență cu proprietatea 3: Toate numerele sunt patrate perfecte.
    5. Ieșire.
    ''')

def main():
    lst = []
    while True:
        show_menu()
        cmd = input("Command: ")
        if cmd == '1':
            lst = read_list()
        elif cmd == '2':
            rez = get_longest_all_even(lst)
            print(rez)
        elif cmd == '3':
            rez = get_longest_arithmetic_progression(lst)
            print(rez)
        elif cmd == '4':
            rez = get_longest_all_perfect_squares(lst)
            print(rez)
        elif cmd == '5':
            break
        else:
            print("Invalid command")



main()