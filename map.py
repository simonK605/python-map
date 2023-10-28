import folium

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

coordinates = [
    {
        "location": [
            40.726025724051794,
            -73.99712101251961
        ],
        "popup": "Museum of Ice Cream",
        "icon": folium.Icon(color="red")
    },
    {
        "location": [
            40.74844664402143,
            -73.98554516800736
        ],
        "popup": "Empire State Building",
        "icon": folium.Icon(color="green")
    }
]

for coordinate in coordinates:
    fg.add_child(folium.Marker(
        location = coordinate["location"],
        popup = coordinate["popup"],
        icon = coordinate["icon"]
    ))

map.add_child(fg)



map.save("map.html")