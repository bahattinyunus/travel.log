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

    def print_dashboard(self, region_data):
        """Prints a high-tech dashboard summary."""
        print(f"\n{Colors.MAGENTA}╔══════════════════════════════════════════════════════════════╗{Colors.ENDC}")
        print(f"{Colors.MAGENTA}║                  MISSION STATUS REPORT                       ║{Colors.ENDC}")
        print(f"{Colors.MAGENTA}╠════════════════════════════════╦═════════════════════════════╣{Colors.ENDC}")
        
        # Stats Row 1
        r_count = str(self.stats['total_regions']).center(5)
        c_count = str(self.stats['total_cities']).center(5)
        l_count = str(self.stats['total_locations']).center(5)
        
        print(f"{Colors.MAGENTA}║{Colors.ENDC} REGIONS: {Colors.CYAN}{r_count}{Colors.ENDC} {Colors.MAGENTA}│{Colors.ENDC} CITIES: {Colors.CYAN}{c_count}{Colors.ENDC} {Colors.MAGENTA}│{Colors.ENDC} LOCATIONS: {Colors.GREEN}{l_count}{Colors.ENDC} {Colors.MAGENTA}║{Colors.ENDC}")
        print(f"{Colors.MAGENTA}╠════════════════════════════════╩═════════════════════════════╣{Colors.ENDC}")
        
        # Most Active Region
        if region_data:
            best_region = max(region_data, key=lambda x: x[1])
            print(f"{Colors.MAGENTA}║{Colors.ENDC} HOTSPOT: {Colors.WARNING}{best_region[0]:<20}{Colors.ENDC} ({best_region[1]} Locs)       {Colors.MAGENTA}║{Colors.ENDC}")
        
        print(f"{Colors.MAGENTA}╚══════════════════════════════════════════════════════════════╝{Colors.ENDC}")

    def run_analysis(self, mock_delay=False):
        """Main analysis loop."""
        
        # Clear screen if not fast mode, to keep the immersive feel
        if not mock_delay:
            os.system('cls' if os.name == 'nt' else 'clear')
        
        print(Colors.CYAN + """
    ╔══════════════════════════════════════════════════════════════╗
    ║   TRAVEL LOG ANALYTICS CORE v4.0 (QUANTUM)                   ║
    ║   CONNECTED TO: ANADOLU_DATABASE                             ║
    ╚══════════════════════════════════════════════════════════════╝
        """ + Colors.ENDC)
        
        if not mock_delay:
            self.type_effect(Colors.GREEN + "> Uplinking to Satellite Network..." + Colors.ENDC, 0.02)
            time.sleep(0.3)
            self.type_effect(Colors.GREEN + "> Downloading Manifest..." + Colors.ENDC, 0.02)
            time.sleep(0.3)
        
        print("\n")
        print(f"{Colors.BOLD}{'REGION ID':<25} | {'CITIES':<10} | {'LOCATIONS':<10}{Colors.ENDC}")
        print(Colors.CYAN + "=" * 60 + Colors.ENDC)

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

            if not mock_delay: time.sleep(0.1)
            
            # Highlight Amasya specially
            color = Colors.WARNING if "Amasya" in region else Colors.BLUE
            if "Karadeniz" in region: # Amasya is inside Karadeniz
                 pass 

            print(f"{Colors.WARNING}{region:<25}{Colors.ENDC} | {Colors.BLUE}{region_cities:<10}{Colors.ENDC} | {Colors.HEADER}{region_locations:<10}{Colors.ENDC}")

        print(Colors.CYAN + "=" * 60 + Colors.ENDC)
        
        # Graph Section with Block Characters
        print(f"\n{Colors.BOLD}>>> DENSITY VISUALIZATION <<<{Colors.ENDC}")
        if region_data:
            max_loc = max([x[1] for x in region_data])
            max_loc = max_loc if max_loc > 0 else 1
            for region, count in region_data:
                # Calculate bar length
                bar_len = int((count / max_loc) * 30)
                # Create a gradient bar if possible, or just solid
                bar = "▓" * bar_len + "░" * (30 - bar_len)
                print(f"{region:<20} : {Colors.GREEN}{bar}{Colors.ENDC} {count}")
            print(Colors.CYAN + "-" * 60 + Colors.ENDC)

        self.print_dashboard(region_data)

        if not mock_delay:
            print(f"\n{Colors.CYAN}> SESSION TERMINATED.{Colors.ENDC}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Travel Log Analytics Tool")
    parser.add_argument("--fast", action="store_true", help="Skip animations")
    args = parser.parse_args()

    analytics = TravelLogAnalytics()
    try:
        analytics.run_analysis(mock_delay=args.fast)
    except KeyboardInterrupt:
        print("\n> ABORTED.")
