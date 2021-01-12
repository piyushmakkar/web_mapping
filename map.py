import pandas as pd
import folium

df = pd.read_csv("Volcanoes.csv")

lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

def colour_producer(elevation):
    if elevation in range(0,1000):
        return "green"
    elif elevation in range(1000,2000):
        return "orange"
    else:
        return "red"

map = folium.Map(location = [22.55,77.405],zoom_start = 2, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")
fgp = folium.FeatureGroup(name = "Population")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], popup = str(el)+" m" , radius = 8,fill_color = colour_producer(el),fill = True, color = 'grey', fill_opacity = 0.8))

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding ='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map.html")
# we can add html commands like text formatig and links in this too, to do that refer the course.
#geojson special case of json 
# we can break the lines in python while passing parameter when it exceeds the line limit
# lambda functions are one line functions without name