import sys

lista = [6, 4, 9.8, 10, 2]
print(lista)
lista.sort()
print(lista)
lista.append(8)
print(lista)
lista.insert(3, 54)
print(lista)
del lista[3]
print(lista)
lista.reverse()
print(lista)

znaki = 'abcde'
print(znaki[2])
print(type())

slownik = {'a': 1, 'b': 2, 'c': 3}
print(slownik)
print(slownik['a'])
slownik.pop('b')
print(slownik)
print(slownik.keys())
print(slownik.values())

# liczba = input('Wprowadz liczbe: ')
# print(liczba + ' to wczytana liczba')
# sys.stdout.write('Wprowadz liczbe: ')
# liczba = sys.stdin.readline()
# print(type(liczba))
# liczba = int(liczba)
# print(type(liczba))
# print(liczba + ' to wczytana liczba')