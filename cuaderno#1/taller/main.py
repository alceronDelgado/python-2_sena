import pandas as pd
# TALLER

# CREAR UN NUEVO DATAFRAM DONDE CON UN DICCIONARIO TIPO CLAVE VALOR
# PODER ALMACENAR LA INFORMACIÓN DE 4 ESTUDIANTES. DE LA SIGUIENTE MANERA
# NOMBRE, APELLIDO, NOTA1, NOTA2, NOTA3, DEFINITIVA. IMPRIMIR EL DATA DRAME.

#alumno = {
#    'Nombre':'',
#    'Edad': 0,
#    'Nota1': 0,
#    'Nota2': 0,
#    'Nota3': 0,
#    'Definitiva': 0
#}

data = {
    'Nombre': ['Alejandro', 'Jose', 'Alfredo','Gonzalo'],
    'Edad': [24,23,20,18],
    'Nota1': [3.0,3.2,4.1,3.3],
    'Nota2': [3.0,3.2,4.1,3.3],
    'Nota3': [3.0,3.2,4.1,3.3],
    'Definitiva': [0,0,0,0],
}

df = pd.DataFrame(data)

print(df)