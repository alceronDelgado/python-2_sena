import pandas as pd
# TALLER 2

# CREAREMOS OTRO NUEVO DATAFRAME.

# NOS PIDEN PARA 5 COLOMBIANOS TIPO DICCIONARIO CLAVE VALOR, DATOS IMPORTANTES
# NOMBRE
#APELLIDO
# DOCUMENTO IDENTIDAD
# ESTATURA EN CENTIMETROS

data = {
    'Nombre': ['Alejandro', 'Isabella', 'Maria', 'Camilo','Diego'],
    'Apellido': ['Gonzalez', 'Millo', 'Doe', 'Smith','Marin'],
    'Documento': ['14620494', '57571895', '39574712', '1107528994','29144652'],
    'Altura_CC': [160,155,175,180,167]
}

df = pd.DataFrame(data)

print(df[['Altura','Apellido','Documento','Nombre']])