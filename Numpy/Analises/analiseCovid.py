import pandas as pd
from urllib.request import urlretrieve      #Pegar base dados de uma url
import matplotlib.pyplot as plt             #Mostrar os dados analisados
 

url = ('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
urlretrieve(url, 'Numpy/Analises/dataBase/global-cases-covid.csv')

dfCovid = pd.read_csv('Numpy/Analises/dataBase/global-cases-covid.csv')  #Realiza a leitura do arquivo

#Gráfico de barras
dfCovid.drop(['Lat', 'Long'], axis = 1, inplace = True)     #Excluindo as colunas Lat e Long
dfCovidPaises = dfCovid.groupby('Country/Region').sum()     #Agrupando as tuplas por país

sBrasil = dfCovidPaises.loc['Brazil']                       #Selecionando a tupla Brazil
sBrasil[sBrasil > 0]                                        #Pegando apenas os casos acima de 0

tamanho = len(sBrasil)                                      #Pegando o tamanho para definir os 30 últimos dias


plt.figure(figsize= (15.0, 8.0))                            #Dinindo o tamanho da imagem
plt.xticks(rotation = 60)                                   #Grau de rotação dos valores no eixo X
plt.bar(sBrasil.index[tamanho - 30:tamanho], sBrasil.values[tamanho - 30:]) 
plt.title('Total de casos confirmados de COVID-19 no Brasil, nos últimos 30 dias')  #Título
plt.savefig('Numpy/Analises/dataBase/Grafico-casos-Brasil.png') #Cria uma imagem neste diretório
