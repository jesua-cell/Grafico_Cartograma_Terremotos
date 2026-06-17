from pathlib import Path
import json
import plotly.express as px

path = Path('Earthquakes_json/all_day.geojson.json')
contenst = path.read_text()
all_eq_data = json.loads(contenst)

all_eq_dicts = all_eq_data['features']
# print(f"Cantidad total de terremotos: {len(all_eq_dicts)}")

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

   # print(mags[:10])
   # print(lons[:5])
   # print(lats[:5])

# Estilos y Representacion del grafico
# Titulo
title = 'Terremotos Globales'
# Funcion scatter_geo() para represnetar en un mapa los datos indicados
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags, color_continuous_scale='Viridis',
                     labels={'color':'Magnitudes'}, 
                     projection='natural earth', 
                     hover_name=eq_titles, )
fig.show()


