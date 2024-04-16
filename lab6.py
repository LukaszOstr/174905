import numpy as np
import math


#a = np.arange(12).reshape((3,4))

#print(a)

#suma calej macierzy
#print(a.sum())

#suma kazdej z kolumn
#print(a.sum(axis=0))

#minimum kazdego wierszu
#print(a.min(axis=1))

#skumulowana suma dla rzedu
#print(a.cumsum(axis=1))


#b = np.arange(3)
#print(b)
#print(np.exp(b))
#print(np.sqrt(b))

#c = np.array([2., -1, 4.])
#print(np.add(b, c))

#a = np.arange(12).reshape((3,4))
#print(a)

#for b in a:
    #print(b)
    #print("")

#d = c.ravel()
#print(d)
#print(d.shape)



#Zad1

#a = np.array([5, 2, 4])
#b = np.array([-2, 1, 5])
#print(a * b)

#zad2
#c = np.array([[4,6,2],[5,5,1],[5,6,2]])
#d = np.array([[1,2,7],[4,8,0],[3,6,7]])

#print(a)
#print(b)
#print("")
#print(a.min(axis=0))
#print(a.min(axis=1))
#print("")
#print(b.min(axis=0))
#print(b.min(axis=1))

#zad3
#print(a.dot(b))

#zad4
e = np.array([3, 8, 1])
f = np.array([2.1, 5.9, 1.6])
#print(e*f)

#zad5
g = np.array([[1, 6, 2],[8, 2, 5]])
for a in g:
    for b in a:
        print(math.sin(b))