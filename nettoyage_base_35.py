import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx
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


# si on a un fichier csv avec la lat et long et que l'on veux en créent un en geopandas
#toujour la longitude en 1er et la latitude en deuxième.
geo_35 = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data["longitude"],data["latitude"]))
#print(geo_35)

#afficher les points en fonction des prix et du 35000

geo_35 = geo_35[(geo_35['code_postal'] == 35000) & (geo_35['valeur_fonciere'] < 200000)]
geo_35.plot(column = "valeur_fonciere",legend = True, figsize = (5,5), cmap = 'RdYlBu')

#on va ajouter un fond a la carte
 #pip install folium matplotlib mapclassify
#geo_35.explore(), ne marche pas, normalement c'est sencer nous mettre une carte interractive.



#geo_wm = geo_35.to_crs(epsg = 3857)

#normalement ça mets un fond de carte de rennes mais je comprend pas pq ça marche pas
ax = geo_35.plot()
cx.add_basemap(ax)
plt.show()




