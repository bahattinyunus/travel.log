import os
import time
import sys
from datetime import datetime

# ANSI Renk Kodları
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ROOT_DIR = "."
REGIONS = [
    "01_Marmara", "02_Ege", "03_Akdeniz", "04_IcAnadolu",
    "05_Karadeniz", "06_DoguAnadolu", "07_GuneydoguAnadolu"
]

def type_effect(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{Colors.GREEN}{bar}{Colors.ENDC}| {percent}% {suffix}')
    sys.stdout.flush()

def analyze_repo():
    stats = {
        "total_regions": 0,
        "total_cities": 0,
        "total_locations": 0,
    }

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Colors.CYAN + """
    ╔══════════════════════════════════════════════════════════════╗
    ║   TRAVEL LOG ACCESS TERMINAL v2.0                            ║
    ║   CONNECTED TO: ANADOLU_DATABASE                             ║
    ╚══════════════════════════════════════════════════════════════╝
    """ + Colors.ENDC)
    
    type_effect(Colors.GREEN + "> Yükleniyor... Core Modules" + Colors.ENDC, 0.05)
    time.sleep(0.5)
    type_effect(Colors.GREEN + "> Sistem: Online" + Colors.ENDC, 0.05)
    print("\n")

    print(f"{Colors.BOLD}{'BÖLGE (REGION)':<25} | {'ŞEHİR (CITY)':<15} | {'LOKASYON (LOC)':<15}{Colors.ENDC}")
    print(Colors.CYAN + "-" * 60 + Colors.ENDC)

    total_files_to_scan = len(REGIONS)
    current_scan = 0

    for region in REGIONS:
        current_scan += 1
        # progress_bar(current_scan, total_files_to_scan, prefix='Scanning:', suffix='Complete', length=30)
        
        region_cities = 0
        region_locations = 0
        
        if os.path.exists(region):
            stats["total_regions"] += 1
            for city in os.listdir(region):
                city_path = os.path.join(region, city)
                if os.path.isdir(city_path):
                    region_cities += 1
                    stats["total_cities"] += 1
                    for loc in os.listdir(city_path):
                        loc_path = os.path.join(city_path, loc)
                        if os.path.isdir(loc_path):
                            region_locations += 1
                            stats["total_locations"] += 1
        
        time.sleep(0.2) # Estetik bekleme
        sys.stdout.write("\033[K") # Satırı temizle
        print(f"{Colors.WARNING}{region:<25}{Colors.ENDC} | {Colors.BLUE}{region_cities:<15}{Colors.ENDC} | {Colors.HEADER}{region_locations:<15}{Colors.ENDC}")

    print(Colors.CYAN + "-" * 60 + Colors.ENDC)
    print(f"\n{Colors.BOLD}>>> SİSTEM ÖZETİ <<<{Colors.ENDC}")
    print(f"[{Colors.GREEN}✔{Colors.ENDC}] Kapsanan Bölgeler : {stats['total_regions']}/7")
    print(f"[{Colors.GREEN}✔{Colors.ENDC}] Toplam Şehir      : {stats['total_cities']}")
    print(f"[{Colors.GREEN}✔{Colors.ENDC}] Arşivlenen Nokta  : {stats['total_locations']}")
    print(f"\n{Colors.CYAN}> Veri analizi tamamlandı. Çıkış yapılıyor...{Colors.ENDC}")

if __name__ == "__main__":
    try:
        analyze_repo()
    except KeyboardInterrupt:
        print("\n> İşlem iptal edildi.")
