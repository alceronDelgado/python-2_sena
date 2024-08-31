import pandas as pd
import numpy as np

#1- Aca se crea el dataframe directamente con read_csv
#df_datos = pd.read_csv('bestsellers_with_categories.csv')

df_datos = pd.read_csv('src/bestsellerswithcategories.csv')

#2- Muestra primeros 5 registros
#print(df_datos.head())

#2.1 - Muestra datos estadisticos del dataframe
#print(df_datos.describe())

#3- Agregar una nueva columna y crear numeros aleatorios usando numpy

#3.1 -Creamos numeros aleatorios
calificacion_critica = np.random.randint(1,5,550)

#3.2 - Agregamos la columna
df_datos['Calificación de la critica'] = calificacion_critica

#4- Atributos, funciones y métodos básicos del dataFrame

    #4.1-Atributos
    #Dimensión
#print(df_datos.shape)

    #Datos del indice, su inicio, final y cada paso de itineración
#print(df_datos.index)

    #Muestra nombre de las columnas
#print(df_datos.columns)

    #Muestra el tipo de dato de cada columna
#print(df_datos.dtypes)

    #4.2 -Métodos del dataframe

    #Muestra primeros 5 elementos del dataframe
#print(df_datos.head())

    #Muestra los 5 últimos elementos del dataframe
#print(df_datos.tail())

    #Muestra info del dataframe
#df_datos.info()

    #Estadisticas básicas del datafram
#print(df_datos.describe())

    #4.3 -Funciones del dataframe

    #Obtener longitud del dataframe
#print(len(df_datos))

    #Obtener el valor máximo del dataframe del index o de cualquier columna
#print(max(df_datos.index))

    #Obtener el valor mínimo del dataframe del index o de cualquier columna
#print(min(df_datos.index))

    #Obtener tipo de datos
#print(type(df_datos))

    #Redondear valores del dataframe
#print(min(df_datos))


#5 Seleccionar 2 o Más columnas
#print(df_datos.columns)
#Ordenar las columnas
columns=['Name', 'Author', 'User Rating', 'Calificación de la critica','Reviews', 'Price', 'Year', 'Genre']
#Cambiar posición de las columnas en dataframe
df_datos = pd.DataFrame(df_datos,columns=columns)

#Mostrar cambios
#print(df_datos.columns)

#6 Operaciones
# Creamos nueva columna y aplicamos operación
df_datos['Calificación Promedio']= round((df_datos['Calificación de la critica'] + df_datos['User Rating'])/2)

#6 operaciones
# Corregido = HAY QUE COLOCARLE EL 1 PARA INDICARLE QUE ES DE UN SOLO DECIMAL, Si no se coloca, le quita los decimales, se transforma a un ENTERO pero visualmente se ve como un DECIMAL
df_datos['Calificación Promedio'] = round(df_datos['Calificación de la critica'] + df_datos['User Rating']/2,1)

#Actualizamos el dataframe
df_datos.update(df_datos)
#Mostramos en pantalla el dataframe
#print(df_datos)

# 7 Contar elementos de genero por categoria 
#print(df_datos['Genre'].value_counts())

# Devolver frecuencia relativa
#print(df_datos['Genre'].value_counts(normalize=True))

# 8 Actualizar nombre de columnas
columnas_nuevas = {
    'User Rating': 'UR',
    'Calificación de la critica': 'CR',
    'Calificación Promedio':'AR'
}
df_datos.rename(columns=columnas_nuevas,inplace=True)

#Seleccionar columnas del dataframe
#print(df_datos[['Name','Author','UR', 'CR', 'AR','Year']])

#Corregido = cambiado la forma de ordenar y actualizar dataframe, solamente es asignar re asignar la variable
df_datos = df_datos[['Name','Author','UR','CR','AR','Year']]

# 9 ordenar dataframe en orden descendente por UR y CR y actualizar dataframe
df_datos.sort_values(['UR','CR'],ascending=False,inplace=True)
print(df_datos)

## TODO: PREGUNTARLE AL INSTRUCTOR SI LA INSTRUCCIÓN UPDATE FUNCIONA PARA ACTUALIZAR O SE DEBE USAR INPLACE=TRUE