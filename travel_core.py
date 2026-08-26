"""
Anadolu Seyahatnamesi - Dijital Seyyah Core Engine
81 İl, 7 Bölge, Koordinatlar, Kütüphane Verileri ve Seyahat Analitiği
"""

import os
import json
import re
import math
from pathlib import Path

# 81 İl Bilgisi ve Koordinat Veritabanı
PROVINCES_DATA = {
    # 01_Marmara (11 İl)
    "01_Marmara/Balikesir": {
        "plate": 10, "name": "Balıkesir", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 39.6484, "lng": 27.8826,
        "landmarks": ["Zağnos Paşa Camii", "Cunda Adası", "Kaz Dağları", "Manyas Kuş Cenneti"],
        "specialties": ["Höşmerim", "Susurluk Tostu & Ayranı", "Balıkesir Kaymaklısı"],
        "quote": "Kaz Dağları'nın oksijeni ile Marmara ve Ege'nin buluştuğu bereketli topraklar.",
        "library": "Balıkesir İl Halk Kütüphanesi - Geniş bahçesi ve sakin çalışma alanlarıyla verimli bir ortam."
    },
    "01_Marmara/Bilecik": {
        "plate": 11, "name": "Bilecik", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 40.1426, "lng": 29.9793,
        "landmarks": ["Şeyh Edebali Türbesi", "Söğüt Ertuğrul Gazi Türbesi", "Saat Kulesi"],
        "specialties": ["Bilecik Güveci", "Pazaryeri Helvası", "Bıldırcın Kebabı"],
        "quote": "Osmanlı Devleti'nin mayalandığı, Şeyh Edebali'nin 'İnsanı yaşat ki devlet yaşasın' nasihatinin yankılandığı kurucu menzil.",
        "library": "Bilecik İl Halk Kütüphanesi - Sakin ve odaklanmaya elverişli butik bir çalışma alanı."
    },
    "01_Marmara/Bursa": {
        "plate": 16, "name": "Bursa", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 40.1885, "lng": 29.0610,
        "landmarks": ["Ulu Cami", "Yeşil Türbe", "Cumalıkızık", "Emir Sultan Camii", "Muradiye Külliyesi"],
        "specialties": ["İskender Kebap", "Kestane Şekeri", "Muradiye Çorbası", "Cantık"],
        "quote": "Bursa'da zaman, bir yeşil şadırvanda şırıldayan suyun musikisidir; Osmanlı'nın kurucu ve manevi payitahtı.",
        "library": "Bursa İl Halk Kütüphanesi - Geniş ve ferah salonları, zengin araştırma kaynakları ve huzurlu bahçesiyle ideal bir ilim yuvası."
    },
    "01_Marmara/Canakkale": {
        "plate": 17, "name": "Çanakkale", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 40.1553, "lng": 26.4142,
        "landmarks": ["Şehitler Abidesi", "Truva Antik Kenti", "Aynalı Çarşı", "Kilitbahir Kalesi"],
        "specialties": ["Peynir Helvası", "Sardalya", "Ezine Peyniri"],
        "quote": "Tarihin yazıldığı, bir milletin bağımsızlık destanını kanıyla mühürlediği manevi boğaz.",
        "library": "Çanakkale Mehmet Akif Ersoy İl Halk Kütüphanesi - Modern deniz manzaralı ferah çalışma ortamı."
    },
    "01_Marmara/Edirne": {
        "plate": 22, "name": "Edirne", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 41.6772, "lng": 26.5557,
        "landmarks": ["Selimiye Camii", "II. Bayezid Külliyesi Sağlık Müzesi", "Meriç Köprüsü", "Eski Cami"],
        "specialties": ["Edirne Tava Ciğeri", "Badem Ezmesi", "Kavala Kurabiyesi"],
        "quote": "Mimar Sinan'ın 'Ustalık eserim' dediği Selimiye ile taçlanmış, Osmanlı'nın Avrupa kapısı payitaht.",
        "library": "Edirne İl Halk Kütüphanesi - Tarihi dokusu içinde sükunet dolu araştırma alanı."
    },
    "01_Marmara/Istanbul": {
        "plate": 34, "name": "İstanbul", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 41.0082, "lng": 28.9784,
        "landmarks": ["Ayasofya-i Kebir", "Süleymaniye Camii", "Topkapı Sarayı", "Eyüp Sultan", "Galata Kulesi"],
        "specialties": ["Sultanahmet Köftesi", "Balık Ekmek", "Boza", "Kanlıca Yoğurdu"],
        "quote": "İki kıtanın secdesi, çağ açıp çağ kapatan ulu fethin emaneti ve medeniyetler başkenti.",
        "library": "Şemsipaşa İlçe Halk Kütüphanesi (Üsküdar) / Rami Kütüphanesi - Denize sıfır konumu ve asırlık atmosferiyle eşsiz bir çalışma sığınağı."
    },
    "01_Marmara/Kirklareli": {
        "plate": 39, "name": "Kırklareli", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 41.7355, "lng": 27.2244,
        "landmarks": ["İğneada Longoz Ormanları", "Dupnisa Mağarası", "Hızırbey Camii"],
        "specialties": ["Kırklareli Köftesi", "Hardaliye", "Kaşar Peyniri"],
        "quote": "Trakya'nın yeşil kalbi, Longoz Ormanları'nın büyüleyici biyoçeşitliliği ve huzurlu bozkırı.",
        "library": "Kırklareli İl Halk Kütüphanesi - Sakin ve odaklanmayı artıran kütüphane düzeni."
    },
    "01_Marmara/Kocaeli": {
        "plate": 41, "name": "Kocaeli", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 40.7654, "lng": 29.9408,
        "landmarks": ["Saat Kulesi", "Sekapark", "Kandıra Kerpe Kayalıkları", "Gayret Gemi Müzesi"],
        "specialties": ["Pişmaniye", "Kandıra Yoğurdu", "Dartı"],
        "quote": "Körfezin sanayi ve lojistik damarı, Samanlı Dağları'nın yeşiliyle kucaklaşan kıyı kenti.",
        "library": "Kocaeli İl Halk Kütüphanesi - Modern iç tasarımı ve güçlü internet altyapısıyla kodlama mesaileri için son derece konforlu."
    },
    "01_Marmara/Sakarya": {
        "plate": 54, "name": "Sakarya", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 40.7731, "lng": 30.4026,
        "landmarks": ["Sapanca Gölü", "Justinianus Köprüsü (Beşköprü)", "Acarlar Longozu", "Taraklı Evleri"],
        "specialties": ["Islama Köfte", "Kabak Tatlısı", "Uğut Tatlısı"],
        "quote": "Sakarya Türküsü'nün döküldüğü ırmak, bereketli ovaları ve kadim Osmanlı kasabalarıyla köklü bir durak.",
        "library": "Sakarya İl Halk Kütüphanesi - Geniş çalışma masaları ve ferah ortamıyla verimli çalışma imkanı."
    },
    "01_Marmara/Tekirdag": {
        "plate": 59, "name": "Tekirdağ", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 40.9781, "lng": 27.5117,
        "landmarks": ["Namık Kemal Evi", "Rákóczi Müzesi", "Rüstem Paşa Camii", "Uçmakdere"],
        "specialties": ["Tekirdağ Köftesi", "Hayrabolu Tatlısı", "Peynir Helvası"],
        "quote": "Marmara'nın rüzgarlı kıyısı, vatan şairi Namık Kemal'in yurdu ve yamaç paraşütünün gözdesi.",
        "library": "Tekirdağ Namık Kemal İl Halk Kütüphanesi - Huzurlu deniz havası eşliğinde çalışma olanağı."
    },
    "01_Marmara/Yalova": {
        "plate": 77, "name": "Yalova", "region": "Marmara", "region_code": "01_Marmara",
        "lat": 40.6549, "lng": 29.2842,
        "landmarks": ["Yürüyen Köşk", "Termal Kaplıcaları", "Sudüşen Şelalesi", "Karaca Arboretumu"],
        "specialties": ["Yalova Köftesi", "Termal Tatlısı", "Kivi"],
        "quote": "Yeşilin her tonunu saklayan şifalı sular diyarı ve çevrecilik sembolü Yürüyen Köşk'ün yurdu.",
        "library": "Yalova İl Halk Kütüphanesi - Şehir merkezinde butik, sakin ve odaklanmaya uygun bir mekan."
    },

    # 02_Ege (8 İl)
    "02_Ege/Afyonkarahisar": {
        "plate": 3, "name": "Afyonkarahisar", "region": "Ege", "region_code": "02_Ege",
        "lat": 38.7569, "lng": 30.5387,
        "landmarks": ["Afyon Kalesi", "Mevlevi Camii ve Türbesi", "Frig Vadisi", "Ulu Cami"],
        "specialties": ["Afyon Sucuğu", "Kaymaklı Ekmek Kadayıfı", "Bükme", "Haşhaşlı Çörek"],
        "quote": "Karahisar Kalesi'nin heybeti, Mevleviliğin ikinci büyük ocağı ve Anadolu'nun kavşak noktası.",
        "library": "Afyonkarahisar Gedik Ahmet Paşa İl Halk Kütüphanesi - Tarihi dokuda sakin çalışma alanı."
    },
    "02_Ege/Aydin": {
        "plate": 9, "name": "Aydın", "region": "Ege", "region_code": "02_Ege",
        "lat": 37.8380, "lng": 27.8456,
        "landmarks": ["Aphrodisias Antik Kenti", "Didim Apollon Tapınağı", "Milet Antik Kenti", "Güvercinada Kalesi"],
        "specialties": ["İncir", "Çine Köftesi", "Zeytinyağlı Börülce", "Kabak Tatlısı"],
        "quote": "Gökyüzünün altındaki en güzel yeryüzü; bereketli Menderes Ovası ve antik mermerlerin zarafeti.",
        "library": "Aydın İl Halk Kütüphanesi - Üniversite ve şehir yaşamının kesiştiği ferah kütüphane."
    },
    "02_Ege/Denizli": {
        "plate": 20, "name": "Denizli", "region": "Ege", "region_code": "02_Ege",
        "lat": 37.7830, "lng": 29.0963,
        "landmarks": ["Pamukkale Travertenleri", "Hierapolis Antik Kenti", "Laodikeia", "Kaklık Mağarası"],
        "specialties": ["Denizli Kebabı", "Zafer Gazozu", "Tavas Pidesi", "Çameli Fasulyesi"],
        "quote": "Beyaz cennet travertenlerin şükür makamı ve antik Hierapolis'in şifalı termal havuzları.",
        "library": "Denizli İl Halk Kütüphanesi - Şehir merkezinde, sessiz çalışma salonları geniş, öğleden sonra kalabalık olabiliyor."
    },
    "02_Ege/Izmir": {
        "plate": 35, "name": "İzmir", "region": "Ege", "region_code": "02_Ege",
        "lat": 38.4192, "lng": 27.1287,
        "landmarks": ["Saat Kulesi", "Efes Antik Kenti", "Tarihi Kemeraltı Çarşısı", "Kadifekale", "Şirince"],
        "specialties": ["İzmir Boyozu", "Kumru", "İzmir Bombası", "Tulum Peyniri", "Şambali"],
        "quote": "Ege'nin incisi; Akdeniz rüzgarının özgürlük fısıldadığı, antik kütüphanelerin ve limanların şehri.",
        "library": "İzmir Milli Kütüphane / Atatürk İl Halk Kütüphanesi - Tarihi neoclassic mimarisi ve muazzam kitap koleksiyonuyla ilham kaynağı."
    },
    "02_Ege/Kutahya": {
        "plate": 43, "name": "Kütahya", "region": "Ege", "region_code": "02_Ege",
        "lat": 39.4244, "lng": 29.9833,
        "landmarks": ["Aizanoi Antik Kenti", "Kütahya Kalesi", "Dönenler Camii (Mevlevihane)", "Çini Müzesi"],
        "specialties": ["Kütahya Güveci", "Cimcik Aşı", "Sini Mantısı"],
        "quote": "Çininin nakış nakış işlendiği sabır şehri, Germiyanoğulları'nın yadigarı ve Mevlevi ocağı.",
        "library": "Kütahya Vahit Paşa İl Halk Kütüphanesi - Yazma eserler koleksiyonu ve huzurlu salonları."
    },
    "02_Ege/Manisa": {
        "plate": 45, "name": "Manisa", "region": "Ege", "region_code": "02_Ege",
        "lat": 38.6140, "lng": 27.4296,
        "landmarks": ["Muradiye Camii", "Sultan Camii", "Spil Dağı Milli Parkı", "Sardes Antik Kenti"],
        "specialties": ["Manisa Kebabı", "Mesir Macunu", "Kula Güveci"],
        "quote": "Şehzadeler şehri; Mimar Sinan'ın Muradiye'si ve Spil Dağı'nın şifalı rüzgarları.",
        "library": "Manisa İl Halk Kütüphanesi - Ferah çalışma salonları ve merkezi konumuyla verimli."
    },
    "02_Ege/Mugla": {
        "plate": 48, "name": "Muğla", "region": "Ege", "region_code": "02_Ege",
        "lat": 37.2153, "lng": 28.3636,
        "landmarks": ["Ölüdeniz", "Kelebekler Vadisi", "Bodrum Kalesi", "Saklıkent Kanyonu", "Dalyan Kaunos Kral Mezarları"],
        "specialties": ["Muğla Köftesi", "Çökertme Kebabı", "Kabak Çiçeği Dolması", "Börülce"],
        "quote": "Turkuaz koyların antik Likya ve Karya ile kucaklaştığı, tabiatın cömertçe sergilendiği cennet köşe.",
        "library": "Muğla İl Halk Kütüphanesi - Üniversite bölgesine yakın, çalışma ortamı sessiz ve ferah, priz sayısı yeterli."
    },
    "02_Ege/Usak": {
        "plate": 64, "name": "Uşak", "region": "Ege", "region_code": "02_Ege",
        "lat": 38.6735, "lng": 29.4059,
        "landmarks": ["Ulubey Kanyonu", "Blaundos Antik Kenti", "Clandras Köprüsü", "Uşak Arkeoloji Müzesi"],
        "specialties": ["Tarhana Çorbası", "Döndürme Böreği", "Ebeli Köftesi"],
        "quote": "Dünyanın en uzun ikinci kanyonuna sahip, Karun Hazineleri'nin saklandığı kadim halı ve kilim diyarı.",
        "library": "Uşak İl Halk Kütüphanesi - Sessiz, nezih ve çalışmaya elverişli ortam."
    },

    # 03_Akdeniz (8 İl)
    "03_Akdeniz/Adana": {
        "plate": 1, "name": "Adana", "region": "Akdeniz", "region_code": "03_Akdeniz",
        "lat": 37.0000, "lng": 35.3213,
        "landmarks": ["Taşköprü", "Sabancı Merkez Camii", "Büyük Saat", "Varda Köprüsü", "Anavarza Antik Kenti"],
        "specialties": ["Adana Kebap", "Şalgam Suyu", "Bici Bici", "Analı Kızlı Çorbası", "Halka Tatlı"],
        "quote": "Seyhan'ın serinliğiyle Çukurova'nın cömert sıcağını harmanlayan, lezzetin ve samimiyetin başkenti.",
        "library": "Adana İl Halk Kütüphanesi - Şehir merkezinde yer alıyor, klimaları yaz sıcağında can kurtarıyor, priz imkanları iyi."
    },
    "03_Akdeniz/Antalya": {
        "plate": 7, "name": "Antalya", "region": "Akdeniz", "region_code": "03_Akdeniz",
        "lat": 36.8969, "lng": 30.7133,
        "landmarks": ["Kaleiçi", "Yivli Minare", "Düden Şelalesi", "Aspendos Tiyatrosu", "Termessos", "Olympos"],
        "specialties": ["Antalya Piyazı (Tahinli)", "Hibeş", "Yanık Dondurma", "Turunç Reçeli"],
        "quote": "Torosların gölgesinde Akdeniz'in kadim kodlarını taşıyan sıcacık liman ve medeniyetler beşiği.",
        "library": "Antalya İl Halk Kütüphanesi - Yeşillikler içindeki bahçesi ve geniş okuma salonlarıyla Akdeniz sıcağında serin bir çalışma limanı."
    },
    "03_Akdeniz/Burdur": {
        "plate": 15, "name": "Burdur", "region": "Akdeniz", "region_code": "03_Akdeniz",
        "lat": 37.7183, "lng": 30.2823,
        "landmarks": ["Salda Gölü", "Sagalassos Antik Kenti", "İnsuyu Mağarası", "Burdur Arkeoloji Müzesi"],
        "specialties": ["Burdur Şiş", "Ceviz Ezmesi", "Testi Kebabı"],
        "quote": "Göller Yöresi'nin incisi Salda'nın turkuaz suları ve Sagalassos'un Antoninler Çeşmesi'nde akan asırlık sular.",
        "library": "Burdur İl Halk Kütüphanesi - Göller yöresinin sükunetini yansıtan sessiz çalışma alanı."
    },
    "03_Akdeniz/Hatay": {
        "plate": 31, "name": "Hatay", "region": "Akdeniz", "region_code": "03_Akdeniz",
        "lat": 36.2023, "lng": 36.1613,
        "landmarks": ["Habib-i Neccar Camii", "St. Pierre Kilisesi", "Titus Tüneli & Beşikli Mağara", "Arkeoloji Müzesi"],
        "specialties": ["Künefe", "Tepsi Kebabı", "Humus", "Muhammara", "Oruk (İçli Köfte)"],
        "quote": "Medeniyetlerin, dinlerin ve kadim lezzetlerin bir arada kardeşçe yaşadığı ibret ve vefa şehri.",
        "library": "Hatay İl Halk Kütüphanesi - Tarihi dokusuyla ilham verici, sessiz çalışma odaları tefekkür ve kodlama için çok uygun."
    },
    "03_Akdeniz/Isparta": {
        "plate": 32, "name": "Isparta", "region": "Akdeniz", "region_code": "03_Akdeniz",
        "lat": 37.7648, "lng": 30.5566,
        "landmarks": ["Eğirdir Gölü", "Kuyucak Lavanta Köyü", "Kovada Gölü Milli Parkı", "Firdevs Bey Camii"],
        "specialties": ["Isparta Kebabı (Fırın Kebap)", "Gül Lokumu & Gül Reçeli", "Kabune Pilavı"],
        "quote": "Güllerin ve lavantaların kokusuyla bezenmiş, Eğirdir Gölü'nün masmavi sükunetinde huzur bulunan diyar.",
        "library": "Isparta Halil Hamit Paşa İl Halk Kütüphanesi - Şehir merkezinde, sessiz çalışma alanları geniş ve ferah."
    },
    "03_Akdeniz/Kahramanmaras": {
        "plate": 46, "name": "Kahramanmaraş", "region": "Akdeniz", "region_code": "03_Akdeniz",
        "lat": 37.5753, "lng": 36.9228,
        "landmarks": ["Maraş Kalesi", "Ulu Cami", "Taş Medrese", "Eshab-ı Kehf Külliyesi (Afşin)"],
        "specialties": ["Maraş Dondurması", "Maraş Tarhanası", "Eli Böğründe", "Kelle Paça"],
        "quote": "Yedi Güzel Adam'ın şiir ocağı, istiklalin kahraman kalesi ve Eshab-ı Kehf'in asırlık uykusunun mekanı.",
        "library": "Kahramanmaraş İl Halk Kütüphanesi - Edebiyat ve düşünce ikliminde verimli çalışma ortamı."
    },
    "03_Akdeniz/Mersin": {
        "plate": 33, "name": "Mersin", "region": "Akdeniz", "region_code": "03_Akdeniz",
        "lat": 36.8121, "lng": 34.6415,
        "landmarks": ["Kızkalesi", "Cennet-Cehennem Obrukları", "Kanlıdivane", "Tarsus Eshab-ı Kehf Mağarası", "St. Paul Kuyusu"],
        "specialties": ["Tantuni", "Cezerye", "Kerebiç", "Tarsus Şalgamı"],
        "quote": "Palmiyeli sahil şeridi, Torosların yaylaları ve Tarsus'un asırlara meydan okuyan manevi derinliği.",
        "library": "Mersin İl Halk Kütüphanesi - Sahile yakın, ferah çalışma masaları ve deniz manzaralı dinlenme alanlarıyla motivasyon verici."
    },
    "03_Akdeniz/Osmaniye": {
        "plate": 80, "name": "Osmaniye", "region": "Akdeniz", "region_code": "03_Akdeniz",
        "lat": 37.0746, "lng": 36.2464,
        "landmarks": ["Kastabala Antik Kenti", "Toprakkale Kalesi", "Karatepe-Aslantaş Açık Hava Müzesi"],
        "specialties": ["Osmaniye Yer Fıstığı", "Tırşık Çorbası", "Kömeç"],
        "quote": "Çukurova'nın doğu kapısı, Hitit kalıntılarının ve kaleler kuşağının nöbet tuttuğu geçit.",
        "library": "Osmaniye Emine Keskiner İl Halk Kütüphanesi - Sessiz, düzenli çalışma ortamı."
    },

    # 04_IcAnadolu (13 İl)
    "04_IcAnadolu/Aksaray": {
        "plate": 68, "name": "Aksaray", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 38.3687, "lng": 34.0370,
        "landmarks": ["Ihlara Vadisi", "Somuncu Baba Türbesi", "Sultanhanı Kervansarayı", "Eğri Minare"],
        "specialties": ["Aksaray Tava", "Şerbetsiz Şekerpare", "Köpük Helva"],
        "quote": "Somuncu Baba'nın fırınındaki sır, Ihlara Vadisi'nin derin tefekkürü ve İpekyolu'nun ulu kervansarayları.",
        "library": "Aksaray İl Halk Kütüphanesi - Bozkırın ortasında modern ve sessiz bir çalışma alanı."
    },
    "04_IcAnadolu/Ankara": {
        "plate": 6, "name": "Ankara", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 39.9334, "lng": 32.8597,
        "landmarks": ["Hacı Bayram-ı Veli Camii", "Ankara Kalesi", "Anıtkabir", "Augustus Tapınağı", "Hamamönü"],
        "specialties": ["Ankara Döneri", "Ankara Simidi", "Beypazarı Kurusu", "Çubuk Turşusu"],
        "quote": "Bozkırın kalbinde Hacı Bayram-ı Veli'nin manevi muhafızlığında kurulan cumhuriyetin payitahtı.",
        "library": "Milli Kütüphane / Cumhurbaşkanlığı Millet Kütüphanesi - Türkiye'nin en görkemli ilim mabetleri; 7/24 çalışma, devasa kaynak arşivi ve üst düzey konsantrasyon."
    },
    "04_IcAnadolu/Cankiri": {
        "plate": 18, "name": "Çankırı", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 40.6013, "lng": 33.6134,
        "landmarks": ["Tarihi Tuz Mağarası", "Çankırı Kalesi", "Taş Mescit (Şifahane)", "Çavundur Kaplıcaları"],
        "specialties": ["Yaren Güveci", "Cimcik Hamuru", "Yumurta Tatlısı"],
        "quote": "Yer altındaki devasa tuz şehri, Selçuklu Taş Mescidi ve yarenlik kültürünün kadim edep diyarı.",
        "library": "Çankırı İl Halk Kütüphanesi - Yarenler diyarında sakin ve samimi bir ilim yuvası."
    },
    "04_IcAnadolu/Eskisehir": {
        "plate": 26, "name": "Eskişehir", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 39.7767, "lng": 30.5206,
        "landmarks": ["Odunpazarı Evleri", "Kurşunlu Külliyesi", "Porsuk Çayı & Adalar", "Yunus Emre Türbesi (Mihalıççık)", "Yazılıkaya Midas"],
        "specialties": ["Çibörek", "Balaban Köfte", "Met Helvası", "Haşhaşlı Ekmek"],
        "quote": "Yunus Emre'nin 'Gelin tanış olalım' davetinin yankılandığı, sanatla yıkanmış dinamik bir kültür kenti.",
        "library": "Eskişehir İl Halk Kütüphanesi - Genç nüfusun yoğun olduğu, dinamik, internet hızı yüksek ve priz imkanı bol olan modern kütüphane."
    },
    "04_IcAnadolu/Karaman": {
        "plate": 70, "name": "Karaman", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 37.1759, "lng": 33.2287,
        "landmarks": ["Karaman Kalesi", "Hatuniye Medresesi", "Yunus Emre Camii", "Aktekke (Mader-i Mevlana) Camii", "Binbirkilise"],
        "specialties": ["Karaman Guymak Tatlısı", "Calla Yemeği", "Batırık"],
        "quote": "Türkçenin resmi dil ilan edildiği Karamanoğlu Mehmet Bey'in yurdu ve Mevlana'nın annesinin medfun olduğu topraklar.",
        "library": "Karaman İl Halk Kütüphanesi - Türk dilinin başkentinde sessiz çalışma salonu."
    },
    "04_IcAnadolu/Kayseri": {
        "plate": 38, "name": "Kayseri", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 38.7312, "lng": 35.4787,
        "landmarks": ["Erciyes Dağı", "Hunat Hatun Külliyesi", "Gevher Nesibe Tıp Medresesi", "Kayseri Kalesi", "Kapuzbaşı Şelaleleri"],
        "specialties": ["Kayseri Mantısı", "Pastırma & Sucuk", "Yağlama (Şebit)", "Nevzine Tatlısı"],
        "quote": "Erciyes'in beyaz karlı zirvesi altında Selçuklu şifahaneleri, Ahilik ahlakı ve ticaret zekasının harmanı.",
        "library": "Kayseri 75. Yıl İl Halk Kütüphanesi / Meryem Ana Şehir Kütüphanesi - Selçuklu esintili mekanlar."
    },
    "04_IcAnadolu/Kirikkale": {
        "plate": 71, "name": "Kırıkkale", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 39.8468, "lng": 33.5153,
        "landmarks": ["Çeşnigir Köprüsü ve Kanyonu", "Silah Sanayi Müzesi", "Hasandede Camii ve Türbesi", "Nur Camii"],
        "specialties": ["Kırıkkale Tavası", "Keskin Tavası", "Tuvalak"],
        "quote": "Kızılırmak'ın süzüldüğü Çeşnigir Köprüsü ve savunma sanayiimizin bozkırdaki omurgası.",
        "library": "Kırıkkale İl Halk Kütüphanesi - Geniş ve aydınlık çalışma ortamı ile odaklanmayı kolaylaştıran düzen."
    },
    "04_IcAnadolu/Kirsehir": {
        "plate": 40, "name": "Kırşehir", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 39.1425, "lng": 34.1709,
        "landmarks": ["Ahi Evran Camii ve Türbesi", "Cacabey Medresesi (Gözlemevi)", "Neşet Ertaş Gönül Sultanları Evi", "Aşıkpaşa Türbesi"],
        "specialties": ["Kırşehir Köftesi", "Çirleme", "Ahi Helvası"],
        "quote": "Ahilik teşkilatının kurucusu Ahi Evran'ın ocağı, gökbilim medresesi Cacabey ve Bozkırın Tezenesi Neşet Ertaş'ın sazının sesi.",
        "library": "Kırşehir İl Halk Kütüphanesi - UNESCO Müzik Şehri'nde huzur dolu araştırma salonu."
    },
    "04_IcAnadolu/Konya": {
        "plate": 42, "name": "Konya", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 37.8667, "lng": 32.4833,
        "landmarks": ["Mevlana Müzesi & Dergahı", "Alaaddin Camii & Tepesi", "İnce Minareli Medrese", "Karatay Medresesi", "Sille Köyü"],
        "specialties": ["Etliekmek", "Fırın Kebabı", "Tirit", "Bamya Çorbası", "Mevlana Şekeri"],
        "quote": "Hazreti Mevlana'nın 'Gel, ne olursan ol yine gel' nidasiyla dünyaya sevgi ve tevhid yayan Selçuklu payitahtı.",
        "library": "Konya İl Halk Kütüphanesi - Geniş ve ferah salonları var, Selçuklu mimarisinin esintilerini taşıyor, çalışma disiplini yüksek."
    },
    "04_IcAnadolu/Nevsehir": {
        "plate": 50, "name": "Nevşehir", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 38.6244, "lng": 34.7144,
        "landmarks": ["Göreme Açık Hava Müzesi", "Uçhisar Kalesi", "Derinkuyu Yeraltı Şehri", "Hacı Bektaş-ı Veli Türbesi", "Paşabağları"],
        "specialties": ["Testi Kebabı", "Kapadokya Şarabı/Üzüm Suyu", "Kabak Çekirdeği", "Nevşehir Tavası"],
        "quote": "Peribacalarının masalsı vadilerinde zamanın durduğu, Hacı Bektaş-ı Veli'nin 'Bir olalım, iri olalım, diri olalım' irfanı.",
        "library": "Nevşehir İl Halk Kütüphanesi - Taş mimarisiyle huzurlu, sessiz odaları odağı artırmak için ideal."
    },
    "04_IcAnadolu/Nigde": {
        "plate": 51, "name": "Niğde", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 37.9667, "lng": 34.6833,
        "landmarks": ["Niğde Kalesi ve Saat Kulesi", "Alaaddin Camii (Güneş Portali)", "Gümüşler Manastırı", "Aladağlar Milli Parkı"],
        "specialties": ["Niğde Tavası", "Niğde Gazozu", "Elma Tatlısı"],
        "quote": "Aladağlar'ın görkemi altında Selçuklu kadın motiflerinin taşa işlendiği ve 'Geçti Bor'un pazarı' deyişinin yurdu.",
        "library": "Niğde İl Halk Kütüphanesi - Sakin ve odaklanmaya elverişli ortam."
    },
    "04_IcAnadolu/Sivas": {
        "plate": 58, "name": "Sivas", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 39.7477, "lng": 37.0179,
        "landmarks": ["Divriği Ulu Cami ve Darüşşifası", "Çifte Minareli Medrese", "Buruciye Medresesi", "Gök Medrese", "Atatürk Kongre ve Etnografya Müzesi"],
        "specialties": ["Sivas Köftesi", "Sivas Katmeri", "Pezik Turşusu", "Madımak"],
        "quote": "Selçuklu taş işçiliğinin şaheseri Divriği Ulu Camii ile taçlanmış, Âşık Veysel'in sazındaki hakikat arayışı.",
        "library": "Sivas Şems-i Sivasî İl Halk Kütüphanesi - Selçuklu esintileriyle bezeli geniş ve son derece düzenli çalışma salonları."
    },
    "04_IcAnadolu/Yozgat": {
        "plate": 66, "name": "Yozgat", "region": "İç Anadolu", "region_code": "04_IcAnadolu",
        "lat": 39.8181, "lng": 34.8147,
        "landmarks": ["Yozgat Çamlığı Milli Parkı", "Çapanoğlu Camii", "Tarihi Saat Kulesi", "Nizamoğlu Konağı", "Kazankaya Kanyonu"],
        "specialties": ["Testi Kebabı", "Arabaşı Çorbası ve Hamuru", "Yozgat Parmak Çöreği"],
        "quote": "Bozkırın ortasında serin bir nefes, Türkiye'nin ilk milli parkı Yozgat Çamlığı'nın gölgesinde samimi bir menzil.",
        "library": "Yozgat İl Halk Kütüphanesi - Sessiz, düzenli çalışma ortamı ve çam kokulu molalar için ideal mekan."
    },

    # 05_Karadeniz (18 İl)
    "05_Karadeniz/Amasya": {
        "plate": 5, "name": "Amasya", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 40.6501, "lng": 35.8353,
        "landmarks": ["Kral Kaya Mezarları", "Harşena Kalesi", "Yalıboyu Evleri", "Sultan II. Bayezid Külliyesi", "Ferhat ile Şirin Su Kanalı"],
        "specialties": ["Amasya Elması", "Amasya Çöreği", "Baklalı Dolma", "Toyga Çorbası"],
        "quote": "Yeşilırmak boyunca inci gibi dizilen Yalıboyu konakları, şehzadeler mektebi ve Ferhat ile Şirin'in efsanevi aşkı.",
        "library": "Amasya İl Halk Kütüphanesi - Yeşilırmak kıyısında, nehrin şırıltısı eşliğinde kod yazma deneyimi sunan eşsiz bir çalışma alanı."
    },
    "05_Karadeniz/Artvin": {
        "plate": 8, "name": "Artvin", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 41.1828, "lng": 41.8183,
        "landmarks": ["Borçka Karagöl", "Şavşat Karagöl", "Mençuna Şelalesi", "Çoruh Vadisi", "Atatepe"],
        "specialties": ["Karalahana Sarması", "Laz Böreği", "Mısır Ekmeği", "Kuymak (Muhlama)"],
        "quote": "Bulutların üzerinde saklı Karagöl'ün zümrüt suları, dik yamaçların inadı ve doğanın muazzam zikri.",
        "library": "Artvin İl Halk Kütüphanesi - Yamaçta kurulu, manzaralı, dik yokuşlardan sonra dinlenip kod yazmak için ideal sessiz sığınak."
    },
    "05_Karadeniz/Bartin": {
        "plate": 74, "name": "Bartın", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 41.6344, "lng": 32.3375,
        "landmarks": ["Amasra Kalesi", "Kemere Köprüsü", "Güzelcehisar Lav Sütunları", "İnkumu Plajı"],
        "specialties": ["Amasra Salatası", "Bartın Pompom Helvası", "Kabak Burması"],
        "quote": "Fatih Sultan Mehmet'in 'Çeşm-i Cihan (Dünyanın Gözbebeği) burası mı ola?' dediği büyüleyici sahil kenti.",
        "library": "Bartın İl Halk Kütüphanesi - Karadeniz kıyısında huzurlu çalışma ortamı."
    },
    "05_Karadeniz/Bayburt": {
        "plate": 69, "name": "Bayburt", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 40.2552, "lng": 40.2249,
        "landmarks": ["Bayburt Kalesi", "Baksı Müzesi", "Kenan Yavuz Etnografya Müzesi", "Çoruh Nehri", "Saat Kulesi"],
        "specialties": ["Bayburt Ketesi", "Tatlı Çorba", "Galaçoş", "Lor Dolması"],
        "quote": "Çoruh Nehri'nin ikiye böldüğü kadim kale kenti ve bozkırın ortasında modern sanatın zirvesi Baksı Müzesi.",
        "library": "Bayburt İl Halk Kütüphanesi - Çoruh Nehri kıyısında, sessiz ve sakin bir çalışma ortamı."
    },
    "05_Karadeniz/Bolu": {
        "plate": 14, "name": "Bolu", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 40.7358, "lng": 31.6061,
        "landmarks": ["Abant Gölü", "Gölcük Tabiat Parkı", "Yedigöller Milli Parkı", "Göynük Tarihi Evleri"],
        "specialties": ["Mengen Aşçı Yemekleri", "Abant Kebabı", "Bolu Çikolatası", "Saray Helvası"],
        "quote": "Yedigöller'in tabiat paleti, Osmanlı kasabası Göynük ve Akşemseddin Hazretleri'nin manevi gölgesi.",
        "library": "Bolu İl Halk Kütüphanesi - Göller ve ormanlar diyarı Bolu'da verimli bir çalışma alanı."
    },
    "05_Karadeniz/Corum": {
        "plate": 19, "name": "Çorum", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 40.5506, "lng": 34.9556,
        "landmarks": ["Hattuşaş (Boğazkale) Hitit Başkenti", "Alacahöyük", "Saat Kulesi", "Ulu Cami", "İncesu Kanyonu"],
        "specialties": ["Çorum Leblebisi", "Çorum Mantısı", "İskilip Dolması"],
        "quote": "3500 yıllık Hitit İmparatorluğu'nun başkenti Hattuşaş'ın aslanlı kapıları ve taş kabartmaları.",
        "library": "Çorum İl Halk Kütüphanesi - Sessiz ve düzenli çalışma odalarıyla odaklanmayı kolaylaştıran sakin bir Anadolu kütüphanesi."
    },
    "05_Karadeniz/Duzce": {
        "plate": 81, "name": "Düzce", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 40.8438, "lng": 31.1565,
        "landmarks": ["Güzeldere Şelalesi", "Samandere Şelalesi", "Akçakoca Ceneviz Kalesi", "Fakıllı Mağarası"],
        "specialties": ["Düzce Köftesi", "İsli Düzce Çerkes Peyniri", "Fındık"],
        "quote": "Şelalelerin coşkusu, yaylaların serinliği ve 81. ilimizin bereketli toprakları.",
        "library": "Düzce İl Halk Kütüphanesi - Sakin ve ferah salonlar."
    },
    "05_Karadeniz/Giresun": {
        "plate": 28, "name": "Giresun", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 40.9128, "lng": 38.3895,
        "landmarks": ["Giresun Kalesi", "Giresun Adası", "Kümbet Yaylası", "Mavi Göl & Kuzalan Şelalesi", "Zeytinlik Mahallesi"],
        "specialties": ["Giresun Fındığı", "Giresun Pidesi", "Karalahana Diblesi", "Isırgan Otu Çorbası"],
        "quote": "Karadeniz'in iki yaşanabilir adasından birine ev sahipliği yapan, zümrüt fındık bahçeleri ve Mavi Göl mucizesi.",
        "library": "Giresun İl Halk Kütüphanesi - Harşit Vadisi ve deniz esintileriyle serin, sakin çalışma masaları mevcut."
    },
    "05_Karadeniz/Gumushane": {
        "plate": 29, "name": "Gümüşhane", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 40.4600, "lng": 39.4700,
        "landmarks": ["Karaca Mağarası", "Torul Cam Seyir Terası", "Tomara Şelalesi", "Süleymaniye Mahallesi", "Krom Vadisi"],
        "specialties": ["Pestil & Köme", "Siron", "Kete", "Gümüşhane Elması"],
        "quote": "Vadiler arasına gizlenmiş sarkıt cenneti Karaca Mağarası ve gümüş madenleriyle parlayan Süleymaniye.",
        "library": "Gümüşhane İl Halk Kütüphanesi - Vadinin serinliğinde, odaklanmayı kolaylaştıran butik ve huzurlu çalışma alanı."
    },
    "05_Karadeniz/Karabuk": {
        "plate": 78, "name": "Karabük", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 41.2061, "lng": 32.6204,
        "landmarks": ["Safranbolu Tarihi Evleri", "Kristal Teras", "Tokatlı Kanyonu", "Bulak Mencilis Mağarası", "Yörük Köyü"],
        "specialties": ["Safranbolu Lokumu", "Bükme Pide", "Kuyu Kebabı", "Safran Çayı"],
        "quote": "UNESCO Dünya Mirası Safranbolu'nun asırlık ahşap konakları, taş sokakları ve safranın eşsiz kokusu.",
        "library": "Karabük İl Halk Kütüphanesi - Safranbolu'nun tarihi atmosferine yakın sessiz kütüphane."
    },
    "05_Karadeniz/Kastamonu": {
        "plate": 37, "name": "Kastamonu", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 41.3887, "lng": 33.7827,
        "landmarks": ["Kastamonu Kalesi", "Nasrullah Camii ve Şadırvanı", "Valla Kanyonu", "Horma Kanyonu", "Şeyh Şaban-ı Veli Türbesi"],
        "specialties": ["Kastamonu Pastırması", "Etli Ekmek", "Siyez Bulguru", "Çekme Helva", "Kuyu Kebabı"],
        "quote": "Şeyh Şaban-ı Veli'nin manevi dergahı, İstiklal Yolu'nun kahraman kadınları ve Ilgaz Dağları'nın heybeti.",
        "library": "Kastamonu İl Halk Kütüphanesi - Tarihi şehir dokusunda ilham dolu çalışma noktası."
    },
    "05_Karadeniz/Ordu": {
        "plate": 52, "name": "Ordu", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 40.9839, "lng": 37.8764,
        "landmarks": ["Boztepe & Teleferik", "Yason Burnu & Kilisesi", "Perşembe Yaylası Menderesleri", "Kurul Kalesi", "Çambaşı Yaylası"],
        "specialties": ["Ordu Pidesi", "Fındık", "Pancar Çorbası", "Melocan Kavurması"],
        "quote": "Boztepe'den Karadeniz'in mavisine bakış ve Perşembe Yaylası'nın doğa harikası menderesleri.",
        "library": "Ordu İl Halk Kütüphanesi - Teleferik hattına yakın konumuyla mola vermeye uygun, çalışma salonları geniş."
    },
    "05_Karadeniz/Rize": {
        "plate": 53, "name": "Rize", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 41.0201, "lng": 40.5234,
        "landmarks": ["Ayder Yaylası", "Pokut & Sal Yaylaları", "Zilkale", "Fırtına Vadisi", "Kaçkar Dağları Milli Parkı"],
        "specialties": ["Rize Çayı", "Muhlama", "Rize Kavurması", "Laz Böreği", "Enişte Lokumu"],
        "quote": "Kaçkarların sisli zirveleri, Fırtına Deresi'nin coşkusu ve dik yamaçlara serilmiş zümrüt çay bahçeleri.",
        "library": "Rize İl Halk Kütüphanesi - Çay tarlalarının yeşili eşliğinde, modern altyapısı ve güçlü internetiyle kodlama için ideal."
    },
    "05_Karadeniz/Samsun": {
        "plate": 55, "name": "Samsun", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 41.2928, "lng": 36.3313,
        "landmarks": ["Bandırma Vapuru Müzesi", "Onur Anıtı", "Şahinkaya Kanyonu", "Kızılırmak Deltası Kuş Cenneti", "Amazon Köyü"],
        "specialties": ["Samsun Pidesi (Bafra/Terme)", "Nokul", "Kaz Tiridi", "Mısır Çorbası"],
        "quote": "Milli Mücadele'nin ilk adımının atıldığı istiklal limanı ve Şahinkaya Kanyonu'nun heybetli suları.",
        "library": "Samsun İl Halk Kütüphanesi - Karadeniz'in en modern kütüphanelerinden biri, priz ve internet altyapısı mükemmel."
    },
    "05_Karadeniz/Sinop": {
        "plate": 57, "name": "Sinop", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 42.0231, "lng": 35.1531,
        "landmarks": ["Tarihi Sinop Cezaevi", "İnceburun Feneri (Türkiye'nin En Kuzeyi)", "Erfelek Tatlıca Şelaleleri", "Hamsilos Koyu"],
        "specialties": ["Sinop Mantısı (Cevizli)", "Nokul", "Palamut / Kalkan Balığı"],
        "quote": "Türkiye'nin en kuzey ucu İnceburun, fiyort benzeri Hamsilos Koyu ve Diyojen'in 'Gölge etme başka ihsan istemez' dediği yer.",
        "library": "Sinop Rıza Nur İl Halk Kütüphanesi - Tarihi ve nostaljik ahşap binasıyla zamanda yolculuk hissi veriyor, huzurlu bir çalışma noktası."
    },
    "05_Karadeniz/Tokat": {
        "plate": 60, "name": "Tokat", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 40.3167, "lng": 36.5500,
        "landmarks": ["Ballıca Mağarası", "Tokat Kalesi", "Taşhan", "Ali Paşa Camii", "Mahperi Hatun Kervansarayı", "Saat Kulesi"],
        "specialties": ["Tokat Kebabı", "Tokat Yaprağı (Sarma)", "Zile Pekmezi", "Çökelekli Katmer"],
        "quote": "Ballıca Mağarası'nın şifalı cüce sarkıtları, 900 adımda 900 yıllık tarihin adımlandığı kadim menzil.",
        "library": "Tokat İl Halk Kütüphanesi - Tarihi hanların gölgesinde huzurlu çalışma alanı."
    },
    "05_Karadeniz/Trabzon": {
        "plate": 61, "name": "Trabzon", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 41.0027, "lng": 39.7168,
        "landmarks": ["Sümela Manastırı", "Ayasofya Camii Müzesi", "Uzungöl", "Atatürk Köşkü", "Boztepe", "Vazelon Manastırı"],
        "specialties": ["Akçaabat Köftesi", "Kuymak", "Hamsiköy Sütlacı", "Trabzon Ekmeği", "Karalahana Çorbası"],
        "quote": "Sarp kayalıklara asılı Sümela Manastırı'nın heybeti, zümrüt yaylalar ve Karadeniz'in hırçın dalgaları.",
        "library": "Trabzon İl Halk Kütüphanesi - Şehir merkezinde vakur bir bina, araştırma ve geliştirme için sessiz odalar sunuyor."
    },
    "05_Karadeniz/Zonguldak": {
        "plate": 67, "name": "Zonguldak", "region": "Karadeniz", "region_code": "05_Karadeniz",
        "lat": 41.4564, "lng": 31.7987,
        "landmarks": ["Gökgöl Mağarası", "Maden Müzesi", "Filyos Kalesi & Antik Kenti", "Harmankaya Şelalesi"],
        "specialties": ["Uğmaç Çorbası", "Malay", "Zonguldak Kestanesi"],
        "quote": "Emeğin başkenti, yerin yüzlerce metre altından çıkarılan kara elmasın ve madencilerin vefası.",
        "library": "Zonguldak İl Halk Kütüphanesi - Karadeniz'in sarp kıyısında sakin bir çalışma ortamı."
    },

    # 06_DoguAnadolu (14 İl)
    "06_DoguAnadolu/Agri": {
        "plate": 4, "name": "Ağrı", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 39.7191, "lng": 43.0503,
        "landmarks": ["İshak Paşa Sarayı", "Ağrı Dağı (5137m)", "Meteor Çukuru", "Doğubayazıt Kalesi", "Balık Gölü"],
        "specialties": ["Abdigör Köftesi", "Ağrı Balı", "Halis (Helise)"],
        "quote": "Türkiye'nin çatısı Ağrı Dağı ve kartal yuvası gibi ovaya bakan masalsı İshak Paşa Sarayı.",
        "library": "Ağrı İl Halk Kütüphanesi - Ağrı Dağı'nın heybeti karşısında sakin çalışma alanı."
    },
    "06_DoguAnadolu/Ardahan": {
        "plate": 75, "name": "Ardahan", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 41.1105, "lng": 42.7022,
        "landmarks": ["Çıldır Gölü (Kışın Donan)", "Ardahan Kalesi", "Şeytan Kalesi", "Atatürk Silüeti (Damal)"],
        "specialties": ["Kaşar Peyniri", "Ardahan Çiçek Balı", "Kaz Eti Yemeği", "Hengel"],
        "quote": "Kışın atlı kızakların kaydığı buz tutmuş Çıldır Gölü ve sarp kayalıklara kurulu Şeytan Kalesi.",
        "library": "Ardahan İl Halk Kütüphanesi - Kışın sıcacık soba sıcaklığında, dışarıdaki dondurucu soğuğa inat sessizce kod yazma imkanı."
    },
    "06_DoguAnadolu/Bingol": {
        "plate": 12, "name": "Bingöl", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 38.8854, "lng": 40.4983,
        "landmarks": ["Yüzen Adalar (Solhan)", "Hesarek Kayak Merkezi", "Kral Kızı Kalesi", "Zağ Mağaraları"],
        "specialties": ["Bingöl Balı", "Gömme", "Mastuva", "Löl"],
        "quote": "Turnalar Gölü'ndeki doğa harikası Yüzen Adalar ve dağların bağrında saklı kaynak suları.",
        "library": "Bingöl İl Halk Kütüphanesi - Samimi ve sessiz çalışma ortamı."
    },
    "06_DoguAnadolu/Bitlis": {
        "plate": 13, "name": "Bitlis", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 38.4006, "lng": 42.1095,
        "landmarks": ["Nemrut Krater Gölü & Kalderası", "Ahlat Selçuklu Mezarlığı", "Bitlis Kalesi", "İhlasiye Medresesi", "Tarihi Taş Evler"],
        "specialties": ["Bitlis Büryan Kebabı", "Ahlat Elması", "Katıklı Dolma", "Karakovan Balı"],
        "quote": "Kubbetü'l-İslam Ahlat'ın ulu mezar taşları ve dünyanın ikinci büyük kalderası Nemrut Krater Gölü.",
        "library": "Bitlis İl Halk Kütüphanesi - Tarihi taş binalar arasında tefekkür dolu araştırma ortamı."
    },
    "06_DoguAnadolu/Elazig": {
        "plate": 23, "name": "Elazığ", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 38.6810, "lng": 39.2264,
        "landmarks": ["Harput Kalesi (Süt Kalesi)", "Harput Ulu Cami (Eğri Minare)", "Hazar Gölü", "Keban Baraj Gölü", "Meryem Ana Kilisesi"],
        "specialties": ["Harput Köftesi", "Gömme", "Orcik (Cevizli Sucuk)", "Çedene Kahvesi"],
        "quote": "Bin yıllık Harput kalesinin vakur duruşu, Gakgoşlar diyarının mertliği ve Hazar Gölü'nün batık şehri.",
        "library": "Elazığ İl Halk Kütüphanesi - Gakgoşlar diyarında modern ve konforlu çalışma odalarıyla geniş bir kütüphane."
    },
    "06_DoguAnadolu/Erzincan": {
        "plate": 24, "name": "Erzincan", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 39.7500, "lng": 39.5000,
        "landmarks": ["Girlevik Şelalesi", "Karanlık Kanyon (Kemaliye)", "Kemaliye Tarihi Taş Evleri", "Ergan Dağı Kayak Merkezi", "Terzibaba Türbesi"],
        "specialties": ["Erzincan Tulum Peyniri", "Kemaliye Lök Tatlısı", "Gözleme & Kete"],
        "quote": "Karanlık Kanyon'un Fırat ile yarıştığı heybet, Girlevik Şelalesi'nin çağıltısı ve Terzibaba'nın teslimiyeti.",
        "library": "Erzincan İl Halk Kütüphanesi - Deprem sonrası yenilenen geniş caddelerin ortasında modern ve ferah bir kütüphane."
    },
    "06_DoguAnadolu/Erzurum": {
        "plate": 25, "name": "Erzurum", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 39.9043, "lng": 41.2679,
        "landmarks": ["Çifte Minareli Medrese", "Yakutiye Medresesi", "Üç Kümbetler", "Erzurum Kalesi", "Tortum Şelalesi", "Palandöken"],
        "specialties": ["Cağ Kebabı", "Kadayıf Dolması", "Erzurum Ketesi", "Aşotu Çorbası"],
        "quote": "Dadaşlar diyarı; Selçuklu medreselerinin göğe uzanan çifte minareleri ve İbrahim Hakkı Hazretleri'nin 'Mevla görelim neyler, neylerse güzel eyler' teslimiyeti.",
        "library": "Erzurum Erzurumlu Emrah İl Halk Kütüphanesi - Tarihi dokusuyla dadaşların vakur çalışma disiplinini yansıtan sessiz çalışma limanı."
    },
    "06_DoguAnadolu/Hakkari": {
        "plate": 30, "name": "Hakkari", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 37.5833, "lng": 43.7333,
        "landmarks": ["Cilo Sat Buzul Gölleri", "Meydan Medresesi", "Zap Vadisi", "Cennet-Cehennem Vadisi", "Merga Bütan"],
        "specialties": ["Hakkari Çorti Aşı", "Doğaba", "Yüksekova Kebabı", "Cevizli Çörek"],
        "quote": "Cilo Dağları'nın buzul gölleri, binlerce yıllık kaya resimleri ve Zap Suyu'nun hırçın yankısı.",
        "library": "Hakkari İl Halk Kütüphanesi - Zirvelerin gölgesinde sakin çalışma ortamı."
    },
    "06_DoguAnadolu/Igdir": {
        "plate": 76, "name": "Iğdır", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 39.9196, "lng": 44.0450,
        "landmarks": ["Tuzluca Tuz Mağaraları", "Ağrı Dağı Milli Parkı", "Ejder Kervansarayı", "Karakale Ören Yeri"],
        "specialties": ["Bozbaş (Piti)", "Taş Köfte", "Iğdır Kayısısı", "Kete"],
        "quote": "Üç ülkeye sınır, Doğu'nun Çukurova'sı mikroklima cenneti ve Tuzluca'nın yer altı mağaraları.",
        "library": "Iğdır İl Halk Kütüphanesi - Doğu sınırında sakin ve ferah bir çalışma mekanı."
    },
    "06_DoguAnadolu/Kars": {
        "plate": 36, "name": "Kars", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 40.6167, "lng": 43.1000,
        "landmarks": ["Ani Harabeleri (Binbir Kiliseli Şehir)", "Kars Kalesi", "Harakani Türbesi", "Havariler Kilisesi (Kümbet Camii)", "Baltık Mimarisi Evleri"],
        "specialties": ["Kars Kaşarı & Gravyeri", "Kars Kaz Eti Pilavı", "Hangel", "Piti (Bozbaş)"],
        "quote": "Ebu'l Hasan Harakani'nin 'Her kim bu kapıya gelirse ekmeğini verin, inancını sormayın' felsefesi ve Ani Harabeleri'nin bin yıllık taşları.",
        "library": "Kars İl Halk Kütüphanesi - Rus döneminden kalma taş binaların mistik havasında, karlar altında kodlama mesaisi yapabileceğiniz sıcak sığınak."
    },
    "06_DoguAnadolu/Malatya": {
        "plate": 44, "name": "Malatya", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 38.3552, "lng": 38.3095,
        "landmarks": ["Arslantepe Höyüğü (UNESCO)", "Battalgazi Ulu Cami", "Silahtar Mustafa Paşa Kervansarayı", "Levent Vadisi Seyir Terası", "Günpınar Şelalesi"],
        "specialties": ["Malatya Kayısısı", "Analı Kızlı", "Kayıslı Kavurma", "Kiraz Yaprağı Köftesi", "Kömbe"],
        "quote": "Dünyanın ilk kerpiç sarayına ev sahipliği yapan Arslantepe, Battalgazi'nin yiğitliği ve kayısı bahçelerinin bereketi.",
        "library": "Malatya İl Halk Kütüphanesi - Şehir merkezinde yer alan, geniş araştırma kaynakları ve rahat çalışma alanları sunan yerleşke."
    },
    "06_DoguAnadolu/Mus": {
        "plate": 49, "name": "Muş", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 38.7432, "lng": 41.5064,
        "landmarks": ["Tarihi Murat Köprüsü", "Muş Kalesi", "Arak Manastırı", "Malazgirt Zafer Anıtı (Meydan Muharebesi Tarihi Milli Parkı)"],
        "specialties": ["Muş Köftesi", "Hafta Direği", "Tırşık", "Muş Çortisi"],
        "quote": "1071 Malazgirt Zaferi ile Anadolu'nun kapılarının İslam'a ve Türklere açıldığı şanlı menzil ve Murat Nehri.",
        "library": "Muş İl Halk Kütüphanesi - Tarihin başladığı ovada sessiz ve sakin çalışma alanı."
    },
    "06_DoguAnadolu/Tunceli": {
        "plate": 62, "name": "Tunceli", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 39.1079, "lng": 39.5401,
        "landmarks": ["Munzur Vadisi Milli Parkı", "Munzur Gözeleri", "Pertek Kalesi", "Düzgün Baba Türbesi", "Pülümür Vadisi & Ağlayan Kayalar"],
        "specialties": ["Şavak Tulum Peyniri", "Munzur Balı", "Zerefet (Babiko)", "Gömme"],
        "quote": "Munzur Suyu'nun berrak gözeleri, doğaya ve canlıya hürmetle bakan irfan geleneği ve sarp kanyonlar.",
        "library": "Tunceli İl Halk Kütüphanesi - Munzur nehrinin esintisiyle serinleyen, sessiz çalışma ortamı ve güler yüzlü çalışanlarıyla butik kütüphane."
    },
    "06_DoguAnadolu/Van": {
        "plate": 65, "name": "Van", "region": "Doğu Anadolu", "region_code": "06_DoguAnadolu",
        "lat": 38.4891, "lng": 43.4089,
        "landmarks": ["Akdamar Adası ve Kilisesi", "Van Kalesi", "Van Gölü (Van Denizi)", "Muradiye Şelalesi", "Hoşap Kalesi", "Çavuştepe Urartu Kalesi"],
        "specialties": ["Van Kahvaltısı", "Otlu Peynir", "İnci Kefali", "Sengeser", "Kavut"],
        "quote": "Urartu krallarının taht kurduğu Van Kalesi, sodalı masmavi Van Denizi ve Akdamar Adası'nın badem çiçekleri.",
        "library": "Van İl Halk Kütüphanesi - Van Gölü manzarasına yakın, geniş çalışma alanlarına sahip modern kütüphane."
    },

    # 07_GuneydoguAnadolu (9 İl)
    "07_GuneydoguAnadolu/Adiyaman": {
        "plate": 2, "name": "Adıyaman", "region": "Güneydoğu Anadolu", "region_code": "07_GuneydoguAnadolu",
        "lat": 37.7648, "lng": 38.2786,
        "landmarks": ["Nemrut Dağı Heykelleri (Gündoğumu/Batımı)", "Cendere Köprüsü", "Arsemia Ören Yeri", "Karakuş Tümülüsü", "Perre Antik Kenti"],
        "specialties": ["Adıyaman Çiğ Köftesi", "Besni Tavası", "Meyir Çorbası", "Buhara Pilavı"],
        "quote": "Kommagene Krallığı'nın tanrı heykelleriyle bezeli Nemrut Zirvesi ve güneşin en görkemli doğup battığı taht.",
        "library": "Adıyaman İl Halk Kütüphanesi - Nemrut'un gölgesinde huzurlu çalışma alanı."
    },
    "07_GuneydoguAnadolu/Batman": {
        "plate": 72, "name": "Batman", "region": "Güneydoğu Anadolu", "region_code": "07_GuneydoguAnadolu",
        "lat": 37.8812, "lng": 41.1294,
        "landmarks": ["Hasankeyf Tarihi Kenti", "Zeynel Bey Türbesi", "Malabadi Köprüsü", "Mor Kiryakus Manastırı"],
        "specialties": ["Batman Kütülk (İçli Köfte)", "Şam Börek", "Tırşık", "Hevra Ekmeği"],
        "quote": "Dicle Nehri'nin bağrından doğan 12 bin yıllık Hasankeyf mağaraları ve Zeynel Bey Türbesi'nin turkuaz çinileri.",
        "library": "Batman İl Halk Kütüphanesi - Dicle kıyısında modern çalışma salonları."
    },
    "07_GuneydoguAnadolu/Diyarbakir": {
        "plate": 21, "name": "Diyarbakır", "region": "Güneydoğu Anadolu", "region_code": "07_GuneydoguAnadolu",
        "lat": 37.9144, "lng": 40.2306,
        "landmarks": ["Diyarbakır Surları (UNESCO)", "Hevsel Bahçeleri", "Ulu Cami (İslam'ın 5. Harem-i Şerifi)", "On Gözlü Köprü", "Dört Ayaklı Minare", "Cahit Sıtkı Tarancı Müzesi"],
        "specialties": ["Diyarbakır Ciğeri", "Kaburga Dolması", "Burma Kadayıf", "Diyarbakır Karpuzu", "Meftune"],
        "quote": "Kara bazalt taşlı asırlık surlar, sahabe mezarları ve İslam aleminin 5. Harem-i Şerifi sayılan Ulu Camii.",
        "library": "Diyarbakır İl Halk Kütüphanesi / Sur İlçe Kütüphanesi - Tarihi surların gölgesinde kadim bilgi ocağı."
    },
    "07_GuneydoguAnadolu/Gaziantep": {
        "plate": 27, "name": "Gaziantep", "region": "Güneydoğu Anadolu", "region_code": "07_GuneydoguAnadolu",
        "lat": 37.0662, "lng": 37.3833,
        "landmarks": ["Zeugma Mozaik Müzesi (Çingene Kızı)", "Gaziantep Kalesi", "Bakırcılar Çarşısı", "Tahmis Kahvesi", "Rumkale"],
        "specialties": ["Gaziantep Baklavası", "Ali Nazik", "Beyran Çorbası", "Katmer", "Küşleme", "Menengiç Kahvesi"],
        "quote": "UNESCO Gastronomi Şehri; Zeugma'nın Çingene Kızı mozaiğinin derin bakışları ve asırlık hanların kahve kokusu.",
        "library": "Gaziantep İl Halk Kütüphanesi / Hasan Celal Güzel Kütüphanesi - Modern donanımlı ve dinamik çalışma atmosferi."
    },
    "07_GuneydoguAnadolu/Kilis": {
        "plate": 79, "name": "Kilis", "region": "Güneydoğu Anadolu", "region_code": "07_GuneydoguAnadolu",
        "lat": 36.7184, "lng": 37.1212,
        "landmarks": ["Ravanda Kalesi", "Oylum Höyük", "Kilis Tarihi Taş Evleri ve Kabaltıları", "Ulu Cami"],
        "specialties": ["Kilis Tavası", "Cennet Çamuru Tatlısı", "Kilis Katmeri", "Zeytinyağı"],
        "quote": "Zeytin ağaçlarının gölgesinde kadim kabaltılı sokaklar, lezzetli Kilis Tavası ve sınır boyunun sıcak insanları.",
        "library": "Kilis İl Halk Kütüphanesi - Samimi ve sessiz çalışma ortamı."
    },
    "07_GuneydoguAnadolu/Mardin": {
        "plate": 47, "name": "Mardin", "region": "Güneydoğu Anadolu", "region_code": "07_GuneydoguAnadolu",
        "lat": 37.3212, "lng": 40.7245,
        "landmarks": ["Mardin Taş Evleri", "Deyrulzafaran Manastırı", "Kasımiye Medresesi", "Mardin Ulu Cami", "Dara Antik Kenti", "Midyat Konukevi"],
        "specialties": ["Mardin Kebabı", "Sembusek", "İrok (Mardin İçli Köftesi)", "Süryani Şarabı/Çöreği", "Mavi Badem Şekeri"],
        "quote": "Gündüzü seyran, gecesi gerdanlık; Mezopotamya ovasına tepeden bakan sarı kalker taşlı masal diyarı.",
        "library": "Mardin İl Halk Kütüphanesi - Taş mimarisi ve Mezopotamya ovasına bakan avlusuyla seyyah yazılımcıya ilham kaynağı."
    },
    "07_GuneydoguAnadolu/Siirt": {
        "plate": 56, "name": "Siirt", "region": "Güneydoğu Anadolu", "region_code": "07_GuneydoguAnadolu",
        "lat": 37.9333, "lng": 41.9500,
        "landmarks": ["İsmail Fakirullah & İbrahim Hakkı Türbesi (Işık Hadisesi - Tillo)", "Veysel Karani Türbesi", "Siirt Ulu Cami", "Rasıl Hacar (Delikli Taş)"],
        "specialties": ["Büryan Kebabı", "Perde Pilavı", "Siirt Fıstığı", "Tayfi Üzümü"],
        "quote": "İlim ve irfan beldesi Tillo'daki güneş hadisesi, Veysel Karani Hazretleri'nin aşkı ve sarp Botan Kanyonu.",
        "library": "Siirt İl Halk Kütüphanesi - Tillo'nun manevi atmosferinde sakin çalışma alanı."
    },
    "07_GuneydoguAnadolu/Sanliurfa": {
        "plate": 63, "name": "Şanlıurfa", "region": "Güneydoğu Anadolu", "region_code": "07_GuneydoguAnadolu",
        "lat": 37.1674, "lng": 38.7938,
        "landmarks": ["Göbeklitepe (Tarihin Sıfır Noktası)", "Balıklıgöl (Halil-ür Rahman)", "Şanlıurfa Kalesi", "Harran Kümbet Evleri", "Karahantepe", "Gümrük Hanı"],
        "specialties": ["Urfa Kebabı", "Çiğ Köfte", "Lahmacun", "Şıllık Tatlısı", "Mırra", "Borani"],
        "quote": "Peygamberler şehri; Hz. İbrahim'in ateşinin gül bahçesine dönüştüğü Balıklıgöl ve insanlık tarihinin sıfır noktası Göbeklitepe.",
        "library": "Şanlıurfa İl Halk Kütüphanesi - Peygamberler şehrinde zengin araştırma kaynakları."
    },
    "07_GuneydoguAnadolu/Sirnak": {
        "plate": 73, "name": "Şırnak", "region": "Güneydoğu Anadolu", "region_code": "07_GuneydoguAnadolu",
        "lat": 37.5164, "lng": 42.4594,
        "landmarks": ["Cudi Dağı (Hz. Nuh'un Gemisi)", "Kırmızı Medrese (Cizre)", "Mem û Zîn Türbesi", "İsmail Ebul-İz El-Cezeri Türbesi", "Kasrik Boğazı"],
        "specialties": ["Kutlık", "Serbıdev", "Hekeheşandi", "Suryaz"],
        "quote": "Hz. Nuh'un gemisinin oturduğu Cudi Dağı, sibernetiğin kurucusu El-Cezeri'nin memleketi ve Mem û Zîn destanı.",
        "library": "Şırnak İl Halk Kütüphanesi - Cudi eteklerinde sessiz ve düzenli çalışma alanı."
    }
}

