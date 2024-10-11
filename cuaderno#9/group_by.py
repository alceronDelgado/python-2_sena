# Group by practica

import numpy as np
import pandas as pd
import seaborn as sns

# round to two decimal places in python pandas
pd.options.display.float_format = '{:,.2f}'.format

# importamos data por defecto que contiene seaborn
df = sns.load_dataset('tips')
#print(df)


# Traeme todos los datos estadisticos que puedan ser calculados, muestra NaN si no se pueden ser calculados
#print(df.describe(include='all'))

# Veamos cuantas veces se repite los registros de la columna day, cuantas veces se repite
#print("Valores únicos de day \n",df['day'].value_counts())

# aplicar porcentaje a las categorias day, del 100% saber cuanto es el porcentaje que ocupa cada categoriwa.
#print("Valor en porcentajes: \n",df['day'].value_counts()  / df['day'].value_counts().sum() * 100)

# Estimaciones estádisticas por el sexo
"""
No funcionó
sex = df.groupby(['sex']).mean().reset_index()

print(sex)

"""

# Porcentaje de propina y factura para saber cuanto corresponde sobre el total de la cuenta
df['Total_Propina'] = df['tip'] / df['total_bill']

#print("total Propina\n",df['Total_Propina'])
#print("Modificado\n",df)

#Aplicamos la moda en base al total Propina pero agrupandolos con su genero
"""
Con esto, concluimos que las mujeres dan un porcentaje mayor de propina
"""
#print("mean \n",df.groupby('sex',observed=False).mean('tip'))

#Usamos el método median para para poder determinar un valor más real estimado
#print("median \n",df.groupby('sex',observed=False).median('tip'))

# Estimación estadistica por agrupaciones
#print(df.groupby('sex',observed=False)[['total_bill']].describe())
#print(df.groupby('sex')[['porcet_tip']].describe())

# Creamos función de dolares a euros para aplicarla a la columna del dataframe
def euros_a_dolares(x):
    return np.mean(x) * 1.12

#print("No aplicado función \n",df)

#print("aplicado función \n",df.groupby('sex',observed=False)[['Total_Propina','total_bill','tip']].apply(euros_a_dolares))


#Mismo proceso pero con el genero y el horario
#print(df.groupby(['sex','time'],observed=False)[['Total_Propina','tip','total_bill']].apply(euros_a_dolares))

#Desvinculación estandar sobre nuestro grupo
#print(df.groupby(['sex','time'],observed=False)[['Total_Propina','tip','total_bill']].apply(np.std, axis = 0))

#Uusar más de una función, usando la sentencia agregated 
#print(df.groupby(['sex','time'],observed=False)[['total_bill','tip']].aggregate([np.mean, np.max]))

# Crear diccionario de funciones
"""
podemos crear un diccionario en donde según su categoría debe de contener las funciones que puedan ser aplicadas
"""

funciones = {
    "tip": [min,max],
    "total_bill": [euros_a_dolares,np.mean]
}

#print(df.groupby(['sex','time'],observed=False)[['tip','total_bill']].aggregate(funciones))

# Función filtro
"""
vamos a crear una función filtro que nos determine le conversión de un valor con ciertos criterios. En este caso, que el valor de la factura supere el valor de 20.

"""
def filtro(x):
    return euros_a_dolares(x['total_bill'].median()) > 20


#print("Ejecutado funciones \n",df.groupby(['sex','time'],observed=False)[['tip','total_bill']].aggregate(funciones))
#df_filtro = df.groupby(['sex','time'],observed=False).filter(filtro)
#print("Función filtro \n",df_filtro)

"""
group by categorias
"""

# Creamos una columna nueva con el valor de 1 

df['Once'] = 1

#print("dataframe con nueva columna \n",df)

#Creamos dataframe nuevo con columnas de sexo y fumadores y hacemos un count usando la columa previamnte creada, la de onces.

"""
le aplique usando count y dió lo mismo que con el método sum
"""
ds = df.groupby(['sex','smoker'],observed=False)[['Once']].sum()
#ds = df.groupby(['sex','smoker'],observed=False)[['Once']].count()

# Aplicar el porcentaje usando una función lambda

#print(ds.groupby(level=0).apply(
#    lambda x:
#      x / x.sum() * 100
#))


#Podemos hacerlo de esta otra forma
#def porcentaje_once(x):
#    return x / x.sum() * 100
#    #return df['Once'] / df['Once'].sum() * 100

#print(ds.groupby(level=0,observed=False).apply(porcentaje_once))

"""
Crear variable numerica continua en categorica
TODO: buscar sobre que es variable numerica continua
"""

#print(pd.cut(df['total_bill'],bins=3))

# VEAMOS CUALES FUERON LAS CATEGORIAS creadas
#print(pd.cut(df['total_bill'],bins=3).value_counts())

# Definir ancho de nuestras categorias
#print(pd.cut(df['total_bill'],bins=[3,18,35,60]).value_counts())

# ahora que creamos categorias de variables numericas, lo guardamos en el dataframe.

df['total_bins'] = pd.cut(df['total_bill'],bins=[3,18,35,60])

#print(df)

# Usamos las categorias continuas para saber cuantas cenas o almuerzos hubo
#print(df.groupby(['time','total_bins'],observed=False)[['Once']].count())


# Lo transformamos en porcentajes
#print(df.groupby(['time', 'total_bins'])[['Once']].count().groupby(level=0).apply(
#    lambda x:
#      x / x.sum() * 100))

"""
TABLAS DINÁMICAS CON PIVO TABLET

USAREMOS PIVOT TABLET que es propio de pandas para poder crear tablas dinámicas

"""


# Vemos el promedio de el genero y cuando pago su factura

#print(df.groupby(['sex','time'],observed=False)[['total_bill']].mean())

# Del resultado anterior resetearemos el index y trearemos es ereulstrado en una nueva variable, vamos a trabajar con ella
st_total = df.groupby(['sex','time'],observed=False)[['total_bill']].mean().reset_index()

# Crear la tabla dinámica 
print("TABLA DINÁMICA POR DEFECTO: \n",st_total.pivot_table(index='sex',columns='time',values='total_bill', observed=False))

# Cuando creamos la tabla dinámica, por defecto pivot tablet lo que hace es hacer el promedio de cada uno de los registros y los organiza como se lo hemos determinado en los parámetros, en caso de que querramos cambiar la función o el calculo que deseemos hacer, usamos el parámetro aggfunc y seguido de esto la función que queremos que nos aplique.
#print("TABLA DINÁMICA FUNCIÓN DIFERENTE \n",st_total.pivot_table(index='sex',columns='time',values='total_bill', observed=False, aggfunc=np.median))
#print("TABLA DINÁMICA FUNCIÓN DIFERENTE \n",df.pivot_table(index='sex', columns='time', values='total_bill', aggfunc=np.median))

# También podemos pasarle una lista
print("TABLA DINÁMICA FUNCIÓN DIFERENTE \n",df.pivot_table(index='sex', columns='time', values='total_bill', aggfunc=[np.median,np.std]))

# Deshacer categorías
print(st_total.unstack())

# Deshacemos su categoria reseteando el index.
print(st_total.unstack().reset_index())