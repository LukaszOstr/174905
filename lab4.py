import math
import random


def zad1():
    a = round((math.exp(4) - math.log(34, 2)) ** 1/3, 2)
    b = round((math.log(20) + math.cos(45) + math.exp(1)) ** 1/3, 2)
    c = round((math.log(20, 3) + math.sin(45) * 5/8) ** 1/4, 2)
    d = round(math.log(23, 3) + (math.sin(34) + 5) ** 1/3, 2)
    e = round((math.log(32, 2) + math.pi + math.sin(56)) ** 1/4, 2)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


def zad2():
    n = int(input())
    if n < 10:
        for i in range(1, n+1):
            print(i * "A")


def zad3():
    n = int(input())
    if n < 10:
        print(n * " " + "A")
        for i in range(1, n):
            print((n-i) * " " + (2*i + 1) * "A")


def zad5():

    n = int(input())
    for i in range(n):
        # lista = []
        suma = 0
        for j in range(n):
            a = random.randint(1, 100)
            suma += a
            # lista.append(a)
        # print(lista)
        print(suma)


def main():
    # zad1()
    # zad2()
    # zad3()
    zad5()


main()
