"""
Anadolu Seyahatnamesi - Dijital Seyyah CLI Aracı
Terminal Üzerinden Seyahat Yönetimi, Rota Optimizasyonu ve Derleme
"""

import sys
import os
import argparse
import random
from pathlib import Path

# Windows UTF-8 Terminal Desteği
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from travel_core import SeyyahEngine, TRAVEL_QUOTES, REGIONS_INFO
from map_generator import MapGenerator

ASCII_LOGO = r"""
  ___  _  _   _   ___   ___  _    _   _   ___ _____   __ _   _  _   _   __  __ ___ ___ ___ 
 / _ \| \| | /_\ |   \ / _ \| |  | | | | / __| __\ \ / //_\ | || | /_\ |  \/  | __/ __|_ _|
| (_) | .` |/ _ \| |) | (_) | |__| |_| | \__ \ _| \ V // _ \| __ |/ _ \| |\/| | _|\__ \| | 
 \___/|_|\_/_/ \_\___/ \___/|____|\___/  |___/___| |_|/_/ \_\_||_/_/ \_\_|  |_|___|___/___|
                  [ D I J I T A L   S E Y Y A H   C L I ]
"""

def print_banner():
    print(ASCII_LOGO)

def cmd_status(args):
    print_banner()
    engine = SeyyahEngine()
    stats = engine.stats
    pct = stats["progress_pct"]
    visited = stats["visited_cities"]
    total = stats["total_cities"]

    # Progress bar
    filled = int((pct / 100) * 30)
    bar = "=" * filled + "-" * (30 - filled)

    print("=" * 74)
    print("                      SEYYAH GENEL DURUM PANELI")
    print("=" * 74)
    print(f" [OK] Kesif Ilerlemesi:  [{bar}] %{pct} ({visited}/{total} Il)")
    print(f" [KM] Tahmini Mesafe:    {stats['estimated_km']:,} km karayolu izi")
    print(f" [OF] Kutuphane Ofisleri: {visited} il halk kutuphanesinde mesai")
    print("-" * 74)
    print("                        BOLGESEL DAGILIM")
    print("-" * 74)

    for reg_code, r in stats["regional_breakdown"].items():
        r_bar_filled = int((r["percentage"] / 100) * 15)
        r_bar = "#" * r_bar_filled + "." * (15 - r_bar_filled)
        print(f" {r['icon']} {r['name']:<24} [{r_bar}] %{r['percentage']:>5.1f} ({r['visited']:>2}/{r['total']:>2})")

    quote = random.choice(TRAVEL_QUOTES)
    print("-" * 74)
    print("                        GUNUN TEFEKKURU")
    print("-" * 74)
    print(f" 📜 \"{quote['quote']}\"")
    print(f"    — {quote['author']}\n")

def cmd_build(args):
    print_banner()
    print("🔨 [1/3] Veri tabanı ve web modülleri senkronize ediliyor...")
    engine = SeyyahEngine()
    json_path, js_path = engine.generate_web_data_json()
    print(f"  ✓ {json_path.name} ve {js_path.name} oluşturuldu.")

    print("🗺️ [2/3] İnteraktif Folium / Leaflet haritası derleniyor...")
    mg = MapGenerator()
    out_map = mg.generate()
    print(f"  ✓ {out_map.name} üretildi.")

    print("📄 [3/3] README.md istatistikleri ve rozetleri güncelleniyor...")
    if engine.update_readme_stats():
        print("  ✓ README.md başarıyla senkronize edildi.")
    else:
        print("  ! README.md bulunamadı.")

    print("\n✨ Derleme tamamlandı! Tüm seyahatname dosyaları güncel.\n")

