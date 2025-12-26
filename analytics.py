import os
import sys
import time
import argparse
from datetime import datetime

# Optional colorama support
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLORAMA = True
except ImportError:
    HAS_COLORAMA = False

class Colors:
    """Handles ANSI color codes safely."""
    if HAS_COLORAMA:
        HEADER = Fore.MAGENTA + Style.BRIGHT
        BLUE = Fore.BLUE
        CYAN = Fore.CYAN
        GREEN = Fore.GREEN
        WARNING = Fore.YELLOW
        FAIL = Fore.RED
        ENDC = Style.RESET_ALL
        BOLD = Style.BRIGHT
    else:
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'

class TravelLogAnalytics:
    REGIONS = [
        "01_Marmara", "02_Ege", "03_Akdeniz", "04_IcAnadolu",
        "05_Karadeniz", "06_DoguAnadolu", "07_GuneydoguAnadolu"
    ]

    def __init__(self, root_dir="."):
        self.root_dir = root_dir
        self.stats = {
            "total_regions": 0,
            "total_cities": 0,
            "total_locations": 0,
        }

    def type_effect(self, text, delay=0.02):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def scan_region(self, region_name):
        """Scans a single region directory."""
        if not os.path.exists(region_name):
            return None

        data = {"cities": 0, "locations": 0}
        for city in os.listdir(region_name):
            city_path = os.path.join(region_name, city)
            if os.path.isdir(city_path):
                data["cities"] += 1
                location_count = 0
                for loc in os.listdir(city_path):
                    loc_path = os.path.join(city_path, loc)
                    if os.path.isdir(loc_path):
                        location_count += 1
                data["locations"] += location_count
        return data

    def run_analysis(self, mock_delay=False):
        """Main analysis loop."""
        
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(Colors.CYAN + """
    ╔══════════════════════════════════════════════════════════════╗
    ║   TRAVEL LOG ACCESS TERMINAL v2.1 (SECURE)                   ║
    ║   CONNECTED TO: ANADOLU_DATABASE                             ║
    ╚══════════════════════════════════════════════════════════════╝
        """ + Colors.ENDC)
        
        self.type_effect(Colors.GREEN + "> Yükleniyor... Core Modules" + Colors.ENDC, 0.05 if not mock_delay else 0)
        if not mock_delay: time.sleep(0.5)
        self.type_effect(Colors.GREEN + "> Sistem: Online" + Colors.ENDC, 0.05 if not mock_delay else 0)
        print("\n")

        print(f"{Colors.BOLD}{'BÖLGE (REGION)':<25} | {'ŞEHİR (CITY)':<15} | {'LOKASYON (LOC)':<15}{Colors.ENDC}")
        print(Colors.CYAN + "-" * 60 + Colors.ENDC)

        region_data = []

        for region in self.REGIONS:
            result = self.scan_region(region)
            
            region_cities = 0
            region_locations = 0
            
            if result:
                self.stats["total_regions"] += 1
                region_cities = result["cities"]
                region_locations = result["locations"]
                self.stats["total_cities"] += region_cities
                self.stats["total_locations"] += region_locations

            region_data.append((region, region_locations))

            if not mock_delay: time.sleep(0.2)
            # Clear line if needed or just print
            print(f"{Colors.WARNING}{region:<25}{Colors.ENDC} | {Colors.BLUE}{region_cities:<15}{Colors.ENDC} | {Colors.HEADER}{region_locations:<15}{Colors.ENDC}")

        print(Colors.CYAN + "-" * 60 + Colors.ENDC)
        
        # Graph Section
        print(f"\n{Colors.BOLD}>>> BÖLGESEL YOĞUNLUK GRAFİĞİ <<<{Colors.ENDC}")
        if region_data:
            max_loc = max([x[1] for x in region_data])
            max_loc = max_loc if max_loc > 0 else 1
            for region, count in region_data:
                bar_len = int((count / max_loc) * 20)
                bar = "█" * bar_len
                print(f"{region:<20} : {Colors.GREEN}{bar:<20}{Colors.ENDC} ({count})")
            print(Colors.CYAN + "-" * 60 + Colors.ENDC)

        self.print_summary()

    def print_summary(self):
        print(f"\n{Colors.BOLD}>>> SİSTEM ÖZETİ <<<{Colors.ENDC}")
        print(f"[{Colors.GREEN}✔{Colors.ENDC}] Kapsanan Bölgeler : {self.stats['total_regions']}/7")
        print(f"[{Colors.GREEN}✔{Colors.ENDC}] Toplam Şehir      : {self.stats['total_cities']}")
        print(f"[{Colors.GREEN}✔{Colors.ENDC}] Arşivlenen Nokta  : {self.stats['total_locations']}")
        print(f"\n{Colors.CYAN}> Veri analizi tamamlandı. Oturum kapatılıyor...{Colors.ENDC}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Travel Log Analytics Tool")
    parser.add_argument("--fast", action="store_true", help="Skip animations")
    args = parser.parse_args()

    analytics = TravelLogAnalytics()
    try:
        analytics.run_analysis(mock_delay=args.fast)
    except KeyboardInterrupt:
        print("\n> İşlem iptal edildi.")