# 7 Bölge İsimleri ve Simgeleri
REGIONS_INFO = {
    "01_Marmara": {"name": "Marmara Bölgesi", "icon": "🏰", "color": "#38bdf8", "desc": "Payitaht ve Tohum: Bir cihan imparatorluğunun mayalandığı iki kıtayı bağlayan kadim topraklar."},
    "02_Ege": {"name": "Ege Bölgesi", "icon": "🌊", "color": "#34d399", "desc": "Zamanın Çizgileri & Zeytin Dalı: Antik mermerlerden turkuaz koylara uzanan bilgelik coğrafyası."},
    "03_Akdeniz": {"name": "Akdeniz Bölgesi", "icon": "☀️", "color": "#f59e0b", "desc": "Sıcaklık & Antik Limanlar: Torosların heybetiyle kucaklaşan bin yıllık limanlar ve bereket ovaları."},
    "04_IcAnadolu": {"name": "İç Anadolu Bölgesi", "icon": "🌾", "color": "#fbbf24", "desc": "Bozkırın Kalbi & İrfan Havzası: Mevlana'dan Yunus Emre'ye, Hacı Bektaş'tan Ahi Evran'a uzanan tevazu yurdu."},
    "05_Karadeniz": {"name": "Karadeniz Bölgesi", "icon": "🌲", "color": "#10b981", "desc": "Zikir, Orman & Dalga: Hırçın dalgaların yemyeşil yaylalarla buluştuğu doğanın muazzam senfonisi."},
    "06_DoguAnadolu": {"name": "Doğu Anadolu Bölgesi", "icon": "🏔️", "color": "#a855f7", "desc": "Zirvelerin İhtişamı & Kaleler: Zorlu iklimlerde pişen hayatların ve sarsılmaz kalelerin vakur duruşu."},
    "07_GuneydoguAnadolu": {"name": "Güneydoğu Anadolu Bölgesi", "icon": "🏜️", "color": "#f97316", "desc": "Mezopotamya'nın Ninnisi & Medeniyet Beşiği: Göbeklitepe'den Harran'a, toprağın taşa, taşın efsaneye dönüştüğü masal."}
}

