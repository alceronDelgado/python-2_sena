# Cuaderno 4 PANDAS + MATPLOID + SEABORN

---

SEGÚN EL TIPO DE GRÁFICO SE DEBE DE APLICA SI ES EJE X O Y.


## Funciones lamba

funciones máginas que nos permite agrupar 

Cuando tenemos un archivo modificado por comas entones los decimales debe de ir por puntos y no por comas, no es un error como tal sino una ambiguedad.

# TODO: Buscar sobre seaborn 

# Seaborn

seaborn = es una alternativa de matplotlib 

---

## Matplotlib

matplotlib = tiene diagrama de barras, histograma, diagrama de sectores, caja y bigotes, dispersión de puntos.

---

Podemos instalar seaborn con matplotlib ya que algunas veces podemos acceder a ciertas funciones de matplotlib e implementaremos pandas y numPy para implementar los datos y valores que queramos agregar.

## GRÁFICOS

Las gráficas no sirven para todos los escenarios


## Crear gráficos básicos

```PYTHON


```
 
**Cada gráfica tiene su respectiva utilidad**


### Gráficos de dispersión

tiene que ver co el promedio, que tan alejado esta del promedio

cargamos los ejes con 2 listas,


### Gráfico de histograma

Sirve para visualizar el proceso de un elemento o un evento como encuesta o algo, de una tendencia, hacía donde va.

no se le pasa valores de x o y 

### Gráfico de barras apiladas.

acá podemos implementar numpy.

### Gráfico de barras

comprar valores entre categorías.

### Gráfico de burbujas

TODO: BUSCAR(CLOSTERIZACIÓN = AGRUPAR LOS DATOS)
TODO: BUSCAR gráfico de control.

```PYTHON
"""Gráfico de Superficie
Los gráficos de superficie muestran una representación tridimensional de los datos."""
import matplotlib.pyplot as plt
## con esto nos sirve para crear gráficas en 3 dimensiones
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np

# Datos de ejemplo
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfico de Superficie')

plt.show()

```

**El valor de python** viene desde estadistica.


### Gráfico de violín

aca podemos importar seaborn, hace que sea un poco más detallado el gráfico, habla a traves de distribución de probabilidad.

si implementamos matplotlib con seaborn es como un complemento

```PYTHON
"""Gráfico de Violín
El gráfico de violín muestra la distribución de los datos a través de la densidad de probabilidad."""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Datos de ejemplo
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure(figsize=(10, 6))
sns.violinplot(data=data)
plt.xlabel('Grupos')
plt.ylabel('Valores')
plt.title('Gráfico de Violín')
plt.grid(True)
plt.show()
```

### Gráfico de pastel

SIRVE PARA MOSTRAR PORCENTAJES DE UN TOTAL.

### Gráfico de boxplot

TODO: buscar sobre gráfico de caja boxplot


### matplot

plt.anotate = sirve para colocar anotaciones sobre el gráfico

podemmos re ajustar la flecha y todo lo demás.


### Gráfico de paleto

se combina gráfico de líneas con barras.

ley 8020 = en el 20 está el 80
es una ley para detectar problemas en costo

### Gráfico de error

indica el grado de error de un proceso, un error... cuesta dinero.

### Gráfico de error

para usar este gráfco se debe usar la librería de networkx

TODO: BUSCAR SOBRE Networkx