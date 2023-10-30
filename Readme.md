# Map Generator

This Python script generates an interactive map using the Folium library based on the coordinates provided in the `coordinates.json` file.

## Stack
- Python: [3.10.12]
- [Folium](https://python-visualization.github.io/folium/): [0.14.0]

## Description
This script reads coordinates from a JSON file (`coordinates.json`), creates a map centered at latitude 40.726025724051794 and longitude -73.99712101251961,

## Usage
1. Ensure you have Python and the necessary packages (Folium) installed.
2. Place your coordinate data in a JSON file named `coordinates.json`. The JSON structure should be as follows:

```json
[
    {
        "location": [latitude, longitude],
        "popup": "Marker Popup Text",
        "iconColor": "green"  // Specify a color for the marker icon
    },
    // Add more coordinates as needed
]
```

3. Run the Python script to generate the map:

```
python your_script.py
```

4. After running the code, an HTML file named map.html will be created in the same directory.

5. Open map.html in a web browser to view the interactive map.