# Evliya Çelebi, İbn Battûta ve Tasavvuf Alıntıları Koleksiyonu
TRAVEL_QUOTES = [
    {"quote": "Dünya bir kitaptır ve seyahat etmeyenler onun sadece bir sayfasını okur.", "author": "Aurelius Augustinus"},
    {"quote": "İyi bir gezginin sabit planları ve varmak gibi bir amacı yoktur.", "author": "Lao Tzu"},
    {"quote": "Gerçek keşif yolculuğu yeni manzaralar bulmak değil, yeni gözlerle bakmaktır.", "author": "Marcel Proust"},
    {"quote": "Kıyıyı gözden kaybetmeye cesaret edemeyenler, yeni okyanuslar keşfedemezler.", "author": "Andre Gide"},
    {"quote": "Yollar, sadece ayakların değil, zihnin de özgürleştiği patikalardır.", "author": "Friedrich Nietzsche"},
    {"quote": "De ki: Yeryüzünde gezip dolaşın da Allah’ın yaratmaya nasıl başladığını görün...", "author": "Kur'an-ı Kerim (Ankebût, 20)"},
    {"quote": "Yolculuğa çıkın ki sıhhat bulasınız ve ganimet elde edesiniz.", "author": "Hz. Muhammed (s.a.v.)"},
    {"quote": "Dünyada tıpkı bir garip veya bir yolcu gibi ol.", "author": "Hz. Muhammed (s.a.v.)"},
    {"quote": "Su akar ve hareket ederse tatlanır ve temiz kalır; durursa bozulur ve kokar. İnsan da seyahat ettikçe kemale erer.", "author": "İmam Şâfiî"},
    {"quote": "Yolculuk; varlığın hakikatini, insanın acziyetini ve nefsin gizli köşelerini ortaya çıkaran en berrak aynadır.", "author": "Muhyiddin İbnü'l-Arabî"},
    {"quote": "Yola çık ki yol sana görünsün; kendini yola bırak ki menzile eresin.", "author": "Ferîdüddin Attar"},
    {"quote": "Yolculuk, önce seni sessizleştirir, sonra da iyi bir hikâye anlatıcısına dönüştürür.", "author": "İbn Battûta"},
    {"quote": "Seyahat Ya Resulallah! Niyetiyle düşülen yollar, bereketiyle menzile erdirir.", "author": "Evliya Çelebi"},
    {"quote": "Gezgin, vardığı yerdeki her taşı bir anı, her insanı bir öğretmen gibi selamlar.", "author": "Kadim Doğu Özdeyişi"}
]


