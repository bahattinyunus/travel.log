import sys
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt, Confirm
from rich import print as rprint
from rich.align import Align
from rich.text import Text
import time
import os
import json
from datetime import datetime
from map_generator import MapGenerator
from analytics import TravelLogAnalytics

console = Console()

class TravelCLI:
    def __init__(self):
        self.analytics = TravelLogAnalytics()
        self.map_gen = MapGenerator()

    def cinematic_boot(self):
        """Simulates a system boot / traveler's preparation."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        boot_text = Text("SİSTEM BAŞLATILIYOR... SEYAHATNAME vPRO", style="bold green")
        console.print(Panel(boot_text, expand=False, border_style="green"))
        time.sleep(0.3)
        
        steps = [
            "Koordinatlar Yükleniyor...",
            "Harita Verileri Senkronize Ediliyor...",
            "Çanta Hazırlanıyor...",
            "Pusula Kalibre Ediliyor...",
            "Rota Hesaplanıyor..."
        ]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task1 = progress.add_task("[cyan]Sistem Hazırlığı", total=100)
            
            for step in steps:
                progress.update(task1, description=f"[cyan][BİLGİ] {step}")
                while progress.tasks[0].completed < progress.tasks[0].total:
                    time.sleep(0.01)
                    progress.update(task1, advance=random.randint(2, 5))
                    if random.random() < 0.1:
                        break
            
            while progress.tasks[0].completed < 100:
                time.sleep(0.01)
                progress.update(task1, advance=5)
                
        console.print("\n[bold green]SİSTEM HAZIR. İYİ YOLCULUKLAR.[/bold green]\n")
        time.sleep(0.2)

    def print_menu(self):
        menu_text = (
            "[bold cyan]1.[/bold cyan] 📝 Yeni Rota Kaydet (New Entry)\n"
            "[bold cyan]2.[/bold cyan] 🗺️  Seyir Haritasını Çiz (Update Map)\n"
            "[bold cyan]3.[/bold cyan] 📊 Keşif Tablosu (Dashboard)\n"
            "[bold cyan]4.[/bold cyan] 🔍 Kayıtları Ara (Deep Search)\n"
            "[bold cyan]5.[/bold cyan] 📦 Veriyi Dışarı Aktar (Export Analytics)\n"
            "[bold cyan]6.[/bold cyan] ❌ Sistemi Kapat (Exit)\n"
        )
        
        panel = Panel(
            Align.center(menu_text),
            title="[bold magenta]SEYAHATNAME vPRO[/bold magenta]",
            border_style="magenta",
            expand=False
        )
        console.print(panel)

    def create_entry(self):
        console.print("\n[bold cyan]>>> YENİ BİR MENZİL KAYDEDİLİYOR <<<[/bold cyan]")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=4)
        table.add_column("İklim (Region)", style="bold blue")
        
        for idx, region in enumerate(self.analytics.REGIONS):
            table.add_row(str(idx+1), region)
            
        console.print(table)
        
        choice_input = Prompt.ask("[bold green]gezgin@seyahat:~[/bold green] Bölge Numarası Seç")
        try:
            choice = int(choice_input)
            if 1 <= choice <= len(self.analytics.REGIONS):
                region = self.analytics.REGIONS[choice-1]
            else:
                 console.print("[bold red]>> GEÇERSİZ SEÇİM.[/bold red]")
                 return
        except ValueError:
             console.print("[bold red]>> GEÇERSİZ SEÇİM.[/bold red]")
             return

        city = Prompt.ask("[bold green]gezgin@seyahat:~[/bold green] Hedef Şehir (örn. Konya)")
        location = Prompt.ask("[bold green]gezgin@seyahat:~[/bold green] Ziyaret Edilen Mekan (örn. Mevlana Müzesi)")
        
        region_path = os.path.join(".", region)
        city_path = os.path.join(region_path, city)
        loc_path = os.path.join(city_path, location.replace(" ", "_"))
        
        if os.path.exists(loc_path):
            console.print("[bold yellow]>> UYARI: Bu mekan zaten kaydedilmiş![/bold yellow]")
            if not Confirm.ask("Üzerine yazılsın mı?"):
                return

        os.makedirs(loc_path, exist_ok=True)
        
        coords = Prompt.ask("[bold green]gezgin@seyahat:~[/bold green] Koordinatlar (Enlem, Boylam) [İsteğe Bağlı]", default="")
        quote = Prompt.ask("[bold green]gezgin@seyahat:~[/bold green] Seyahat Notu (Kısa Açıklama/Alıntı)", default="")
        
        try:
            with open(os.path.join("_Sablon", "location_template.md"), "r", encoding="utf-8") as f:
                template_content = f.read()
        except FileNotFoundError:
            console.print("[bold red]>> CRITICAL ERROR: Template Missing![/bold red]")
            return

        filled_content = template_content.replace("[Lokasyon Adı]", location)
        filled_content = filled_content.replace("DD.MM.YYYY", datetime.now().strftime("%d.%m.%Y"))
        
        if coords:
            filled_content = filled_content.replace("XX.XXXX, YY.YYYY", coords)
        
        if quote:
            filled_content = filled_content.replace("[Buraya lokasyonla ilgili kısa, vurucu bir alıntı veya his eklenecek]", quote)
            
        target_file = os.path.join(loc_path, "README.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(filled_content)
            
        console.print(f"\n[bold green]>> KAYIT BAŞARILI:[bold green] Şuraya kaydedildi:\n{target_file}")
        time.sleep(1)

    def interactive_mode(self):
        import random
        # make random available for cinematic boot
        global random
        import random
        
        self.cinematic_boot()
        while True:
            self.print_menu()
            choice = Prompt.ask("[bold green]gezgin@seyahat:~[/bold green] Komut Nedir?")
            
            if choice == "1":
                self.create_entry()
            elif choice == "2":
                with console.status("[bold green]Seyir Haritası Çiziliyor...") as status:
                    try:
                        self.map_gen.generate_map()
                        console.print("[bold green]>> Harita oluşturuldu: travel_map.html.[/bold green]")
                    except Exception as e:
                        console.print(f"[bold red]>> Harita çizilirken hata oluştu: {e}[/bold red]")
                time.sleep(1)
            elif choice == "3":
                self.analytics.run_analysis()
                Prompt.ask("\n[bold yellow][MENÜYE DÖNMEK İÇİN ENTER'A BAS][/bold yellow]")
            elif choice == "4":
                console.print("[bold cyan]>> Arama özelliği henüz vPRO sürümünde geliştiriliyor...[/bold cyan]")
                time.sleep(1)
            elif choice == "5":
                console.print("[bold cyan]>> Verileri dışarı aktarım yapılıyor...[/bold cyan]")
                time.sleep(1)
            elif choice == "6":
                console.print("[bold green]>> Sistem Kapatıldı. İyi yolculuklar.[/bold green]")
                break
            else:
                console.print("[bold red]>> GEÇERSİZ KOMUT.[/bold red]")
                time.sleep(0.5)

    def main(self):
        parser = argparse.ArgumentParser(description="Seyahatname vPRO")
        subparsers = parser.add_subparsers(dest="command", help="System Commands")
        
        subparsers.add_parser("add", help="New Entry")
        subparsers.add_parser("map", help="Update Map")
        subparsers.add_parser("stats", help="Show Dashboard")
        
        args = parser.parse_args()
        
        if args.command == "add":
            self.create_entry()
        elif args.command == "map":
            self.map_gen.generate_map()
        elif args.command == "stats":
            self.analytics.run_analysis()
        else:
            self.interactive_mode()

if __name__ == "__main__":
    cli = TravelCLI()
    try:
        cli.main()
    except KeyboardInterrupt:
        console.print("\n[bold red]>> FORCED SHUTDOWN.[/bold red]")
