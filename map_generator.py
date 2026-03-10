import json
import os
import folium
from folium.plugins import MarkerCluster

class MapGenerator:
    def __init__(self, data_file="travel_data.json", output_file="travel_map.html"):
        self.data_file = data_file
        self.output_file = output_file
        
        # Approximate coordinates for the 81 provinces to plot them exactly
        self.city_coords = {
            "Adana": [37.0000, 35.3213], "Adıyaman": [37.7648, 38.2786], "Afyonkarahisar": [38.7507, 30.5567],
            "Ağrı": [39.7191, 43.0503], "Aksaray": [38.3687, 34.0370], "Amasya": [40.6500, 35.8333],
            "Ankara": [39.9208, 32.8541], "Antalya": [36.8841, 30.7056], "Ardahan": [41.1105, 42.7022],
            "Artvin": [41.1828, 41.8183], "Aydın": [37.8444, 27.8458], "Balıkesir": [39.6484, 27.8826],
            "Bartın": [41.6344, 32.3375], "Batman": [37.8812, 41.1351], "Bayburt": [40.2552, 40.2249],
            "Bilecik": [40.1451, 29.9798], "Bingöl": [38.8847, 40.4939], "Bitlis": [38.4011, 42.1078],
            "Bolu": [40.7392, 31.6111], "Burdur": [37.7204, 30.2908], "Bursa": [40.1828, 29.0667],
            "Çanakkale": [40.1553, 26.4142], "Çankırı": [40.6013, 33.6134], "Çorum": [40.5506, 34.9556],
            "Denizli": [37.7765, 29.0864], "Diyarbakır": [37.9144, 40.2306], "Düzce": [40.8438, 31.1565],
            "Edirne": [41.6771, 26.5557], "Elazığ": [38.6810, 39.2264], "Erzincan": [39.7500, 39.5000],
            "Erzurum": [39.9043, 41.2679], "Eskişehir": [39.7767, 30.5206], "Gaziantep": [37.0662, 37.3833],
            "Giresun": [40.9128, 38.3895], "Gümüşhane": [40.4597, 39.4745], "Hakkari": [37.5833, 43.7333],
            "Hatay": [36.2000, 36.1667], "Iğdır": [39.9237, 44.0450], "Isparta": [37.7648, 30.5566],
            "İstanbul": [41.0082, 28.9784], "İzmir": [38.4192, 27.1287], "Kahramanmaraş": [37.5847, 36.9339],
            "Karabük": [41.2061, 32.6226], "Karaman": [37.1811, 33.2222], "Kars": [40.6013, 43.0975],
            "Kastamonu": [41.3766, 33.7765], "Kayseri": [38.7312, 35.4787], "Kilis": [36.7161, 37.1150],
            "Kırıkkale": [39.8468, 33.5153], "Kırklareli": [41.7333, 27.2167], "Kırşehir": [39.1425, 34.1709],
            "Kocaeli": [40.7654, 29.9408], "Konya": [37.8667, 32.4833], "Kütahya": [39.4167, 29.9833],
            "Malatya": [38.3552, 38.3095], "Manisa": [38.6191, 27.4289], "Mardin": [37.3122, 40.7339],
            "Mersin": [36.8000, 34.6333], "Muğla": [37.2153, 28.3636], "Muş": [38.7304, 41.4910],
            "Nevşehir": [38.6244, 34.7144], "Niğde": [37.9667, 34.6833], "Ordu": [40.9839, 37.8764],
            "Osmaniye": [37.0742, 36.2472], "Rize": [41.0201, 40.5234], "Sakarya": [40.6940, 30.4358],
            "Samsun": [41.2867, 36.3300], "Şanlıurfa": [37.1500, 38.8000], "Siirt": [37.9333, 41.9500],
            "Sinop": [42.0231, 35.1531], "Şırnak": [37.5164, 42.4611], "Sivas": [39.7477, 37.0179],
            "Tekirdağ": [40.9833, 27.5167], "Tokat": [40.3167, 36.5500], "Trabzon": [41.0015, 39.7178],
            "Tunceli": [39.1079, 39.5401], "Uşak": [38.6823, 29.4082], "Van": [38.4891, 43.3853],
            "Yalova": [40.6500, 29.2833], "Yozgat": [39.8181, 34.8147], "Zonguldak": [41.4564, 31.7987],
            # Aliases
            "Afyon": [38.7507, 30.5567], "Urfa": [37.1500, 38.8000], "Maras": [37.5847, 36.9339]
        }
        
    def _normalize(self, name):
        tr_to_en = {
            'ı': 'i', 'I': 'I', 'İ': 'I', 'i': 'i',
            'ğ': 'g', 'Ğ': 'G',
            'ü': 'u', 'Ü': 'U',
            'ş': 's', 'Ş': 'S',
            'ö': 'o', 'Ö': 'O',
            'ç': 'c', 'Ç': 'C'
        }
        name = name.translate(str.maketrans(tr_to_en))
        return name.lower().strip()

    def generate_map(self):
        # We find visited checking README actual list
        visited_cities = set()
        if os.path.exists("README.md"):
            with open("README.md", "r", encoding="utf-8") as f:
                content = f.read()
                # we know "✅ **CityName**" is the syntax now
                import re
                matches = re.findall(r"✅ \*\*([^\*]+)\*\*", content)
                for m in matches:
                    visited_cities.add(m.strip())

        # Center of Turkey approx: 38.9637, 35.2433
        m = folium.Map(location=[38.9637, 35.2433], zoom_start=6, tiles='CartoDB dark_matter')
        
        # Add a custom title HTML
        loc = 'Türkiye Keşif Haritası - Travel.log'
        title_html = f'''
             <h3 align="center" style="font-size:20px; color:white;"><b>{loc}</b></h3>
             '''
        m.get_root().html.add_child(folium.Element(title_html))

        marker_cluster = MarkerCluster().add_to(m)
        
        plotted = 0
        for city_raw in visited_cities:
            # find coords
            for c_name, coords in self.city_coords.items():
                if self._normalize(c_name) == self._normalize(city_raw):
                    folium.Marker(
                        location=coords,
                        popup=f"<b>{city_raw}</b><br>1 Adet Rota Ziyaret Edildi.",
                        icon=folium.Icon(color="green", icon="info-sign"),
                    ).add_to(marker_cluster)
                    plotted += 1
                    break
        
        # Add unvisited as small dots
        for c_name, coords in self.city_coords.items():
            if c_name in ["Afyon", "Urfa", "Maras"]: continue # skip aliases
            
            is_visited = False
            for v in visited_cities:
                if self._normalize(c_name) == self._normalize(v):
                    is_visited = True
                    break
            
            if not is_visited:
                folium.CircleMarker(
                    location=coords,
                    radius=3,
                    color="#444444",
                    fill=True,
                    fill_color="#444444",
                    fill_opacity=0.7,
                    tooltip=f"Keşfedilmeyi bekliyor: {c_name}"
                ).add_to(m)

        m.save(self.output_file)
        return plotted

if __name__ == "__main__":
    mg = MapGenerator()
    mg.generate_map()
    print("Map generated.")
