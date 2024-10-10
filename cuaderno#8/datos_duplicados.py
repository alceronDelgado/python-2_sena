import pandas as pd

duplicate = {
    "a" : ["H"] * 2 + ["O"] * 3 + ["L"] * 4 + ["A"] * 5,
    "b" : ["1"] * 2 + ["2"] * 3 + ["3"] * 4 + ["4"] * 5,
}

df = pd.DataFrame(duplicate)

#print(df)

# Encontrar datos duplicados, muestra un true
#print(df.duplicated())

# Sentencia first and last
"""
se usa para validar cuales datos son duplicados o no. por defecto marca el last
"""

#print(df.duplicated(keep='first'))
#print(df.duplicated(keep='last'))

## sacar los datos no duplicados, lo negamos usando el caracter "~"
#print(df[~df.duplicated()])

## sacar exclusivamente los datos duplicados
#print(df[df.duplicated(keep=False)])

# Eliminar duplicados, por defecto, guarda los del primer elemento keep="first"
print(df.drop_duplicates(["a"],keep="last"))