def cmd_plan_route(args):
    print_banner()
    engine = SeyyahEngine()
    start_city = args.start or (list(engine.visited_provinces.values())[0]["name"] if engine.visited_provinces else "İstanbul")
    stops = args.stops or 7

    print(f"🧭 '{start_city}' noktasından başlayarak en yakın {stops} duraklık keşif rotası planlanıyor...\n")
    route = engine.plan_optimal_route(start_city, max_stops=stops)

    if not route or len(route) < 2:
        print("Tüm iller ziyaret edilmiş veya rota hesaplanamadı!")
        return

    total_km = 0
    print("  DURAK  SEHIR               BOLGE           MESAFE     ONE CIKAN DURAK")
    print("  " + "-" * 70)
    for idx, stop in enumerate(route):
        dist = stop.get("distance_from_prev_km", 0)
        total_km += dist
        landmark = stop.get("landmarks", ["Menzil"])[0] if stop.get("landmarks") else "Menzil"
        dist_str = f"{dist} km" if idx > 0 else "BASLANGIC"
        print(f"  [{idx+1:02d}]   {stop['name']:<18} {stop['region']:<14} {dist_str:<10} 📍 {landmark}")

    print("  " + "-" * 70)
    print(f"  🛣️ Toplam Planlanan Yolculuk: {total_km:,} km\n")

def cmd_export_book(args):
    print_banner()
    print("📚 'ANADOLU_SEYAHATNAMESI.md' derleniyor...")
    engine = SeyyahEngine()
    visited = sorted(engine.visited_provinces.values(), key=lambda p: (p["region_code"], p["name"]))

    book_content = f"""# 🕌 ANADOLU SEYAHATNAMESİ: DİJİTAL SEYYAH KÜLLİYATI

> *"Biz yolların bitmediği, keşfin son bulmadığı bir alemde Hakikati ve Güzelliği arayan yolcularız."*

---

## 📊 Seyahatname Özeti
* **Toplam Ziyaret Edilen İl:** {engine.stats['visited_cities']} / 81
* **Keşif Oranı:** %{engine.stats['progress_pct']}
* **Kat Edilen Tahmini Mesafe:** {engine.stats['estimated_km']:,} km
* **Kapsanan Bölgeler:** 7 / 7

---

## 📑 İÇİNDEKİLER
"""
    for idx, p in enumerate(visited, 1):
        book_content += f"{idx}. [{p['name']} ({p['region']})](#{p['slug'].lower()})\n"

    book_content += "\n---\n\n"

    for p in visited:
        book_content += f"""## <a id="{p['slug'].lower()}"></a>📍 {p['name']} ({p['plate']:02d}) - {p['region']}

> *"{p.get('custom_quote', p.get('quote', ''))}"*

### 🏛️ Öne Çıkan Miras & Duraklar
"""
        for lm in p.get("landmarks", []):
            book_content += f"- [x] {lm}\n"

        book_content += f"""
### 🍽️ Yöresel Tatlar
{', '.join(p.get('specialties', ['Yöresel lezzetler']))}

### 💻 Seyyahın Kütüphane Ofisi
{p.get('custom_library', p.get('library', 'İl Halk Kütüphanesi'))}

---
"""

    out_file = Path("ANADOLU_SEYAHATNAMESI.md")
    out_file.write_text(book_content, encoding="utf-8")
    print(f"✓ Külliyat başarıyla '{out_file.name}' dosyasına aktarıldı ({len(visited)} İl).\n")

def main():
    parser = argparse.ArgumentParser(description="Dijital Seyyah - Anadolu Seyahatnamesi CLI")
    subparsers = parser.add_subparsers(dest="command", help="Komutlar")

    # status
    p_status = subparsers.add_parser("status", help="Genel seyahat durumu ve istatistikleri")
    p_status.set_defaults(func=cmd_status)

    # build
    p_build = subparsers.add_parser("build", help="Tüm veri ve harita çıktılarını derle")
    p_build.set_defaults(func=cmd_build)

    # plan-route
    p_route = subparsers.add_parser("plan-route", help="En yakın rotayı hesapla")
    p_route.add_argument("--start", help="Başlangıç şehri")
    p_route.add_argument("--stops", type=int, default=7, help="Durak sayısı")
    p_route.set_defaults(func=cmd_plan_route)

    # export-book
    p_book = subparsers.add_parser("export-book", help="Tüm gezilen illeri tek bir Markdown kitabına derle")
    p_book.set_defaults(func=cmd_export_book)

    args = parser.parse_args()
    if args.command and hasattr(args, "func"):
        args.func(args)
    else:
        cmd_status(args)

if __name__ == "__main__":
    main()
