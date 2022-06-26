# Carregue conjunto de dados chamado kc_house_csv do HD para a memória
#pip install pandas
import pandas as pd

#Função
#Biblioteca Pandas - excluisva para manipulação de dados
data = pd.read_csv('datasets/kc_house_data.csv')

#Mostre na tela as 5 primeiras linhas do conjunto de dados.
#print(data.head())

#Mostre o número de colunas e número de linhas dos conjunto de dados
#print(data.shape)

#Mostre o nome das colunas do conjunto de dados
#print(data.columns)

#Mostre na tela o conjunto de dados ordenados pela coluna price
#print(data[['id', 'price']].sort_values('price'))

#Mostre na tela o conjunto de dados ordenados pela coluna price do maior para menor
print(data[['id', 'price']].sort_values('price', ascending=False))

