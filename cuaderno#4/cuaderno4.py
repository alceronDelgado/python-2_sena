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

# Punto 0 - Crear dataframe = DONE

df = pd.DataFrame(data)
#print(df)

# Punto 1 jugadores por liga = DONE

players_by_league = df.groupby('Liga').agg({'Goles':['max','min']}).reset_index()

#print(players_by_league)

# Punto 2 - Tres jugadores con más goles por temporada = DONE

top_3_players = df.groupby('Temporada').apply(lambda x: x.nlargest(3, 'Goles')).reset_index(drop=True)
#print("Tres primeros jugadores por temporada:")
#print(top_3_players)


# Punto 3 = ranking de jugadores ordenados por goles = DONE
top_goals = df.groupby('Temporada')['Goles'].sum()

#print(top_goals)

# Punto 4 = Promedio de goles por temporada = DONE

prom_player = df['Goles'].mean()

#print(prom_player)

# Crear gráfico

# Gráfico de dispersión

salary = df['Salario']

#print(salary)

"""GRAFICO DE DISPERSION""" # DONE
#x = df['Goles']
#y = df['Salario']
#
#plt.scatter(x, y, color='red', marker='o')
#plt.xlabel('Goles Proposito')
#plt.ylabel('Salario')
#plt.title('Gráfico de Dispersión')
#plt.show()

"""GRÁFICO DE BARRAS""" # DONE
#x = df['Liga']
#y = df['Salario']

#print(y)
#Definimos la figura
#plt.figure(figsize=(12,6))
#Definimos el color de la barra
#plt.bar(x,y,color='skyblue',edgecolor='black')
#plt.xlabel(x)
#plt.ylabel(y)
#plt.title("Goles x liga")
#plt.grid(axis='y', linestyle='--', alpha=0.7)
#plt.show()

"""GRÁFICO DE TORTA""" # DONE
# PROPOSITO = goles proposito de cada liga

#goles_by_league = df.groupby('Liga').sum()['Goles']

#leagues = df['Liga'].unique()


#sizes = goles_by_league
#labels = ['La Liga' 'Serie A' 'Ligue 1' 'Bundesliga' 'Premier League']
#colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
#plt.figure(figsize=(4,4))
#plt.pie(goles_by_league, labels=goles_by_league, colors=colors, autopct='%1.1f%%', startangle=140)
#plt.title('Gráfico de Torta')
#plt.show()

"""GRÁFICO DE VIOLIN""" # DONE
# Objetivo = proporción de goles en cada liga. 
#players_by_league 
#plt.figure(figsize=(10, 6))
#sns.violinplot(data=players_by_league)
#plt.xlabel('Grupos')
#plt.ylabel('Valores')
#plt.title('Gráfico de Violín')
#plt.grid(True)
#plt.show()