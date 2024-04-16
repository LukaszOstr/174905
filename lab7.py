import pandas as pd
import numpy as np
import openpyxl


s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
#print(s)

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11198846, 1303171835, 32623747]}
df = pd.DataFrame(data)
#print(df)
#print(s['c'])
#print(s.c)
#print("")

#print(df[0:1])
#print("")

#print(df['Populacja'])
#print("")

#print(df.iloc[0, 0])
#print("")

#print(df.loc[0, 'Kraj'])
#print("")

#print(df.at[0, 'Kraj'])
#print("")

#print(df.loc[0])
#print("")

#print('kraj: ' + df.Kraj)
#print(df.sample())
#print("")

#print(df.sample(2))
#print("")
#print(df.sample(frac=0.5))
#print("")
#print(df.sample(n=10, replace=True))
#print("")
#print(df.head())
#print("")
#print(df.head(2))
#print("")
#print(df.tail(1))
#print(df.describe())
#print(df.T)
#print("")

#print(s[(s > 9)])

#print(s.where(s > 10))

#print(s.where(s > 10, 'za male'))

seria = s.copy()
seria.where(seria > 10, 'za male', inplace=True)
#print('########')
#print(seria)

#print(s[~(s > 10)])

#print(s[(s < 13) & (s > 8)])
#
#print(df[df['Populacja'] > 12000000])
#print(df[(df.Populacja > 15000000) & (df.index.isin([0, 2]))])

#print('########')
szukaj = ['Belgia', 'Brasilia']
#print(df.isin(szukaj))

s['e'] = 25
#print(s.e)
s['f'] = 16
#print(s)

df.loc[3] = 'dodane'
#print(df)
#print("")


new_df = df.drop([3])
#print(new_df)
#print("")

df.drop([3], inplace=True)
#print(df)
#print("")

#df.drop('Kraj', axis=1, inplace=True)

df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Poludniowa']
#print(df)

#
#print(df.sort_values('Kraj'))
#print("")

grouped = df.groupby(['Kontynent'])
#print(grouped.get_group('Europa'))
#print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))


