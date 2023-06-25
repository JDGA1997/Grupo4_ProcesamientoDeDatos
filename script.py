import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'dataset/cars.csv'

# Cargar el archivo CSV en un DataFrame de Pandas
df = pd.read_csv(file_path)

# Imprimir las primeras filas del DataFrame
print(df.head())


#Diagrama de Barras

conteo_fabricantes = df['manufacturer_name'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=conteo_fabricantes.index, y=conteo_fabricantes.values, color='green')
plt.title('Cantidad de vehículos por fabricante')
plt.xlabel('Fabricante')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()


#Histograma

valores_odometro = df['odometer_value']

plt.figure(figsize=(8, 6))
sns.histplot(valores_odometro, kde=True, color='blue')
plt.title('Distribución de valores del odómetro')
plt.xlabel('Valor del odómetro')
plt.ylabel('Frecuencia')
plt.show()


#Grafico de Torta

colores = df['color'].value_counts()
etiquetas = colores.index

plt.figure(figsize=(8, 6))
plt.pie(colores, labels=etiquetas, autopct='%1.1f%%')
plt.title('Distribución de colores de los vehículos')
plt.show()


#Diagrama de Puntos

year_produced = df['year_produced']
engine_capacity = df['engine_capacity']

plt.figure(figsize=(8, 6))
sns.scatterplot(x=year_produced, y=engine_capacity)
plt.title('Relación entre año de producción y capacidad del motor')
plt.xlabel('Año de producción')
plt.ylabel('Capacidad del motor')
plt.show()