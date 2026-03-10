import os

VISITED_DEEP_DETAILS = {
    "Istanbul": {
        "hikmet": "İstanbul bir ayna gibidir; ona yüzünü dönen, zamanın ve tarihin kalbinde kendi yansımasını görür.",
        "quote": "\"İmparatorlukların ebediyete karıştığı, taşın ve denizin şiir yazdığı yedi tepeli masal.\"",
        "description": "Dünyanın gözbebeği, asırlık payitaht. Topraklarında barındırdığı medeniyetlerin nefesini her sokağında hissettiren bu kadim şehir, asla uyumayan bir deryadır. Ayasofya'nın kubbesinden süzülen solgun bir ışık, Galata'nın rutubetli taşları, Boğaz'ın hırçın rüzgarına karışan eski zaman fısıltıları... İstanbul aceleyle gezilecek bir yer değil; durup kulak verilecek, derin bir nefesle içe çekilecek devasa bir roman gibidir.",
        "sufi_notes": "İstanbul'un sokaklarında kaybolmak, aslında kendini bulmanın bir yoludur. Buradaki her kalıntı bize zamanın ne kadar hızlı ve acımasız aktığını; ancak yaşanmışlıkların, sanatın ve estetiğin asırlarca kalplere nasıl dokunduğunu hatırlatır.",
        "landmarks": ["Ayasofya", "Topkapı Sarayı", "Galata Kulesi", "Süleymaniye Camii", "Yerebatan Sarnıcı"]
    },
    "Konya": {
        "hikmet": "Susuzluktan kuruyan bozkırı yeşerten yağmur değil, gönülden kopan sevginin pınarıdır.",
        "quote": "\"Rüzgârın en hafif estiği, sarı buğday başakları arasında sükunetin demlendiği diyar.\"",
        "description": "Çöllerin ortasında bir vaha gibi duran, yalnızlığın ve dinginliğin başkenti. Dışarıdan bakıldığında sessiz, sert ve kurak görünen bu bozkır, içine girildiğinde eşsiz bir hoşgörü ve estetik barındırır. Sarının her tonunu barındıran ovaları, güneş batarken insana dünyanın karmaşasını unutturur.",
        "sufi_notes": "Konya'da rüzgârı dinlemek, insanın kendi gürültüsünden kaçıp sükunetini bulması gibidir. Burada göğe uzanan sadece minareler değil; sevgiyle, estetikle ve tevazuyla yükselen bir kültürün kökleridir.",
        "landmarks": ["Mevlana Müzesi", "Alaeddin Tepesi", "Karatay Medresesi", "Sille Köyü", "Meke Gölü"]
    },
    "Bursa": {
        "hikmet": "Dağın yüceliği zirvesinden değil, eteklerindeki çınarlara verdiği hayattan gelir.",
        "quote": "\"Suyun sesine karışan çınar yapraklarının, bir çınarın gölgesinde büyüyen medeniyetin beşiği.\"",
        "description": "Uludağ'ın eteklerine yaslanmış, yeşiliyle ve suyuyla nefes alan asil şehir. Her köşebaşından bir çeşme sesi gelir; her sokakta tarihin ahşap ve taşlarla ilmek ilmek işlenmiş bir sükuneti vardır. Bursa, doğa ile insanın en zarif şekilde uyumlandığı kadim bir huzur yuvasıdır.",
        "sufi_notes": "Ulu bir çınarın altında oturup dinlenmek, kök salmanın ve sabrın gücünü öğretir. Bursa, ne kadar büyürse büyüsün, o ilk toprağa düşen tohumun tevazusunu hep koruması gerektiğini fısıldar.",
        "landmarks": ["Ulu Cami", "Tarihi İnkaya Çınarı", "Yeşil Türbe", "Koza Han", "Cumalıkızık"]
    },
    "Ankara": {
        "hikmet": "Taşa ve yokluğa karşı dikilen bir irade, en güçlü çelikten daha serttir.",
        "quote": "\"Yorgun bir bozkırda imkansızın nasıl başardığını haykıran, vakur ve kararlı başkent.\"",
        "description": "Anadolu'nun kalbi, Friglerden günümüz Cumhuriyetine uzanan, daima ayakta kalmanın direncini simgeleyen şehir. Güçlü ayazı insanın tenini sıyırırken, sokaklarındaki ciddiyet ve kararlılık ruhu ateşler. Görkemli binaların veya parıltının değil; emeğin, kararlılığın ve inancın merkezidir.",
        "sufi_notes": "Ankara bize zorluklara karşı dik durmayı öğretir. Hiçbir şeyin kolay verilmediği bu topraklarda atılan her temel, inancın imkansızlıkları nasıl yarıp geçtiğine dair sessiz bir derstir.",
        "landmarks": ["Anıtkabir", "Ankara Kalesi", "Anadolu Medeniyetleri Müzesi", "Atakule", "Kuğulu Park"]
    },
    "Amasya": {
        "hikmet": "Kayaya kazınan en büyük iz güç değil, suların getirdiği yaşamdır.",
        "quote": "\"Nehrin ikiye böldüğü, kralların gölgesiyle dağların şarkısının birbirine karıştığı vadi.\"",
        "description": "Yeşilırmak'ın nazlı nazlı aktığı dar bir vadiye gizlenmiş masal şehri. Nehrin iki yakasındaki yalıboyu evleri, onların üstüne yükselen hırçın kayalar ve bu kayalara kazınmış antik mezarlar... Amasya, nehrin ritmiyle tarihin donup kaldığı efsunlu bir seyir terasıdır.",
        "sufi_notes": "Bir dağın sinesine kazınmış o kocaman mezarlar bile zamanın karşısında ufalanır; fakat o ırmak asırlardır hep aynı türküyü söyler. İnsana kalıcı olanın kibir ve güç değil, doğanın bitimsiz akışı olduğunu anlatır.",
        "landmarks": ["Kral Kaya Mezarları", "Amasya Kalesi", "Yalıboyu Evleri", "Ferhat ile Şirin Aşıklar Müzesi"]
    },
    "Corum": {
        "hikmet": "Medeniyet kılıçla kurulsa da, yalnızca masaya barışın mührü basıldığında yücelir.",
        "quote": "\"Taş tabletlerin arasında yankılanan ilk barışın, bereketli topraklardaki unutulmaz izi.\"",
        "description": "Hititlerin kadim güneşi altında yıkanan, bereketin ve tarihin toprakları. Çorum, gösterişten uzak tepelerinde binlerce yıllık bir miras saklar. Hattuşaş'ın yıkıntıları arasında yürürken duyulan tek ses, toprağın ve rüzgarın binlerce yıllık şahitliğidir.",
        "sufi_notes": "Krallar unutulur, surlar yıkılır, ama insanlık tarihine düşülen 'barış' notu sonsuza kadar toprağın hafızasında kalır. Gücün ardındaki zarafet ve barışın kıymeti, bu harabelerde yatar.",
        "landmarks": ["Hattuşaş Antik Kenti", "Alacahöyük", "Çorum Müzesi", "Yazılıkaya", "Şapinuva"]
    },
    "Samsun": {
        "hikmet": "En hırçın fırtınalarda uyanan irade, dalgaları uysallaştıran tek pusuladır.",
        "quote": "\"Kurtuluşa atılan o ilk sağlam adımın, denizin tuzuna karışıp bir milleti dirilttiği liman.\"",
        "description": "Karadeniz'in deli dalgalarına karşı hep bir fener gibi durmuş, umudun limanı. Dağlardan denize doğru uzanan yemyeşil tepelerin ve hırçın Karadeniz sahilinin tam ortasında bir direniş şehridir. Rüzgar burada her zaman bağımsızlığı fısıldar.",
        "sufi_notes": "Bazen gitmek değil, tam aksine dalgaların üzerine doğru 'ilk adımı' atmak gerekir. Hayattaki tüm korku ve engeller, insanın karar verip bir adım atmasıyla aşılmaya başlanır.",
        "landmarks": ["Onur Anıtı", "Bandırma Vapuru", "Amisos Tepesi", "Amazon Köyü"]
    },
    "Sinop": {
        "hikmet": "En karanlık zindan dört duvar arası değil, insanın kendi kendine ördüğü sınırlardır.",
        "quote": "\"Hırçın Karadeniz ile huzurlu limanın buluştuğu, kendi gölgesiyle baş başa kalan yarımada.\"",
        "description": "Gölgelerin ve dinginliğin şehri. Anadolu'nun en kuzey ucu, dalgaların duvarları dövdüğü, ormanın adeta denize döküldüğü efsanevi yarımada. Dar sokaklarında deniz kokusu ve rüzgar hiç eksik olmaz. Hem bir inziva köşesi hem de doğal bir hapishane kadar izole ve vakurdur.",
        "sufi_notes": "Tarihi cezaevinin ürpertici havası ve soğuk duvarları, özgürlüğün değerini; dışarıdaki uçsuz bucaksız deniz ise insanın içindeki sonsuzluk tutkusunu temsil eder.",
        "landmarks": ["Tarihi Sinop Cezaevi", "Sinop Kalesi", "Hamsilos Tabiat Parkı", "Erfelek Şelaleleri"]
    },
    "Giresun": {
        "hikmet": "Dalgaların dövdüğü kayalar ne kadar sarp ise, dalların verdiği meyveler o kadar tatlıdır.",
        "quote": "\"Yeşilin en koyusunun, denizin en mavisinin sonsuz bir hasretle kucaklaştığı yer.\"",
        "description": "Ormanın denize paralel bir sükunetle uzandığı, sislerin ardında gizli kalmış güzellik. Yaylalarındaki serin rüzgarlar ciğerlere hayat basarken, o dik yamaçlarda yeşeren doğa insan emeğinin en güzel karşılığını verir.",
        "sufi_notes": "Doğadaki zorluk ve enginlik, sabırla yoğrulduğunda en tatlı meyvelerini sunar. İnsan doğanın bu inatçı ama verimli karakterine bakıp kendi içindeki çetin mücadelelerin sonunun da huzura çıkacağını idrak edebilir.",
        "landmarks": ["Giresun Kalesi", "Kuzalan Şelalesi", "Mavi Göl", "Giresun Adası"]
    },
    "Ordu": {
        "hikmet": "Göğe ne kadar yükselir ve yeryüzüne şefkatle bakarsan, yollar o kadar aydınlanır.",
        "quote": "\"Bulutların üzerine kurulan tahtından, Karadeniz'in dantel gibi örülmüş kıyılarını izleyen şehir.\"",
        "description": "Boztepe'den bakıldığında ayakların atında uzanan muazzam manzaranın şehri. Yaylalarının uçsuz bucaksız sisli tepeleri, kıyıların eşsiz sükunetiyle birleşir. Dağların omuzlarında kurulu bu şehir, Karadeniz'in en nazlı ve narin çocuklarından biridir.",
        "sufi_notes": "Yüksek bir tepeden o uçsuz bucaksız denize ve yeşile bakmak, insanın dünyanın ne kadar devasa, kendisinin ise ne kadar narin bir zerreden ibaret olduğunu anlaması için yeterlidir.",
        "landmarks": ["Boztepe", "Yason Burnu", "Perşembe Yaylası", "Kurul Kalesi"]
    },
    "Kocaeli": {
        "hikmet": "Emeğin işlediği demir pas tutmaz; yorgunluk, yeni bir inşanın umut kıvılcımıdır.",
        "quote": "\"Fabrika bacalarından tüten umutlarla tarihin sulara bıraktığı mirasın beraber yeşerdiği diyar.\"",
        "description": "Denizin kıyısında, köprülerin ağzında, demirin ve ateşin şekillendiği büyük endüstri başkenti. Dışarıdan sadece sanayi görünse de, kıyılarında ve dağ eteklerinde doğanın ve tarihin en sakin köşelerini barındırır. Emek ve üretimin dinmez ritmidir.",
        "sufi_notes": "Çarkların, çekiçlerin ve koca fabrikaların sesi, aslında insan aklının ve emeğinin birer senfonisidir. Hiçbir şey emeksiz şekillenmez, demir bile önce ateşe sabırla dayanmalıdır.",
        "landmarks": ["Sekapark", "Kartepe", "İzmit Saat Kulesi", "Osman Hamdi Bey Evi"]
    },
    "Antalya": {
        "hikmet": "Sonsuz maviliğin ufku, geçmişi hatırlar ancak daima yarına daha umutla bakar.",
        "quote": "\"Kayalıklarına çarpıp geri çekilen suların, asırların mirasını şefkatle yıkadığı cennet kıyı.\"",
        "description": "Akdeniz'in vitrini; güneşi, tarihi ve doğayı cömertçe kucaklayan sıcak coğrafya. Bir yanda Torosların heybeti, diğer yanda insanın ruhunu yatıştıran engin mavi. Kaleiçi'nin dar ve nostaljik sokaklarında yürürken, antik krallıkların ayak seslerini ve yorgun denizcilerin rahat nefesini hissedersiniz.",
        "sufi_notes": "Güneyin bu kızgın güneşi ve tatlı tuzlu suyu, bedeni yorarken zihni tazeler. Her kalıntı, geçmiş zamanın telaşının ne denli boş olduğunu, asıl gerçeğin anı yaşamak (Carpe diem'in en samimi hali) olduğunu fısıldar.",
        "landmarks": ["Kaleiçi", "Hadrian Kapısı", "Olympos Antik Kenti", "Phaselis", "Kurşunlu Şelalesi"]
    },
    "Denizli": {
        "hikmet": "Sabırla süzülen küçük su damlaları, asırlar içinde en sert kayaları bile beyaz bir pamuğa döndürür.",
        "quote": "\"Yeraltından fışkıran sıcağın sanata, antik zamanların ise derin bir sessizliğe dönüştüğü o eşsiz coğrafya.\"",
        "description": "Pamuk gibi görünen travertenlerin bembeyaz şefkati ve Hierapolis'in o büyüleyici devasa kalıntıları. Toprağın altında kaynayan şifalı sular, yeryüzüne çıktığında muazzam bir doğa heykeli inşa eder. Denizli, tabiatın en zarif işçiliğini sergilediği bir sanat atölyesidir.",
        "sufi_notes": "Travertenleri oluşturan o damlalar bize 'damlaya damlaya göl olur' değil; 'damlaya damlaya mucizeler doğar' der. Her büyük güzelliğin ardında asırlık bir sabır ve yavaş ama tükenmez bir gayret yatar.",
        "landmarks": ["Pamukkale Travertenleri", "Hierapolis Antik Kenti", "Laodikeia", "Karahayıt Suları"]
    }
}

