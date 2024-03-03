import sys


# lista = [5, 23, 76, 2, 4, 25]
# a = int(input('Wprowadz liczbe: '))

# if a ** 2 in lista:
# print('kwadrat wystepuje')
# else:
# print('kwadrat nie wystepuje')

def zad1():
    zdanie = str(input())
    slowa = zdanie.split()
    print(len(slowa))


def zad2():
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    x = str(a ** b + c)

    sys.stdout.write(x)


def zad3():
    napis = str(input())
    i = 0
    palindrom = True
    while i < len(napis) - 1:
        if napis[i] != napis[-i - 1]:
            palindrom = False
            break
        i += 1
    if palindrom:
        print("Napis jest palindromem")
    else:
        print("Napis nie jest palindromem")


def zad4():
    liczba = int(input())
    pierwsza = True
    for i in range(2, liczba):
        if liczba % i == 0:
            pierwsza = False
            break
    if pierwsza:
        print("Liczba jest pierwsza")
    else:
        print("Liczba nie jest pierwsza")


def zad5():
    licznik = 0
    for i in range(1, 1001):
        suma_dzielnikow = 0
        for j in range(1, i):
            if i % j == 0:
                suma_dzielnikow += j
        if suma_dzielnikow == i:
            licznik += 1
    print(licznik)


def zad6():
    a, b, c = 3, 13, 7
    x, y, z = 1.2, 5.8, 2.0
    lista = [a, x, y, c, z, b]
    print(lista)
    for i in range(len(lista) - 1):
        lista[i] *= lista[i]
    print(lista)


def zad7():
    i = 10
    lista = []
    while i > 0:
        a = int(input("Wczytaj liczbę: "))
        if a % 2 == 0:
            lista.append(a)
        i -= 1
    print(lista)


def zad8():
    lista = [2, 31.5, 'abc', 6, 31.5, 31.5, 'abc', 2, 4346, 'xyz']
    slownik = {}
    klucze_lista = []
    for i in lista:
        if i not in klucze_lista:
            klucze_lista.append(i)
            slownik[i] = 1
        else:
            slownik[i] += 1
    print(slownik)

    for i in klucze_lista:
         if type(i) is str:
            del slownik[i]

    print(slownik)


def main():
    # zad1()
    # zad2()
    # zad3()
    # zad4()
    # zad5()
    # zad6()
    # zad7()
    zad8()

main()
