from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import folium
import pandas as pd

# Load stops data
stops = pd.read_csv('stops.txt')

# Extract coordinates for clustering
coords = stops[['stop_lat', 'stop_lon']].values

kmeans = KMeans(n_clusters=10, random_state=0).fit(coords)
stops['cluster'] = kmeans.labels_


plt.scatter(stops['stop_lon'], stops['stop_lat'], c=stops['cluster'], cmap='viridis', s=10)
plt.title('Stop Clusters')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Create a map for clusters
map = folium.Map(location=[53.5461, -113.4938], zoom_start=12)

# Add clustered stops
for _, row in stops.iterrows():
    folium.CircleMarker(
        [row['stop_lat'], row['stop_lon']],
        radius=5,
        color=f"#{row['cluster'] * 111111}",
        fill=True,
        fill_opacity=0.6,
    ).add_to(map)

# Save the cluster map
map.save("stop_clusters_map.html")
print("Cluster map saved as stop_clusters_map.html")
