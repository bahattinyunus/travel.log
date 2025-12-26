import os
import json
from datetime import datetime

# Konfigürasyon
ROOT_DIR = "."
REGIONS = [
    "01_Marmara", "02_Ege", "03_Akdeniz", "04_IcAnadolu",
    "05_Karadeniz", "06_DoguAnadolu", "07_GuneydoguAnadolu"
]

def analyze_repo():
    stats = {
        "total_regions": 0,
        "total_cities": 0,
        "total_locations": 0,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "coverage": {}
    }

    print("📊 Travel Log: Sistem Analizi Başlatılıyor...\n")
    print(f"{'Bölge':<20} | {'Şehir':<10} | {'Lokasyon':<10}")
    print("-" * 46)

    for region in REGIONS:
        if not os.path.exists(region):
            continue
        
        stats["total_regions"] += 1
        region_cities = 0
        region_locations = 0
        
        # Şehirleri tara
        for city in os.listdir(region):
            city_path = os.path.join(region, city)
            if os.path.isdir(city_path):
                region_cities += 1
                stats["total_cities"] += 1
                
                # Lokasyonları tara (Alt klasörler)
                for loc in os.listdir(city_path):
                    loc_path = os.path.join(city_path, loc)
                    if os.path.isdir(loc_path):
                        region_locations += 1
                        stats["total_locations"] += 1

        stats["coverage"][region] = {
            "cities": region_cities,
            "locations": region_locations
        }
        
        print(f"{region:<20} | {region_cities:<10} | {region_locations:<10}")

    print("-" * 46)
    print(f"\n🌍 TOPLAM İSTATİSTİKLER")
    print(f"   ➤ Aktif Bölge: {stats['total_regions']}/7")
    print(f"   ➤ Keşfedilen Şehir: {stats['total_cities']}")
    print(f"   ➤ Detaylı Lokasyon: {stats['total_locations']}")
    print(f"\n✅ Analiz tamamlandı. Sistem kararlı.")

if __name__ == "__main__":
    analyze_repo()
