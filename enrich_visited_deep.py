import os

VISITED_DEEP_DETAILS = {
    "Istanbul": {
        "hikmet": "İstanbul bir ayna gibidir; ona yüzünü dönen, zamanın ve tarihin kalbinde kendi yansımasını görür.",
        "quote": "\"İmparatorlukların ebediyete karıştığı, taşın ve denizin şiir yazdığı yedi tepeli masal.\"",
        "description": "Dünyanın gözbebeği, iki kıtayı birbirine diken asırlık payitaht. Topraklarında barındırdığı üç büyük imparatorluğun kültürel ve mimari nefesini her sokağında hissettiren bu kadim şehir, asla uyumayan devasa bir deryadır.\n\nAyasofya'nın kubbesinden süzülen solgun bir ışık, Galata'nın rutubetli taşlarına sinmiş anılar, Boğaz'ın hırçın rüzgarına karışan eski zaman fısıltıları... İstanbul, dar vakitlerde aceleyle 'gezilecek' değil; durup uzun uzadıya kulak verilecek, derin bir nefesle içe çekilecek, insanın kendi varoluşunu sorgulayabileceği uçsuz bucaksız bir romandır.",
        "sufi_notes": "İstanbul'un karmaşık sokaklarında kaybolmak, aslında kendini bulmanın, içindeki kaosu dindirmenin bir yoludur. Buradaki her yıkık dökük kalıntı, bize zamanın ne kadar hızlı aktığını ve insan ömrünün ne denli kısa olduğunu hatırlatırken; aynı zamanda yaşanmışlıkların, estetiğin ve inancın nesiller boyu kalplere nasıl dokunabildiğini gösterir.",
        "gastronomi": "- **Tarihi Süleymaniye Kurufasulyeci:** Çınar altında, bakır taslarda sunulan asırlık gelenek.\n- **Eminönü Balık Ekmek:** Boğaz esintisi ve martı sesleri eşliğinde hızlı ama unutulmaz bir klasik.\n- **Vefa Bozacısı:** Soğuk akşamlarda tarçın kokusuyla ısınan tarihi muhabbetler.",
        "landmarks": ["Ayasofya-i Kebir Cami-i Şerifi", "Topkapı Sarayı", "Galata Kulesi", "Süleymaniye Camii", "Yerebatan Sarnıcı", "Kapalıçarşı"]
    },
    "Konya": {
        "hikmet": "Susuzluktan kuruyan bozkırı yeşerten yağmur değil, gönülden kopan sevginin ve hoşgörünün pınarıdır.",
        "quote": "\"Rüzgârın en hafif estiği, sarı buğday başakları arasında evrensel sükunetin demlendiği Selçuklu diyarı.\"",
        "description": "Çöllerin ve uçsuz bucaksız ovaların ortasında bir vaha gibi duran, yalnızlığın ve dinginliğin başkenti. Dışarıdan bakıldığında sessiz, sert ve kurak görünen bu bozkır, içine girildiğinde eşsiz bir hoşgörü, tasavvuf ve estetik barındırır.\n\nMevlana'nın yüzyılları aşan 'Ne olursan ol gel' çağrısının yankılandığı sokaklarında gezinirken, sarının ve toprağın her tonu güneşte parlar. Konya, insanın dış dünyadaki karmaşayı geride bırakıp içselliğine uzandığı mistik bir kervansaraydır.",
        "sufi_notes": "Konya'da bozkır rüzgârını dinlemek, insanın kendi gürültüsünden kaçıp sükunetini bulması gibidir. Burada göğe uzanan sadece yeşil çinili minareler değil; sevgiyle, estetikle ve tevazuyla yükselen ulu bir düşünce sisteminin kökleridir. Her semazen dönüşünde kainatın sırrını fısıldar.",
        "gastronomi": "- **Etliekmek:** İnce hamur, ustalık ve odun ateşinin harika buluşması (özellikle Havzan veya Meram bölgesinde).\n- **Fırın Kebabı:** Saatlerce bakır tepsilerde ağır ağır pişen Selçuklu mirası et yemeği.\n- **Bamya Çorbası:** Düğünlerin ve özel günlerin ekşi-tatlı eşsiz başlangıcı.",
        "landmarks": ["Mevlana Müzesi", "Alaeddin Tepesi", "Karatay Medresesi", "Sille Köyü", "Kelebekler Vadisi"]
    },
    "Bursa": {
        "hikmet": "Dağın yüceliği sadece zirvesindeki karlardan değil, eteklerindeki çınarlara verdiği can suyundan gelir.",
        "quote": "\"Suyun sesine karışan ulu çınar yapraklarının, bir imparatorluğun doğuşuna beşiklik ettiği yeşil başkent.\"",
        "description": "Uludağ'ın eteklerine şefkatle yaslanmış, yeşiliyle ve suyuyla her nefeste hayat bulan asil Osmanlı şehri. Her köşebaşındaki tarihi bir şadırvandan su sesi gelir; dar sokaklarında ahşap ve taşlarla ilmek ilmek işlenmiş, asırlara meydan okuyan bir sükunet vardır.\n\nBursa, doğa ile insanın, yeşil ile mimarinin en zarif şekilde uyumlandığı kadim bir huzur yuvasıdır. Hanlar bölgesindeki çay molaları, zamanın burada daha yavaş aktığının en büyük kanıtıdır.",
        "sufi_notes": "Tarihi İnkaya çınarının altında kök salmak ve göğe yükselmek üzerine düşünmek, insana sabrın gücünü öğretir. Bursa, ne kadar büyürse büyüsün, o ilk toprağa düşen Osman Gazi tohumunun tevazusunu hep koruması gerektiğini sessizce anlatır.",
        "gastronomi": "- **Tarihi İskender Kebap:** Pide, tereyağı, enfes döner ve salçanın 1800'lerden gelen büyük buluşması.\n- **Pideli Köfte:** Kayhan çarşısında esnafın en sevdiği, iskenderin mütevazı ama bir o kadar lezzetli kardeşi.\n- **Tahinli Pide:** Sabahın erken saatlerinde fırından yeni çıkmış, çayın en büyük yoldaşı.",
        "landmarks": ["Ulu Cami", "Tarihi İnkaya Çınarı", "Yeşil Türbe", "Koza Han", "Cumalıkızık", "Tophane"]
    },
    "Ankara": {
        "hikmet": "Taşa ve yokluğa karşı dikilen bir Cumhuriyet iradesi, dünyadaki en güçlü çelikten daha aşılmazdır.",
        "quote": "\"Yorgun bir bozkırda imkansızın nasıl başarıldığını haykıran, vakur, kararlı ve devrimci başkent.\"",
        "description": "Anadolu'nun kalbi, Friglerden Cumhuriyetin kuruluş yıllarına kadar uzanan, daima ayakta kalmanın direncini simgeleyen şehir. Güçlü ayazı insanın tenini sıyırsa da, sokaklarındaki ciddiyet ve kararlılık devletin ve milletin ruhunu ateşler.\n\nAnkara, görkemli sarayların veya boğaz parıltısının değil; emeğin, kararlılığın, diplomasinin ve 'kendi küllerinden doğma' inancının merkezidir. Ulus meydanındaki her kaldırım taşı Cumhuriyetin ilk adımlarını şahididir.",
        "sufi_notes": "Ankara bize en büyük zorluklara karşı dik durmayı öğretir. Hiçbir şeyin altın tepside sunulmadığı, aksine tırnaklarla kazınarak kazanıldığı bu topraklarda atılan her sağlam temel, inancın imkansızlıkları nasıl yarıp geçtiğine dair bir belgeseldir.",
        "gastronomi": "- **Ankara Simidi:** Pekmezi bol, dışı çıtır, içi tel tel dökülen vazgeçilmez sabah lezzeti.\n- **Ankara Tava:** Arpa şehriye ve ağır ateşte pişmiş kuzu etinin doyurucu senfonisi.\n- **Beypazarı Kurusu:** Çay masalarının aylarca bayatlamayan, tarçın kokulu yoldaşı.",
        "landmarks": ["Anıtkabir", "Ankara Kalesi", "Anadolu Medeniyetleri Müzesi", "I. ve II. Meclis Binaları", "Atakule", "Eymir Gölü"]
    },
    "Amasya": {
        "hikmet": "Kayaya kazınan en büyük iz kralların gücü değil, vadiden usulca akan suların getirdiği yaşamdır.",
        "quote": "\"Nehrin ikiye böldüğü, Ferhat'ın gölgesiyle dağların şarkısının rüzgarda birbirine karıştığı elma kokulu vadi.\"",
        "description": "Yeşilırmak'ın nazlı nazlı aktığı dar ve sarp bir vadiye gizlenmiş masal şehri. Nehrin iki yakasını süsleyen ince işçilikli yalıboyu evleri, onların üstüne heybetle yükselen hırçın kayalar ve bu kayalara kazınmış iki bin yıllık Pontus antik Kral Kaya mezarları...\n\nAmasya, nehrin ritmiyle tarihin donup kaldığı bir seyir terasıdır. Şehzadelerin devlet yönetmeyi öğrendikleri bu topraklar, küçük yüzölçümüne rağmen kültürel olarak bir imparatorluk büyüklüğündedir.",
        "sufi_notes": "Bir dağın sinesine kibre kapılarak kazınmış o kocaman kral mezarları bile zamanın karşısında ufalanır; fakat o mütevazı görünümlü ırmak asırlardır hep aynı türküyü söyler. Amasya insana kalıcı olanın güç değil, doğanın akışına uyum sağlamak olduğunu öğretir.",
        "gastronomi": "- **Amasya Çöreği:** Haşhaş ve cevizin odun ateşinde buluştuğu efsane lezzet.\n- **Keşkek:** Özel günlerin ve bayramların büyük bakır kazanlarda dövülerek yapılan baştacı yemeği.\n- **Misket Elması:** Sulu, kokulu ve şehrin simgesi olan enfes meyve.",
        "landmarks": ["Kral Kaya Mezarları", "Amasya Kalesi", "Amasya Yalıboyu Evleri", "Hazeranlar Konağı", "Ferhat ile Şirin Aşıklar Müzesi", "II. Bayezid Külliyesi"]
    },
    "Corum": {
        "hikmet": "Medeniyetler kılıçla veya kanla kurulsa da, yalnızca masaya barışın mührü basıldığında yarına kalır.",
        "quote": "\"Çivi yazılı taş tabletlerin arasında yankılanan ilk barışın, bereketli topraklardaki unutulmaz izi.\"",
        "description": "Hititlerin kadim güneşi altında yıkanan, bereketin, tarihin ve Anadolu uygarlıklarının beşiği. Çorum, gösterişten uzak tepelerinde binlerce yıllık bir imparatorluk mirasını saklar.\n\nHattuşaş'ın yıkıntıları arasında, Aslanlı Kapı'dan içeri doğru yürürken duyulan tek ses, toprağın ve rüzgarın binlerce yıllık şahitliğinin ninnisine benzer. Şehir, leblebicilerinin burna dolan o güzel kavrulmuş kokusu ile samimi, mütevazı ama derin bir karakter sergiler.",
        "sufi_notes": "Krallar unutulup gider, aşılamaz denen devasa surlar yıkılır. Ancak insanlık tarihine düşülen 'Kadeş Barış Antlaşması' notu sonsuza kadar toprağın hafızasında kalır. Gücün ardındaki asıl zarafet ve barışın kıymeti, bu bozkır harabelerinde yatar.",
        "gastronomi": "- **Taze Kavrulmuş Çorum Leblebisi:** Sokakları saran sıcacık, odun ateşi tadında nohutun sanata dönüşmüş hali.\n- **İskilip Dolması:** Ağzı mühürlenmiş kazanlarda saatlerce pişen destansı ziyafet yemeği.\n- **Kuru Mantı:** Genellikle fırınlanıp kurutularak saklanan ve kışın yoğurtla şölene dönüşen lezzet.",
        "landmarks": ["Hattuşaş Antik Kenti (Boğazkale)", "Alacahöyük", "Çorum Müzesi", "Yazılıkaya Açık Hava Tapınağı", "Şapinuva", "Saat Kulesi"]
    },
    "Samsun": {
        "hikmet": "En hırçın fırtınalarda uyanan irade, coşkulu dalgaları uysallaştıran ve rotayı çizen tek pusuladır.",
        "quote": "\"Kurtuluşa atılan o tarifsiz ilk sağlam adımın, denizin tuzuna karışıp bir milleti dirilttiği özgürlük limanı.\"",
        "description": "Karadeniz'in deli dalgalarına karşı hep bir fener gibi aydınlık ve dik durmuş umudun şehri. Dağlardan denize doğru uzanan yemyeşil tepelerin ve hırçın Karadeniz sahilinin tam ortasında, medeniyet ve doğanın büyük kucaklaşmasıdır.\n\nAtatürk'ün Bandırma Vapuru ile ufukta göründüğü o tarihi anın ruhunu tütünde, denizde ve rüzgarda her an hissedebilirsiniz. Karadeniz'in en modern şehirlerinden biri olarak ticareti, tarihi ve gençliği aynı sokaklarda barındırır.",
        "sufi_notes": "Bazen pasif kalıp beklemek değil, tam aksine dalgaların üzerine doğru inançla o 'ilk adımı' atmak gerekir. Hayattaki tüm korkular, umutsuzluklar ve engeller, insanın karar verip Bandırma misali yola çıkmasıyla küçülmeye başlar.",
        "gastronomi": "- **Bafra Pidesi:** İncecik, kapalı hamurun içinde bol tereyağı ile harmanlanmış kıymalı şaheser.\n- **Terme Pidesi:** Daha yumuşak, açık ve sucuk/kaşar varyasyonlarıyla zengin lezzet.\n- **Çakallı Menemeni:** Suyunu çektirip peynirle karamelleşen, ekmek bandırmalık efsanevi yol üstü kahvaltısı.",
        "landmarks": ["Onur Anıtı (Atatürk Heykeli)", "Bandırma Vapuru ve Milli Mücadele Parkı", "Amisos Tepesi", "Amazon Köyü", "Kurtuluş Yolu"]
    },
    "Sinop": {
        "hikmet": "En karanlık zindan kalın dört duvar arası ve demir parmaklıklar değil, insanın kendi kafasında ördüğü sınırlardır.",
        "quote": "\"Hırçın Karadeniz ile huzurlu limanın buluştuğu, deniz kokulu yalnızlığıyla baş başa kalan filozof yarımada.\"",
        "description": "Gölgelerin, sükunetin ve en kuzeyin şehri. Anadolu'nun denize bir mızrak ucu gibi uzanan en uç noktası. Dalgaların yüzlerce yıllık kale duvarlarını dövdüğü, ormanın adeta denize döküldüğü ve insanın doğayla baş başa kaldığı efsanevi bir liman!\n\nDar sokaklarında deniz kokusu evlerin pencerelerinden içeri dolar. Hem inziva köşesi arayan bir bilge kadar huzurlu, hem de asırlık tarihi cezaevinin ürpertici havasını taşıyan acılı bir hafıza mekanıdır. Diogenes'in fenerle gündüz vakti insan aradığı bu topraklar, tefekkürün tam merkezidir.",
        "sufi_notes": "Tarihi cezaevinin nemli, ürpertici havası ve soğuk duvarları bize dışarıdaki özgürlüğün, bir nefes almanın değerini hatırlatırken; duvarın hemen dibindeki uçsuz bucaksız deniz, insanın kalbindeki sınır tanımaz umudu ve sonsuzluk tutkusunu temsil eder.",
        "gastronomi": "- **Sinop Mantısı (Cevizli Mantı):** Yarısı yoğurtlu, yarısı bol cevizli olarak sunulan sıradışı bir hamur işi vizyonu.\n- **Nokul:** Üzümlü ve cevizli, çay saatlerinin başrol oyuncusu, kıyır kıyır bir yöresel börek/çörek.\n- **Taze Karadeniz Balıkları:** Özellikle kış aylarında İnceburun açıklarından tutulan hamsi ve istavrit.",
        "landmarks": ["Tarihi Sinop Cezaevi", "Sinop Kalesi", "Hamsilos Tabiat Parkı", "Erfelek Tatlıca Şelaleleri", "İnceburun Deniz Feneri"]
    },
    "Giresun": {
        "hikmet": "Karadeniz'in dalgalarının dövdüğü kayalar ne kadar sarp ise, zorluklarla bezenmiş o dalların verdiği fındıklar o kadar tatlıdır.",
        "quote": "\"Yeşilin en koyusunun, denizin en mavisinin ve zorlu yamaçlardaki emeğin sonsuz bir memleket hasretiyle kucaklaştığı yer.\"",
        "description": "Ormanın denize paralel bir sükunet ve inatla uzandığı, sislerin ardında gizli kalmış muazzam tabiat. Yaylalarındaki serin rüzgarlar insanın kalbine yaşama sevinci pompalarken, o sarp yamaçlarda yeşeren doğa insan emeğinin en dürüst karşılığını sunar.\n\nSadece adasındaki Amazon efsaneleri değil, yaylarındaki uçsuz bucaksız yeşil dalgalar da Giresun'u Karadeniz'in en otantik ve dokusu bozulmamış incilerinden biri yapar.",
        "sufi_notes": "Doğadaki her türlü zorluk ve ulaşılamazlık, sabır ve emekle yoğrulduğunda en tatlı meyvelerini (örneğin fındığı) cömertçe sunar. İnsan doğanın bu inatçı ama verimli karakterine bakıp kendi içindeki çetin mücadelelerin de eninde sonunda çiçek açacağını idrak edebilir.",
        "gastronomi": "- **Giresun Kalite Fındık:** Dünyanın en iyi, en yağlı ve lezzetli tombul fındığı.\n- **Pancarlı Karalahana Çorbası:** Karalahana, mısır yarması ve fasulyenin oluşturduğu tam bir şifa deposu.\n- **Görele Pidesi:** Özel hamuru ve mis gibi köy tereyağıyla taçlandırılmış çıtır Karadeniz pidesi.",
        "landmarks": ["Giresun Kalesi", "Kuzalan Şelalesi", "Mavi Göl", "Giresun Adası (Aretias)", "Kümbet Yaylası"]
    },
    "Ordu": {
        "hikmet": "Göğe ne kadar yükselir ve aşağıya kibirle değil de şefkatle bakarsan, önündeki yollar ve denizler o kadar aydınlanır.",
        "quote": "\"Bulutların üzerine kurulan tahtından, Karadeniz'in ince dantel gibi örülmüş muazzam kıyılarını izleyen zarif şehir.\"",
        "description": "Boztepe'ye çıkıp teleferikten bakıldığında, ayağınızın altında uzanan o muazzam yeşil ve mavi uçurumun şehri. Yaylalarının (Perşembe, Çambaşı) uçsuz bucaksız sisli tepeleri, mendereslerin muazzam kıvrımları ve kıyıların eşsiz sükuneti birleşir.\n\nBurası, insanın metropol gürültüsünden kaçıp kafa dinlemek için haritadan gözü kapalı seçeceği, doğanın merhametli kollarında kurulu, Karadeniz'in en nazlı çocuklarından biridir.",
        "sufi_notes": "Yüksek bir tepeden o uçsuz bucaksız denize ve ucu bucağı görünmeyen ormanlara bakmak; insanın evrenin ne kadar devasa, kendisinin ve dertlerinin ise ne kadar narin bir zerreden ibaret olduğunu anlaması için ruhsal bir aynadır.",
        "gastronomi": "- **Ordu Tostu:** İki kalın ekmek dilimi arasına konulan özel sucuk ezmesinin preslenmesiyle yapılan kült sokak lezzeti.\n- **Yalıköy Köftesi:** Baharatsız, sadece etin kendi muazzam lezzetiyle şekillendirilen Karadeniz köftesi.\n- **Melocan (Diken Ucu) Kavurması:** Doğadan toplanan narin bitkilerin yöresel bir kavurmayla şölene dönüşmesi.",
        "landmarks": ["Boztepe ve Teleferik", "Yason Burnu ve Kilisesi", "Perşembe Yaylası (Menderesler)", "Kurul Kalesi"]
    },
    "Kocaeli": {
        "hikmet": "Emeğin teriyle işlediği demir pas tutmaz; yorgunluk, yeni bir inşanın umut kıvılcımıdır.",
        "quote": "\"Fabrika bacalarından tüten isli umutlarla, bitinya krallığından kalma mirasın beraber yeşerdiği üretim diyarı.\"",
        "description": "Denizin kıyısında, körfez köprülerinin ağzında, demirin, plastiğin ve ateşin şekillendiği Türkiye'nin devasa endüstri başkenti. Dışarıdan veya otobandan bakıldığında sadece sanayi bacaları ve duman görünse de, şehrin biraz içine sızınca Kartepe'nin karlarına ve Kandıra'nın yemyeşil koylarına ulaşırsınız.\n\nKocaeli, gece gündüz uyumayan bir üretim arzusuyla, dağların arkasındaki gizli doğanın sürekli bir mücadele ve denge içinde yaşadığı, dinamik bir şehirdir.",
        "sufi_notes": "Çarkların, çekiçlerin ve koca fabrikaların geceyi aydınlatan ateşli sesi, aslında insan aklının, hayatta kalma refleksinin ve emeğinin birer senfonisidir. Hiçbir şey durduk yere şekillenmez; demir bile işe yaramak için önce ateşe sabırla dayanmalıdır.",
        "gastronomi": "- **Pişmaniye:** Çekildikçe incelen, ustalık isteyen ve damakta eriyen tatlı tel tel Kar demeti.\n- **Değirmendere Fındığı / Yarımca Kirazı:** Endüstrinin tam kalbinden fışkıran yöresel doğa mucizeleri.\n- **Kandıra Yoğurdu:** Manda sütünden yapılan, bıçakla kesilebilecek kadar kıvamlı ve doğal yoğurt.",
        "landmarks": ["Sekapark (Eski Kağıt Fabrikası Dönüşümü)", "Kartepe Kayak Merkezi", "İzmit Tarihi Saat Kulesi", "Osman Hamdi Bey Evi (Eskihisar)", "Kefken ve Kerpe Kayalıkları"]
    },
    "Antalya": {
        "hikmet": "Sonsuz maviliğin ufku, geçmişi derinliklerinde hatırlar ancak daima doğacak yeni güne daha büyük umutla bakar.",
        "quote": "\"Kayalıklarına gürültüyle çarpıp geri çekilen suların, asırların mirasını şefkatle yıkadığı sıcak Akdeniz cenneti.\"",
        "description": "Akdeniz'in şüphesiz vitrini; güneşi, Likya ve Pamfilya antik kentlerini ve turkuaz doğayı cömertçe kucaklayan o sıcak coğrafya. Bir yanda Torosların kar kaplı heybeti dururken, diğer yanda insanın ruhunu yatıştıran engin mavi plajlar uzanır.\n\nKaleiçi'nin begonvillerle süslenmiş, dar ve nostaljik sokaklarında yürürken, antik krallıkların ayak seslerini ve yorgun kalyoncuların kalkanlara vuran mızrak seslerini bir film şeridi gibi hissedersiniz.",
        "sufi_notes": "Güneyin bu kızgın Akdeniz güneşi ve şifalı tatlı-tuzlu suyu, bedeni yorarken zihni tazeler. Karşınıza çıkan her amfi tiyatro ve kalıntı, geçmiş zamanın dünya telaşının ne denli boş olduğunu, asıl gerçeğin o anı en güzel şekilde yaşamak olduğunu fısıldar.",
        "gastronomi": "- **Piyaz (Antalya Usulü):** Tahinli, sirkeli sosuyla alışılagelmiş piyazları unutturan, kendi başına harika bir öğün.\n- **Hibeş:** Tahin, sarımsak, limon ve baharatların harmanından doğan muazzam yerel meze.\n- **Yanık Dondurma (Keçi Sütlü):** İsli, yanık kokulu ve sakızlı eşsiz bir serinletici.",
        "landmarks": ["Tarihi Kaleiçi ve Yivli Minare", "Hadrian Kapısı (Üç Kapılar)", "Olympos ve Phaselis Antik Kentleri", "Düden ve Kurşunlu Şelaleleri", "Aspendos Antik Tiyatrosu"]
    },
    "Denizli": {
        "hikmet": "Sabırla süzülen küçük ısrarlı su damlaları, asırlar içinde en sert ve karanlık kayaları bile bembeyaz bir pamuk tarlasına döndürür.",
        "quote": "\"Yeraltından fokurdayarak fışkıran sıcağın sanata, antik zamanların ve gladyatörlerin ise derin bir sessizliğe dönüştüğü o eşsiz coğrafya.\"",
        "description": "Uzaktan pamuk tarlaları gibi görünen travertenlerin bembeyaz şefkati ve hemen yanı başındaki Hierapolis'in büyüleyici, devasa lahit kalıntıları. Toprağın altında kaynayan ve efsanelere konu olan şifalı sular, yeryüzüne çıktığında muazzam bir doğa heykeli inşa eder.\n\nDenizli, tekstilin, dokumanın ve tabiatın en zarif işçiliğini birleştirerek yeryüzü tuvalinde sergilediği inanılmaz bir sanat atölyesi gibidir.",
        "sufi_notes": "Travertenleri adım adım, milim milim oluşturan o incecik damlalar bize sadece 'damlaya damlaya göl olur' demez; 'israr ederek, damlaya damlaya imkansız doğa mucizeleri yaratılır' der. Dünyadaki her büyük güzelliğin ardında asırlık sessiz bir sabır ve yavaş ama tükenmez bir gayret yatar.",
        "gastronomi": "- **Denizli Kebabı (Fırın Kebabı):** Elle yenmesi adet olan, sakız odunu ateşinde taş fırınlarda pişen kuzu şöleni.\n- **Zafer Gazozu:** Bölgenin retro ve popüler serinleticisi.\n- **Yanık Yoğurt:** Bakır kazanlarda bilerek dibi tutturularak elde edilen özel isli lezzet.",
        "landmarks": ["Pamukkale Travertenleri", "Hierapolis Antik Kenti ve Antik Havuz", "Laodikeia Antik Kenti", "Karahayıt Kırmızı Su Suları", "Teleferik ve Bağbaşı Yaylası"]
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
                
                if 'gastronomi' in details:
                    content += f"### 🍽️ Yöresel Lezzet Tavsiyeleri\n{details['gastronomi']}\n\n"
                
                content += "### ⛺ Konaklama ve Bütçe Stratejisi\n"
                content += "- **Sıfır Konaklama Maliyeti:** GSB Seyahatsever projesi kapsamında şehirdeki KYK yurtlarında 5 gün ücretsiz konaklanmıştır.\n"
                content += "- **Ulaşım Optimizasyonu:** Bir önceki ilden rotaya devam edilerek yol masrafı minimize edilmiştir.\n\n"
                content += "### 💻 Yarı Göçebe Mesaisi (Upskilling)\n"
                content += "- **Kütüphane Rutini:** Gündüzleri İl Halk Kütüphanesinde zaman geçirilerek yazılım projeleri geliştirilmiş ve eğitimlere devam edilmiştir.\n"
                content += "- **Şehri Sindirme:** Kalan vakitlerde şehrin tarihi ve kültürel dokusu acele etmeden, derinlemesine keşfedilmiştir.\n\n"
                content += "### ✨ Keşfedilesi Duraklar\nBu şehrin havasını solumak, ruhuna dokunmak için mutlaka adımlanması gereken köşe taşları:\n"
                
                for loc in details['landmarks']:
                    content += f"- [ ] **{loc}**\n"
                    
                content += "\n---\n*Bu il bizzat deneyimlenmiş, yolları aşındırılmış ve seyahatnameye sevgiyle işlenmiştir.* ✅\n"
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Deeply enriched: {file_path}")

if __name__ == "__main__":
    enrich_visited()