REGIONS_MAP = {
    "01_Marmara": ["Istanbul", "Kocaeli", "Bursa"],
    "02_Ege": ["Denizli"],
    "03_Akdeniz": ["Antalya"],
    "04_IcAnadolu": ["Ankara", "Konya"],
    "05_Karadeniz": ["Amasya", "Corum", "Samsun", "Sinop", "Giresun", "Ordu"]
}

def enrich_visited():
    for region, cities in REGIONS_MAP.items():
        if not os.path.exists(region):
            continue
        
        # Match exact folder names in the directory
        actual_folders = os.listdir(region)
        
        for folder in actual_folders:
            clean_city = folder.strip()
            # If standard ascii matching
            lookup_key = clean_city
            if clean_city == "İstanbul": lookup_key = "Istanbul"
            if clean_city == "Çorum": lookup_key = "Corum"
            
            if lookup_key in VISITED_DEEP_DETAILS:
                
                details = VISITED_DEEP_DETAILS[lookup_key]
                file_path = os.path.join(region, folder, "README.md")
                
                content = f"# 📍 {clean_city} - Seyahat ve Tefekkür Notları\n\n"
                content += f"## 📜 Şehrin Ruhu\n> \"{details['hikmet']}\"\n"
                content += f"> {details['quote']}\n\n"
                content += f"### 🌍 Şehrin Dokusu ve Hatırası\n{details['description']}\n\n"
                content += f"### 🕊️ Gezginin Not Defterinden (İçsel Düşünceler)\n{details['sufi_notes']}\n\n"
                content += "### ✨ Keşfedilesi Duraklar\nBu şehrin havasını solumak, ruhuna dokunmak için mutlaka adımlanması gereken köşe taşları:\n"
                
                for loc in details['landmarks']:
                    content += f"- [ ] **{loc}**\n"
                    
                content += "\n---\n*Bu il bizzat deneyimlenmiş, yolları aşındırılmış ve seyahatnameye sevgiyle işlenmiştir.* ✅\n"
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Deeply enriched: {file_path}")

if __name__ == "__main__":
    enrich_visited()