class SeyyahEngine:
    def __init__(self, repo_root="."):
        self.repo_root = Path(repo_root).resolve()
        self.provinces = PROVINCES_DATA.copy()
        self.visited_provinces = {}
        self.unvisited_provinces = {}
        self.stats = {}
        self.refresh()

    def refresh(self):
        """Repositorydeki dosyaları tarar ve ziyaret durumlarını senkronize eder."""
        self.visited_provinces = {}
        self.unvisited_provinces = {}

        for key, p_data in self.provinces.items():
            reg_code, city_slug = key.split("/")
            city_readme = self.repo_root / reg_code / city_slug / "README.md"
            banner_path = self.repo_root / reg_code / city_slug / "banner.jpg"

            p_data["visited"] = False
            p_data["has_banner"] = banner_path.exists()
            p_data["banner_rel"] = f"{reg_code}/{city_slug}/banner.jpg" if banner_path.exists() else "assets/banner.jpg"
            p_data["readme_rel"] = f"{reg_code}/{city_slug}/README.md"
            p_data["slug"] = city_slug

            if city_readme.exists():
                try:
                    content = city_readme.read_text(encoding="utf-8")
                    # Ziyaret edilmiş kriteri: '✅' işareti veya zengin içerik
                    is_visited = "✅" in content or (len(content) > 700 and "Henüz bu kadim şehre" not in content and "Henüz adımlanmamış" not in content)
                    if is_visited:
                        p_data["visited"] = True
                        p_data["content_size"] = len(content)
                        # İçerikten ek bilgileri ayıkla
                        self._extract_city_details(p_data, content)
                        self.visited_provinces[key] = p_data
                    else:
                        self.unvisited_provinces[key] = p_data
                except Exception:
                    self.unvisited_provinces[key] = p_data
            else:
                self.unvisited_provinces[key] = p_data

        self._compute_stats()

    def _extract_city_details(self, p_data, content):
        """Markdown içeriğinden alıntı ve detayları çıkarır."""
        quote_match = re.search(r'## 📜 Şehrin Ruhu\s*>\s*"([^"]+)"', content)
        if quote_match:
            p_data["custom_quote"] = quote_match.group(1).strip()
        
        lib_match = re.search(r'\*Seyyahın Kütüphane Notu:\*\s*(.+)', content)
        if lib_match:
            p_data["custom_library"] = lib_match.group(1).strip()

    def _compute_stats(self):
        """Genel ve bölgesel istatistikleri hesaplar."""
        total = len(self.provinces)
        visited = len(self.visited_provinces)
        pct = round((visited / total) * 100, 1) if total > 0 else 0

        # Bölgesel istatistikler
        reg_stats = {}
        for reg_code, r_info in REGIONS_INFO.items():
            reg_total = sum(1 for k in self.provinces if k.startswith(reg_code))
            reg_visited = sum(1 for k in self.visited_provinces if k.startswith(reg_code))
            reg_pct = round((reg_visited / reg_total) * 100, 1) if reg_total > 0 else 0
            reg_stats[reg_code] = {
                "name": r_info["name"],
                "icon": r_info["icon"],
                "color": r_info["color"],
                "desc": r_info["desc"],
                "total": reg_total,
                "visited": reg_visited,
                "percentage": reg_pct
            }

        # Tahmini seyahat mesafesi (Ziyaret edilen iller arası enlem-boylam üzerinden km hesabı)
        estimated_km = self._calculate_route_km()

        self.stats = {
            "total_cities": total,
            "visited_cities": visited,
            "unvisited_cities": total - visited,
            "progress_pct": pct,
            "estimated_km": estimated_km,
            "regional_breakdown": reg_stats
        }

    def _calculate_route_km(self):
        """Ziyaret edilen şehirler arası toplam kat edilen tahmini yolculuk mesafesi."""
        visited_list = list(self.visited_provinces.values())
        if len(visited_list) < 2:
            return 0
        
        # Şehirleri boylam/enleme göre sıralayarak yaklaşık bir gezi rotası çizgisi hesapla
        sorted_cities = sorted(visited_list, key=lambda c: (c["lng"], c["lat"]))
        total_km = 0
        for i in range(len(sorted_cities) - 1):
            c1 = sorted_cities[i]
            c2 = sorted_cities[i + 1]
            total_km += self.calculate_distance_km(c1["lat"], c1["lng"], c2["lat"], c2["lng"])
        
        # Karayolu katsayısı (kuş uçuşuna göre ~1.35 çarpanı)
        return int(total_km * 1.35)

    @staticmethod
    def calculate_distance_km(lat1, lon1, lat2, lon2):
        """Haversine formülü ile iki nokta arası küresel mesafe (km)."""
        R = 6371.0  # Dünya yarıçapı km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) ** 2 +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return round(R * c, 1)

    def plan_optimal_route(self, start_city_name=None, max_stops=10):
        """Ziyaret edilmemiş şehirler arasında en optimize gezi rotasını önerir."""
        unvisited = list(self.unvisited_provinces.values())
        if not unvisited:
            return []

        # Başlangıç şehri bul
        start_city = None
        if start_city_name:
            for p in self.provinces.values():
                if p["name"].lower() == start_city_name.lower() or p["slug"].lower() == start_city_name.lower():
                    start_city = p
                    break

        if not start_city:
            if self.visited_provinces:
                start_city = list(self.visited_provinces.values())[0]
            else:
                start_city = self.provinces.get("01_Marmara/Istanbul", unvisited[0])

        current = start_city
        remaining = unvisited.copy()
        route = [current]
        
        while remaining and len(route) <= max_stops:
            nearest = min(remaining, key=lambda c: self.calculate_distance_km(current["lat"], current["lng"], c["lat"], c["lng"]))
            dist = self.calculate_distance_km(current["lat"], current["lng"], nearest["lat"], nearest["lng"])
            nearest_copy = nearest.copy()
            nearest_copy["distance_from_prev_km"] = int(dist * 1.35)
            route.append(nearest_copy)
            remaining.remove(nearest)
            current = nearest

        return route

    def generate_web_data_json(self):
        """Frontend web uygulaması için `travel_data.json` ve `web_data.js` üretir."""
        export_data = {
            "stats": self.stats,
            "regions": REGIONS_INFO,
            "quotes": TRAVEL_QUOTES,
            "provinces": self.provinces
        }
        
        # travel_data.json
        json_path = self.repo_root / "travel_data.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)

        # web_data.js
        js_path = self.repo_root / "web_data.js"
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(f"// Otomatik Üretilen Dijital Seyyah Veri Modülü\nconst TRAVEL_DATA = {json.dumps(export_data, ensure_ascii=False, indent=2)};\n")

        return json_path, js_path

    def update_readme_stats(self):
        """README.md dosyasındaki genel ilerleme, badge'ler ve bölge listesini günceller."""
        readme_path = self.repo_root / "README.md"
        if not readme_path.exists():
            return False

        content = readme_path.read_text(encoding="utf-8")
        pct = self.stats["progress_pct"]
        visited_count = self.stats["visited_cities"]
        total_count = self.stats["total_cities"]

        # Badge güncelle
        content = re.sub(
            r'Keşif-[0-9.]+%%25-brightgreen',
            f'Keşif-{pct}%25-brightgreen',
            content
        )

        # Progress bar hesapla (20 blokluk gösterge)
        filled_blocks = int(round((pct / 100) * 20))
        empty_blocks = 20 - filled_blocks
        progress_bar = "🟩" * filled_blocks + "⬜" * empty_blocks

        # Genel İlerleme Satırı
        content = re.sub(
            r'\*\*🏆 Genel İlerleme:\*\* %[0-9.]+ \([0-9]+ / 81 İl\)\n[🟩⬜]+',
            f'**🏆 Genel İlerleme:** %{pct} ({visited_count} / {total_count} İl)\n{progress_bar}',
            content
        )

        # Bölge başlıklarındaki (x/y) sayıları güncelle
        for reg_code, r_stat in self.stats["regional_breakdown"].items():
            r_icon = r_stat["icon"]
            r_name = r_stat["name"]
            v = r_stat["visited"]
            t = r_stat["total"]
            pattern = rf'\*\*{re.escape(r_icon)}\s+{re.escape(r_name)}\s+\(\d+/\d+\)\*\*'
            replacement = f'**{r_icon} {r_name} ({v}/{t})**'
            content = re.sub(pattern, replacement, content)

        readme_path.write_text(content, encoding="utf-8")
        return True


if __name__ == "__main__":
    engine = SeyyahEngine()
    print(f"Toplam İl: {engine.stats['total_cities']}")
    print(f"Ziyaret Edilen: {engine.stats['visited_cities']} (%{engine.stats['progress_pct']})")
    print(f"Tahmini Seyahat: {engine.stats['estimated_km']} km")
    engine.generate_web_data_json()
    engine.update_readme_stats()
    print("Veriler başarıyla üretildi ve senkronize edildi.")
