import random
import math

def zad1():
    A = [1-x for x in range(1,11)]
    B = [4 ** x for x in range(7)]
    C = [x for x in B if x % 2 == 0]
    print(A)
    print(B)
    print(C)


def zad2():
    lista1 = []
    for i in range(10):
        lista1.append(random.randint(1, 101))
    print(lista1)

    nowa_lista = [x for x in lista1 if x % 2 == 0]
    print(nowa_lista)

def zad3():
    produkty = {'ziemniaki': 'kg', 'bulki': 'sztuki', 'jablka': 'kg', 'batony': 'sztuki'}
    produkty_sztuki = [x for x in produkty.keys() if produkty[x] == 'sztuki']
    print(produkty_sztuki)


def zad4():
    def trojkat_prostokatny(a,b,c):
        if ((a>b and a>c and a<b+c) or (b>a and b>c and b<a+c) or (c>b and c>a and c<a+b)):
            print("Trojkat o podanych wymiarach jest prostokatny")
        else:
            print("Trojkat o podanych wymiarach nie jest prostokatny")


def zad5():
    def pole_trapezu(a=1, b=1, h=1):
        return (a + b) * h / 2


def zad6():
    def iloczyn_el_ciagu(a=1, b=4, ile=10):
        suma = a
        for i in range(1,ile+1):
            suma += a*b**i
        return suma


def zad7():
    try:
        a = float(input())
        print(math.sqrt(a))
    except ValueError:
        print("Wartosc nie moze byc ujemna")

def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    #zad6()
    zad7()

main()