"""
This simple code is to use folium and plot if on a map by setting it up on HTML page.
Once a map has been set, based on the input file 'Volcanoes_USA.txt', it will plot those volcanoes on the USA map.
We are assigning markers to those points.
Once those markers are set, we have tried to load a world json file, and also create a lambda function based on the population.

__author__ = Arvind
__Date__ = 09/20/2017
"""

import folium
import pandas as pd

data = pd.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map=folium.Map(location=[42.3457,-71.08],zoom_start=6,tiles="Mapbox Bright")

"""
Add a featureGroup
put multiple markers within a list
"""
def color_of_icon(elevation):
	if elevation<1500:
		return 'darkpurple'
	elif 1500<=elevation<2750:
		return 'darkgreen'
	else:
		return 'darkred'


fgv = folium.FeatureGroup(name="Volcanoes")

#Adding of a marker
for l,n,el in zip(lat,lon,elev):
	#fg.add_child(folium.Marker(location=[l,n],popup=str(el),icon=folium.Icon(color=icon_color(el))))
	fgv.add_child(folium.CircleMarker(location=[l,n],radius=5,popup=str(el),fill=True,fill_color=color_of_icon(el),color='grey',fill_opacity=1.0))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json',"r",encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'yellow'if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.save("Volcano.html")