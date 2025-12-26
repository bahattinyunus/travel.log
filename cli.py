import os
import sys
import shutil
import argparse
from datetime import datetime
from analytics import TravelLogAnalytics, Colors
from map_generator import MapGenerator

class TravelCLI:
    def __init__(self):
        self.analytics = TravelLogAnalytics()
        self.map_gen = MapGenerator()

    def ask_input(self, prompt, required=True):
        while True:
            value = input(f"{Colors.GREEN}?{Colors.ENDC} {prompt}: ").strip()
            if value:
                return value
            if not required:
                return ""
            print(f"{Colors.FAIL}Bu alan zorunludur.{Colors.ENDC}")

    def create_entry(self):
        print(f"\n{Colors.CYAN}=== YENİ SEYAHAT KAYDI ==={Colors.ENDC}")
        
        # Select Region
        print("\nBölgeler:")
        for idx, region in enumerate(self.analytics.REGIONS):
            print(f"{idx+1}. {region}")
        
        while True:
            try:
                choice = int(self.ask_input("Bölge numarası seçin"))
                if 1 <= choice <= len(self.analytics.REGIONS):
                    region = self.analytics.REGIONS[choice-1]
                    break
            except ValueError:
                pass
            print(f"{Colors.FAIL}Geçersiz seçim.{Colors.ENDC}")

        city = self.ask_input("Şehir adı (Örn: Mugla)")
        location = self.ask_input("Lokasyon adı (Örn: Kelebekler Vadisi)")
        
        # Create paths
        region_path = os.path.join(".", region)
        city_path = os.path.join(region_path, city)
        loc_path = os.path.join(city_path, location.replace(" ", "_"))
        
        if os.path.exists(loc_path):
            print(f"{Colors.WARNING}Uyarı: Bu lokasyon zaten var!{Colors.ENDC}")
            if self.ask_input("Üzerine yazmak istiyor musunuz? (e/h)").lower() != 'e':
                return

        os.makedirs(loc_path, exist_ok=True)
        
        # Prepare content
        coords = self.ask_input("Koordinatlar (Enlem, Boylam) [Boş geçilebilir]", required=False)
        quote = self.ask_input("Kısa bir alıntı/söz", required=False)
        review = self.ask_input("Kısa izleniminiz")
        
        template_content = ""
        try:
            with open(os.path.join("_Sablon", "location_template.md"), "r", encoding="utf-8") as f:
                template_content = f.read()
        except FileNotFoundError:
            print(f"{Colors.FAIL}Şablon bulunamadı!{Colors.ENDC}")
            return

        # Fill template
        filled_content = template_content.replace("[Lokasyon Adı]", location)
        filled_content = filled_content.replace("DD.MM.YYYY", datetime.now().strftime("%d.%m.%Y"))
        
        if coords:
            filled_content = filled_content.replace("XX.XXXX, YY.YYYY", coords)
        
        if quote:
            filled_content = filled_content.replace("[Buraya lokasyonla ilgili kısa, vurucu bir alıntı veya his eklenecek]", quote)
            
        # Write file
        target_file = os.path.join(loc_path, "README.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(filled_content)
            
        print(f"\n{Colors.GREEN}✔ Kayıt başarıyla oluşturuldu: {target_file}{Colors.ENDC}")
        print(f"{Colors.BLUE}Not: Detayları düzenlemek için dosyayı açabilirsiniz.{Colors.ENDC}")

    def main(self):
        parser = argparse.ArgumentParser(description="Travel Log Elite CLI")
        subparsers = parser.add_subparsers(dest="command", help="Komutlar")
        
        subparsers.add_parser("add", help="Yeni bir seyahat kaydı ekle")
        subparsers.add_parser("map", help="İnteraktif haritayı güncelle")
        subparsers.add_parser("stats", help="İstatistikleri göster")
        
        args = parser.parse_args()
        
        if args.command == "add":
            self.create_entry()
        elif args.command == "map":
            self.map_gen.generate_map()
        elif args.command == "stats":
            self.analytics.run_analysis()
        else:
            parser.print_help()

if __name__ == "__main__":
    cli = TravelCLI()
    try:
        cli.main()
    except KeyboardInterrupt:
        print("\nÇıkış yapıldı.")
