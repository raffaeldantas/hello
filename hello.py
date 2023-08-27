import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

# Carrega o shapefile dos estados do Brasil
brasil = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
estados = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filtra os estados do Brasil
brasil = brasil[brasil['name'] == 'Brazil']

# Carrega o shapefile dos estados do Brasil
estados = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plota o mapa do Brasil com os estados
fig, ax = plt.subplots(figsize=(10, 8))
brasil.plot(ax=ax, color='lightgray', edgecolor='black')
estados.boundary.plot(ax=ax, linewidth=1, color='black')

ax.set_title('Mapa do Brasil com Estados')
plt.axis('off')  # Desativa os eixos
plt.show()
