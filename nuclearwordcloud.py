# Import libraries

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Read data

dados = pd.read_csv('D:/ProgramacaoJoao/bubblegraph/nuclear_explosions.csv')


# Renaming Columns

dados.rename(columns = {'WEAPON SOURCE COUNTRY': 'weapon_source_country','WEAPON DEPLOYMENT LOCATION':'weapon_deployment_location','Data.Source':'data_source', 'Data.Purpose': 'data_purpose', 'Data.Name': 'data_name', 'Data.Type':'data_type'}, inplace = True)

# Instantiate lists

columns_list = ['weapon_source_country', 'weapon_deployment_location', 'data_source', 'data_purpose', 'data_name', 'data_type']
words_list = []


# Looping through columns and generating words list/string

for i in columns_list:
    for j in range(0, len(dados[i])):
        #print(dados[i][j])
        words_list.append(dados[i][j])

words_string = ' '

for i in range(0, len(words_list)):
    a = words_list[i]
    words_string += ' ' + a.strip()


# Ploting word cloud


word_cloud = WordCloud(width=1000, height=500, collocations=False).generate(words_string)

#width=480, height=480, margin=0, max_words=25, collocations=True, repeat=False

plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

image = word_cloud.to_file('D:/ProgramacaoJoao/bubblegraph/nuclearwordcloud_figure_1.png')