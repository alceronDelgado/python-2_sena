# TAREA

---

buscar sobre series en pandas
Que es indexación
Y que es selección de datos

`**Solución**

## Series

---

Se usan 2 estructuras de datos, series y dataframe.
Serie = no es más que una serie de números, datos y/o entidades que tiene indices y datos, donde su indice inicia desde 0.

Una serie le adjunta automáticamente un indice, inicia desde 0.

```python
import pandas as pd


# Crear serie
obj = pd.Series([4,67,-5,3])

# Ver sus valores
obj.values

# Ver sus indeces
obj.index


# Otra forma de definir indices es que nosotros pdoemos definir los indices 
obj2 = pd.Series([4,67,-5,3] ,index = ["a","b","c","d"])

# Si hacemos un print nos muestra los valores con los indices que le determinamos.

# Seleccion de elementos, pdoemos seleccionar el elemento a traves de su indice.

obj2["a"]

# Si hacemos un print su salida en pantalla es 4.


# Seleccionar varios elementos
# Es en doble corchete porque el primer corchete corresponde a donde están ubicado los datos y el segundo corchete a donde debemos determinar los rangos.
obj2[["a","b"]]

# Seleccionar valores con ciertos criterios
obj2[obj2 > 3]

# Operadores = podemos multiplicar los datos 
obj2 * 2


```

## Indexación

### Crear series por medio de diccionarios

```Python

# Tenemos ciudades que se le asignan cada uno de sus indices
sdata = {"Texas" : 31500, "Paris" : 15000, "Dallas" : 4300, "kiev" : 100000 }

# Crear serie, usamos pandas y en el parentesís le entregamos el diccionario de los datos.

objeto3 = pd.Series(sdata)

## Si imprimimos, nos devuelve otra serie que tiene sus indices y sus valores valores

print(objeto3)

## Crear serie en el orden que queramos

# Creamos lista con los siguientes elementos:
state = [ "Paris", "Texas","Dallas","Valle Del Lili"]

# Le mandamos el diccionario que creamos y seguido de una coma con la sentencia index le pasamos los indices que queremos asignarle, en este caso le asignamos la lista states que creamos
objeto4 = pd.Series(sdata,index=state)

print(objeto4)

# Nos muestra en pantalla los datos ordenados pero del orden al que nosotros le colocamos en la lista.



```

### Conocer si algunos datos de la serie es un dato faltante o valido

Existen valores que están vacios.

Si tenemos NaN signficaq ue son valores faltante, por medio de un código podemos desplegar los datos que esten vacios.

```Python
import pandas as pd

sdata = {"Texas" : 31500, "Paris" : 15000, "Dallas" : 4300, "kiev" : 100000 }

state = ["Dallas", "Paris", "Texas","Valle Del Lili"]

objeto4 = pd.Series(sdata,index=state)

# En este código el valor de valle del lili no se encuentra, vamos a traerlo

# Con esto nos muestra TRUE si los datos son vacios
pd.isnull(objeto4)

# Podemos hacerlo al contrario, cuales son los valores que no están vacios

# Nos muestra en true aquellos datos que NO ESTAN VACIOS y con FALSE aquellos datos VACIOS
pd.notnull(objeto4)

# Otra forma, que es lo mismo

objeto4.notnull()
objeto4.isnull()

```

## Operaciones **Entre series**

Podemos multiplicar los datos de los diferentes dataframe, lo que hace es comparar que los indices sean iguales y cuando son iguales, los suma, los que no son iguales no raliza la operación o en su defecto, deja un valor vacio.

```PYTHON
#Ejemplo de suma

import pandas as pd

sdata1 = {
    "Valle grande": 1900,
    "Buga": 7003,
    "Santa Fe": 5257,
    "Puerto Arandano": 4829,
}
sdata2 = {
    "Valle grande": 12500,
    "Floralia": 400,
    "Santa Fe": 983,
    "Puerto Arandano": 3400,
}


index = ["Puerto Arandano", "Valle grande", "Buga", "Santa Fe"]
index2 = ["Puerto Arandano", "Floralia grande", "Valle grande", "Santa Fe"]



objeto1 = pd.Series(sdata1, index = index)
objeto2 = pd.Series(sdata2, index = index2)

print(objeto1)
print("\n")
print(objeto2)
print("\n")

#La salida es la suma de los datos, PERO lo que hace es comparar que sus indices y sus valores sean iguales para que así se puedan multiplicar. 
print(objeto1 + objeto2)

```

## Asignar nombre a las series

```PYTHON

#Podemos ponerle nombre al objeto
obj4.name = "poblacion"

#Ponerle nombre a los indices
obj4.index.name = "estado"

#Salida en pantalla nos muestra el nombre de la serie que le asignamos y el nombre a los indices
print(obj4)

```

## Selección de datos

Para poder seleccionar datos utilizamos iloc, que nos permite traer datos de manera filtrada, según el criterio o la columna como también su fila.
