import pandas as pd
import folium


stops = pd.read_csv('stops.txt')
routes = pd.read_csv('routes.txt')
trips = pd.read_csv('trips.txt')
stop_times = pd.read_csv('stop_times.txt')
shapes = pd.read_csv('shapes.txt')





map = folium.Map(location=[53.5461, -113.4938], zoom_start=12)


for _, row in stops.iterrows():
    folium.Marker(
        [row['stop_lat'], row['stop_lon']],
        popup=row['stop_name']
    ).add_to(map)


map.save("edmonton_stops_map.html")
print("Map saved as edmonton_stops_map.html")
