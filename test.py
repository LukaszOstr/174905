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
    try:
        if ile <= 0:
            raise ValueError

        lista = []
        for i in range(ile):
            lista.append(random.randint(min,max))
        print(lista)

        result_list = []
        if ile % n == 0:
            for i in range(0,len(lista),n):
                temp_list = []
                for j in range(i,i+n):
                    temp_list.append(lista[j])
                result_list.append(temp_list)
        else:
            raise ValueError
        return result_list

    except ValueError:
        return "error"

min = 2
max = 9
ile = 24
n = 3
#print(funkcja(min, max,ile,n))


#Zad3
def plik(nazwa_pliku):
    a = open(nazwa_pliku,"r")
    b = a.readlines()
    lista = []
    for line in b:
        temp = [int(i) for i in line.split()]
        min = temp[0]
        for i in temp:
            if (i < min):
                min = i
        lista.append(min)
    print(lista)

plik('liczby.txt')



#Zad4
def pole():
    try:
        a = int(input("Wpisz dlugosc boku podstawy: "))
        h = int(input("Wpisz wysokosc graniastoslupa: "))
        if(a < 0 or h < 0):
            raise ValueError
        return a*a*h
    except ValueError:
        return "error"
#print(pole())

