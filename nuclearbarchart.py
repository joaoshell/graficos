# Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns


# Reading data

dados = pd.read_csv('D:/ProgramacaoJoao/bubblegraph/nuclear_explosions.csv')


# Renaming columns

dados.rename(columns = {'WEAPON SOURCE COUNTRY': 'weapon_source_country',
                        'Date.Year':'date_year'}, inplace = True)


# Grouping data and counting ocurrences by year

agrupado = dados.groupby(['weapon_source_country', 'date_year'])['date_year'].count().reset_index(name='count')


# Plotting the graph

fig, ax = plt.subplots()

ax.bar(agrupado['date_year'], agrupado['count'], label=agrupado['count'])

ax.set_ylabel('Date Year')
ax.set_title('Number of warheads deployed')

plt.show()