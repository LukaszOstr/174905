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
        if napis[i] != napis[-i-1]:
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
        k = i
        suma_dzielnikow = 1
        for j in range(2, i):
            if k % j == 0:
                k = k / j
                suma_dzielnikow += j
            if k == 1:
                break
        if suma_dzielnikow == i:
            licznik += 1
    print(licznik)

def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    zad5()
main()