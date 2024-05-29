import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




def zad2():
    x = np.arange(1,20)
    y = 1/x

    plt.plot(x, y, 'g>:', label='f(x) = 1/x',)
    plt.title("Wykres funkcji f(x) dla x[1,20]")

    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.xticks(np.arange(0, 21, 2.5))
    plt.yticks(np.arange(0, 1.1, 0.2))

    plt.legend()

def zad3():
    x = np.arange(0, 30.05, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, 'g', label='y = sin(x)')
    plt.plot(x, y2, 'r', label='y = cos(x)')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.xticks(np.arange(0, 30, np.pi))

    plt.legend()

def zad5():




def main():
    #zad2()
    #zad3()
    zad5()
    plt.show()



main()