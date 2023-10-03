import pandas as pd 

datos = pd.read_csv('datos.csv')
print(datos)

wines = wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(wines.shape)
print(wines.head)

