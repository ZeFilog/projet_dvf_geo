import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx
import folium
import plotly.express as px
from branca.colormap import linear

data = pd.read_csv('35.csv', low_memory= False)

#https://www.youtube.com/watch?v=7VmVxe2MS1c

#print(data.shape)
#print(data.head)
#data = data.dropna(axis = 0)
#print(data['id_mutation'].value_counts())
#print(data['valeur_fonciere'].value_counts())

#print(data.loc[:,['code_postal','valeur_fonciere']].groupby('code_postal').mean())
#data.loc[:,['code_postal','valeur_fonciere']].groupby('code_postal').mean().plot.bar()
#plt.show()


"""
# si on a un fichier csv avec la lat et long et que l'on veux en créent un en geopandas
#toujour la longitude en 1er et la latitude en deuxième.
geo_35 = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data["longitude"],data["latitude"]))
#print(geo_35)

#afficher les points en fonction des prix et du 35000
map_Rennes = gpd.read_file('perimetres-des-12-quartiers-de-la-ville-de-rennes.geojson')
map_Rennes.plot()
geo_35 = geo_35[(geo_35['code_postal'] == 35000) & (geo_35['valeur_fonciere'] < 200000)]
geo_35.plot(ax = map_Rennes.axes[0],column = "valeur_fonciere",legend = True, figsize = (5,5), cmap = 'RdYlBu')

ax = geo_35.add_subplot(1, 1, 1)

# Utilisez la méthode set_aspect sur l'objet AxesSubplot
#ax.set_aspect('equal')
#geo_35.plot(ax = map_Rennes.axes[0])

#geo_35.plot(ax = map_Rennes.axes[0],column = "valeur_fonciere",cmap = 'viridis')

#on va ajouter un fond a la carte
 #pip install folium matplotlib mapclassify
#geo_35.explore(), ne marche pas, normalement c'est sencer nous mettre une carte interractive.



#geo_wm = geo_35.to_crs(epsg = 3857)

#normalement ça mets un fond de carte de rennes mais je comprend pas pq ça marche pas
geo_35

plt.show()
"""
def graph(data):
    data = data[(data["valeur_fonciere"] < 500000)&(data["code_postal"] == 35000)]

    data["lat"] = data["latitude"].mean()
    data["lon"] = data["longitude"].mean()

    # Création de la carte de chaleur
    fig = px.density_heatmap(data, x="lon", y="lat", nbinsx=500, nbinsy=500, hover_name="valeur_fonciere", color_continuous_scale='Jet')

    return fig.show()

def graph2(data):
    # chargement des données

    # filtrage des données pour valeur_fonciere < 200000 et Rennes
    data = data[(data['valeur_fonciere'] < 500000) & (data['code_postal'] == '35000')]

    # création de la carte
    m = folium.Map(location=[48.1134, -1.6779], zoom_start=13)

    # création de la palette de couleurs
    colormap = linear.YlGn_09.scale(data['valeur_fonciere'].min(), data['valeur_fonciere'].max())
    colormap.caption = 'Valeur foncière'

    # ajout des marqueurs sur la carte
    for row in data.itertuples():
        folium.CircleMarker(
            location=[row.latitude, row.longitude],
            radius=5,
            color=colormap(row.valeur_fonciere),
            fill=True,
            fill_color=colormap(row.valeur_fonciere),
            fill_opacity=0.7,
            popup=str(row.valeur_fonciere)
        ).add_to(m)

    # ajout de la palette de couleurs sur la carte
    m.add_child(colormap)
    m.save("carte_chaleur_valeur_fonciere.html")

    # affichage de la carte
    return print("prout")

graph2(data)