![Travel Log Banner](assets/banner.png)

<p align="center">
    <img src="https://img.shields.io/badge/Bölge-7%2F7-success?style=for-the-badge&logo=map-location&logoColor=white" alt="Regions">
    <img src="https://img.shields.io/badge/Durum-Aktif%20Arşiv-blue?style=for-the-badge&logo=github" alt="Status">
    <img src="https://img.shields.io/badge/Lisans-MIT-orange?style=for-the-badge" alt="License">
    <br>
    <br>
    <strong>🦅 "Seyahat ya Resulallah" diyerek yola çıkanların izinde...</strong>
</p>

<div align="center">
  <h3>🌍 SEYAHAT SEVER VİZYONU</h3>
  <p><em>"Biz, yolların bitmediği, keşfin son bulmadığı bir dünyanın yolcularıyız. Her durak yeni bir hikaye, her şehir yeni bir nefestir. Bu repo, <strong>gerçek bir seyahat severin</strong> dijital hafızasıdır."</em></p>
</div>

# 🇹🇷 TRAVEL LOG: ANADOLU SEYAHATNAMESİ

> *"Çok yaşayan çok görür, çok gezen daha çok görür."* - Türk Atasözü

## 📜 Dijital Evliya Çelebi Manifestosu

> *"Seyahat ya Resulallah" diyerek yola çıkanların izinde, verinin gücüyle geleceğe yürüyenlere...*

### 1. Amaç: Dijital Ölümsüzlük
Bizler, Anadolu'nun kadim taşlarına dokunan rüzgarın sadece tenimizde değil, dijital hafızada da esmesini istiyoruz. Gördüğümüz her antik kent, yediğimiz her yemek, duyduğumuz her efsane; silikon çiplerin ve manyetik disklerin üzerinde sonsuzluğa kavuşmalıdır. Bu repo, **unutuşa karşı açılmış bir savaştır.**

### 2. Derin Belgeleme (Deep Documentation)
Süzegeçe yapılan "check-in"ler değil, derinlemesine analizler bizim işimiz.
*   **Sığ Gezgin**: "Buradaydım." der.
*   **Dijital Evliya**: "Burası tarihte neydi, bugün ne, ve ben burada ne hissettim?" diye sorar.
Veri, sadece bilgi değil; bağlamdır, histir, koddur.

### 3. Açık Kaynak Miras
Bilgi paylaştıkça çoğalır, kod paylaştıkça güçlenir. Gezi notlarımız, rotalarımız ve keşiflerimiz; mülkiyetin değil, insanlığın ortak malıdır. Bu repo, gelecek nesil gezginlere, tarihçilere ve veri madencilerine bırakılmış **açık bir mektuptur.**

### 4. Yavaş Seyahat, Hızlı Teknoloji
Ayaklarımız toprağa basarken yavaşlamayı, teknolojiyi kullanırken hızlanmayı seçiyoruz.
*   Doğayı izlerken analog,
*   Onu kaydederken dijitaliz.

### 5. Vizyon 2071
Hedefimiz sadece bugünü değil, yarım asır sonrasını planlamak. Bu repo, 2071 yılında bir arkeolog veya bir yapay zeka tarafından okunduğunda, 2020'lerin Anadolusu'na dair **en net, en saf ve en insani veriyi** sunmalıdır.

## 🧱 Yapı (Structure)
Repo, Türkiye'nin 7 coğrafi bölgesine göre ayrılmıştır. Her bölge klasörü, o coğrafyanın ruhunu taşıyan şehirleri ve mekanları barındırır.

*   `01_Marmara`
*   `02_Ege`
*   `03_Akdeniz`
*   `04_IcAnadolu`
*   `05_Karadeniz`
*   `06_DoguAnadolu`
*   `07_GuneydoguAnadolu`

## 🛠️ Kurulum ve Hazırlık (Installation)

Sistemi yerel makinenize kurmak ve katkıda bulunmak için:

### Gereksinimler
*   Python 3.8+
*   Git

```bash
# Repoyu klonla
git clone https://github.com/bahattinyunus/travel.log.git
cd travel.log

# Gerekli paketleri yükle (Opsiyonel, analiz aracı için)
pip install -r requirements.txt
```

## 🚀 Kullanım (Usage)

### 1. 🪄 CLI Sihirbazı (Yeni!)
Artık dosyalarla manuel uğraşmak yok. Terminalden sihirbazı başlatın:

```bash
# Yeni kayıt ekle
python cli.py add

# Haritayı güncelle
python cli.py map

# İstatistikleri gör
python cli.py stats
```

> `python cli.py add` komutu size bölge, şehir ve mekan sorar, otomatik klasör açar ve şablonu doldurur.

### 2. Harita (Interactive Map)
Gezdiğiniz tüm yerleri interaktif bir haritada görmek için:
1.  `python cli.py map` çalıştırın.
2.  `travel_map.html` dosyasını tarayıcıda açın.
3.  Anadolu'nun üzerindeki ayak izlerinizin keyfini çıkarın.

### 3. Otomasyon
Bu repo, **GitHub Actions** ile korunmaktadır. Her push işleminde veri bütünlüğü ve kod kalitesi otomatik olarak test edilir.






## 📍 Mevcut Kapsam (Current Coverage)
Anadolu'nun dört bir yanındaki ayak izlerimiz (Toplam 23 Nokta):

