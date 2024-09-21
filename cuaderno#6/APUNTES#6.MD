# Como lidar con datos faltantes en dataframes

## nan

significa not a number, no tiene absolutamente nada.

## CONOCER NÚMERO DE FILAS NULAS

usando el parámetro axis=1

se le da el valor de 1 poruqe le indicamos que se vaya por la coordenada x, es decir, por la fila.

## Conocer TODOS LOS NULOS.

**size-df ** tamaño del dataframe
**sum().sum()*** que me recorra y me suma las filas y columnas
df.size-df.isnull().sum().sum()

## DROPNA

TODO: buscar sobre group by
