import os

def update_readme():
    try:
        with open('README.md', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # 1. Add Banner if not present
        if "![Travel Log Banner]" not in content:
            # Find the second line (after the main header or similar) or just prepend
            # But usually README starts with # Title. Let's prepend to file.
            content = "![Travel Log Banner](assets/banner.png)\n\n" + content

        # 2. Add Amasya Highlight if not present
        highlight_section = """
## ⭐ Editörün Seçimi (Editor's Choice): Amasya
> *"Anadolu'nun Oxford'u, Şehzadeler Şehri..."*

Bu ay rotamızı **Amasya**'ya çevirdik. Tarih, doğa ve kültürün bu kadar iç içe geçtiği nadir yerlerden.
*   👑 **Krallar Vadisi:** Harşena Dağı'na oyulmuş devasa anıt mezarlar.
*   🏡 **Yalıboyu:** Yeşilırmak kenarındaki o masalsı ahşap evler.
*   🍏 **Lezzet:** Misket elması ve meşhur çiçek bamyası.

👉 **[Şehir Rehberini İncele](./05_Karadeniz/Amasya/README.md)**

"""
        if "Editörün Seçimi" not in content:
            insertion_marker = "## 📍 Mevcut Kapsam (Current Coverage)"
            if insertion_marker in content:
                content = content.replace(insertion_marker, highlight_section + insertion_marker)
            else:
                print("Could not find insertion marker for highlight.")

        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("README updated successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_readme()
