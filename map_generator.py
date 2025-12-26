import os
import re
import folium
import webbrowser
from analytics import TravelLogAnalytics, Colors

class MapGenerator:
    def __init__(self, root_dir="."):
        self.root_dir = root_dir
        self.analytics = TravelLogAnalytics(root_dir)
        # Regex to find "Koordinatlar: XX.XXXX, YY.YYYY"
        # Flexible for spaces and comma
        self.coord_pattern = re.compile(r'\*\*Koordinatlar:\*\*\s*`?([0-9\.]+),\s*([0-9\.]+)`?')

    def extract_coordinates(self, file_path):
        """Extracts lat, lon from a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                match = self.coord_pattern.search(content)
                if match:
                    return float(match.group(1)), float(match.group(2))
        except Exception as e:
            print(f"{Colors.FAIL}Error reading {file_path}: {e}{Colors.ENDC}")
        return None

    def generate_map(self, output_file="travel_map.html"):
        print(f"{Colors.CYAN}>>> Harita Jeneratörü Başlatılıyor...{Colors.ENDC}")
        
        # Center map on Anatolia roughly
        m = folium.Map(location=[39.0, 35.0], zoom_start=6, tiles="CartoDB dark_matter")
        
        locations_found = 0
        
        for region in self.analytics.REGIONS:
            region_path = os.path.join(self.root_dir, region)
            if not os.path.exists(region_path):
                continue
                
            for city in os.listdir(region_path):
                city_path = os.path.join(region_path, city)
                if not os.path.isdir(city_path):
                    continue
                    
                for loc in os.listdir(city_path):
                    if loc.endswith(".md"):
                        # Direct MD file in city folder
                        file_path = os.path.join(city_path, loc)
                        loc_name = loc.replace(".md", "")
                    else:
                        # Folder inside city
                        loc_path = os.path.join(city_path, loc)
                        if os.path.isdir(loc_path):
                            # Try to find README.md or md file with same name
                            possible_files = [os.path.join(loc_path, "README.md"), os.path.join(loc_path, f"{loc}.md")]
                            file_path = None
                            for p in possible_files:
                                if os.path.exists(p):
                                    file_path = p
                                    break
                            loc_name = loc
                        else:
                            continue

                    if file_path:
                        coords = self.extract_coordinates(file_path)
                        if coords:
                            locations_found += 1
                            folium.Marker(
                                location=coords,
                                popup=f"<b>{loc_name}</b><br>{city}, {region}",
                                icon=folium.Icon(color="red", icon="info-sign")
                            ).add_to(m)
                            print(f"{Colors.GREEN}✔ Konum eklendi: {loc_name}{Colors.ENDC}")

        if locations_found > 0:
            m.save(output_file)
            print(f"\n{Colors.BOLD}>>> Harita oluşturuldu: {output_file}{Colors.ENDC}")
            print(f"{Colors.CYAN}>>> Tarayıcıda açılıyor...{Colors.ENDC}")
            webbrowser.open(f"file://{os.path.abspath(output_file)}")
        else:
            print(f"{Colors.WARNING}>>> Hiçbir koordinat bulunamadı. Lütfen kayıtlarınızı kontrol edin.{Colors.ENDC}")

if __name__ == "__main__":
    generator = MapGenerator()
    generator.generate_map()
