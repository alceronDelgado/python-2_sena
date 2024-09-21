import seaborn as snb

df = snb.load_dataset('diamonds')
print(df)

grouped = df.groupby('cut',observed=False)
print(grouped)

#Calcular media de precio de cada grupo
#mean_price = grouped['price'].mean()
#print(mean_price)

#Calcular suma total de precios
total_price = grouped['price'].sum()

print(total_price)


#Contar el número de elementos de cada grupo
count_by = grouped.size()
print(count_by)

for i in [0,1,2,3,'Hola']:
    print(i)
    
