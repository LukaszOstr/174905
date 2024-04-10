import numpy as np

def zad1():
    a = np.arange(3,46,3)
    print(a)


def zad2():
    list = [3.4, 21.43, 9.12]
    a = np.array(list)
    print(a)
    b = a.astype(dtype='int64')
    print(b)
    c = np.array(list, dtype='int32')
    print(c)


def zad3(n):
    a = np.arange(1,n*n+1)
    b = a.reshape((n,n))

    print(b)

def zad4(podstawa, ilosc):
    a = np.logspace(1,ilosc,num=ilosc,base=podstawa)
    print(a)


def zad5(dlugosc):
    v = np.arange(dlugosc,0,-1)
    mat = np.diag(v)
    print(mat)


def zad6():
    mrowka = np.array(list('mrowka'))
    armata = np.array(list('armata'))
    armata = np.flip(armata)
    malina = np.array(list('malina'))

    wykreslanka = np.diag(mrowka)
    wykreslanka[:,0] = malina
    wykreslanka[5, :] = armata

    print(wykreslanka)


def zad7(n):

    lista=[]
    for i in range(n):
        lista.append(2)


    mat = np.zeros((n,n))
    for i in range(n):
        mat += np.diag([a for a in range()],-1)

    print(mat)


def main():
    #zad1()
    #zad2()
    #zad3(4)
    #zad4(6,4)
    #zad5(4)
    #zad6()
    zad7(3)


main()

