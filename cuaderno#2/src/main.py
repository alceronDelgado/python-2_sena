import pandas as pd
import numpy as np

# crear serie en pandas

serie = pd.Series([10,20,30])

# Trabajar con diccionarios.

dict_data = {'CO':100,'MX':200,'AR':300}

ahorros_mensuales = pd.Series(['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio'].range(200,350,25))
ahorros_mensuales



dict_data = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'idioma': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}
dict_data