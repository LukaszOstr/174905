import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# dane = pd.read_csv('dane.csv', sep=';')
imiona = pd.read_excel("imiona.xlsx")
zamowienia = pd.read_csv("zamowienia.csv", delimiter=';')


#Zad1
a = imiona.groupby('Rok').sum()['Liczba']
a.plot()


#Zad2
b = imiona.groupby('Plec').agg({'Liczba':['sum']})
#print(b)


b1 = b.plot.bar()
b1.set_ylabel('Mln')
b1.set_xlabel('Plec')
b1.tick_params(axis='x', labelrotation=0)
b1.legend()
b1.set_title('Liczba urodzonych chlopcow i dziewczynek')


#Zad3

c = imiona[imiona['Rok'] >= 2013].groupby('Plec').agg({'Liczba':['sum']})
#print(c)

c1 = c.plot(kind='pie',subplots=True, autopct='%.2f%%')
plt.title('Ilosc urodzonych chlopcow i dziewczynek w ostatnich 5 latach')


#Zad4
d = zamowienia.groupby('Sprzedawca').agg({'idZamowienia':['count']})
#print(d)
d1 = d.plot.bar()
d1.set_ylabel('Ilosc zlozonych zamowien')
d1.set_xlabel('Sprzedawca')
d1.set_title('Ilosc zlozonych zamowien przez poszczegolnych pracownikow')





plt.show()

