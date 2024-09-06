# Cuaderno 3 apuntes

~~Podemos usar numpy para realizar calculos y pandas para analizar datos que tenemos~~

## Crear dataframes

opcion 1: crear el arreglo de manera manual

```PYTHON
data = np.array([[1, 4], [2, 5], [3, 6]])
```

OPCIÓN 2: uno de los elementos de las herramentas de pandas es dataframe, tiene una palabra reservada que es DataFrame.

Hay indices para las filas y las columnas

opción 2: crear data a través de un solo arreglo

---

```PYTHON
data = [[1, 4], [2, 5], [3, 6]]

df = pd.DataFrame(data, index=['row1', 'row2', 'row3'],
                 columns=['col1', 'col2'])
```

## Dataframe a través de un diccionario

```PYTHON
equipo_futbol = ['Barcelona','Ac Milan','Argentina','Atletico de bilbao','Napoli','Liverpool']
titulos = [0,10,92,30,20,12]
liga = ['LaLiga','Serie A','Selecció Nacional','La Liga','Serie A','Premier League']

dict_equipos = {
    'equipos': equipo_futbol,
    'titulos': titulos,
    'liga': liga
}

df = pd.DataFrame(dict_equipos)

df
```

## Trabajar un archivo externo separado por comas

P**ASOS**

* Instalar la librería xlsx: pip install xlsx
* Colocar la ruta = podemos trabajar rutas relativas
Si tienes una profundidad muy alta en carpetas PYTHON no te va a funcionar, colocarla máximo el archivo en donde tenga un total de 3 o 4 carpetas como máximo, para evitarse todo eso colocarlo al mismo nivel en donde se ejcuten los dataframe, es decir, en donde se ejecute el parchivo .py

usando la función read_csv vamos a leer el archivo
se puede hacer con excel XLS
XLSX

la diferencia es que XLS es la versión vieja de excel
la versión XLSX trabaja con la versión office 365 y versión recientes

para usar el excel debemos de ver que este instalado la librería xlrd

```PYTHON
df_examenes = pd.read_csv

```

## Leer reportes

df = pd.read_excel('nombre del archivo.xls')

también leer por hojas de excel

pd.read_excel('ruta/al/archivo.xls', sheet_name='NombreDeLaHoja')

## Métodos de pandas

```PYTHON

#mostrar primeras 5 columnas

df_examenes.head() = muestra los titulos

```

VER LOS RESTANTES EN EL CUADERNO DE COLAB

df_examenes.describe() = si a la hora de haer esto nos aparece un float en valores de enteros, significa que hay un NAN y eso daña la eso la estádistica

## Funciones en pandas

en las funciones invocamos la función, llamando la función y le pasamos el parámetro

### longitud

len(df_examenes)

## Operaciones en dataframes

VER LAS OPERACIONES EN EL CUADERO DE COLAB

## Contar valores en data frame

hay 2 maneras

usando la función len y el método count

```PYTHON

#funcion len
len(df_examenes['gender'])

#metodo .count()
df_examenes['gender'].count()


```

## Contando elementos de género por categoría

```PYTHON

df_examenes['gender'].value_counts()

```

Si sumamos los resultado que arroja y no nos da el total de las filas del dataframe, significa que tenemos un error.

## Ordenar descendentemente por múltiples columnas y actualizar el dataframe

```PYTHON

df_examenes.sort_values(['math score', 'reading score'], ascending=False, inplace=True)
df_examenes

```

con el parámetro inplace REEMPLAZA LA DATA QUE ESTÁ EN MEMORIA.
