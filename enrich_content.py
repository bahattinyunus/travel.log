import os

# 13 Visited Cities with specific Sufi/Cultural landmarks
VISITED_DETAILS = {
    "Istanbul": {
        "description": "Dünyanın gözbebeği, payitaht. Hem zahiri ihtişamı hem batıni derinliğiyle seyyahların sığınağı.",
        "landmarks": ["Eyüp Sultan Camii", "Aziz Mahmud Hüdayi Türbesi", "Galata Mevlevihanesi", "Süleymaniye Camii"],
        "hikmet": "İstanbul bir şehirdir ki, yedi tepe üzerinde yedi veli bekler."
    },
    "Konya": {
        "description": "Aşkın merkezi, Mevlana'nın yurdu. Hamdım, piştim, yandım diyenlerin durak noktası.",
        "landmarks": ["Mevlana Müzesi", "Şems-i Tebrizi Türbesi", "Sadreddin Konevi Camii", "İnce Minareli Medrese"],
        "hikmet": "Gel, ne olursan ol yine gel... Ama buraya aşkla gel."
    },
    "Bursa": {
        "description": "Evliyalar şehri, Osmanlı'nın ilk payitahtı. Ulu bir çınar gibi kökleri tarihin derinliklerinde.",
        "landmarks": ["Ulu Cami", "Emir Sultan Türbesi", "Üftade Hazretleri Makamı", "Yeşil Türbe"],
        "hikmet": "Bursa'da zaman, bir eski cami avlusunda sükutla geçer."
    },
    "Ankara": {
        "description": "Anadolu'nun kalbi, Hacı Bayram-ı Veli'nin manevi muhafızlığında bir şehir.",
        "landmarks": ["Hacı Bayram-ı Veli Camii", "Taceddin Dergahı", "Ankara Kalesi"],
        "hikmet": "Dışarısını imar ederken içerisini haraap etme."
    },
    "Amasya": {
        "description": "Şehzadeler şehri, Ferhat ile Şirin'in diyarı. Yeşilırmak'ın aynasında tarihini izleyen kent.",
        "landmarks": ["Kral Kaya Mezarları", "Şeyh Hamdullah Türbesi", "II. Bayezid Külliyesi"],
        "hikmet": "Dağları delmek zordur ama gönülleri delmek (feth etmek) daha zordur."
    },
    "Corum": {
        "description": "Hititlerin kadim diyarı, leblebi kokulu Anadolu şehri.",
        "landmarks": ["Hattuşaş Antik Kenti", "Laçin Kapılıkaya Anıtsal Mezarı", "Ulu Cami"],
        "hikmet": "Geçmişin izleri üzerindeki bugünün bereketini gör."
    },
    "Samsun": {
        "description": "Milli Mücadele'nin meşale şehri. Karadeniz'in giriş kapısı.",
        "landmarks": ["Onur Anıtı", "Bandırma Gemi Müzesi", "Amisos Tepesi"],
        "hikmet": "Her büyük yürüyüş ilk bir adımla başlar."
    },
    "Sinop": {
        "description": "Mutluluğun ve sükunetin şehri. Karadeniz'in en kuzey ucu.",
        "landmarks": ["Sinop Kalesi", "Tarihi Sinop Cezaevi", "Hamsilos Koyu"],
        "hikmet": "Gölge etme başka ihsan istemem (Diyojen)."
    },
    "Giresun": {
        "description": "Fındığın ve kirazın ana vatanı. Mavi ile yeşilin kucaklaştığı yer.",
        "landmarks": ["Giresun Kalesi", "Zeytinlik Semti", "Giresun Adası"],
        "hikmet": "Denizin cömertliği insanın tevazusuyla birleşir."
    },
    "Ordu": {
        "description": "Deresi yukarı akan, fındığın diyarı, Karadeniz'in nazlı şehri.",
        "landmarks": ["Boztepe", "Yason Burnu", "Kurul Kalesi"],
        "hikmet": "Yükseklere çıkmadan ufku göremezsin."
    },
    "Kocaeli": {
        "description": "Sanayinin ve tarihin iç içe geçtiği, Marmara'nın kilit noktası.",
        "landmarks": ["İzmit Saat Kulesi", "Osman Hamdi Bey Müzesi", "Kocaeli Bilim Merkezi"],
        "hikmet": "Emek, en büyük hazinedir."
    },
    "Antalya": {
        "description": "Akdeniz'in incisi, kadim uygarlıkların limanı.",
        "landmarks": ["Kaleiçi", "Hadrian Kapısı", "Yivli Minare Camii"],
        "hikmet": "Güneşin her gün yeniden doğuşu, umudun bitmeyeceğinin delilidir."
    },
    "Denizli": {
        "description": "Pamuktan kalelerin, Hierapolis'in şifalı sularının şehri.",
        "landmarks": ["Pamukkale Travertenleri", "Hierapolis Antik Kenti", "Laodikeia"],
        "hikmet": "Su gibi aziz ol, aktığın yeri güzelleştir."
    }
}

