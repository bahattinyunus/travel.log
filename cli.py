import os
import sys
import time
import shutil
import argparse
import random
import json
from datetime import datetime
from analytics import TravelLogAnalytics, Colors
from map_generator import MapGenerator

class TravelCLI:
    def __init__(self):
        self.analytics = TravelLogAnalytics()
        self.map_gen = MapGenerator()

    # ... (cinematic_boot and print_menu unchanged, effectively kept by context if not replaced, 
    # but since I must replace blocks, I will target the class structure carefully or rewrite large chunks if needed.
    # To be safe and since I'm adding methods, I will insert them before `interactive_mode` and update `interactive_mode` and `main`)

    def cinematic_boot(self):
        """Simulates a high-tech system boot."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.GREEN}INITIALIZING TRAVEL LOG PROTOCOL...{Colors.ENDC}")
        time.sleep(0.5)
        
        steps = [
            "Loading Core Modules...",
            "Encrypting Connection...",
            "Calibrating Satellite Sensors...",
            "Accessing Anadolu_Database...",
            "Verifying Integrity Hashes..."
        ]
        
        for step in steps:
            print(f"{Colors.CYAN}[SYS] {step}{Colors.ENDC}")
            time.sleep(random.uniform(0.1, 0.4))
            
        print(f"\n{Colors.BOLD}{Colors.GREEN}ACCESS GRANTED.{Colors.ENDC}\n")
        time.sleep(0.5)

    def print_menu(self):
        print(f"{Colors.MAGENTA}╔════════════════════════════════════════╗{Colors.ENDC}")
        print(f"{Colors.MAGENTA}║      TRAVEL COMMAND CENTER v3.1        ║{Colors.ENDC}")
        print(f"{Colors.MAGENTA}╚════════════════════════════════════════╝{Colors.ENDC}")
        print("1. 📝 New Entry (Yeni Kayıt)")
        print("2. 🗺️  Update Map (Harita Güncelle)")
        print("3. 📊 System Stats (İstatistikler)")
        print("4. 🔍 Search Logs (Arama)")
        print("5. 📦 Export Data (JSON İhracat)")
        print("6. 🐇 Secret Protocol")
        print("7. ❌ Exit (Çıkış)")
        print(f"{Colors.CYAN}-{Colors.ENDC}"*40)

    def ask_input(self, prompt, required=True):
        while True:
            value = input(f"{Colors.GREEN}user@travellog:~${Colors.ENDC} {prompt}: ").strip()
            if value:
                return value
            if not required:
                return ""
            print(f"{Colors.FAIL}>> ERROR: Input required.{Colors.ENDC}")

    def create_entry(self):
        print(f"\n{Colors.CYAN}>>> INITIATING NEW LOG SEQUENCE <<<{Colors.ENDC}")
        
        # Select Region
        print("\n[DETECTED REGIONS]:")
        for idx, region in enumerate(self.analytics.REGIONS):
            print(f"{Colors.BLUE}{idx+1}.{Colors.ENDC} {region}")
        
        while True:
            try:
                choice_input = self.ask_input("Select Region ID")
                choice = int(choice_input)
                if 1 <= choice <= len(self.analytics.REGIONS):
                    region = self.analytics.REGIONS[choice-1]
                    break
            except ValueError:
                pass
            print(f"{Colors.FAIL}>> INVALID SELECTION.{Colors.ENDC}")

        city = self.ask_input("Target City (e.g., Amasya)")
        location = self.ask_input("Target Location (e.g., Harşena)")
        
        # Create paths
        region_path = os.path.join(".", region)
        city_path = os.path.join(region_path, city)
        loc_path = os.path.join(city_path, location.replace(" ", "_"))
        
        if os.path.exists(loc_path):
            print(f"{Colors.WARNING}>> ALERT: Location already indexed!{Colors.ENDC}")
            if self.ask_input("Overwrite? (y/n)").lower() != 'y':
                return

        os.makedirs(loc_path, exist_ok=True)
        
        # Prepare content
        coords = self.ask_input("Coordinates (Lat, Lon) [Optional]", required=False)
        quote = self.ask_input("Mission Quote [Optional]", required=False)
        review = self.ask_input("Mission Report (Impressions)")
        
        template_content = ""
        try:
            with open(os.path.join("_Sablon", "location_template.md"), "r", encoding="utf-8") as f:
                template_content = f.read()
        except FileNotFoundError:
            print(f"{Colors.FAIL}>> CRITICAL ERROR: Template Missing!{Colors.ENDC}")
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
            
        print(f"\n{Colors.GREEN}>> SUCCESS: Log encrypted and saved to:{Colors.ENDC}")
        print(f"{target_file}")
        print(f"{Colors.BLUE}>> INFO: Ready for manual editing.{Colors.ENDC}")
        time.sleep(1)

    def search_logs(self):
        keyword = self.ask_input("Enter Search Keyword")
        print(f"\n{Colors.CYAN}>>> SCANNING DATABASE FOR '{keyword}'... <<<{Colors.ENDC}")
        time.sleep(0.5)
        
        found_count = 0
        for region in self.analytics.REGIONS:
            if not os.path.exists(region): continue
            for root, dirs, files in os.walk(region):
                for file in files:
                    if file.lower() == "readme.md":
                        path = os.path.join(root, file)
                        try:
                            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                                content = f.read()
                                if keyword.lower() in content.lower():
                                    found_count += 1
                                    rel_path = os.path.relpath(path, ".")
                                    print(f"{Colors.GREEN}[HIT]{Colors.ENDC} Found in: {Colors.BOLD}{rel_path}{Colors.ENDC}")
                        except:
                            pass
        
        if found_count == 0:
            print(f"{Colors.FAIL}>> NO MATCHES FOUND.{Colors.ENDC}")
        else:
            print(f"\n{Colors.GREEN}>> SCAN COMPLETE. Total Matches: {found_count}{Colors.ENDC}")
        
        input(f"\n{Colors.WARNING}[PRESS ENTER TO CONTINUE]{Colors.ENDC}")

    def export_data(self):
        print(f"\n{Colors.CYAN}>>> EXPORTING DATA TO JSON... <<<{Colors.ENDC}")
        data = []
        
        for region in self.analytics.REGIONS:
            if not os.path.exists(region): continue
            for root, dirs, files in os.walk(region):
                if "README.md" in files:
                    path = os.path.join(root, "README.md")
                    try:
                        with open(path, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                            # Basic extraction
                            parts = root.split(os.sep)
                            # Expected structure: ./Region/City/Location
                            entry = {
                                "region": parts[1] if len(parts) > 1 else "Unknown",
                                "city": parts[2] if len(parts) > 2 else "Unknown",
                                "location": parts[3] if len(parts) > 3 else "Unknown",
                                "path": path,
                                "size_bytes": len(content)
                            }
                            data.append(entry)
                    except:
                        pass
        
        output_file = "travel_data.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print(f"{Colors.GREEN}>> SUCCESS: Data exported to {output_file}{Colors.ENDC}")
        print(f"{Colors.BLUE}>> Total Entries Encoded: {len(data)}{Colors.ENDC}")
        time.sleep(1)

    def secret_protocol(self):
        print(f"\n{Colors.FAIL}{Colors.BOLD}*** TOP SECRET PROTOCOL INITIATED ***{Colors.ENDC}")
        time.sleep(1)
        print("Decrypting legacy files...")
        time.sleep(1)
        print(f"{Colors.GREEN}")
        print("      _~")
        print("   _~ )_)_~")
        print("   )_))_))_)")
        print("   _!__!__!_")
        print("   \\______t/")
        print(" ~~~~~~~~~~~~~")
        print(f"{Colors.ENDC}")
        print(f"{Colors.CYAN}The Digital Evliya Çelebi sails forever...{Colors.ENDC}")
        time.sleep(2)

    def interactive_mode(self):
        self.cinematic_boot()
        while True:
            self.print_menu()
            choice = self.ask_input("Command")
            
            if choice == "1":
                self.create_entry()
            elif choice == "2":
                self.map_gen.generate_map()
                print(f"{Colors.GREEN}>> Map updated.{Colors.ENDC}")
                time.sleep(1)
            elif choice == "3":
                self.analytics.run_analysis()
                input(f"\n{Colors.WARNING}[PRESS ENTER TO RETURN]{Colors.ENDC}")
            elif choice == "4":
                self.search_logs()
            elif choice == "5":
                self.export_data()
            elif choice == "6":
                self.secret_protocol()
            elif choice == "7":
                print(f"{Colors.GREEN}>> System Shutdown.{Colors.ENDC}")
                break
            else:
                print(f"{Colors.FAIL}>> UKNOWN COMMAND.{Colors.ENDC}")
                time.sleep(0.5)

    def main(self):
        parser = argparse.ArgumentParser(description="Travel Log Elite CLI")
        subparsers = parser.add_subparsers(dest="command", help="System Commands")
        
        subparsers.add_parser("add", help="New Entry")
        subparsers.add_parser("map", help="Update Map")
        subparsers.add_parser("stats", help="Show Dashboard")
        subparsers.add_parser("search", help="Search Logs")
        subparsers.add_parser("export", help="Export to JSON")
        
        args = parser.parse_args()
        
        if args.command == "add":
            self.create_entry()
        elif args.command == "map":
            self.map_gen.generate_map()
        elif args.command == "stats":
            self.analytics.run_analysis()
        elif args.command == "search":
            self.search_logs()
        elif args.command == "export":
            self.export_data()
        else:
            # Default to interactive mode if no args
            self.interactive_mode()

if __name__ == "__main__":
    cli = TravelCLI()
    try:
        cli.main()
    except KeyboardInterrupt:
        print(f"\n{Colors.FAIL}>> FORCED SHUTDOWN.{Colors.ENDC}")
