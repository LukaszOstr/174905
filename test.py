import math
import random
import sys

#Zad1
suma = 0
for x in range(25,41):
    suma += math.pow(math.sin(x) + math.log(36,4),1/3)
suma = round(suma,2)
#print(suma)

#Zad2
def funkcja(min, max, ile, n):
    if min > max:
        return "error"

    lista = []
    for i in range(ile):
        lista.append(random.randint(min,max))
    k = 0
    for j in lista:
        if(k == n):
            sys.stdout.writelines("\n")
            k = 0
        temp = str(j)
        sys.stdout.writelines(temp)
        sys.stdout.writelines(" ")

        k += 1

min = 2
max = 9
ile = 25
n = 5
#funkcja(min, max,ile,n)


#Zad3
def plik(nazwa_pliku):
    a = open(nazwa_pliku,"r")
    b = a.readlines()
    for line in b:
        temp = [int(i) for i in line.split()]
        min = temp[0]
        for i in temp:
            if (i < min):
                min = i
        print(min)

#plik('liczby.txt')



#Zad4
def pole(a,h):
    if(a<0 or h<0):
        return "Dlugosci nie moga byc ujemne"
    else:
        return a*a*h
a = int(input("Wpisz dlugosc boku podstawy: "))
h = int(input("Wpisz wysokosc graniastoslupa: "))
print(pole(a,h))

