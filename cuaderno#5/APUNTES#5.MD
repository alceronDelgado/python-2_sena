# Merge pandas

para hacer un merge de un dataframe a otro datadrae debemo de tener en común la columna, y también el tipo de dato debe de ser el mismo.

## inner

unir los 2 dataframes que solo traiga lo que coincide
entre los 2 dataframe solo trae su coincidencia

## outer

unir todos los valores tanto la derecha como la izquierda
cuando no hay registro de datos en el dataframe, pandas nos coloca un NaN

## cambiar nombre a las etiquetas que se le han realizado el merge

```PYTHON

pd.merge(df_left, df_right, how='outer', on= 'A', suffixes=['_left', '_right'])

```

## TODO: BUSCAR TEORIA DE CONJUNTOS