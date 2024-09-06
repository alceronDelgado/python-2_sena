# Series

Le entregamos los indices y usted nos devuelve los valores que le pedimos
podemos trabajarlo con diccionarios, listas, conjuntos.

Con esto, vamos a poder pedir datos estadisticos.

Después de todo eso, vamos a poder hacer un gráfico de barras.
Gráficos de dispersión,

Todos los temas que estamos viendo vamos a terminar haciendo gráficos con Mathploit.

Todo número que se multiplique por 0 da 0.

Si multiplicamos un valor por null = entonces da null.

la forma de escribir en python por NaN, no va a mostrar nada, NaN se expresa de esa forma pero en pantalla, desde código fuente se maneja con nan.

nan = significa que no hay nada, es vácio, es nulo.

---

si vemos que hay parentesis significa que es una función

```PYTHON

pd.Series(Esto es un parámetro)

```

---

## Series.value

Me trae los valores de la serie

```PYTHON
Series.value()
```

---

Series.shape

trae el tamaño de la series

---

``**Slicing**``

Me trae el número 7, lo que usamos son los indices, no las posiciones.
serie[7]

Si hacemos slicing con doble corchete, lo que hacemos es traer trabajarlo con los indices

```PYTHON

# Me trae los valores que representan a los indices que le mandamos, le damos el número del index.
serie[[0,4,2]]

```

---

## Personalizar indices

```PYTHON
# El index lo que hace es definir lo datos
serie = pd.Series([10,9,8,7], index = ['a','b','c','d','w'])

```

Slicing con los indices

```PYTHON

#Me muestra los datos dicho
serie[['c', 'd', 'e','a']]

# Mue muestra desde la e hasta el final
serie[:'e' ]

# Muestra e hasta que termine
Serie['e':]

# Muestra desde e hasta la z, si el valor no está  aún así pandas sigue recorriendo el valor y llega hasta z
Serie['e':'z']

```

## Definir diccionario como series

llamo la función series y mandamos por parámetro el diccionario, cuando pasamos esto lo que pasa es que mandamos hace que la clave (CO,MX,AR) sean como los títulos de una tabla de excel.

```PYTHON
pd.Series(dict_data, index=['CO', 'MX', 'PE'])
```

## VALORES NULOS

con numpy podemos determinar si el valor es nulo

```python
np.nan * 10
```

## isnull, null

Con esto mostramos si sabemos cuales son los valores nulos, nos devuelve booleanos

```python
serie.isnull()
serie.notnull()
```

## FILTRADO DE DATOS

Usando la función any nos devuelve un true o false si en la serie de los datos esta bien o mal.

serie.isnull().any() #La salida debe ser siempre TRUE, significa que todos los datos está bien establecidos

PARA LA PRÓXIMA CLASE VAMOS A TRABAJAR ARCHIVOS DE EXCEL

Datos unidimensionales = una dimensión, datos de una columna

## PROMEDIO A UNA CANTIDAD DE DATOS

Teniendo una serie, le colocamos la sentencia mean()

```PYTHON

#Notas de la clase con promedio
Series([5.7,8.5,9.1,5.5,8.2,9.0,10,7.0,7.7,9.9],index=["Juan","Jenifer","David","Pablo","Armando","Magdalena","Francesca","Rosmery","Vicente","Martin"].mean())
```

```PYTHON
#Valor máximo
Series([5.7,8.5,9.1,5.5,8.2,9.0,10,7.0,7.7,9.9],index=["Juan","Jenifer","David","Pablo","Armando","Magdalena","Francesca","Rosmery","Vicente","Martin"].max())
```

```PYTHON
#Valor mínimo
Series([5.7,8.5,9.1,5.5,8.2,9.0,10,7.0,7.7,9.9],index=["Juan","Jenifer","David","Pablo","Armando","Magdalena","Francesca","Rosmery","Vicente","Martin"].min())
```

## Rangos de series

usando la función range podemos determinar un rango de funciones, recordemos que un range en python es excluyente.

```PYTHON

ahorros_mensuales = pd.Series(['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],range(100,340,20))
ahorros_mensuales

```

Buscar un poco más sobre NUMEROS ASCII

## FUNCIÓN ILOC

Con la función iloc nos muestra fila columna, df.iloc(fila,columna)

---

## FUNCIÓN LOC

Con la función loc lo que hacemos es extraer los datos del dataframe pero por medio de su indice

```PYTHON
pd= series.loc(fila,columna)
```
