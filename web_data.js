// Otomatik Üretilen Dijital Seyyah Veri Modülü
const TRAVEL_DATA = {
  "stats": {
    "total_cities": 81,
    "visited_cities": 39,
    "unvisited_cities": 42,
    "progress_pct": 48.1,
    "estimated_km": 10898,
    "regional_breakdown": {
      "01_Marmara": {
        "name": "Marmara Bölgesi",
        "icon": "🏰",
        "color": "#38bdf8",
        "desc": "Payitaht ve Tohum: Bir cihan imparatorluğunun mayalandığı iki kıtayı bağlayan kadim topraklar.",
        "total": 11,
        "visited": 3,
        "percentage": 27.3
      },
      "02_Ege": {
        "name": "Ege Bölgesi",
        "icon": "🌊",
        "color": "#34d399",
        "desc": "Zamanın Çizgileri & Zeytin Dalı: Antik mermerlerden turkuaz koylara uzanan bilgelik coğrafyası.",
        "total": 8,
        "visited": 3,
        "percentage": 37.5
      },
      "03_Akdeniz": {
        "name": "Akdeniz Bölgesi",
        "icon": "☀️",
        "color": "#f59e0b",
        "desc": "Sıcaklık & Antik Limanlar: Torosların heybetiyle kucaklaşan bin yıllık limanlar ve bereket ovaları.",
        "total": 8,
        "visited": 5,
        "percentage": 62.5
      },
      "04_IcAnadolu": {
        "name": "İç Anadolu Bölgesi",
        "icon": "🌾",
        "color": "#fbbf24",
        "desc": "Bozkırın Kalbi & İrfan Havzası: Mevlana'dan Yunus Emre'ye, Hacı Bektaş'tan Ahi Evran'a uzanan tevazu yurdu.",
        "total": 13,
        "visited": 8,
        "percentage": 61.5
      },
      "05_Karadeniz": {
        "name": "Karadeniz Bölgesi",
        "icon": "🌲",
        "color": "#10b981",
        "desc": "Zikir, Orman & Dalga: Hırçın dalgaların yemyeşil yaylalarla buluştuğu doğanın muazzam senfonisi.",
        "total": 18,
        "visited": 11,
        "percentage": 61.1
      },
      "06_DoguAnadolu": {
        "name": "Doğu Anadolu Bölgesi",
        "icon": "🏔️",
        "color": "#a855f7",
        "desc": "Zirvelerin İhtişamı & Kaleler: Zorlu iklimlerde pişen hayatların ve sarsılmaz kalelerin vakur duruşu.",
        "total": 14,
        "visited": 9,
        "percentage": 64.3
      },
      "07_GuneydoguAnadolu": {
        "name": "Güneydoğu Anadolu Bölgesi",
        "icon": "🏜️",
        "color": "#f97316",
        "desc": "Mezopotamya'nın Ninnisi & Medeniyet Beşiği: Göbeklitepe'den Harran'a, toprağın taşa, taşın efsaneye dönüştüğü masal.",
        "total": 9,
        "visited": 0,
        "percentage": 0.0
      }
    }
  },
  "regions": {
    "01_Marmara": {
      "name": "Marmara Bölgesi",
      "icon": "🏰",
      "color": "#38bdf8",
      "desc": "Payitaht ve Tohum: Bir cihan imparatorluğunun mayalandığı iki kıtayı bağlayan kadim topraklar."
    },
    "02_Ege": {
      "name": "Ege Bölgesi",
      "icon": "🌊",
      "color": "#34d399",
      "desc": "Zamanın Çizgileri & Zeytin Dalı: Antik mermerlerden turkuaz koylara uzanan bilgelik coğrafyası."
    },
    "03_Akdeniz": {
      "name": "Akdeniz Bölgesi",
      "icon": "☀️",
      "color": "#f59e0b",
      "desc": "Sıcaklık & Antik Limanlar: Torosların heybetiyle kucaklaşan bin yıllık limanlar ve bereket ovaları."
    },
    "04_IcAnadolu": {
      "name": "İç Anadolu Bölgesi",
      "icon": "🌾",
      "color": "#fbbf24",
      "desc": "Bozkırın Kalbi & İrfan Havzası: Mevlana'dan Yunus Emre'ye, Hacı Bektaş'tan Ahi Evran'a uzanan tevazu yurdu."
    },
    "05_Karadeniz": {
      "name": "Karadeniz Bölgesi",
      "icon": "🌲",
      "color": "#10b981",
      "desc": "Zikir, Orman & Dalga: Hırçın dalgaların yemyeşil yaylalarla buluştuğu doğanın muazzam senfonisi."
    },
    "06_DoguAnadolu": {
      "name": "Doğu Anadolu Bölgesi",
      "icon": "🏔️",
      "color": "#a855f7",
      "desc": "Zirvelerin İhtişamı & Kaleler: Zorlu iklimlerde pişen hayatların ve sarsılmaz kalelerin vakur duruşu."
    },
    "07_GuneydoguAnadolu": {
      "name": "Güneydoğu Anadolu Bölgesi",
      "icon": "🏜️",
      "color": "#f97316",
      "desc": "Mezopotamya'nın Ninnisi & Medeniyet Beşiği: Göbeklitepe'den Harran'a, toprağın taşa, taşın efsaneye dönüştüğü masal."
    }
  },
  "quotes": [
    {
      "quote": "Dünya bir kitaptır ve seyahat etmeyenler onun sadece bir sayfasını okur.",
      "author": "Aurelius Augustinus"
    },
    {
      "quote": "İyi bir gezginin sabit planları ve varmak gibi bir amacı yoktur.",
      "author": "Lao Tzu"
    },
    {
      "quote": "Gerçek keşif yolculuğu yeni manzaralar bulmak değil, yeni gözlerle bakmaktır.",
      "author": "Marcel Proust"
    },
    {
      "quote": "Kıyıyı gözden kaybetmeye cesaret edemeyenler, yeni okyanuslar keşfedemezler.",
      "author": "Andre Gide"
    },
    {
      "quote": "Yollar, sadece ayakların değil, zihnin de özgürleştiği patikalardır.",
      "author": "Friedrich Nietzsche"
    },
    {
      "quote": "De ki: Yeryüzünde gezip dolaşın da Allah’ın yaratmaya nasıl başladığını görün...",
      "author": "Kur'an-ı Kerim (Ankebût, 20)"
    },
    {
      "quote": "Yolculuğa çıkın ki sıhhat bulasınız ve ganimet elde edesiniz.",
      "author": "Hz. Muhammed (s.a.v.)"
    },
    {
      "quote": "Dünyada tıpkı bir garip veya bir yolcu gibi ol.",
      "author": "Hz. Muhammed (s.a.v.)"
    },
    {
      "quote": "Su akar ve hareket ederse tatlanır ve temiz kalır; durursa bozulur ve kokar. İnsan da seyahat ettikçe kemale erer.",
      "author": "İmam Şâfiî"
    },
    {
      "quote": "Yolculuk; varlığın hakikatini, insanın acziyetini ve nefsin gizli köşelerini ortaya çıkaran en berrak aynadır.",
      "author": "Muhyiddin İbnü'l-Arabî"
    },
    {
      "quote": "Yola çık ki yol sana görünsün; kendini yola bırak ki menzile eresin.",
      "author": "Ferîdüddin Attar"
    },
    {
      "quote": "Yolculuk, önce seni sessizleştirir, sonra da iyi bir hikâye anlatıcısına dönüştürür.",
      "author": "İbn Battûta"
    },
    {
      "quote": "Seyahat Ya Resulallah! Niyetiyle düşülen yollar, bereketiyle menzile erdirir.",
      "author": "Evliya Çelebi"
    },
    {
      "quote": "Gezgin, vardığı yerdeki her taşı bir anı, her insanı bir öğretmen gibi selamlar.",
      "author": "Kadim Doğu Özdeyişi"
    }
  ],
  "provinces": {
    "01_Marmara/Balikesir": {
      "plate": 10,
      "name": "Balıkesir",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 39.6484,
      "lng": 27.8826,
      "landmarks": [
        "Zağnos Paşa Camii",
        "Cunda Adası",
        "Kaz Dağları",
        "Manyas Kuş Cenneti"
      ],
      "specialties": [
        "Höşmerim",
        "Susurluk Tostu & Ayranı",
        "Balıkesir Kaymaklısı"
      ],
      "quote": "Kaz Dağları'nın oksijeni ile Marmara ve Ege'nin buluştuğu bereketli topraklar.",
      "library": "Balıkesir İl Halk Kütüphanesi - Geniş bahçesi ve sakin çalışma alanlarıyla verimli bir ortam.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "01_Marmara/Balikesir/README.md",
      "slug": "Balikesir"
    },
    "01_Marmara/Bilecik": {
      "plate": 11,
      "name": "Bilecik",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 40.1426,
      "lng": 29.9793,
      "landmarks": [
        "Şeyh Edebali Türbesi",
        "Söğüt Ertuğrul Gazi Türbesi",
        "Saat Kulesi"
      ],
      "specialties": [
        "Bilecik Güveci",
        "Pazaryeri Helvası",
        "Bıldırcın Kebabı"
      ],
      "quote": "Osmanlı Devleti'nin mayalandığı, Şeyh Edebali'nin 'İnsanı yaşat ki devlet yaşasın' nasihatinin yankılandığı kurucu menzil.",
      "library": "Bilecik İl Halk Kütüphanesi - Sakin ve odaklanmaya elverişli butik bir çalışma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "01_Marmara/Bilecik/README.md",
      "slug": "Bilecik"
    },
    "01_Marmara/Bursa": {
      "plate": 16,
      "name": "Bursa",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 40.1885,
      "lng": 29.061,
      "landmarks": [
        "Ulu Cami",
        "Yeşil Türbe",
        "Cumalıkızık",
        "Emir Sultan Camii",
        "Muradiye Külliyesi"
      ],
      "specialties": [
        "İskender Kebap",
        "Kestane Şekeri",
        "Muradiye Çorbası",
        "Cantık"
      ],
      "quote": "Bursa'da zaman, bir yeşil şadırvanda şırıldayan suyun musikisidir; Osmanlı'nın kurucu ve manevi payitahtı.",
      "library": "Bursa İl Halk Kütüphanesi - Geniş ve ferah salonları, zengin araştırma kaynakları ve huzurlu bahçesiyle ideal bir ilim yuvası.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "01_Marmara/Bursa/banner.jpg",
      "readme_rel": "01_Marmara/Bursa/README.md",
      "slug": "Bursa",
      "content_size": 2533,
      "custom_quote": "Yeşil Bursa, Osmanlı'nın ilk payitahtı, Uludağ'ın eteklerinde kurulmuş manevi bir sığınaktır.",
      "custom_library": "Bursa İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "01_Marmara/Canakkale": {
      "plate": 17,
      "name": "Çanakkale",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 40.1553,
      "lng": 26.4142,
      "landmarks": [
        "Şehitler Abidesi",
        "Truva Antik Kenti",
        "Aynalı Çarşı",
        "Kilitbahir Kalesi"
      ],
      "specialties": [
        "Peynir Helvası",
        "Sardalya",
        "Ezine Peyniri"
      ],
      "quote": "Tarihin yazıldığı, bir milletin bağımsızlık destanını kanıyla mühürlediği manevi boğaz.",
      "library": "Çanakkale Mehmet Akif Ersoy İl Halk Kütüphanesi - Modern deniz manzaralı ferah çalışma ortamı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "01_Marmara/Canakkale/README.md",
      "slug": "Canakkale"
    },
    "01_Marmara/Edirne": {
      "plate": 22,
      "name": "Edirne",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 41.6772,
      "lng": 26.5557,
      "landmarks": [
        "Selimiye Camii",
        "II. Bayezid Külliyesi Sağlık Müzesi",
        "Meriç Köprüsü",
        "Eski Cami"
      ],
      "specialties": [
        "Edirne Tava Ciğeri",
        "Badem Ezmesi",
        "Kavala Kurabiyesi"
      ],
      "quote": "Mimar Sinan'ın 'Ustalık eserim' dediği Selimiye ile taçlanmış, Osmanlı'nın Avrupa kapısı payitaht.",
      "library": "Edirne İl Halk Kütüphanesi - Tarihi dokusu içinde sükunet dolu araştırma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "01_Marmara/Edirne/README.md",
      "slug": "Edirne"
    },
    "01_Marmara/Istanbul": {
      "plate": 34,
      "name": "İstanbul",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 41.0082,
      "lng": 28.9784,
      "landmarks": [
        "Ayasofya-i Kebir",
        "Süleymaniye Camii",
        "Topkapı Sarayı",
        "Eyüp Sultan",
        "Galata Kulesi"
      ],
      "specialties": [
        "Sultanahmet Köftesi",
        "Balık Ekmek",
        "Boza",
        "Kanlıca Yoğurdu"
      ],
      "quote": "İki kıtanın secdesi, çağ açıp çağ kapatan ulu fethin emaneti ve medeniyetler başkenti.",
      "library": "Şemsipaşa İlçe Halk Kütüphanesi (Üsküdar) / Rami Kütüphanesi - Denize sıfır konumu ve asırlık atmosferiyle eşsiz bir çalışma sığınağı.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "01_Marmara/Istanbul/banner.jpg",
      "readme_rel": "01_Marmara/Istanbul/README.md",
      "slug": "Istanbul",
      "content_size": 2696,
      "custom_quote": "Yedi tepenin üstünde yükselen camileriyle, iki kıtayı birbirine bağlayan boğazıyla dünya tarihinin kalbidir.",
      "custom_library": "Istanbul İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "01_Marmara/Kirklareli": {
      "plate": 39,
      "name": "Kırklareli",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 41.7355,
      "lng": 27.2244,
      "landmarks": [
        "İğneada Longoz Ormanları",
        "Dupnisa Mağarası",
        "Hızırbey Camii"
      ],
      "specialties": [
        "Kırklareli Köftesi",
        "Hardaliye",
        "Kaşar Peyniri"
      ],
      "quote": "Trakya'nın yeşil kalbi, Longoz Ormanları'nın büyüleyici biyoçeşitliliği ve huzurlu bozkırı.",
      "library": "Kırklareli İl Halk Kütüphanesi - Sakin ve odaklanmayı artıran kütüphane düzeni.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "01_Marmara/Kirklareli/README.md",
      "slug": "Kirklareli"
    },
    "01_Marmara/Kocaeli": {
      "plate": 41,
      "name": "Kocaeli",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 40.7654,
      "lng": 29.9408,
      "landmarks": [
        "Saat Kulesi",
        "Sekapark",
        "Kandıra Kerpe Kayalıkları",
        "Gayret Gemi Müzesi"
      ],
      "specialties": [
        "Pişmaniye",
        "Kandıra Yoğurdu",
        "Dartı"
      ],
      "quote": "Körfezin sanayi ve lojistik damarı, Samanlı Dağları'nın yeşiliyle kucaklaşan kıyı kenti.",
      "library": "Kocaeli İl Halk Kütüphanesi - Modern iç tasarımı ve güçlü internet altyapısıyla kodlama mesaileri için son derece konforlu.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "01_Marmara/Kocaeli/banner.jpg",
      "readme_rel": "01_Marmara/Kocaeli/README.md",
      "slug": "Kocaeli",
      "content_size": 2467,
      "custom_quote": "Sanayinin gri çehresinin arkasında, asırlık çınarların ve körfezin mavi sularının fısıldadığı kadim bir tarih saklıdır.",
      "custom_library": "Kocaeli İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "01_Marmara/Sakarya": {
      "plate": 54,
      "name": "Sakarya",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 40.7731,
      "lng": 30.4026,
      "landmarks": [
        "Sapanca Gölü",
        "Justinianus Köprüsü (Beşköprü)",
        "Acarlar Longozu",
        "Taraklı Evleri"
      ],
      "specialties": [
        "Islama Köfte",
        "Kabak Tatlısı",
        "Uğut Tatlısı"
      ],
      "quote": "Sakarya Türküsü'nün döküldüğü ırmak, bereketli ovaları ve kadim Osmanlı kasabalarıyla köklü bir durak.",
      "library": "Sakarya İl Halk Kütüphanesi - Geniş çalışma masaları ve ferah ortamıyla verimli çalışma imkanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "01_Marmara/Sakarya/README.md",
      "slug": "Sakarya"
    },
    "01_Marmara/Tekirdag": {
      "plate": 59,
      "name": "Tekirdağ",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 40.9781,
      "lng": 27.5117,
      "landmarks": [
        "Namık Kemal Evi",
        "Rákóczi Müzesi",
        "Rüstem Paşa Camii",
        "Uçmakdere"
      ],
      "specialties": [
        "Tekirdağ Köftesi",
        "Hayrabolu Tatlısı",
        "Peynir Helvası"
      ],
      "quote": "Marmara'nın rüzgarlı kıyısı, vatan şairi Namık Kemal'in yurdu ve yamaç paraşütünün gözdesi.",
      "library": "Tekirdağ Namık Kemal İl Halk Kütüphanesi - Huzurlu deniz havası eşliğinde çalışma olanağı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "01_Marmara/Tekirdag/README.md",
      "slug": "Tekirdag"
    },
    "01_Marmara/Yalova": {
      "plate": 77,
      "name": "Yalova",
      "region": "Marmara",
      "region_code": "01_Marmara",
      "lat": 40.6549,
      "lng": 29.2842,
      "landmarks": [
        "Yürüyen Köşk",
        "Termal Kaplıcaları",
        "Sudüşen Şelalesi",
        "Karaca Arboretumu"
      ],
      "specialties": [
        "Yalova Köftesi",
        "Termal Tatlısı",
        "Kivi"
      ],
      "quote": "Yeşilin her tonunu saklayan şifalı sular diyarı ve çevrecilik sembolü Yürüyen Köşk'ün yurdu.",
      "library": "Yalova İl Halk Kütüphanesi - Şehir merkezinde butik, sakin ve odaklanmaya uygun bir mekan.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "01_Marmara/Yalova/README.md",
      "slug": "Yalova"
    },
    "02_Ege/Afyonkarahisar": {
      "plate": 3,
      "name": "Afyonkarahisar",
      "region": "Ege",
      "region_code": "02_Ege",
      "lat": 38.7569,
      "lng": 30.5387,
      "landmarks": [
        "Afyon Kalesi",
        "Mevlevi Camii ve Türbesi",
        "Frig Vadisi",
        "Ulu Cami"
      ],
      "specialties": [
        "Afyon Sucuğu",
        "Kaymaklı Ekmek Kadayıfı",
        "Bükme",
        "Haşhaşlı Çörek"
      ],
      "quote": "Karahisar Kalesi'nin heybeti, Mevleviliğin ikinci büyük ocağı ve Anadolu'nun kavşak noktası.",
      "library": "Afyonkarahisar Gedik Ahmet Paşa İl Halk Kütüphanesi - Tarihi dokuda sakin çalışma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "02_Ege/Afyonkarahisar/README.md",
      "slug": "Afyonkarahisar"
    },
    "02_Ege/Aydin": {
      "plate": 9,
      "name": "Aydın",
      "region": "Ege",
      "region_code": "02_Ege",
      "lat": 37.838,
      "lng": 27.8456,
      "landmarks": [
        "Aphrodisias Antik Kenti",
        "Didim Apollon Tapınağı",
        "Milet Antik Kenti",
        "Güvercinada Kalesi"
      ],
      "specialties": [
        "İncir",
        "Çine Köftesi",
        "Zeytinyağlı Börülce",
        "Kabak Tatlısı"
      ],
      "quote": "Gökyüzünün altındaki en güzel yeryüzü; bereketli Menderes Ovası ve antik mermerlerin zarafeti.",
      "library": "Aydın İl Halk Kütüphanesi - Üniversite ve şehir yaşamının kesiştiği ferah kütüphane.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "02_Ege/Aydin/README.md",
      "slug": "Aydin"
    },
    "02_Ege/Denizli": {
      "plate": 20,
      "name": "Denizli",
      "region": "Ege",
      "region_code": "02_Ege",
      "lat": 37.783,
      "lng": 29.0963,
      "landmarks": [
        "Pamukkale Travertenleri",
        "Hierapolis Antik Kenti",
        "Laodikeia",
        "Kaklık Mağarası"
      ],
      "specialties": [
        "Denizli Kebabı",
        "Zafer Gazozu",
        "Tavas Pidesi",
        "Çameli Fasulyesi"
      ],
      "quote": "Beyaz cennet travertenlerin şükür makamı ve antik Hierapolis'in şifalı termal havuzları.",
      "library": "Denizli İl Halk Kütüphanesi - Şehir merkezinde, sessiz çalışma salonları geniş, öğleden sonra kalabalık olabiliyor.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "02_Ege/Denizli/banner.jpg",
      "readme_rel": "02_Ege/Denizli/README.md",
      "slug": "Denizli",
      "content_size": 2377,
      "custom_quote": "Pamukkale'nin beyaz travertenleriyle doğanın ve tarihin beyaz bir rüya gibi birleştiği şehir.",
      "custom_library": "Denizli İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "02_Ege/Izmir": {
      "plate": 35,
      "name": "İzmir",
      "region": "Ege",
      "region_code": "02_Ege",
      "lat": 38.4192,
      "lng": 27.1287,
      "landmarks": [
        "Saat Kulesi",
        "Efes Antik Kenti",
        "Tarihi Kemeraltı Çarşısı",
        "Kadifekale",
        "Şirince"
      ],
      "specialties": [
        "İzmir Boyozu",
        "Kumru",
        "İzmir Bombası",
        "Tulum Peyniri",
        "Şambali"
      ],
      "quote": "Ege'nin incisi; Akdeniz rüzgarının özgürlük fısıldadığı, antik kütüphanelerin ve limanların şehri.",
      "library": "İzmir Milli Kütüphane / Atatürk İl Halk Kütüphanesi - Tarihi neoclassic mimarisi ve muazzam kitap koleksiyonuyla ilham kaynağı.",
      "visited": true,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "02_Ege/Izmir/README.md",
      "slug": "Izmir",
      "content_size": 2584,
      "custom_quote": "Ege'nin incisi İzmir, körfezin serin imbat rüzgarıyla yıkanan, hoşgörünün ve özgürlüğün simgesi kadim kent.",
      "custom_library": "Izmir İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "02_Ege/Kutahya": {
      "plate": 43,
      "name": "Kütahya",
      "region": "Ege",
      "region_code": "02_Ege",
      "lat": 39.4244,
      "lng": 29.9833,
      "landmarks": [
        "Aizanoi Antik Kenti",
        "Kütahya Kalesi",
        "Dönenler Camii (Mevlevihane)",
        "Çini Müzesi"
      ],
      "specialties": [
        "Kütahya Güveci",
        "Cimcik Aşı",
        "Sini Mantısı"
      ],
      "quote": "Çininin nakış nakış işlendiği sabır şehri, Germiyanoğulları'nın yadigarı ve Mevlevi ocağı.",
      "library": "Kütahya Vahit Paşa İl Halk Kütüphanesi - Yazma eserler koleksiyonu ve huzurlu salonları.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "02_Ege/Kutahya/README.md",
      "slug": "Kutahya"
    },
    "02_Ege/Manisa": {
      "plate": 45,
      "name": "Manisa",
      "region": "Ege",
      "region_code": "02_Ege",
      "lat": 38.614,
      "lng": 27.4296,
      "landmarks": [
        "Muradiye Camii",
        "Sultan Camii",
        "Spil Dağı Milli Parkı",
        "Sardes Antik Kenti"
      ],
      "specialties": [
        "Manisa Kebabı",
        "Mesir Macunu",
        "Kula Güveci"
      ],
      "quote": "Şehzadeler şehri; Mimar Sinan'ın Muradiye'si ve Spil Dağı'nın şifalı rüzgarları.",
      "library": "Manisa İl Halk Kütüphanesi - Ferah çalışma salonları ve merkezi konumuyla verimli.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "02_Ege/Manisa/README.md",
      "slug": "Manisa"
    },
    "02_Ege/Mugla": {
      "plate": 48,
      "name": "Muğla",
      "region": "Ege",
      "region_code": "02_Ege",
      "lat": 37.2153,
      "lng": 28.3636,
      "landmarks": [
        "Ölüdeniz",
        "Kelebekler Vadisi",
        "Bodrum Kalesi",
        "Saklıkent Kanyonu",
        "Dalyan Kaunos Kral Mezarları"
      ],
      "specialties": [
        "Muğla Köftesi",
        "Çökertme Kebabı",
        "Kabak Çiçeği Dolması",
        "Börülce"
      ],
      "quote": "Turkuaz koyların antik Likya ve Karya ile kucaklaştığı, tabiatın cömertçe sergilendiği cennet köşe.",
      "library": "Muğla İl Halk Kütüphanesi - Üniversite bölgesine yakın, çalışma ortamı sessiz ve ferah, priz sayısı yeterli.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "02_Ege/Mugla/banner.jpg",
      "readme_rel": "02_Ege/Mugla/README.md",
      "slug": "Mugla",
      "content_size": 2383,
      "custom_quote": "Turkuaz koyları, yeşil çam ormanları ve beyaz Muğla evleriyle doğanın en cömert davrandığı yeryüzü cenneti.",
      "custom_library": "Mugla İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "02_Ege/Usak": {
      "plate": 64,
      "name": "Uşak",
      "region": "Ege",
      "region_code": "02_Ege",
      "lat": 38.6735,
      "lng": 29.4059,
      "landmarks": [
        "Ulubey Kanyonu",
        "Blaundos Antik Kenti",
        "Clandras Köprüsü",
        "Uşak Arkeoloji Müzesi"
      ],
      "specialties": [
        "Tarhana Çorbası",
        "Döndürme Böreği",
        "Ebeli Köftesi"
      ],
      "quote": "Dünyanın en uzun ikinci kanyonuna sahip, Karun Hazineleri'nin saklandığı kadim halı ve kilim diyarı.",
      "library": "Uşak İl Halk Kütüphanesi - Sessiz, nezih ve çalışmaya elverişli ortam.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "02_Ege/Usak/README.md",
      "slug": "Usak"
    },
    "03_Akdeniz/Adana": {
      "plate": 1,
      "name": "Adana",
      "region": "Akdeniz",
      "region_code": "03_Akdeniz",
      "lat": 37.0,
      "lng": 35.3213,
      "landmarks": [
        "Taşköprü",
        "Sabancı Merkez Camii",
        "Büyük Saat",
        "Varda Köprüsü",
        "Anavarza Antik Kenti"
      ],
      "specialties": [
        "Adana Kebap",
        "Şalgam Suyu",
        "Bici Bici",
        "Analı Kızlı Çorbası",
        "Halka Tatlı"
      ],
      "quote": "Seyhan'ın serinliğiyle Çukurova'nın cömert sıcağını harmanlayan, lezzetin ve samimiyetin başkenti.",
      "library": "Adana İl Halk Kütüphanesi - Şehir merkezinde yer alıyor, klimaları yaz sıcağında can kurtarıyor, priz imkanları iyi.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "03_Akdeniz/Adana/banner.jpg",
      "readme_rel": "03_Akdeniz/Adana/README.md",
      "slug": "Adana",
      "content_size": 2368,
      "custom_quote": "Torosların gölgesinde, Seyhan Nehri'nin bereketli toprakları üzerinde yükselen, sıcakkanlı ve coşkulu şehir.",
      "custom_library": "Adana İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "03_Akdeniz/Antalya": {
      "plate": 7,
      "name": "Antalya",
      "region": "Akdeniz",
      "region_code": "03_Akdeniz",
      "lat": 36.8969,
      "lng": 30.7133,
      "landmarks": [
        "Kaleiçi",
        "Yivli Minare",
        "Düden Şelalesi",
        "Aspendos Tiyatrosu",
        "Termessos",
        "Olympos"
      ],
      "specialties": [
        "Antalya Piyazı (Tahinli)",
        "Hibeş",
        "Yanık Dondurma",
        "Turunç Reçeli"
      ],
      "quote": "Torosların gölgesinde Akdeniz'in kadim kodlarını taşıyan sıcacık liman ve medeniyetler beşiği.",
      "library": "Antalya İl Halk Kütüphanesi - Yeşillikler içindeki bahçesi ve geniş okuma salonlarıyla Akdeniz sıcağında serin bir çalışma limanı.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "03_Akdeniz/Antalya/banner.jpg",
      "readme_rel": "03_Akdeniz/Antalya/README.md",
      "slug": "Antalya",
      "content_size": 2394,
      "custom_quote": "Akdeniz'in parlayan güneşi, antik limanları, heybetli surları ve eşsiz doğasıyla tarihin ve coğrafyanın zirvesi.",
      "custom_library": "Antalya İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "03_Akdeniz/Burdur": {
      "plate": 15,
      "name": "Burdur",
      "region": "Akdeniz",
      "region_code": "03_Akdeniz",
      "lat": 37.7183,
      "lng": 30.2823,
      "landmarks": [
        "Salda Gölü",
        "Sagalassos Antik Kenti",
        "İnsuyu Mağarası",
        "Burdur Arkeoloji Müzesi"
      ],
      "specialties": [
        "Burdur Şiş",
        "Ceviz Ezmesi",
        "Testi Kebabı"
      ],
      "quote": "Göller Yöresi'nin incisi Salda'nın turkuaz suları ve Sagalassos'un Antoninler Çeşmesi'nde akan asırlık sular.",
      "library": "Burdur İl Halk Kütüphanesi - Göller yöresinin sükunetini yansıtan sessiz çalışma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "03_Akdeniz/Burdur/README.md",
      "slug": "Burdur"
    },
    "03_Akdeniz/Hatay": {
      "plate": 31,
      "name": "Hatay",
      "region": "Akdeniz",
      "region_code": "03_Akdeniz",
      "lat": 36.2023,
      "lng": 36.1613,
      "landmarks": [
        "Habib-i Neccar Camii",
        "St. Pierre Kilisesi",
        "Titus Tüneli & Beşikli Mağara",
        "Arkeoloji Müzesi"
      ],
      "specialties": [
        "Künefe",
        "Tepsi Kebabı",
        "Humus",
        "Muhammara",
        "Oruk (İçli Köfte)"
      ],
      "quote": "Medeniyetlerin, dinlerin ve kadim lezzetlerin bir arada kardeşçe yaşadığı ibret ve vefa şehri.",
      "library": "Hatay İl Halk Kütüphanesi - Tarihi dokusuyla ilham verici, sessiz çalışma odaları tefekkür ve kodlama için çok uygun.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "03_Akdeniz/Hatay/banner.jpg",
      "readme_rel": "03_Akdeniz/Hatay/README.md",
      "slug": "Hatay",
      "content_size": 2398,
      "custom_quote": "Dinlerin ve dillerin kardeşçe kucaklaştığı, tarihin en eski yerleşim yerlerinden biri olan hoşgörü başkenti.",
      "custom_library": "Hatay İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "03_Akdeniz/Isparta": {
      "plate": 32,
      "name": "Isparta",
      "region": "Akdeniz",
      "region_code": "03_Akdeniz",
      "lat": 37.7648,
      "lng": 30.5566,
      "landmarks": [
        "Eğirdir Gölü",
        "Kuyucak Lavanta Köyü",
        "Kovada Gölü Milli Parkı",
        "Firdevs Bey Camii"
      ],
      "specialties": [
        "Isparta Kebabı (Fırın Kebap)",
        "Gül Lokumu & Gül Reçeli",
        "Kabune Pilavı"
      ],
      "quote": "Güllerin ve lavantaların kokusuyla bezenmiş, Eğirdir Gölü'nün masmavi sükunetinde huzur bulunan diyar.",
      "library": "Isparta Halil Hamit Paşa İl Halk Kütüphanesi - Şehir merkezinde, sessiz çalışma alanları geniş ve ferah.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "03_Akdeniz/Isparta/banner.jpg",
      "readme_rel": "03_Akdeniz/Isparta/README.md",
      "slug": "Isparta",
      "content_size": 2275,
      "custom_quote": "Güllerin ve lavantaların kokusuyla bezenmiş, göller yöresinin incisi, doğa harikası şehir.",
      "custom_library": "Isparta İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "03_Akdeniz/Kahramanmaras": {
      "plate": 46,
      "name": "Kahramanmaraş",
      "region": "Akdeniz",
      "region_code": "03_Akdeniz",
      "lat": 37.5753,
      "lng": 36.9228,
      "landmarks": [
        "Maraş Kalesi",
        "Ulu Cami",
        "Taş Medrese",
        "Eshab-ı Kehf Külliyesi (Afşin)"
      ],
      "specialties": [
        "Maraş Dondurması",
        "Maraş Tarhanası",
        "Eli Böğründe",
        "Kelle Paça"
      ],
      "quote": "Yedi Güzel Adam'ın şiir ocağı, istiklalin kahraman kalesi ve Eshab-ı Kehf'in asırlık uykusunun mekanı.",
      "library": "Kahramanmaraş İl Halk Kütüphanesi - Edebiyat ve düşünce ikliminde verimli çalışma ortamı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "03_Akdeniz/Kahramanmaras/README.md",
      "slug": "Kahramanmaras"
    },
    "03_Akdeniz/Mersin": {
      "plate": 33,
      "name": "Mersin",
      "region": "Akdeniz",
      "region_code": "03_Akdeniz",
      "lat": 36.8121,
      "lng": 34.6415,
      "landmarks": [
        "Kızkalesi",
        "Cennet-Cehennem Obrukları",
        "Kanlıdivane",
        "Tarsus Eshab-ı Kehf Mağarası",
        "St. Paul Kuyusu"
      ],
      "specialties": [
        "Tantuni",
        "Cezerye",
        "Kerebiç",
        "Tarsus Şalgamı"
      ],
      "quote": "Palmiyeli sahil şeridi, Torosların yaylaları ve Tarsus'un asırlara meydan okuyan manevi derinliği.",
      "library": "Mersin İl Halk Kütüphanesi - Sahile yakın, ferah çalışma masaları ve deniz manzaralı dinlenme alanlarıyla motivasyon verici.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "03_Akdeniz/Mersin/banner.jpg",
      "readme_rel": "03_Akdeniz/Mersin/README.md",
      "slug": "Mersin",
      "content_size": 2373,
      "custom_quote": "Akdeniz kıyısında uzanan palmiyeleri, Kızkalesi ve antik kentleriyle tarihin denizle buluştuğu liman kent.",
      "custom_library": "Mersin İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "03_Akdeniz/Osmaniye": {
      "plate": 80,
      "name": "Osmaniye",
      "region": "Akdeniz",
      "region_code": "03_Akdeniz",
      "lat": 37.0746,
      "lng": 36.2464,
      "landmarks": [
        "Kastabala Antik Kenti",
        "Toprakkale Kalesi",
        "Karatepe-Aslantaş Açık Hava Müzesi"
      ],
      "specialties": [
        "Osmaniye Yer Fıstığı",
        "Tırşık Çorbası",
        "Kömeç"
      ],
      "quote": "Çukurova'nın doğu kapısı, Hitit kalıntılarının ve kaleler kuşağının nöbet tuttuğu geçit.",
      "library": "Osmaniye Emine Keskiner İl Halk Kütüphanesi - Sessiz, düzenli çalışma ortamı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "03_Akdeniz/Osmaniye/README.md",
      "slug": "Osmaniye"
    },
    "04_IcAnadolu/Aksaray": {
      "plate": 68,
      "name": "Aksaray",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 38.3687,
      "lng": 34.037,
      "landmarks": [
        "Ihlara Vadisi",
        "Somuncu Baba Türbesi",
        "Sultanhanı Kervansarayı",
        "Eğri Minare"
      ],
      "specialties": [
        "Aksaray Tava",
        "Şerbetsiz Şekerpare",
        "Köpük Helva"
      ],
      "quote": "Somuncu Baba'nın fırınındaki sır, Ihlara Vadisi'nin derin tefekkürü ve İpekyolu'nun ulu kervansarayları.",
      "library": "Aksaray İl Halk Kütüphanesi - Bozkırın ortasında modern ve sessiz bir çalışma alanı.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "04_IcAnadolu/Aksaray/banner.jpg",
      "readme_rel": "04_IcAnadolu/Aksaray/README.md",
      "slug": "Aksaray",
      "content_size": 2345,
      "custom_quote": "Ihlara Vadisi'nin dik yamaçları arasında, Melendiz Çayı'nın şırıltısıyla demlenen bozkırın mistik kapısı.",
      "custom_library": "Aksaray İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "04_IcAnadolu/Ankara": {
      "plate": 6,
      "name": "Ankara",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 39.9334,
      "lng": 32.8597,
      "landmarks": [
        "Hacı Bayram-ı Veli Camii",
        "Ankara Kalesi",
        "Anıtkabir",
        "Augustus Tapınağı",
        "Hamamönü"
      ],
      "specialties": [
        "Ankara Döneri",
        "Ankara Simidi",
        "Beypazarı Kurusu",
        "Çubuk Turşusu"
      ],
      "quote": "Bozkırın kalbinde Hacı Bayram-ı Veli'nin manevi muhafızlığında kurulan cumhuriyetin payitahtı.",
      "library": "Milli Kütüphane / Cumhurbaşkanlığı Millet Kütüphanesi - Türkiye'nin en görkemli ilim mabetleri; 7/24 çalışma, devasa kaynak arşivi ve üst düzey konsantrasyon.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "04_IcAnadolu/Ankara/banner.jpg",
      "readme_rel": "04_IcAnadolu/Ankara/README.md",
      "slug": "Ankara",
      "content_size": 2447,
      "custom_quote": "Vakur ve tarihi Ankara, Türkiye Cumhuriyeti'nin kalbi, bozkırın ortasında yükselen azim ve kararlılık abidesi.",
      "custom_library": "Ankara İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "04_IcAnadolu/Cankiri": {
      "plate": 18,
      "name": "Çankırı",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 40.6013,
      "lng": 33.6134,
      "landmarks": [
        "Tarihi Tuz Mağarası",
        "Çankırı Kalesi",
        "Taş Mescit (Şifahane)",
        "Çavundur Kaplıcaları"
      ],
      "specialties": [
        "Yaren Güveci",
        "Cimcik Hamuru",
        "Yumurta Tatlısı"
      ],
      "quote": "Yer altındaki devasa tuz şehri, Selçuklu Taş Mescidi ve yarenlik kültürünün kadim edep diyarı.",
      "library": "Çankırı İl Halk Kütüphanesi - Yarenler diyarında sakin ve samimi bir ilim yuvası.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "04_IcAnadolu/Cankiri/README.md",
      "slug": "Cankiri"
    },
    "04_IcAnadolu/Eskisehir": {
      "plate": 26,
      "name": "Eskişehir",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 39.7767,
      "lng": 30.5206,
      "landmarks": [
        "Odunpazarı Evleri",
        "Kurşunlu Külliyesi",
        "Porsuk Çayı & Adalar",
        "Yunus Emre Türbesi (Mihalıççık)",
        "Yazılıkaya Midas"
      ],
      "specialties": [
        "Çibörek",
        "Balaban Köfte",
        "Met Helvası",
        "Haşhaşlı Ekmek"
      ],
      "quote": "Yunus Emre'nin 'Gelin tanış olalım' davetinin yankılandığı, sanatla yıkanmış dinamik bir kültür kenti.",
      "library": "Eskişehir İl Halk Kütüphanesi - Genç nüfusun yoğun olduğu, dinamik, internet hızı yüksek ve priz imkanı bol olan modern kütüphane.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "04_IcAnadolu/Eskisehir/banner.jpg",
      "readme_rel": "04_IcAnadolu/Eskisehir/README.md",
      "slug": "Eskisehir",
      "content_size": 2419,
      "custom_quote": "Porsuk Çayı'nın iki yakasında yükselen, gençliğin, sanatın ve Odunpazarı'nın tarihi evlerinin harmanlandığı kültür şehri.",
      "custom_library": "Eskisehir İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "04_IcAnadolu/Karaman": {
      "plate": 70,
      "name": "Karaman",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 37.1759,
      "lng": 33.2287,
      "landmarks": [
        "Karaman Kalesi",
        "Hatuniye Medresesi",
        "Yunus Emre Camii",
        "Aktekke (Mader-i Mevlana) Camii",
        "Binbirkilise"
      ],
      "specialties": [
        "Karaman Guymak Tatlısı",
        "Calla Yemeği",
        "Batırık"
      ],
      "quote": "Türkçenin resmi dil ilan edildiği Karamanoğlu Mehmet Bey'in yurdu ve Mevlana'nın annesinin medfun olduğu topraklar.",
      "library": "Karaman İl Halk Kütüphanesi - Türk dilinin başkentinde sessiz çalışma salonu.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "04_IcAnadolu/Karaman/README.md",
      "slug": "Karaman"
    },
    "04_IcAnadolu/Kayseri": {
      "plate": 38,
      "name": "Kayseri",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 38.7312,
      "lng": 35.4787,
      "landmarks": [
        "Erciyes Dağı",
        "Hunat Hatun Külliyesi",
        "Gevher Nesibe Tıp Medresesi",
        "Kayseri Kalesi",
        "Kapuzbaşı Şelaleleri"
      ],
      "specialties": [
        "Kayseri Mantısı",
        "Pastırma & Sucuk",
        "Yağlama (Şebit)",
        "Nevzine Tatlısı"
      ],
      "quote": "Erciyes'in beyaz karlı zirvesi altında Selçuklu şifahaneleri, Ahilik ahlakı ve ticaret zekasının harmanı.",
      "library": "Kayseri 75. Yıl İl Halk Kütüphanesi / Meryem Ana Şehir Kütüphanesi - Selçuklu esintili mekanlar.",
      "visited": false,
      "has_banner": true,
      "banner_rel": "04_IcAnadolu/Kayseri/banner.jpg",
      "readme_rel": "04_IcAnadolu/Kayseri/README.md",
      "slug": "Kayseri"
    },
    "04_IcAnadolu/Kirikkale": {
      "plate": 71,
      "name": "Kırıkkale",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 39.8468,
      "lng": 33.5153,
      "landmarks": [
        "Çeşnigir Köprüsü ve Kanyonu",
        "Silah Sanayi Müzesi",
        "Hasandede Camii ve Türbesi",
        "Nur Camii"
      ],
      "specialties": [
        "Kırıkkale Tavası",
        "Keskin Tavası",
        "Tuvalak"
      ],
      "quote": "Kızılırmak'ın süzüldüğü Çeşnigir Köprüsü ve savunma sanayiimizin bozkırdaki omurgası.",
      "library": "Kırıkkale İl Halk Kütüphanesi - Geniş ve aydınlık çalışma ortamı ile odaklanmayı kolaylaştıran düzen.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "04_IcAnadolu/Kirikkale/banner.jpg",
      "readme_rel": "04_IcAnadolu/Kirikkale/README.md",
      "slug": "Kirikkale",
      "content_size": 2327,
      "custom_quote": "Bozkırın ortasında Kızılırmak'ın sularıyla hayat bulan, cumhuriyetin sanayi hamleleriyle gelişmiş mütevazı şehir.",
      "custom_library": "Kirikkale İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "04_IcAnadolu/Kirsehir": {
      "plate": 40,
      "name": "Kırşehir",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 39.1425,
      "lng": 34.1709,
      "landmarks": [
        "Ahi Evran Camii ve Türbesi",
        "Cacabey Medresesi (Gözlemevi)",
        "Neşet Ertaş Gönül Sultanları Evi",
        "Aşıkpaşa Türbesi"
      ],
      "specialties": [
        "Kırşehir Köftesi",
        "Çirleme",
        "Ahi Helvası"
      ],
      "quote": "Ahilik teşkilatının kurucusu Ahi Evran'ın ocağı, gökbilim medresesi Cacabey ve Bozkırın Tezenesi Neşet Ertaş'ın sazının sesi.",
      "library": "Kırşehir İl Halk Kütüphanesi - UNESCO Müzik Şehri'nde huzur dolu araştırma salonu.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "04_IcAnadolu/Kirsehir/README.md",
      "slug": "Kirsehir"
    },
    "04_IcAnadolu/Konya": {
      "plate": 42,
      "name": "Konya",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 37.8667,
      "lng": 32.4833,
      "landmarks": [
        "Mevlana Müzesi & Dergahı",
        "Alaaddin Camii & Tepesi",
        "İnce Minareli Medrese",
        "Karatay Medresesi",
        "Sille Köyü"
      ],
      "specialties": [
        "Etliekmek",
        "Fırın Kebabı",
        "Tirit",
        "Bamya Çorbası",
        "Mevlana Şekeri"
      ],
      "quote": "Hazreti Mevlana'nın 'Gel, ne olursan ol yine gel' nidasiyla dünyaya sevgi ve tevhid yayan Selçuklu payitahtı.",
      "library": "Konya İl Halk Kütüphanesi - Geniş ve ferah salonları var, Selçuklu mimarisinin esintilerini taşıyor, çalışma disiplini yüksek.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "04_IcAnadolu/Konya/banner.jpg",
      "readme_rel": "04_IcAnadolu/Konya/README.md",
      "slug": "Konya",
      "content_size": 2465,
      "custom_quote": "Hazreti Mevlana'nın hoşgörü ve aşk iklimiyle demlenmiş, Selçuklu'nun muhteşem payitahtı, irfan merkezi.",
      "custom_library": "Konya İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "04_IcAnadolu/Nevsehir": {
      "plate": 50,
      "name": "Nevşehir",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 38.6244,
      "lng": 34.7144,
      "landmarks": [
        "Göreme Açık Hava Müzesi",
        "Uçhisar Kalesi",
        "Derinkuyu Yeraltı Şehri",
        "Hacı Bektaş-ı Veli Türbesi",
        "Paşabağları"
      ],
      "specialties": [
        "Testi Kebabı",
        "Kapadokya Şarabı/Üzüm Suyu",
        "Kabak Çekirdeği",
        "Nevşehir Tavası"
      ],
      "quote": "Peribacalarının masalsı vadilerinde zamanın durduğu, Hacı Bektaş-ı Veli'nin 'Bir olalım, iri olalım, diri olalım' irfanı.",
      "library": "Nevşehir İl Halk Kütüphanesi - Taş mimarisiyle huzurlu, sessiz odaları odağı artırmak için ideal.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "04_IcAnadolu/Nevsehir/banner.jpg",
      "readme_rel": "04_IcAnadolu/Nevsehir/README.md",
      "slug": "Nevsehir",
      "content_size": 2421,
      "custom_quote": "Kapadokya'nın masalsı vadilerinde, peri bacalarının rüzgarla fısıldaştığı, zamanın ve mekanın ötesinde bir rüya coğrafyası.",
      "custom_library": "Nevsehir İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "04_IcAnadolu/Nigde": {
      "plate": 51,
      "name": "Niğde",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 37.9667,
      "lng": 34.6833,
      "landmarks": [
        "Niğde Kalesi ve Saat Kulesi",
        "Alaaddin Camii (Güneş Portali)",
        "Gümüşler Manastırı",
        "Aladağlar Milli Parkı"
      ],
      "specialties": [
        "Niğde Tavası",
        "Niğde Gazozu",
        "Elma Tatlısı"
      ],
      "quote": "Aladağlar'ın görkemi altında Selçuklu kadın motiflerinin taşa işlendiği ve 'Geçti Bor'un pazarı' deyişinin yurdu.",
      "library": "Niğde İl Halk Kütüphanesi - Sakin ve odaklanmaya elverişli ortam.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "04_IcAnadolu/Nigde/README.md",
      "slug": "Nigde"
    },
    "04_IcAnadolu/Sivas": {
      "plate": 58,
      "name": "Sivas",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 39.7477,
      "lng": 37.0179,
      "landmarks": [
        "Divriği Ulu Cami ve Darüşşifası",
        "Çifte Minareli Medrese",
        "Buruciye Medresesi",
        "Gök Medrese",
        "Atatürk Kongre ve Etnografya Müzesi"
      ],
      "specialties": [
        "Sivas Köftesi",
        "Sivas Katmeri",
        "Pezik Turşusu",
        "Madımak"
      ],
      "quote": "Selçuklu taş işçiliğinin şaheseri Divriği Ulu Camii ile taçlanmış, Âşık Veysel'in sazındaki hakikat arayışı.",
      "library": "Sivas Şems-i Sivasî İl Halk Kütüphanesi - Selçuklu esintileriyle bezeli geniş ve son derece düzenli çalışma salonları.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "04_IcAnadolu/Sivas/banner.jpg",
      "readme_rel": "04_IcAnadolu/Sivas/README.md",
      "slug": "Sivas",
      "content_size": 2511,
      "custom_quote": "Selçuklu çinilerinde gökyüzünü arayan, bozkırın ortasında yükselen ulu medreseleriyle vakur ve tarihi şehir.",
      "custom_library": "Sivas İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "04_IcAnadolu/Yozgat": {
      "plate": 66,
      "name": "Yozgat",
      "region": "İç Anadolu",
      "region_code": "04_IcAnadolu",
      "lat": 39.8181,
      "lng": 34.8147,
      "landmarks": [
        "Yozgat Çamlığı Milli Parkı",
        "Çapanoğlu Camii",
        "Tarihi Saat Kulesi",
        "Nizamoğlu Konağı",
        "Kazankaya Kanyonu"
      ],
      "specialties": [
        "Testi Kebabı",
        "Arabaşı Çorbası ve Hamuru",
        "Yozgat Parmak Çöreği"
      ],
      "quote": "Bozkırın ortasında serin bir nefes, Türkiye'nin ilk milli parkı Yozgat Çamlığı'nın gölgesinde samimi bir menzil.",
      "library": "Yozgat İl Halk Kütüphanesi - Sessiz, düzenli çalışma ortamı ve çam kokulu molalar için ideal mekan.",
      "visited": true,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "04_IcAnadolu/Yozgat/README.md",
      "slug": "Yozgat",
      "content_size": 1492,
      "custom_quote": "Bozkırın ortasında serin bir nefes, Yozgat Çamlığı'nın gölgesinde saklı kalan samimi bir Anadolu şehri."
    },
    "05_Karadeniz/Amasya": {
      "plate": 5,
      "name": "Amasya",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 40.6501,
      "lng": 35.8353,
      "landmarks": [
        "Kral Kaya Mezarları",
        "Harşena Kalesi",
        "Yalıboyu Evleri",
        "Sultan II. Bayezid Külliyesi",
        "Ferhat ile Şirin Su Kanalı"
      ],
      "specialties": [
        "Amasya Elması",
        "Amasya Çöreği",
        "Baklalı Dolma",
        "Toyga Çorbası"
      ],
      "quote": "Yeşilırmak boyunca inci gibi dizilen Yalıboyu konakları, şehzadeler mektebi ve Ferhat ile Şirin'in efsanevi aşkı.",
      "library": "Amasya İl Halk Kütüphanesi - Yeşilırmak kıyısında, nehrin şırıltısı eşliğinde kod yazma deneyimi sunan eşsiz bir çalışma alanı.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Amasya/banner.jpg",
      "readme_rel": "05_Karadeniz/Amasya/README.md",
      "slug": "Amasya",
      "content_size": 2401,
      "custom_quote": "Kral Kaya Mezarları'nın gölgesinde, Yeşilırmak'ın iki yakasında yükselen Yalıboyu evleriyle tarihin secdesi.",
      "custom_library": "Amasya İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Artvin": {
      "plate": 8,
      "name": "Artvin",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 41.1828,
      "lng": 41.8183,
      "landmarks": [
        "Borçka Karagöl",
        "Şavşat Karagöl",
        "Mençuna Şelalesi",
        "Çoruh Vadisi",
        "Atatepe"
      ],
      "specialties": [
        "Karalahana Sarması",
        "Laz Böreği",
        "Mısır Ekmeği",
        "Kuymak (Muhlama)"
      ],
      "quote": "Bulutların üzerinde saklı Karagöl'ün zümrüt suları, dik yamaçların inadı ve doğanın muazzam zikri.",
      "library": "Artvin İl Halk Kütüphanesi - Yamaçta kurulu, manzaralı, dik yokuşlardan sonra dinlenip kod yazmak için ideal sessiz sığınak.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Artvin/banner.jpg",
      "readme_rel": "05_Karadeniz/Artvin/README.md",
      "slug": "Artvin",
      "content_size": 2364,
      "custom_quote": "Karagöl'ün büyüleyici yansımasında yeşilin binbir tonunu barındıran, dik yamaçların ve sisli yaylaların şehri.",
      "custom_library": "Artvin İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Bartin": {
      "plate": 74,
      "name": "Bartın",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 41.6344,
      "lng": 32.3375,
      "landmarks": [
        "Amasra Kalesi",
        "Kemere Köprüsü",
        "Güzelcehisar Lav Sütunları",
        "İnkumu Plajı"
      ],
      "specialties": [
        "Amasra Salatası",
        "Bartın Pompom Helvası",
        "Kabak Burması"
      ],
      "quote": "Fatih Sultan Mehmet'in 'Çeşm-i Cihan (Dünyanın Gözbebeği) burası mı ola?' dediği büyüleyici sahil kenti.",
      "library": "Bartın İl Halk Kütüphanesi - Karadeniz kıyısında huzurlu çalışma ortamı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "05_Karadeniz/Bartin/README.md",
      "slug": "Bartin"
    },
    "05_Karadeniz/Bayburt": {
      "plate": 69,
      "name": "Bayburt",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 40.2552,
      "lng": 40.2249,
      "landmarks": [
        "Bayburt Kalesi",
        "Baksı Müzesi",
        "Kenan Yavuz Etnografya Müzesi",
        "Çoruh Nehri",
        "Saat Kulesi"
      ],
      "specialties": [
        "Bayburt Ketesi",
        "Tatlı Çorba",
        "Galaçoş",
        "Lor Dolması"
      ],
      "quote": "Çoruh Nehri'nin ikiye böldüğü kadim kale kenti ve bozkırın ortasında modern sanatın zirvesi Baksı Müzesi.",
      "library": "Bayburt İl Halk Kütüphanesi - Çoruh Nehri kıyısında, sessiz ve sakin bir çalışma ortamı.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Bayburt/banner.jpg",
      "readme_rel": "05_Karadeniz/Bayburt/README.md",
      "slug": "Bayburt",
      "content_size": 2359,
      "custom_quote": "Baksı Müzesi ile modern sanatı bozkırın tepesinde buluşturan, Çoruh'un serinlettiği tarihi kale şehir.",
      "custom_library": "Bayburt İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Bolu": {
      "plate": 14,
      "name": "Bolu",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 40.7358,
      "lng": 31.6061,
      "landmarks": [
        "Abant Gölü",
        "Gölcük Tabiat Parkı",
        "Yedigöller Milli Parkı",
        "Göynük Tarihi Evleri"
      ],
      "specialties": [
        "Mengen Aşçı Yemekleri",
        "Abant Kebabı",
        "Bolu Çikolatası",
        "Saray Helvası"
      ],
      "quote": "Yedigöller'in tabiat paleti, Osmanlı kasabası Göynük ve Akşemseddin Hazretleri'nin manevi gölgesi.",
      "library": "Bolu İl Halk Kütüphanesi - Göller ve ormanlar diyarı Bolu'da verimli bir çalışma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "05_Karadeniz/Bolu/README.md",
      "slug": "Bolu"
    },
    "05_Karadeniz/Corum": {
      "plate": 19,
      "name": "Çorum",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 40.5506,
      "lng": 34.9556,
      "landmarks": [
        "Hattuşaş (Boğazkale) Hitit Başkenti",
        "Alacahöyük",
        "Saat Kulesi",
        "Ulu Cami",
        "İncesu Kanyonu"
      ],
      "specialties": [
        "Çorum Leblebisi",
        "Çorum Mantısı",
        "İskilip Dolması"
      ],
      "quote": "3500 yıllık Hitit İmparatorluğu'nun başkenti Hattuşaş'ın aslanlı kapıları ve taş kabartmaları.",
      "library": "Çorum İl Halk Kütüphanesi - Sessiz ve düzenli çalışma odalarıyla odaklanmayı kolaylaştıran sakin bir Anadolu kütüphanesi.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Corum/banner.jpg",
      "readme_rel": "05_Karadeniz/Corum/README.md",
      "slug": "Corum",
      "content_size": 2438,
      "custom_quote": "Hattuşaş antik kentinin binlerce yıllık mabet kalıntılarıyla Hitit uygarlığının gücünü fısıldayan kadim topraklar.",
      "custom_library": "Corum İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Duzce": {
      "plate": 81,
      "name": "Düzce",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 40.8438,
      "lng": 31.1565,
      "landmarks": [
        "Güzeldere Şelalesi",
        "Samandere Şelalesi",
        "Akçakoca Ceneviz Kalesi",
        "Fakıllı Mağarası"
      ],
      "specialties": [
        "Düzce Köftesi",
        "İsli Düzce Çerkes Peyniri",
        "Fındık"
      ],
      "quote": "Şelalelerin coşkusu, yaylaların serinliği ve 81. ilimizin bereketli toprakları.",
      "library": "Düzce İl Halk Kütüphanesi - Sakin ve ferah salonlar.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "05_Karadeniz/Duzce/README.md",
      "slug": "Duzce"
    },
    "05_Karadeniz/Giresun": {
      "plate": 28,
      "name": "Giresun",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 40.9128,
      "lng": 38.3895,
      "landmarks": [
        "Giresun Kalesi",
        "Giresun Adası",
        "Kümbet Yaylası",
        "Mavi Göl & Kuzalan Şelalesi",
        "Zeytinlik Mahallesi"
      ],
      "specialties": [
        "Giresun Fındığı",
        "Giresun Pidesi",
        "Karalahana Diblesi",
        "Isırgan Otu Çorbası"
      ],
      "quote": "Karadeniz'in iki yaşanabilir adasından birine ev sahipliği yapan, zümrüt fındık bahçeleri ve Mavi Göl mucizesi.",
      "library": "Giresun İl Halk Kütüphanesi - Harşit Vadisi ve deniz esintileriyle serin, sakin çalışma masaları mevcut.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Giresun/banner.jpg",
      "readme_rel": "05_Karadeniz/Giresun/README.md",
      "slug": "Giresun",
      "content_size": 2342,
      "custom_quote": "Karadeniz'in tek yaşanabilir adasına sahip olan, fındığın ve yeşilin dalgalarla buluştuğu sahil şehri.",
      "custom_library": "Giresun İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Gumushane": {
      "plate": 29,
      "name": "Gümüşhane",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 40.46,
      "lng": 39.47,
      "landmarks": [
        "Karaca Mağarası",
        "Torul Cam Seyir Terası",
        "Tomara Şelalesi",
        "Süleymaniye Mahallesi",
        "Krom Vadisi"
      ],
      "specialties": [
        "Pestil & Köme",
        "Siron",
        "Kete",
        "Gümüşhane Elması"
      ],
      "quote": "Vadiler arasına gizlenmiş sarkıt cenneti Karaca Mağarası ve gümüş madenleriyle parlayan Süleymaniye.",
      "library": "Gümüşhane İl Halk Kütüphanesi - Vadinin serinliğinde, odaklanmayı kolaylaştıran butik ve huzurlu çalışma alanı.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Gumushane/banner.jpg",
      "readme_rel": "05_Karadeniz/Gumushane/README.md",
      "slug": "Gumushane",
      "content_size": 2262,
      "custom_quote": "Karaca Mağarası'nın büyüleyici sarkıtlarıyla yeraltı saraylarını andıran, vadiler arasına gizlenmiş gümüş şehir.",
      "custom_library": "Gumushane İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Karabuk": {
      "plate": 78,
      "name": "Karabük",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 41.2061,
      "lng": 32.6204,
      "landmarks": [
        "Safranbolu Tarihi Evleri",
        "Kristal Teras",
        "Tokatlı Kanyonu",
        "Bulak Mencilis Mağarası",
        "Yörük Köyü"
      ],
      "specialties": [
        "Safranbolu Lokumu",
        "Bükme Pide",
        "Kuyu Kebabı",
        "Safran Çayı"
      ],
      "quote": "UNESCO Dünya Mirası Safranbolu'nun asırlık ahşap konakları, taş sokakları ve safranın eşsiz kokusu.",
      "library": "Karabük İl Halk Kütüphanesi - Safranbolu'nun tarihi atmosferine yakın sessiz kütüphane.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "05_Karadeniz/Karabuk/README.md",
      "slug": "Karabuk"
    },
    "05_Karadeniz/Kastamonu": {
      "plate": 37,
      "name": "Kastamonu",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 41.3887,
      "lng": 33.7827,
      "landmarks": [
        "Kastamonu Kalesi",
        "Nasrullah Camii ve Şadırvanı",
        "Valla Kanyonu",
        "Horma Kanyonu",
        "Şeyh Şaban-ı Veli Türbesi"
      ],
      "specialties": [
        "Kastamonu Pastırması",
        "Etli Ekmek",
        "Siyez Bulguru",
        "Çekme Helva",
        "Kuyu Kebabı"
      ],
      "quote": "Şeyh Şaban-ı Veli'nin manevi dergahı, İstiklal Yolu'nun kahraman kadınları ve Ilgaz Dağları'nın heybeti.",
      "library": "Kastamonu İl Halk Kütüphanesi - Tarihi şehir dokusunda ilham dolu çalışma noktası.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "05_Karadeniz/Kastamonu/README.md",
      "slug": "Kastamonu"
    },
    "05_Karadeniz/Ordu": {
      "plate": 52,
      "name": "Ordu",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 40.9839,
      "lng": 37.8764,
      "landmarks": [
        "Boztepe & Teleferik",
        "Yason Burnu & Kilisesi",
        "Perşembe Yaylası Menderesleri",
        "Kurul Kalesi",
        "Çambaşı Yaylası"
      ],
      "specialties": [
        "Ordu Pidesi",
        "Fındık",
        "Pancar Çorbası",
        "Melocan Kavurması"
      ],
      "quote": "Boztepe'den Karadeniz'in mavisine bakış ve Perşembe Yaylası'nın doğa harikası menderesleri.",
      "library": "Ordu İl Halk Kütüphanesi - Teleferik hattına yakın konumuyla mola vermeye uygun, çalışma salonları geniş.",
      "visited": true,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "05_Karadeniz/Ordu/README.md",
      "slug": "Ordu",
      "content_size": 2348,
      "custom_quote": "Boztepe'den Karadeniz'i ayaklar altına seren, mavi ile yeşilin en kusursuz birleştiği huzurlu sahil şehri.",
      "custom_library": "Ordu İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Rize": {
      "plate": 53,
      "name": "Rize",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 41.0201,
      "lng": 40.5234,
      "landmarks": [
        "Ayder Yaylası",
        "Pokut & Sal Yaylaları",
        "Zilkale",
        "Fırtına Vadisi",
        "Kaçkar Dağları Milli Parkı"
      ],
      "specialties": [
        "Rize Çayı",
        "Muhlama",
        "Rize Kavurması",
        "Laz Böreği",
        "Enişte Lokumu"
      ],
      "quote": "Kaçkarların sisli zirveleri, Fırtına Deresi'nin coşkusu ve dik yamaçlara serilmiş zümrüt çay bahçeleri.",
      "library": "Rize İl Halk Kütüphanesi - Çay tarlalarının yeşili eşliğinde, modern altyapısı ve güçlü internetiyle kodlama için ideal.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Rize/banner.jpg",
      "readme_rel": "05_Karadeniz/Rize/README.md",
      "slug": "Rize",
      "content_size": 2343,
      "custom_quote": "Fırtına Deresi'nin coşkulu sesi, Zil Kale'nin sarp kayalıklardaki asil duruşu ve yeşilin vatanı Rize.",
      "custom_library": "Rize İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Samsun": {
      "plate": 55,
      "name": "Samsun",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 41.2928,
      "lng": 36.3313,
      "landmarks": [
        "Bandırma Vapuru Müzesi",
        "Onur Anıtı",
        "Şahinkaya Kanyonu",
        "Kızılırmak Deltası Kuş Cenneti",
        "Amazon Köyü"
      ],
      "specialties": [
        "Samsun Pidesi (Bafra/Terme)",
        "Nokul",
        "Kaz Tiridi",
        "Mısır Çorbası"
      ],
      "quote": "Milli Mücadele'nin ilk adımının atıldığı istiklal limanı ve Şahinkaya Kanyonu'nun heybetli suları.",
      "library": "Samsun İl Halk Kütüphanesi - Karadeniz'in en modern kütüphanelerinden biri, priz ve internet altyapısı mükemmel.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Samsun/banner.jpg",
      "readme_rel": "05_Karadeniz/Samsun/README.md",
      "slug": "Samsun",
      "content_size": 2340,
      "custom_quote": "Milli Mücadele'nin ilk adımının atıldığı, kurtuluş meşalesinin yandığı vakur ve öncü sahil şehri.",
      "custom_library": "Samsun İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Sinop": {
      "plate": 57,
      "name": "Sinop",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 42.0231,
      "lng": 35.1531,
      "landmarks": [
        "Tarihi Sinop Cezaevi",
        "İnceburun Feneri (Türkiye'nin En Kuzeyi)",
        "Erfelek Tatlıca Şelaleleri",
        "Hamsilos Koyu"
      ],
      "specialties": [
        "Sinop Mantısı (Cevizli)",
        "Nokul",
        "Palamut / Kalkan Balığı"
      ],
      "quote": "Türkiye'nin en kuzey ucu İnceburun, fiyort benzeri Hamsilos Koyu ve Diyojen'in 'Gölge etme başka ihsan istemez' dediği yer.",
      "library": "Sinop Rıza Nur İl Halk Kütüphanesi - Tarihi ve nostaljik ahşap binasıyla zamanda yolculuk hissi veriyor, huzurlu bir çalışma noktası.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Sinop/banner.jpg",
      "readme_rel": "05_Karadeniz/Sinop/README.md",
      "slug": "Sinop",
      "content_size": 2259,
      "custom_quote": "Karadeniz'in en uç noktasında, Hamsilos fiyordu ve tarihi cezaeviyle sükunet bulmuş sakin şehir.",
      "custom_library": "Sinop İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Tokat": {
      "plate": 60,
      "name": "Tokat",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 40.3167,
      "lng": 36.55,
      "landmarks": [
        "Ballıca Mağarası",
        "Tokat Kalesi",
        "Taşhan",
        "Ali Paşa Camii",
        "Mahperi Hatun Kervansarayı",
        "Saat Kulesi"
      ],
      "specialties": [
        "Tokat Kebabı",
        "Tokat Yaprağı (Sarma)",
        "Zile Pekmezi",
        "Çökelekli Katmer"
      ],
      "quote": "Ballıca Mağarası'nın şifalı cüce sarkıtları, 900 adımda 900 yıllık tarihin adımlandığı kadim menzil.",
      "library": "Tokat İl Halk Kütüphanesi - Tarihi hanların gölgesinde huzurlu çalışma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "05_Karadeniz/Tokat/README.md",
      "slug": "Tokat"
    },
    "05_Karadeniz/Trabzon": {
      "plate": 61,
      "name": "Trabzon",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 41.0027,
      "lng": 39.7168,
      "landmarks": [
        "Sümela Manastırı",
        "Ayasofya Camii Müzesi",
        "Uzungöl",
        "Atatürk Köşkü",
        "Boztepe",
        "Vazelon Manastırı"
      ],
      "specialties": [
        "Akçaabat Köftesi",
        "Kuymak",
        "Hamsiköy Sütlacı",
        "Trabzon Ekmeği",
        "Karalahana Çorbası"
      ],
      "quote": "Sarp kayalıklara asılı Sümela Manastırı'nın heybeti, zümrüt yaylalar ve Karadeniz'in hırçın dalgaları.",
      "library": "Trabzon İl Halk Kütüphanesi - Şehir merkezinde vakur bir bina, araştırma ve geliştirme için sessiz odalar sunuyor.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "05_Karadeniz/Trabzon/banner.jpg",
      "readme_rel": "05_Karadeniz/Trabzon/README.md",
      "slug": "Trabzon",
      "content_size": 2526,
      "custom_quote": "Sümela Manastırı'nın dik yamacında yükselen mistik duruşu, Uzungöl'ün sisli doğası ve köklü geçmişiyle Karadeniz'in kalbi.",
      "custom_library": "Trabzon İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "05_Karadeniz/Zonguldak": {
      "plate": 67,
      "name": "Zonguldak",
      "region": "Karadeniz",
      "region_code": "05_Karadeniz",
      "lat": 41.4564,
      "lng": 31.7987,
      "landmarks": [
        "Gökgöl Mağarası",
        "Maden Müzesi",
        "Filyos Kalesi & Antik Kenti",
        "Harmankaya Şelalesi"
      ],
      "specialties": [
        "Uğmaç Çorbası",
        "Malay",
        "Zonguldak Kestanesi"
      ],
      "quote": "Emeğin başkenti, yerin yüzlerce metre altından çıkarılan kara elmasın ve madencilerin vefası.",
      "library": "Zonguldak İl Halk Kütüphanesi - Karadeniz'in sarp kıyısında sakin bir çalışma ortamı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "05_Karadeniz/Zonguldak/README.md",
      "slug": "Zonguldak"
    },
    "06_DoguAnadolu/Agri": {
      "plate": 4,
      "name": "Ağrı",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 39.7191,
      "lng": 43.0503,
      "landmarks": [
        "İshak Paşa Sarayı",
        "Ağrı Dağı (5137m)",
        "Meteor Çukuru",
        "Doğubayazıt Kalesi",
        "Balık Gölü"
      ],
      "specialties": [
        "Abdigör Köftesi",
        "Ağrı Balı",
        "Halis (Helise)"
      ],
      "quote": "Türkiye'nin çatısı Ağrı Dağı ve kartal yuvası gibi ovaya bakan masalsı İshak Paşa Sarayı.",
      "library": "Ağrı İl Halk Kütüphanesi - Ağrı Dağı'nın heybeti karşısında sakin çalışma alanı.",
      "visited": true,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Agri/README.md",
      "slug": "Agri",
      "content_size": 2892,
      "custom_quote": "Türkiye'nin zirvesi Ağrı Dağı'nın heybeti, ovaya kartal yuvası gibi bakan İshak Paşa Sarayı'nın masalsı silüeti ve Doğubayazıt'ın kadim nefesi.",
      "custom_library": "Ağrı İl Halk Kütüphanesi - Sessiz, geniş çalışma masaları ve odaklanmayı artıran vakur bir çalışma ortamı."
    },
    "06_DoguAnadolu/Ardahan": {
      "plate": 75,
      "name": "Ardahan",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 41.1105,
      "lng": 42.7022,
      "landmarks": [
        "Çıldır Gölü (Kışın Donan)",
        "Ardahan Kalesi",
        "Şeytan Kalesi",
        "Atatürk Silüeti (Damal)"
      ],
      "specialties": [
        "Kaşar Peyniri",
        "Ardahan Çiçek Balı",
        "Kaz Eti Yemeği",
        "Hengel"
      ],
      "quote": "Kışın atlı kızakların kaydığı buz tutmuş Çıldır Gölü ve sarp kayalıklara kurulu Şeytan Kalesi.",
      "library": "Ardahan İl Halk Kütüphanesi - Kışın sıcacık soba sıcaklığında, dışarıdaki dondurucu soğuğa inat sessizce kod yazma imkanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Ardahan/README.md",
      "slug": "Ardahan"
    },
    "06_DoguAnadolu/Bingol": {
      "plate": 12,
      "name": "Bingöl",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 38.8854,
      "lng": 40.4983,
      "landmarks": [
        "Yüzen Adalar (Solhan)",
        "Hesarek Kayak Merkezi",
        "Kral Kızı Kalesi",
        "Zağ Mağaraları"
      ],
      "specialties": [
        "Bingöl Balı",
        "Gömme",
        "Mastuva",
        "Löl"
      ],
      "quote": "Turnalar Gölü'ndeki doğa harikası Yüzen Adalar ve dağların bağrında saklı kaynak suları.",
      "library": "Bingöl İl Halk Kütüphanesi - Samimi ve sessiz çalışma ortamı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Bingol/README.md",
      "slug": "Bingol"
    },
    "06_DoguAnadolu/Bitlis": {
      "plate": 13,
      "name": "Bitlis",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 38.4006,
      "lng": 42.1095,
      "landmarks": [
        "Nemrut Krater Gölü & Kalderası",
        "Ahlat Selçuklu Mezarlığı",
        "Bitlis Kalesi",
        "İhlasiye Medresesi",
        "Tarihi Taş Evler"
      ],
      "specialties": [
        "Bitlis Büryan Kebabı",
        "Ahlat Elması",
        "Katıklı Dolma",
        "Karakovan Balı"
      ],
      "quote": "Kubbetü'l-İslam Ahlat'ın ulu mezar taşları ve dünyanın ikinci büyük kalderası Nemrut Krater Gölü.",
      "library": "Bitlis İl Halk Kütüphanesi - Tarihi taş binalar arasında tefekkür dolu araştırma ortamı.",
      "visited": true,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Bitlis/README.md",
      "slug": "Bitlis",
      "content_size": 2938,
      "custom_quote": "Kubbetü'l-İslam Ahlat'ın ulu Selçuklu mezar taşları, Van Gölü'nün turkuaz kıyıları ve dünyanın doğa harikası Nemrut Krater Gölü.",
      "custom_library": "Bitlis İl Halk Kütüphanesi - Tarihi taş binalar arasında sükunet dolu, araştırmaya uygun ortam."
    },
    "06_DoguAnadolu/Elazig": {
      "plate": 23,
      "name": "Elazığ",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 38.681,
      "lng": 39.2264,
      "landmarks": [
        "Harput Kalesi (Süt Kalesi)",
        "Harput Ulu Cami (Eğri Minare)",
        "Hazar Gölü",
        "Keban Baraj Gölü",
        "Meryem Ana Kilisesi"
      ],
      "specialties": [
        "Harput Köftesi",
        "Gömme",
        "Orcik (Cevizli Sucuk)",
        "Çedene Kahvesi"
      ],
      "quote": "Bin yıllık Harput kalesinin vakur duruşu, Gakgoşlar diyarının mertliği ve Hazar Gölü'nün batık şehri.",
      "library": "Elazığ İl Halk Kütüphanesi - Gakgoşlar diyarında modern ve konforlu çalışma odalarıyla geniş bir kütüphane.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "06_DoguAnadolu/Elazig/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Elazig/README.md",
      "slug": "Elazig",
      "content_size": 2319,
      "custom_quote": "Harput Kalesi'nin bin yıllık surları, Hazar Gölü'nün mavi sularıyla Doğu'nun köklü kültür havzası.",
      "custom_library": "Elazig İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "06_DoguAnadolu/Erzincan": {
      "plate": 24,
      "name": "Erzincan",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 39.75,
      "lng": 39.5,
      "landmarks": [
        "Girlevik Şelalesi",
        "Karanlık Kanyon (Kemaliye)",
        "Kemaliye Tarihi Taş Evleri",
        "Ergan Dağı Kayak Merkezi",
        "Terzibaba Türbesi"
      ],
      "specialties": [
        "Erzincan Tulum Peyniri",
        "Kemaliye Lök Tatlısı",
        "Gözleme & Kete"
      ],
      "quote": "Karanlık Kanyon'un Fırat ile yarıştığı heybet, Girlevik Şelalesi'nin çağıltısı ve Terzibaba'nın teslimiyeti.",
      "library": "Erzincan İl Halk Kütüphanesi - Deprem sonrası yenilenen geniş caddelerin ortasında modern ve ferah bir kütüphane.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "06_DoguAnadolu/Erzincan/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Erzincan/README.md",
      "slug": "Erzincan",
      "content_size": 2379,
      "custom_quote": "Girlevik Şelalesi'nin serin suları, Kemaliye Kanyonu'nun dik yamaçlarıyla depremlerden küllerinden doğan şehir.",
      "custom_library": "Erzincan İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "06_DoguAnadolu/Erzurum": {
      "plate": 25,
      "name": "Erzurum",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 39.9043,
      "lng": 41.2679,
      "landmarks": [
        "Çifte Minareli Medrese",
        "Yakutiye Medresesi",
        "Üç Kümbetler",
        "Erzurum Kalesi",
        "Tortum Şelalesi",
        "Palandöken"
      ],
      "specialties": [
        "Cağ Kebabı",
        "Kadayıf Dolması",
        "Erzurum Ketesi",
        "Aşotu Çorbası"
      ],
      "quote": "Dadaşlar diyarı; Selçuklu medreselerinin göğe uzanan çifte minareleri ve İbrahim Hakkı Hazretleri'nin 'Mevla görelim neyler, neylerse güzel eyler' teslimiyeti.",
      "library": "Erzurum Erzurumlu Emrah İl Halk Kütüphanesi - Tarihi dokusuyla dadaşların vakur çalışma disiplinini yansıtan sessiz çalışma limanı.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "06_DoguAnadolu/Erzurum/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Erzurum/README.md",
      "slug": "Erzurum",
      "content_size": 2423,
      "custom_quote": "Palandöken Dağı'nın karlı zirveleri, Çifte Minareli Medrese'nin asil taş kapısıyla Doğu'nun kilit taşı vakur şehir.",
      "custom_library": "Erzurum İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "06_DoguAnadolu/Hakkari": {
      "plate": 30,
      "name": "Hakkari",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 37.5833,
      "lng": 43.7333,
      "landmarks": [
        "Cilo Sat Buzul Gölleri",
        "Meydan Medresesi",
        "Zap Vadisi",
        "Cennet-Cehennem Vadisi",
        "Merga Bütan"
      ],
      "specialties": [
        "Hakkari Çorti Aşı",
        "Doğaba",
        "Yüksekova Kebabı",
        "Cevizli Çörek"
      ],
      "quote": "Cilo Dağları'nın buzul gölleri, binlerce yıllık kaya resimleri ve Zap Suyu'nun hırçın yankısı.",
      "library": "Hakkari İl Halk Kütüphanesi - Zirvelerin gölgesinde sakin çalışma ortamı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Hakkari/README.md",
      "slug": "Hakkari"
    },
    "06_DoguAnadolu/Igdir": {
      "plate": 76,
      "name": "Iğdır",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 39.9196,
      "lng": 44.045,
      "landmarks": [
        "Tuzluca Tuz Mağaraları",
        "Ağrı Dağı Milli Parkı",
        "Ejder Kervansarayı",
        "Karakale Ören Yeri"
      ],
      "specialties": [
        "Bozbaş (Piti)",
        "Taş Köfte",
        "Iğdır Kayısısı",
        "Kete"
      ],
      "quote": "Üç ülkeye sınır, Doğu'nun Çukurova'sı mikroklima cenneti ve Tuzluca'nın yer altı mağaraları.",
      "library": "Iğdır İl Halk Kütüphanesi - Doğu sınırında sakin ve ferah bir çalışma mekanı.",
      "visited": true,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Igdir/README.md",
      "slug": "Igdir",
      "content_size": 2894,
      "custom_quote": "Üç ülkeye sınır açan serhat ovası, Doğu'nun Çukurova'sı mikroklima cenneti ve Tuzluca'nın yer altı kristal mağaraları.",
      "custom_library": "Iğdır İl Halk Kütüphanesi - Şehir merkezinde sakin, aydınlık ve odaklanmayı kolaylaştıran ortam."
    },
    "06_DoguAnadolu/Kars": {
      "plate": 36,
      "name": "Kars",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 40.6167,
      "lng": 43.1,
      "landmarks": [
        "Ani Harabeleri (Binbir Kiliseli Şehir)",
        "Kars Kalesi",
        "Harakani Türbesi",
        "Havariler Kilisesi (Kümbet Camii)",
        "Baltık Mimarisi Evleri"
      ],
      "specialties": [
        "Kars Kaşarı & Gravyeri",
        "Kars Kaz Eti Pilavı",
        "Hangel",
        "Piti (Bozbaş)"
      ],
      "quote": "Ebu'l Hasan Harakani'nin 'Her kim bu kapıya gelirse ekmeğini verin, inancını sormayın' felsefesi ve Ani Harabeleri'nin bin yıllık taşları.",
      "library": "Kars İl Halk Kütüphanesi - Rus döneminden kalma taş binaların mistik havasında, karlar altında kodlama mesaisi yapabileceğiniz sıcak sığınak.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "06_DoguAnadolu/Kars/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Kars/README.md",
      "slug": "Kars",
      "content_size": 2388,
      "custom_quote": "Ani Harabeleri'nin hüzünlü ve görkemli kalıntıları, Rus mimarisi tarihi sokaklarıyla sınır boyunun asil şehri.",
      "custom_library": "Kars İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "06_DoguAnadolu/Malatya": {
      "plate": 44,
      "name": "Malatya",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 38.3552,
      "lng": 38.3095,
      "landmarks": [
        "Arslantepe Höyüğü (UNESCO)",
        "Battalgazi Ulu Cami",
        "Silahtar Mustafa Paşa Kervansarayı",
        "Levent Vadisi Seyir Terası",
        "Günpınar Şelalesi"
      ],
      "specialties": [
        "Malatya Kayısısı",
        "Analı Kızlı",
        "Kayıslı Kavurma",
        "Kiraz Yaprağı Köftesi",
        "Kömbe"
      ],
      "quote": "Dünyanın ilk kerpiç sarayına ev sahipliği yapan Arslantepe, Battalgazi'nin yiğitliği ve kayısı bahçelerinin bereketi.",
      "library": "Malatya İl Halk Kütüphanesi - Şehir merkezinde yer alan, geniş araştırma kaynakları ve rahat çalışma alanları sunan yerleşke.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "06_DoguAnadolu/Malatya/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Malatya/README.md",
      "slug": "Malatya",
      "content_size": 2430,
      "custom_quote": "Arslantepe Höyüğü ile devletleşmenin ilk adımlarına tanıklık eden, kayısının ve bereketli ovaların şehri.",
      "custom_library": "Malatya İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "06_DoguAnadolu/Mus": {
      "plate": 49,
      "name": "Muş",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 38.7432,
      "lng": 41.5064,
      "landmarks": [
        "Tarihi Murat Köprüsü",
        "Muş Kalesi",
        "Arak Manastırı",
        "Malazgirt Zafer Anıtı (Meydan Muharebesi Tarihi Milli Parkı)"
      ],
      "specialties": [
        "Muş Köftesi",
        "Hafta Direği",
        "Tırşık",
        "Muş Çortisi"
      ],
      "quote": "1071 Malazgirt Zaferi ile Anadolu'nun kapılarının İslam'a ve Türklere açıldığı şanlı menzil ve Murat Nehri.",
      "library": "Muş İl Halk Kütüphanesi - Tarihin başladığı ovada sessiz ve sakin çalışma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Mus/README.md",
      "slug": "Mus"
    },
    "06_DoguAnadolu/Tunceli": {
      "plate": 62,
      "name": "Tunceli",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 39.1079,
      "lng": 39.5401,
      "landmarks": [
        "Munzur Vadisi Milli Parkı",
        "Munzur Gözeleri",
        "Pertek Kalesi",
        "Düzgün Baba Türbesi",
        "Pülümür Vadisi & Ağlayan Kayalar"
      ],
      "specialties": [
        "Şavak Tulum Peyniri",
        "Munzur Balı",
        "Zerefet (Babiko)",
        "Gömme"
      ],
      "quote": "Munzur Suyu'nun berrak gözeleri, doğaya ve canlıya hürmetle bakan irfan geleneği ve sarp kanyonlar.",
      "library": "Tunceli İl Halk Kütüphanesi - Munzur nehrinin esintisiyle serinleyen, sessiz çalışma ortamı ve güler yüzlü çalışanlarıyla butik kütüphane.",
      "visited": true,
      "has_banner": true,
      "banner_rel": "06_DoguAnadolu/Tunceli/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Tunceli/README.md",
      "slug": "Tunceli",
      "content_size": 2424,
      "custom_quote": "Munzur Vadisi'nin hırçın suları, Ovacık Gözeleri'nin kutsal kaynaklarıyla doğanın en el değmemiş mistik coğrafyası.",
      "custom_library": "Tunceli İl Halk Kütüphanesi - Sessiz, çalışma disiplinine uygun, internet imkanı sunan verimli bir ilim yuvası."
    },
    "06_DoguAnadolu/Van": {
      "plate": 65,
      "name": "Van",
      "region": "Doğu Anadolu",
      "region_code": "06_DoguAnadolu",
      "lat": 38.4891,
      "lng": 43.4089,
      "landmarks": [
        "Akdamar Adası ve Kilisesi",
        "Van Kalesi",
        "Van Gölü (Van Denizi)",
        "Muradiye Şelalesi",
        "Hoşap Kalesi",
        "Çavuştepe Urartu Kalesi"
      ],
      "specialties": [
        "Van Kahvaltısı",
        "Otlu Peynir",
        "İnci Kefali",
        "Sengeser",
        "Kavut"
      ],
      "quote": "Urartu krallarının taht kurduğu Van Kalesi, sodalı masmavi Van Denizi ve Akdamar Adası'nın badem çiçekleri.",
      "library": "Van İl Halk Kütüphanesi - Van Gölü manzarasına yakın, geniş çalışma alanlarına sahip modern kütüphane.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "06_DoguAnadolu/Van/README.md",
      "slug": "Van"
    },
    "07_GuneydoguAnadolu/Adiyaman": {
      "plate": 2,
      "name": "Adıyaman",
      "region": "Güneydoğu Anadolu",
      "region_code": "07_GuneydoguAnadolu",
      "lat": 37.7648,
      "lng": 38.2786,
      "landmarks": [
        "Nemrut Dağı Heykelleri (Gündoğumu/Batımı)",
        "Cendere Köprüsü",
        "Arsemia Ören Yeri",
        "Karakuş Tümülüsü",
        "Perre Antik Kenti"
      ],
      "specialties": [
        "Adıyaman Çiğ Köftesi",
        "Besni Tavası",
        "Meyir Çorbası",
        "Buhara Pilavı"
      ],
      "quote": "Kommagene Krallığı'nın tanrı heykelleriyle bezeli Nemrut Zirvesi ve güneşin en görkemli doğup battığı taht.",
      "library": "Adıyaman İl Halk Kütüphanesi - Nemrut'un gölgesinde huzurlu çalışma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "07_GuneydoguAnadolu/Adiyaman/README.md",
      "slug": "Adiyaman"
    },
    "07_GuneydoguAnadolu/Batman": {
      "plate": 72,
      "name": "Batman",
      "region": "Güneydoğu Anadolu",
      "region_code": "07_GuneydoguAnadolu",
      "lat": 37.8812,
      "lng": 41.1294,
      "landmarks": [
        "Hasankeyf Tarihi Kenti",
        "Zeynel Bey Türbesi",
        "Malabadi Köprüsü",
        "Mor Kiryakus Manastırı"
      ],
      "specialties": [
        "Batman Kütülk (İçli Köfte)",
        "Şam Börek",
        "Tırşık",
        "Hevra Ekmeği"
      ],
      "quote": "Dicle Nehri'nin bağrından doğan 12 bin yıllık Hasankeyf mağaraları ve Zeynel Bey Türbesi'nin turkuaz çinileri.",
      "library": "Batman İl Halk Kütüphanesi - Dicle kıyısında modern çalışma salonları.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "07_GuneydoguAnadolu/Batman/README.md",
      "slug": "Batman"
    },
    "07_GuneydoguAnadolu/Diyarbakir": {
      "plate": 21,
      "name": "Diyarbakır",
      "region": "Güneydoğu Anadolu",
      "region_code": "07_GuneydoguAnadolu",
      "lat": 37.9144,
      "lng": 40.2306,
      "landmarks": [
        "Diyarbakır Surları (UNESCO)",
        "Hevsel Bahçeleri",
        "Ulu Cami (İslam'ın 5. Harem-i Şerifi)",
        "On Gözlü Köprü",
        "Dört Ayaklı Minare",
        "Cahit Sıtkı Tarancı Müzesi"
      ],
      "specialties": [
        "Diyarbakır Ciğeri",
        "Kaburga Dolması",
        "Burma Kadayıf",
        "Diyarbakır Karpuzu",
        "Meftune"
      ],
      "quote": "Kara bazalt taşlı asırlık surlar, sahabe mezarları ve İslam aleminin 5. Harem-i Şerifi sayılan Ulu Camii.",
      "library": "Diyarbakır İl Halk Kütüphanesi / Sur İlçe Kütüphanesi - Tarihi surların gölgesinde kadim bilgi ocağı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "07_GuneydoguAnadolu/Diyarbakir/README.md",
      "slug": "Diyarbakir"
    },
    "07_GuneydoguAnadolu/Gaziantep": {
      "plate": 27,
      "name": "Gaziantep",
      "region": "Güneydoğu Anadolu",
      "region_code": "07_GuneydoguAnadolu",
      "lat": 37.0662,
      "lng": 37.3833,
      "landmarks": [
        "Zeugma Mozaik Müzesi (Çingene Kızı)",
        "Gaziantep Kalesi",
        "Bakırcılar Çarşısı",
        "Tahmis Kahvesi",
        "Rumkale"
      ],
      "specialties": [
        "Gaziantep Baklavası",
        "Ali Nazik",
        "Beyran Çorbası",
        "Katmer",
        "Küşleme",
        "Menengiç Kahvesi"
      ],
      "quote": "UNESCO Gastronomi Şehri; Zeugma'nın Çingene Kızı mozaiğinin derin bakışları ve asırlık hanların kahve kokusu.",
      "library": "Gaziantep İl Halk Kütüphanesi / Hasan Celal Güzel Kütüphanesi - Modern donanımlı ve dinamik çalışma atmosferi.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "07_GuneydoguAnadolu/Gaziantep/README.md",
      "slug": "Gaziantep"
    },
    "07_GuneydoguAnadolu/Kilis": {
      "plate": 79,
      "name": "Kilis",
      "region": "Güneydoğu Anadolu",
      "region_code": "07_GuneydoguAnadolu",
      "lat": 36.7184,
      "lng": 37.1212,
      "landmarks": [
        "Ravanda Kalesi",
        "Oylum Höyük",
        "Kilis Tarihi Taş Evleri ve Kabaltıları",
        "Ulu Cami"
      ],
      "specialties": [
        "Kilis Tavası",
        "Cennet Çamuru Tatlısı",
        "Kilis Katmeri",
        "Zeytinyağı"
      ],
      "quote": "Zeytin ağaçlarının gölgesinde kadim kabaltılı sokaklar, lezzetli Kilis Tavası ve sınır boyunun sıcak insanları.",
      "library": "Kilis İl Halk Kütüphanesi - Samimi ve sessiz çalışma ortamı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "07_GuneydoguAnadolu/Kilis/README.md",
      "slug": "Kilis"
    },
    "07_GuneydoguAnadolu/Mardin": {
      "plate": 47,
      "name": "Mardin",
      "region": "Güneydoğu Anadolu",
      "region_code": "07_GuneydoguAnadolu",
      "lat": 37.3212,
      "lng": 40.7245,
      "landmarks": [
        "Mardin Taş Evleri",
        "Deyrulzafaran Manastırı",
        "Kasımiye Medresesi",
        "Mardin Ulu Cami",
        "Dara Antik Kenti",
        "Midyat Konukevi"
      ],
      "specialties": [
        "Mardin Kebabı",
        "Sembusek",
        "İrok (Mardin İçli Köftesi)",
        "Süryani Şarabı/Çöreği",
        "Mavi Badem Şekeri"
      ],
      "quote": "Gündüzü seyran, gecesi gerdanlık; Mezopotamya ovasına tepeden bakan sarı kalker taşlı masal diyarı.",
      "library": "Mardin İl Halk Kütüphanesi - Taş mimarisi ve Mezopotamya ovasına bakan avlusuyla seyyah yazılımcıya ilham kaynağı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "07_GuneydoguAnadolu/Mardin/README.md",
      "slug": "Mardin"
    },
    "07_GuneydoguAnadolu/Siirt": {
      "plate": 56,
      "name": "Siirt",
      "region": "Güneydoğu Anadolu",
      "region_code": "07_GuneydoguAnadolu",
      "lat": 37.9333,
      "lng": 41.95,
      "landmarks": [
        "İsmail Fakirullah & İbrahim Hakkı Türbesi (Işık Hadisesi - Tillo)",
        "Veysel Karani Türbesi",
        "Siirt Ulu Cami",
        "Rasıl Hacar (Delikli Taş)"
      ],
      "specialties": [
        "Büryan Kebabı",
        "Perde Pilavı",
        "Siirt Fıstığı",
        "Tayfi Üzümü"
      ],
      "quote": "İlim ve irfan beldesi Tillo'daki güneş hadisesi, Veysel Karani Hazretleri'nin aşkı ve sarp Botan Kanyonu.",
      "library": "Siirt İl Halk Kütüphanesi - Tillo'nun manevi atmosferinde sakin çalışma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "07_GuneydoguAnadolu/Siirt/README.md",
      "slug": "Siirt"
    },
    "07_GuneydoguAnadolu/Sanliurfa": {
      "plate": 63,
      "name": "Şanlıurfa",
      "region": "Güneydoğu Anadolu",
      "region_code": "07_GuneydoguAnadolu",
      "lat": 37.1674,
      "lng": 38.7938,
      "landmarks": [
        "Göbeklitepe (Tarihin Sıfır Noktası)",
        "Balıklıgöl (Halil-ür Rahman)",
        "Şanlıurfa Kalesi",
        "Harran Kümbet Evleri",
        "Karahantepe",
        "Gümrük Hanı"
      ],
      "specialties": [
        "Urfa Kebabı",
        "Çiğ Köfte",
        "Lahmacun",
        "Şıllık Tatlısı",
        "Mırra",
        "Borani"
      ],
      "quote": "Peygamberler şehri; Hz. İbrahim'in ateşinin gül bahçesine dönüştüğü Balıklıgöl ve insanlık tarihinin sıfır noktası Göbeklitepe.",
      "library": "Şanlıurfa İl Halk Kütüphanesi - Peygamberler şehrinde zengin araştırma kaynakları.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "07_GuneydoguAnadolu/Sanliurfa/README.md",
      "slug": "Sanliurfa"
    },
    "07_GuneydoguAnadolu/Sirnak": {
      "plate": 73,
      "name": "Şırnak",
      "region": "Güneydoğu Anadolu",
      "region_code": "07_GuneydoguAnadolu",
      "lat": 37.5164,
      "lng": 42.4594,
      "landmarks": [
        "Cudi Dağı (Hz. Nuh'un Gemisi)",
        "Kırmızı Medrese (Cizre)",
        "Mem û Zîn Türbesi",
        "İsmail Ebul-İz El-Cezeri Türbesi",
        "Kasrik Boğazı"
      ],
      "specialties": [
        "Kutlık",
        "Serbıdev",
        "Hekeheşandi",
        "Suryaz"
      ],
      "quote": "Hz. Nuh'un gemisinin oturduğu Cudi Dağı, sibernetiğin kurucusu El-Cezeri'nin memleketi ve Mem û Zîn destanı.",
      "library": "Şırnak İl Halk Kütüphanesi - Cudi eteklerinde sessiz ve düzenli çalışma alanı.",
      "visited": false,
      "has_banner": false,
      "banner_rel": "assets/banner.jpg",
      "readme_rel": "07_GuneydoguAnadolu/Sirnak/README.md",
      "slug": "Sirnak"
    }
  }
};