REGIONS_MAP = {
    "01_Marmara": ["Istanbul", "Edirne", "Kirklareli", "Tekirdag", "Canakkale", "Kocaeli", "Sakarya", "Bilecik", "Bursa", "Balikesir", "Yalova"],
    "02_Ege": ["Izmir", "Manisa", "Aydin", "Denizli", "Mugla", "Afyonkarahisar", "Kutahya", "Usak"],
    "03_Akdeniz": ["Antalya", "Isparta", "Burdur", "Adana", "Mersin", "Hatay", "Osmaniye", "Kahramanmaras"],
    "04_IcAnadolu": ["Ankara", "Konya", "Kayseri", "Eskisehir", "Sivas", "Kirikkale", "Aksaray", "Karaman", "Kirsehir", "Nigde", "Nevsehir", "Yozgat", "Cankiri"],
    "05_Karadeniz": ["Bolu", "Duzce", "Zonguldak", "Karabuk", "Bartin", "Kastamonu", "Sinop", "Cankiri", "Corum", "Amasya", "Samsun", "Tokat", "Ordu", "Giresun", "Gumushane", "Bayburt", "Trabzon", "Rize", "Artvin"],
    "06_DoguAnadolu": ["Malatya", "Erzincan", "Tunceli", "Elazig", "Bingol", "Erzurum", "Mus", "Bitlis", "Kars", "Agri", "Ardahan", "Igdir", "Van", "Hakkari"],
    "07_GuneydoguAnadolu": ["Gaziantep", "Kilis", "Adiyaman", "Sanliurfa", "Diyarbakir", "Mardin", "Batman", "Siirt", "Sirnak"]
}

def enrich_readme(file_path, city_name, region_name):
    # Normalize city_name for comparison
    clean_city = city_name.strip()
    
    # Base template for all
    content = f"# 📍 {city_name} - Keşif Notları\n\n"
    
    if clean_city in VISITED_DETAILS:
        details = VISITED_DETAILS[clean_city]
        content += f"## 📜 Şehir Manifestosu\n> \"{details['hikmet']}\"\n\n"
        content += f"### 🌍 Hakkında\n{details['description']}\n\n"
        content += "### ✨ Tarihi ve Kültürel Duraklar (Önerilen)\n"
        for loc in details['landmarks']:
            content += f"- [ ] **{loc}**\n"
        content += "\n---\n*Bu il bizzat gezgin tarafından ziyaret edilmiş ve kayıt altına alınmıştır.* ✅\n"
    else:
        content += "## 📜 Şehir Felsefesi\n> \"Dünyanın her köşesi, yeni bir hikayenin başlangıcıdır.\"\n\n"
        content += f"### 🌍 {city_name} Hakkında\nAnadolu'nun zengin kültüründe henüz keşfedilmeyi ve deneyimlenmeyi bekleyen bir durak.\n\n"
        content += "### 🕊️ Gelecek Rotalar\nBu il henüz seyahatnameye detaylı olarak dahil edilmemiştir. Gelecekteki rotalarımızdan biri olması planlanmaktadır.\n"

    content += "\n## 📂 Alt İçerikler\nBu klasörde şehre ait özel mekanlar, fotoğraflar ve kişisel notlar yer alır.\n"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    for region, cities in REGIONS_MAP.items():
        if not os.path.exists(region): continue
        
        # In reality, the folders use TR characters maybe? Let's list the dir to see exact names
        actual_folders = os.listdir(region)
        for folder in actual_folders:
            folder_path = os.path.join(region, folder)
            if os.path.isdir(folder_path):
                readme_path = os.path.join(folder_path, "README.md")
                # we don't care about the cities list in REGIONS_MAP as much as the actual folders
                enrich_readme(readme_path, folder, region)
                print(f"Enriched: {readme_path}")

if __name__ == "__main__":
    main()
