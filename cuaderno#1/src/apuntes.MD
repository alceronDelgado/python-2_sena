# python-2_sena

Apuntes python PATH SENA 2

---

## Análitica de datos o ciencia de datos

`Las listas, tuplas, Colecciones y conjuntos en general son considerado COLECCIONES.`

``` python

#Lista (arrays)
lista_numeros = Listas[1,2,3,4,5]
#Tupla
tupla_numeros = tuple(1,3,4,6,5)
#Conjunto
alejandro = {
    key: 1,
    value: "alejandro"
}
Conjuntos{
    'Item 1', 'Item2', 'Item N'
}
```

## Data

Data frame y data set son diferentes, son completamente diferentes

Elemmentos de dos dimensiones data frame, es el principio de las colecciones.
Permite manejar volumenes amplios de datos, pero de 2 dimenciones

`Data Set` = maneja largo, por ancho y por altura. Lo podemos usar para cconectarnos a una base de datos relacional o no relacional.

---

## DataFrame

Estructura de datos bidimensional
Etiquetas = a que se refiere?
Flexbilidad = puede manejar datos restantes, y manipular la información.

## DataSet

Pueden unidimensionales(lista de valores) o multidimensionales(tabla con varias columnas y filas)

CSV = Comma-separated values
JSON = Archivo ordenado estructurado.

EN UN DATA SET SE PUEDE MODIFICAR LA INFORMACIÓN?

Con el dataSet cargamos la información al dataframe para poder trabajar con esos datos.

## NUMPY

Con numpy si implementamos datos de tipo string e int no marca un error pero no es recomendable, nos muestra un dtype, significa que hasta cierto punto numpy si te recibe los datos independientemenete de su tipo.

```python
dtype='<U21' que es como una advertencia.>'
```

### funciones NUMPY

> SHAPE

nos muestra la dimensión de la lista

arrays = cuando inicializamos un array de derecha a izquierda debemos indicarle que arranque en -1

```python
np.array([[1,2,3,4],[6,7,8,9]]).shape = (2,4)
```

`Las listas deben ser homogenemos, en filas y columnas`

slicing = cortar una pequeña parte del elemento.

## PANDAS

En pandas para definir valores exige simetría.

Cuando escribimos la función DataFrame lo primero que hace es definir la simetría de los datos, si la simetría de los datos es homogenea, no tendrá problemas al visualizar los datos.

## describe

me muestra una descripción de los datos del dataframe, este nos muestra un minímo, máximo, etc.

```python
df.describe()
```

> Etiquetas de filas y columnas.

sirve para saber en que paso ubicación está el índice del elemento.

```python
df.index

#start = inicia en 0
#stop = termina en 5
#step = con paso en 1
rangeIndex(start=0, stop=5, step=1)
```

> VALUES

extraer en un arreglo los valores del data frame.

```python
df.values()
```

## Otros

```python

# Si la función no tiene parentesis, significa que no lleva parámetros.

df.info() #Muestra promedio de los elementos, máximo, minimo, porcentajes, etc.
print(df)
df.describe() #Nos muestra los tipos de datos que hay, su dimensión... entre otros
df.index # Nos muestra en donde se encuentra el elemento
df.columns # trae las columnas del dataframe
df.values # trae los valores pero en un arreglo
```

## Extracción de datos

```python
df['Caracteristicas1'] # me trae exclusivamente la columna que queremos
print(df[['Columna1', 'Columna 2']]) # Me trae las columas que queremos, el primer corchete es el dataframe, el segundo las columnas que quiero traer
```

## loc

extrae datos de las etiquetas como las filas o las etiquetas.

```python
#Es una localización de datos.
df.iloc[0,0]

print(df3.iloc([0,1])) # TODO: POR MEJORAR Y ENCONTRAR TODOS DATOS

```

## df.iloc con condiciones

Usamos la funcion iloc para poder definir o extraer los datos pero que se definan con ciertos criterios, como por ejemplo que un dato sea mayor a 3.

```python
df ['Nota3'] > 3 # Extrae los datos con condicionales.
```

## TAREA

buscar sobre series en pandas
Que es indexación
Y que es selección de datos
