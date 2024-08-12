#TALLER 3

# FRUTAS Y PLATOS TIPICOS 

# DATAFRAME VA A CONTENER 5 FRUTAS DIFERENTES, 3 CARACTERISTICAS DE LA FRUTA

import pandas as pd

data = {
    'Fruta': ['Mango','Peras','Banano','Sandia','Melon'],
    'Caracteristicas': ['Forma ovalada','Cascara Lisa','Forma alargada', '','']
}

df = pd.DataFrame(data)

print(df[['Caracteristicas','Fruta']])


df.iloc([0,3])