| Bölge | Şehir | Lokasyon | Kategori |
|-------|-------|----------|----------|
| 🏰 Marmara | İstanbul | Galata Kulesi | Tarihi Yapı |
| 🏰 Marmara | İstanbul | Ayasofya | Tarihi / Dini |
| 🏰 Marmara | İstanbul | Topkapı Sarayı | Saray / Müze |
| 🏰 Marmara | Çanakkale | Truva (Troya) | Antik Kent |
| 🌊 Ege | İzmir | Saat Kulesi | Şehir Dokusu |
| 🌊 Ege | İzmir | Efes Antik Kenti | Antik Kent |
| 🌊 Ege | İzmir | Şirince Köyü | Köy / Doğa |
| ☀️ Akdeniz | Antalya | Kaleiçi | Antik Kent |
| ☀️ Akdeniz | Antalya | Kaputaş Plajı | Plaj / Doğa |
| ☀️ Akdeniz | Antalya | Olympos | Tarih / Doğa |
| ☀️ Akdeniz | Mersin | Kızkalesi | Kale / Plaj |
| 🌾 İç Anadolu | Ankara | Anıtkabir | Anıt Mezar |
| 🌾 İç Anadolu | Nevşehir | Kapadokya | Doğa / Balon |
| 🌾 İç Anadolu | Konya | Tuz Gölü | Doğa / Manzara |
| 🌲 Karadeniz | Trabzon | Sümela Manastırı | İnanç / Doğa |
| 🌲 Karadeniz | Rize | Ayder Yaylası | Yayla / Doğa |
| ⭐ Karadeniz | Amasya | Kral Kaya Mezarları | Tarihi / Arkeoloji |
| ⭐ Karadeniz | Amasya | Yalıboyu Evleri | Sivil Mimari |
| ⭐ Karadeniz | Amasya | Ferhat ile Şirin | Efsane / Müze |
| 🏔️ Doğu Anadolu | Van | Akdamar Adası | Tarihi / Doğa |
| 🏔️ Doğu Anadolu | Ağrı | İshak Paşa Sarayı | Saray / Mimari |
| 🏔️ Doğu Anadolu | Kars | Ani Harabeleri | Antik Kent |
| 🏜️ G.Doğu Anadolu | Mardin | Ulu Camii | Tarihi Yapı |


## ✅ 81 İl Keşif Haritası

**🏆 Genel İlerleme:** %16.0 (13 / 81 İl)
🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜

> *Sürücü koltuğunda bizzat geçilen ve anı biriktirilen eşsiz rotalar...*

**🏰 Marmara Bölgesi (3/11)**
❌ Balıkesir • ❌ Bilecik • ✅ **Bursa** • ❌ Edirne • ✅ **Kocaeli** • ❌ Kırklareli • ❌ Sakarya • ❌ Tekirdağ • ❌ Yalova • ❌ Çanakkale • ✅ **İstanbul**

**🌊 Ege Bölgesi (1/8)**
❌ Afyonkarahisar • ❌ Aydın • ✅ **Denizli** • ❌ Kütahya • ❌ Manisa • ❌ Muğla • ❌ Uşak • ❌ İzmir

**☀️ Akdeniz Bölgesi (1/8)**
❌ Adana • ✅ **Antalya** • ❌ Burdur • ❌ Hatay • ❌ Isparta • ❌ Kahramanmaraş • ❌ Mersin • ❌ Osmaniye

**🌾 İç Anadolu Bölgesi (2/13)**
❌ Aksaray • ✅ **Ankara** • ❌ Eskişehir • ❌ Karaman • ❌ Kayseri • ✅ **Konya** • ❌ Kırıkkale • ❌ Kırşehir • ❌ Nevşehir • ❌ Niğde • ❌ Sivas • ❌ Yozgat • ❌ Çankırı

**🌲 Karadeniz Bölgesi (6/18)**
✅ **Amasya** • ❌ Artvin • ❌ Bartın • ❌ Bayburt • ❌ Bolu • ❌ Düzce • ✅ **Giresun** • ❌ Gümüşhane • ❌ Karabük • ❌ Kastamonu • ✅ **Ordu** • ❌ Rize • ✅ **Samsun** • ✅ **Sinop** • ❌ Tokat • ❌ Trabzon • ❌ Zonguldak • ✅ **Çorum**

**🏔️ Doğu Anadolu Bölgesi (0/14)**
❌ Ardahan • ❌ Ağrı • ❌ Bingöl • ❌ Bitlis • ❌ Elazığ • ❌ Erzincan • ❌ Erzurum • ❌ Hakkari • ❌ Iğdır • ❌ Kars • ❌ Malatya • ❌ Muş • ❌ Tunceli • ❌ Van

**🏜️ G.Doğu Anadolu Bölgesi (0/9)**
❌ Adıyaman • ❌ Batman • ❌ Diyarbakır • ❌ Gaziantep • ❌ Kilis • ❌ Mardin • ❌ Siirt • ❌ Şanlıurfa • ❌ Şırnak

## 🧬 Sistem Mimarisi
*   `01_...07_Regions/`: Ana veri katmanı.
*   `analytics.py`: Veri madenciliği ve raporlama motoru (CLI).
*   `tests/`: Sistem bütünlüğü testleri.
*   `_Sablon/`: Standart veri giriş şablonları.
*   `.github/`: CI/CD otomasyon protokolleri.

## 🤝 Katkıda Bulunma (Contributing)
Bu proje açık kaynaklı bir mirastır. Lütfen `CONTRIBUTING.md` dosyasını inceleyin.

---
<p align="center">
    <sub>Generated by Intelligence " 2024</sub>
</p>
