import pandas as pd
import folium
cities = pd.read_excel("all_US_states.xlsx",sheet_name='Alaska')

world_all_cities_tooltip = folium.Map(
    zoom_start=2,
    location=[13.133932434766733, 16.103938729508073]
)

for _, city in cities.iterrows():
    folium.Marker(
        location=[city['latitude'], city['longitude']],
        popup=city['city'],
        tooltip=city['city'],
    ).add_to(world_all_cities_tooltip)

world_all_cities_tooltip.save('world_all_cities_tooltip.html')
