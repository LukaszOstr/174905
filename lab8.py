import pandas as pd
import numpy as np
import openpy

# Zad1
x = pd.read_excel("imiona.xlsx")
imiona = pd.DataFrame(x)

# Zad2
a = imiona[imiona['Liczba'] > 1000]
b = imiona[imiona['Imie'] == 'ŁUKASZ']
c = imiona['Liczba'].sum()
d = imiona['Liczba'].where((imiona['Rok'] <= 2005) & (imiona['Rok'] >= 2000)).sum()
e = imiona.groupby('Plec').sum()['Liczba']
f = imiona.groupby(['Rok','Plec']).head(1)
g = imiona.sort_values('Liczba',ascending=False).groupby('Plec').head(1)

# Zad3
y = pd.read_csv("zamowienia.csv", delimiter=';')
zamowienia = pd.DataFrame(y)

h = zamowienia['Sprzedawca'].unique()
i = zamowienia['Utarg'].sort_values(ascending=False).head()
j = zamowienia.groupby('Sprzedawca').count()['idZamowienia']
k = zamowienia.groupby('Kraj').count()['idZamowienia']
l = zamowienia.where(zamowienia['Rok'].dt.year == 2005)

print(k)

