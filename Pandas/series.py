import pandas as pd
import numpy as np

data = {
   'Nome' : ['Alice', 'Jorge', 'Isabella'],
   'Idade' : [35, 25, 23]
}

df = pd.DataFrame(data)
print(df.describe().round(2).to_string()) #Retorna as principais medidas arredondadas

sd = pd.Series(data = [5.50, 7.56, 8.50], index = ['seg', 'terc', 'quar'])
print(sd.describe())

s = pd.Series(np.random.randint(0, 25, 7))
print(s)

series = pd.Series(data = [451, 627, 292, 95], 
                   index = ['Fundamental completo', 
                'Médio completo', 'Superior completo', 'Pós-graduação completa'])

print(series['Superior completo' : ].sum()) #REtorna a quantidade de pessoas com curso superior pra cima

series2 = pd.Series(data = [68, 93, 22, 0], 
                   index = ['Fundamental completo', 
                'Médio completo', 'Superior completo', 'Pós-graduação completa'])

serieResultante = series + series2
print(serieResultante.sum()) #Retorna a nova quantidade de inscritos

s = pd.Series(data = [2, 7, 5, 10, 6], index = ['Wilfred Abbie Harry Julia Carrie'.split()])
print (s[s> s.mean()].index)     #Nome dos alunos que tiraram notas acima da média
