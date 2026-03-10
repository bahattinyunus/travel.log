import os

VISITED_DEEP_DETAILS = {
    "Istanbul": {
        "hikmet": "İstanbul, iki kıtayı birbirine diken altın bir iğne gibidir.",
        "quote": "\"İki denizin birleştiği yer... Hem Doğu'nun kalbini hem Batı'nın aklını cem eden eşsiz bir metropol.\"",
        "description": "Dünyanın gözbebeği, asırlık payitaht. Hem ihtişamı hem de tarihi derinliğiyle gezginlerin vazgeçilmezi. Topraklarında barındırdığı sayısız medeniyetin iziyle ayakta duran bu kadim şehir, her sokağında ayrı bir sır fısıldar. Ayasofya'nın kubbesinden süzülen ışıkta tarihin ağırlığını, Galata'nın dar sokaklarında zamanın akışını duyarsınız. Boğaz'ın suları, adeta şehrin hiç bitmeyen enerjisini yansıtan bir ayna gibidir. Gündüzü telaşla geçerken, gecesi derin bir felsefi sükunete erer.",
        "sufi_notes": "İstanbul'u layıkıyla gezmek, sadece taşını toprağını görmek değil, üzerine sinmiş tarihi hissetmektir. Tarihi yarımadada yürürken asırların ne kadar çabuk geçtiğini düşünmek ve her taşı yontanın bıraktığı mirası anlamaktır.",
        "landmarks": ["Ayasofya", "Topkapı Sarayı", "Galata Kulesi", "Süleymaniye Camii"]
    },
    "Konya": {
        "hikmet": "Gel, ne olursan ol yine gel... Ama buraya anlamaya gel.",
        "quote": "\"Felsefenin ve hoşgörünün harmanlandığı, bilgeliğin toprakla buluştuğu yer.\"",
        "description": "Hoşgörünün merkezi, bilgelerin yurdu. Selçuklu'nun başkenti olan bu kadim şehir, sadece tarihi eserleriyle değil, derin felsefik mirasıyla da kalpleri celbeder. Çöllerin ortasında bir vaha gibi, kültürel kuraklığı çeken zihinleri serinleten bir havzadır. Geçmişten fısıldanan sevgi ve hoşgörü, asırlardır bu şehrin sokaklarına yayılmıştır.",
        "sufi_notes": "Konya'da atılan her adım, barış ve bilgeliğin izinde atılmış bir adımdır. Müze ve medrese ziyaretleri sadece bir mekanı görmek değil, evrensel insanlık değerlerini özümsemenin bir yoludur.",
        "landmarks": ["Mevlana Müzesi", "Şems-i Tebrizi Anıtı", "Karatay Medresesi", "İnce Minareli Medrese"]
    },
    "Bursa": {
        "hikmet": "Bursa'da zaman, bir eski çınar gölgesinde sükutla geçer.",
        "quote": "\"İmparatorlukların doğuşuna tanıklık etmiş, her taşında emeğin ve tarihin izi olan topraklar.\"",
        "description": "Yeşilin ve tarihin şehri, Osmanlı'nın ilk asil başkenti. Uludağ'ın eteklerine bir inci gerdanlık gibi dizilmiş olan bu şehir, yeşilin her tonunu barındırdığı gibi, zihnin de her türlü dinginliğine ev sahipliği yapar. Ulu Cami'nin o haşmetli mimarisi, şehrin tarihi çarşılarından yayılan çekiç sesleriyle birleşir. Bursa, metropolün gürültüsünden sıyrılıp doğayla ve tarihle baş başa kalmanın adresidir.",
        "sufi_notes": "Bursa sokaklarında yürümek, bir cihan sahnnesinin kuruluşunu tefekkür etmektir. Su sesleriyle uyanıp, rüzgarın taşıdığı ipek kokusuyla uykuya dalar bu şehrin konukları.",
        "landmarks": ["Ulu Cami", "Tarihi Çınar", "Yeşil Türbe", "Koza Han", "Muradiye Külliyesi"]
    },
    "Ankara": {
        "hikmet": "Bir milleti inşa eden irade, bu bozkırın tam kalbinde atar.",
        "quote": "\"Taşın ve toprağın asil bir direnişle, yepyeni bir ülkeye dönüştüğü o kararlı merkez.\"",
        "description": "Anadolu'nun kalbi, Cumhuriyet'in başkenti. Ankara sadece siyasetin değil, asırlardır süregelen kültürel bir direnişin de merkezidir. Kalenin eteklerinden süzülen o eski zaman kokusu, modern caddelerin telaşına karışır. Augustus Tapınağı ile yan yana duran eski evler, bu topraklardaki çok kültürlü mozaikin en somut yüzüdür.",
        "sufi_notes": "Ankara, zorluklardan nasıl yeni bir başlangıç çıkarılabileceğinin yeryüzündeki kanıtıdır. Şehre bakan her gezgin, yıkıntılardan yükselen bir milletin azmini kalbine kazımalıdır.",
        "landmarks": ["Anıtkabir", "Ankara Kalesi", "Anadolu Medeniyetleri Müzesi", "Tarihi TBMM Binası"]
    },
    "Amasya": {
        "hikmet": "Dağları delmek zordur ama zamanı anlamak daha zordur.",
        "quote": "\"Kayaların nehrin akışını sessizce izlediği, efsanelerin taşa kazındığı vadi.\"",
        "description": "Şehzadeler şehri, epik hikayelerin diyarı. Yeşilırmak'ın aynasında tarihini izleyen kent. Amasya vadinin içine gizlenmiş, sırlarını sadece ona gönül verenlere açan mütavazı bir şehirdir. Akşamları kayalara oyulmuş mezarlara vuran ışıklarla aydınlanan şehir, insanın doğa karşısındaki çabasının muazzam bir tezatını sunar.",
        "sufi_notes": "Amasya'da Ferhat'ın Şirin'e duyduğu aşkın aslında insanın bir gaye uğruna neleri feda edebileceğinin öyküsü olduğunu tefekkür etmek gerekir. Yalıboyu evlerindeki ahşap işçiliği, Amasya insanının sanata olan tutkusunu yansıtır.",
        "landmarks": ["Kral Kaya Mezarları", "Amasya Kalesi", "II. Bayezid Külliyesi", "Yalıboyu Evleri"]
    },
    "Corum": {
        "hikmet": "Geçmişin yıkıntıları üzerindeki bugünün direncini keşfet.",
        "quote": "\"Toprağın bereketlendiği, kadim krallıkların fısıltılarının rüzgara karıştığı il.\"",
        "description": "Hititlerin kadim diyarı, Anadolu'nun sessiz bekçisi. Çorum, gösterişten uzak, bağrında binlerce yıllık bir uygarlığı saklayan mütevazı bir ev sahibidir. Hattuşaş'ın yıkıntıları arasında yürürken insan, bir zamanlar dünyayı yöneten krallıkların şimdi rüzgarda savrulan topraktan ibaret olduğunu görür ve gücün geçiciliğini anlar.",
        "sufi_notes": "Bu şehir bize her saltanatın bir gün biteceğini, elde kalan tek şeyin kültür ve insanlık mirası olduğunu hatırlatır. Çorum'un toprakları, tarihin tekerrürden ibaret olduğunun doğal bir müzesidir.",
        "landmarks": ["Hattuşaş Antik Kenti", "Alacahöyük", "Çorum Müzesi", "İncesu Kanyonu"]
    },
    "Samsun": {
        "hikmet": "Büyük değişimler, cesurca atılan ilk adımla başlar.",
        "quote": "\"Umut, güneşin denizden doğuşuyla bir olup kara bulutları dağıttığı yerdedir.\"",
        "description": "Milli Mücadele'nin meşale şehri. Karadeniz'in giriş kapısı. Hırçın dalgaların umuda dönüştüğü, zulme ve karanlığa karşı ilk adımın atıldığı kutlu rıhtım. Samsun, sadece yakın tarihin değil, Amazonların efsanelerinden, ilk çağ yerleşimlerine kadar uzanan bir direniş ve azim diyarıdır.",
        "sufi_notes": "Nasıl ki ülkenin uyanışı için atılan ilk adım bu şehirden başladıysa, insanın kendi hayatını değiştirecek kararları alması da böyle kesin bir başlangıç gerektirir. Burada denizin dalgası, gezginin kalbindeki özgürlük hissiyle aynı ritimde atar.",
        "landmarks": ["Onur Anıtı", "Bandırma Vapuru Müzesi", "Amisos Tepesi", "Amazon Köyü"]
    },
    "Sinop": {
        "hikmet": "Gölge etme, doğanın ve sükunetin tadını çıkar.",
        "quote": "\"Mutluluğun sırrı çok şeye sahip olmakta değil, doğayla uyum içinde yaşamaktır.\"",
        "description": "Mutluluğun ve sükunetin şehri. Karadeniz'in en kuzey ucu. Dalgaların dövdüğü kaleleri ve tarih boyunca hüznü barındıran cezaeviyle zıtlıkların uyumunu sergileyen Sinop, inzivaya çekilmek isteyen ruhlar için bir barınaktır. Denizin kokusu ve ormanın fısıltısı, dünya telaşını ardında bırakanlara teselli verir.",
        "sufi_notes": "Diyojen'in dünya malından vazgeçişini anımsatan bu şehir, sade yaşam felsefesine ne kadar yakındır. Tarihi hapishanede yaşananları tefekkür ederken, özgürlüğün insan için en değerli hazine olduğu idrak edilir.",
        "landmarks": ["Tarihi Sinop Cezaevi", "Sinop Kalesi", "Hamsilos Tabiat Parkı", "Erfelek Şelaleleri"]
    },
    "Giresun": {
        "hikmet": "Denizin sonsuzluğu insanın doğaya olan saygısıyla dalgalanır.",
        "quote": "\"Yeşille mavinin sırrına erdiği, doğanın tüm zenginliklerini sunduğu Karadeniz yurdu.\"",
        "description": "Kirazın ve fındığın ana vatanı. Mavi ile yeşilin kucaklaştığı nokta. Şehrin sokaklarında dolaşırken dağlardan gelen yayla havası ve denizden esen rüzgar birbirine karışır. Giresun Adası'ndaki söylenceler, zeytinlik semtindeki tarihi evlerin estetiğiyle birleşir. Burada zaman ağır işler, insanlar doğanın ritmine göre hareket eder.",
        "sufi_notes": "Çetin arazide gösterilen emek ve fındık ağacının direnci, Anadolu insanının ne kadar güçlü olduğunun kanıtıdır. Giresun'da dağlar ile deniz insanın doğaya boyun eğişinden çok onunla dost oluşunu simgeler.",
        "landmarks": ["Giresun Kalesi", "Zeytinlik Semti", "Giresun Adası", "Kuzalan Şelalesi"]
    },
    "Ordu": {
        "hikmet": "Ufku görebilmek için bulutların üzerine çıkman gerekir.",
        "quote": "\"Eşsiz koyların, yemyeşil tepelerle buluştuğu yükseklerin sığınağı.\"",
        "description": "Derelerin kıvrılarak aktığı, Karadeniz'in modern ve tabiatla iç içe şehri. Ordu'nun dağları denize öyle güzel uzanır ki, insan Boztepe'den aşağı bakarken manzaranın büyüklüğünden etkilenir. Karadeniz'in coşkulu doğası burada en pitoresk halini almıştır. Vadilerin içindeki ince yollar, oksijenin ve yeşilin bol olduğu yaylalara çıkar.",
        "sufi_notes": "Boztepe'den uçsuz bucaksız denize bakmak, insanın yeryüzündeki yerini ve evrenin sonsuzluğunu sorgulamasına sebep olur. Yason burnunda batan güneşi izlemek saf bir aydınlanma anıdır.",
        "landmarks": ["Boztepe", "Yason Burnu", "Kurul Kalesi", "Perşembe Yaylası"]
    },
    "Kocaeli": {
        "hikmet": "Emek, dünyayı döndüren asıl çarktır.",
        "quote": "\"Taşın terlediği, demirin şekil bulduğu, sanayinin ve üretimin başkenti.\"",
        "description": "Sanayinin ve emeğin iç içe geçtiği merkez. Kocaeli, bir yanı büyük tesislerin dinamizmiyle atarken, diğer yanı Kartepe'nin ormanlarıyla, Maşukiye'nin şırıl şırıl akan dereleriyle nefes alan bir şehirdir. Roma'dan Osmanlı'ya süzülen tarih, yerini modern çağın hızlı tempolu yaşamına bırakmış olsa da, şehrin Körfez'e yansıyan ışıkları umudu temsil eder.",
        "sufi_notes": "Kocaeli'de insan eliyle oluşturulan büyük mühendislik eserlerini görmek, insan aklının ve çalışıcılığının sınırlarını anlamamızı sağlar. Ter döken işçinin emeği, modern uygarlığın temel taşıdır.",
        "landmarks": ["İzmit Saat Kulesi", "Osman Hamdi Bey Evi", "Kartepe", "Sekapark"]
    },
    "Antalya": {
        "hikmet": "Güneşin her gün yeniden doğuşu, tarihin hiç bitmeyecek döngüsünü anlatır.",
        "quote": "\"Dağların heybetiyle denizin bitimsiz kumsallarının buluştuğu antik medeniyetler beşiği.\"",
        "description": "Akdeniz'in vitrini, sayısız uygarlığın limanı. Olympos'un yanan ateşi, Kaleiçi'nin dar sokaklarını süsleyen begonviller, Antalya'yı sadece bir tatil cenneti değil, aynı zamanda devasa bir açık hava müzesi yapar. Romalıların, Selçukluların adımladığı mozaiklerde yürümek, tarih içindeki yolculuğu iliklerinize kadar hissettirir.",
        "sufi_notes": "Hadrian Kapısı'ndan geçerken asırların ne kadar çabuk geçtiği ve devasa imparatorluklardan geriye sadece sütunların ve sanatsal yapıların kaldığı idrak edilir. Akdeniz'in mavisi, insana sonsuz bir huzur verir.",
        "landmarks": ["Kaleiçi", "Hadrian Kapısı", "Antalya Müzesi", "Olympos Antik Kenti", "Kaputaş Plajı"]
    },
    "Denizli": {
        "hikmet": "Güzellik, tabiatın suyu taşa işlemesi kadar ağır ve gerçektir.",
        "quote": "\"Beyaz kayaların içinden sızan şifa, toprağın sabrının yeryüzüne çıkmış kanıtıdır.\"",
        "description": "Bembeyaz travertenlerin, antik kentlerin şehri. Denizli, Ege'nin iç kesimlerinde tarih ve jeolojinin mucizevi birleşimidir. Pamukkale'nin eşsiz beyazlığı, doğanın bir sanatçı edasıyla yeryüzünü nasıl şekillendirdiğini gösterir. Laodikeia ve Hierapolis'in kalıntıları arasında dolaşırken, eski çağların yaşam kültürüne tanıklık edersiniz.",
        "sufi_notes": "Termal suların yerin derinliklerinden çıkıp taşları beyaza boyaması gibi, gezginin de yolculuklarında yaşadığı deneyimlerin karakterini şekillendirmesini izleriz. Denizli, doğanın sanatına duyulan saygının şehridir.",
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
                
                content = f"# 📍 {clean_city} - Seyahat ve Keşif Notları\n\n"
                content += f"## 📜 Şehir Manifestosu\n> \"{details['hikmet']}\"\n"
                content += f"> {details['quote']}\n\n"
                content += f"### 🌍 Şehrin Ruhu ve Kültürel Dokusu\n{details['description']}\n\n"
                content += f"### 🕊️ Felsefi Notlar (Gezgin Perspektifi)\n{details['sufi_notes']}\n\n"
                content += "### ✨ Tarihi ve Kültürel Duraklar\nGezginin adımlaması ve keşfetmesi tavsiye edilen önemli mekanlar:\n"
                
                for loc in details['landmarks']:
                    content += f"- [ ] **{loc}**\n"
                    
                content += "\n---\n*Bu il bizzat deneyimlenmiş ve tarihi dokusu kayıt altına alınmıştır.* ✅\n"
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Deeply enriched: {file_path}")

if __name__ == "__main__":
    enrich_visited()
