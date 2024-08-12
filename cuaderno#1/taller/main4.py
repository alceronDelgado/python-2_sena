# TALLER 4

# FERRETERIA

# 5 ELEMENTOS EN UN CLAVE VALOR, 4 CARACTERISTICAS PARA CADA ELEMENTO.
#DEBO INSTALAR PANDAS
import pandas as pd

data = {
    'Herramienta': ['Zerrucho','Martillo','Tornillo','Tubos','Pintura'],
    'Caracteristicas1': ['Es cortortante','Diferentes tamaños','Oxidante', 'Pesado','Tiene soporte de madera'],
    'Caracteristicas2': ['Diferente material','Facil de usar','Diferente color', 'Pesado','Apuntillar cualquier cosa'],
    'Caracteristicas3': ['Diferente color','es accesible de comprar','Diferentes marcas', 'multiples tamaños','imantados'],
    'Caracteristicas4': ['Diferente color','diferente medida','para cable y acueducto', 'Fácil de cortar',''],
}

df = pd.DataFrame(data)

df.info()
print(df)




data = {
    'Herramienta': ['Zerrucho','Martillo','Tornillo','Tubos','Pintura'],
    'Caracteristicas1': [['Es cortortante','Diferentes tamaños','Oxidante', 'Pesado','Tiene soporte de madera'],['Diferente material','Facil de usar','Diferente color', 'Pesado','Apuntillar cualquier cosa']],
    'Caracteristicas2': [],
    'Caracteristicas3': ['Diferente color','es accesible de comprar','Diferentes marcas', 'multiples tamaños','imantados'],
    'Caracteristicas4': ['Diferente color','diferente medida','para cable y acueducto', 'Fácil de cortar',''],
}

