import folium
import os

m = folium.Map(location=[43.6798,40.2814], zoom_start=17)
walkData=os.path.join('walk.json')
folium.GeoJson(walkData,name='walk').add_to(m)

m.save("map.html")
