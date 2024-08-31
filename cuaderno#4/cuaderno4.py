import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Nombre': ['Lionel', 'Cristiano', 'Neymar', 'Kylian', 'Robert', 'Kevin', 'Virgil', 'Sergio', 'Eden', 'Mohamed'],
    'Apellido': ['Messi', 'Ronaldo', 'Neymar', 'Mbappe', 'Lewandowski', 'De Bruyne', 'Van Dijk', 'Ramos', 'Hazard', 'Salah'],
    'Liga': ['La Liga', 'Serie A', 'Ligue 1', 'Ligue 1', 'Bundesliga', 'Premier League', 'Premier League', 'La Liga', 'La Liga', 'Premier League'],
    'Salario': [65000000, 54000000, 36000000, 35000000, 45000000, 33000000, 25000000, 30000000, 25000000, 20000000],
    'Temporada': [2018, 2023, 2022, 2022, 2022, 2022, 2022, 2022, 2014, 2022],
    'Goles': [30, 28, 22, 25, 35, 18, 12, 15, 10, 20]
}

# reset index = importante resetear elindex porque si no va a tener en cuenta el index del anterior dataframe

df = pd.DataFrame(data)

# Punto 1 jugadores por liga

players_by_league = df.groupby(['Liga','Nombre']).mean()

print(players_by_league)


# Punto 3
top_goals = df.groupby('Temporada')['Goles'].sum()

#print(top_goals)

# Punto 4

prom_player = df['Goles'].mean()

# Buscar salario

salary = df['Salario']


# Punto 5 Goles máximos y mínimos

all_league_max_min = df.groupby('Liga').agg({'Goles': ['max','min']}).reset_index()
league = df.groupby('Liga')
print(league)

#print(all_league_max_min)

# creamos columnas
#columnas = ['Columna1','Columna2','Columna3']

#print(all_league_max_min)

# Crear gráfico

# Gráfico de dispersión

"""GRAFICO DE DISPERSION""" # HECHO
#x = goals
#y = salary
#
#plt.scatter(x, y, color='red', marker='o')
#plt.xlabel('Goles Proposito')
#plt.ylabel('Salario')
#plt.title('Gráfico de Dispersión')
#plt.show()


# Datos de ejemplo
