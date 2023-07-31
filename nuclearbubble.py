# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reading data
dados = pd.read_csv('') #add the path and file to read it


# enaming columns
dados.rename(columns = {'WEAPON SOURCE COUNTRY': 'weapon_source_country','Data.Purpose':'data_purpose',
                        'Date.Year':'date_year', 'Data.Yeild.Lower': 'data_yeild_lower', 'Data.Yeild.Upper': 'data_yeild_upper'}, inplace = True)


# grouping data and counting how many occurences by year
agrupado = dados.groupby(['weapon_source_country', 'data_purpose', 'date_year'])['date_year'].count().reset_index(name="count")


# setting the scope to wr purposes
data = agrupado.loc[agrupado.data_purpose == 'Wr']

# plotitng the graph

sns.set_style("whitegrid") #settint the grid to white

#plotting with three dimentions and coloring it with the hue feature
sns.scatterplot(data=data, x="date_year", y="count", size="weapon_source_country", hue="weapon_source_country", legend=True, alpha=1, sizes=(1, 300))

#renaming the axis
plt.xlabel("Year")
plt.ylabel("Quantity")

#relocating the legend
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', fontsize=10)

#showing the result
plt.show()
