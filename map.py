import folium
import json

# Read the coordinates from a JSON
with open('coordinates.json', 'r') as coordinatesJson:
    coordinates = json.load(coordinatesJson)

# Create a map
map = folium.Map(
    location = [
        40.726025724051794,
        -73.99712101251961
    ],
    zoom_start = 10,
    tiles = "cartodbpositron",
)

# Add a marker
fg = folium.FeatureGroup(name="Map")

for coordinate in coordinates:
    fg.add_child(folium.Marker(
        location = coordinate["location"],
        popup = coordinate["popup"],
        icon = folium.Icon(color=coordinate["iconColor"])
    ))

map.add_child(fg)

map.save("map.html")