import folium

# pip install folium

latitude = 51.229675
longitude = 17.012230

map = folium.Map(location=[latitude, longitude], zoom_start=12)

# marker = folium.Marker(location=[latitude, longitude], popup="Tu jestem")
marker = folium.Marker(
    location=[latitude, longitude],
    popup=f'Szerokosc {latitude}, Długość {longitude}',
    icon=folium.Icon(color='red')
)

marker.add_to(map)
map.save('mapa.html')
