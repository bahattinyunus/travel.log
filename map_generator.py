"""
Anadolu Seyahatnamesi - İnteraktif Folium / Leaflet Harita Üreteci
Pulsing Glowing Markerlar, Glassmorphism Panel ve Zengin Popup Kartları
"""

import os
import folium
from pathlib import Path
from travel_core import SeyyahEngine, REGIONS_INFO

class MapGenerator:
    def __init__(self, repo_root="."):
        self.engine = SeyyahEngine(repo_root)
        self.output_file = Path(repo_root) / "travel_map.html"

    def generate(self):
        # Türkiye merkezli Folium Haritası (Koyu Şık Tema)
        m = folium.Map(
            location=[39.0, 35.3],
            zoom_start=6,
            tiles="CartoDB dark_matter",
            control_scale=True,
            prefer_canvas=True
        )

        stats = self.engine.stats
        pct = stats["progress_pct"]
        visited_count = stats["visited_cities"]
        total_cities = stats["total_cities"]

        # Özel CSS Stilleri
        css_style = """
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');
        
        .map-title-panel {
            position: absolute;
            top: 20px;
            left: 20px;
            z-index: 1000;
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            padding: 20px 24px;
            color: #f8fafc;
            font-family: 'Plus Jakarta Sans', sans-serif;
            box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.05);
            max-width: 340px;
            pointer-events: auto;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .map-title-panel:hover {
            border-color: rgba(0, 242, 254, 0.35);
            box-shadow: 0 25px 50px -12px rgba(0, 242, 254, 0.2);
        }
        .map-title-panel h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 18px;
            font-weight: 800;
            margin: 0 0 6px 0;
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .map-title-panel .subtitle {
            font-size: 12px;
            color: #94a3b8;
            margin: 0 0 16px 0;
            line-height: 1.5;
        }
        .progress-container {
            background: rgba(30, 41, 59, 0.7);
            border-radius: 10px;
            padding: 10px 12px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            margin-bottom: 14px;
        }
        .progress-info {
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 8px;
            color: #e2e8f0;
        }
        .progress-info .pct {
            color: #00f2fe;
            font-weight: 700;
        }
        .progress-bar-bg {
            background: rgba(255, 255, 255, 0.08);
            border-radius: 999px;
            height: 7px;
            overflow: hidden;
        }
        .progress-bar-fill {
            background: linear-gradient(90deg, #10b981 0%, #00f2fe 100%);
            height: 100%;
            border-radius: 999px;
            transition: width 1s ease-in-out;
            box-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
        }
        .stats-pills {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 12px;
        }
        .stat-pill {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            padding: 6px 10px;
            text-align: center;
        }
        .stat-pill .num {
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 14px;
            color: #38bdf8;
        }
        .stat-pill .lbl {
            font-size: 10px;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .visited-cities-list {
            margin-top: 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 10px;
            max-height: 110px;
            overflow-y: auto;
        }
        .visited-cities-list h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 11px;
            font-weight: 700;
            color: #10b981;
            margin: 0 0 6px 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .visited-cities-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
        }
        .city-badge {
            background: rgba(16, 185, 129, 0.15);
            color: #6ee7b7;
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 4px;
            padding: 2px 6px;
            font-size: 10px;
            font-weight: 500;
        }
        .panel-quote {
            margin: 12px 0 0 0;
            font-size: 11px;
            color: #cbd5e1;
            font-style: italic;
            text-align: center;
            border-top: 1px dashed rgba(255, 255, 255, 0.1);
            padding-top: 8px;
        }

        /* Pulsing Glow Marker */
        .pulsing-marker {
            position: relative;
            width: 18px;
            height: 18px;
        }
        .pulsing-marker .dot {
            width: 14px;
            height: 14px;
            background: linear-gradient(135deg, #10b981 0%, #00f2fe 100%);
            border-radius: 50%;
            position: absolute;
            top: 2px;
            left: 2px;
            box-shadow: 0 0 12px rgba(0, 242, 254, 0.8), 0 0 0 2px rgba(255, 255, 255, 0.8);
            cursor: pointer;
            transition: transform 0.2s ease;
        }
        .pulsing-marker:hover .dot {
            transform: scale(1.35);
        }
        .pulsing-marker .pulse {
            width: 32px;
            height: 32px;
            background: rgba(0, 242, 254, 0.4);
            border-radius: 50%;
            position: absolute;
            top: -7px;
            left: -7px;
            animation: pulse-ring 2.2s infinite ease-out;
            pointer-events: none;
        }
        @keyframes pulse-ring {
            0% { transform: scale(0.4); opacity: 1; }
            100% { transform: scale(1.6); opacity: 0; }
        }

        /* Tooltip & Popups */
        .leaflet-popup-content-wrapper {
            background: rgba(15, 23, 42, 0.95) !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 16px !important;
            color: #f8fafc !important;
            padding: 0 !important;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.75) !important;
            overflow: hidden !important;
        }
        .leaflet-popup-content {
            margin: 0 !important;
            line-height: 1.4 !important;
        }
        .leaflet-popup-tip {
            background: rgba(15, 23, 42, 0.95) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
        }
        .custom-popup-card {
            font-family: 'Plus Jakarta Sans', sans-serif;
            width: 280px;
        }
        .popup-image-header {
            position: relative;
            height: 120px;
            background-size: cover;
            background-position: center;
            border-radius: 16px 16px 0 0;
            display: flex;
            align-items: flex-end;
            padding: 12px 14px;
        }
        .popup-image-overlay {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.2) 0%, rgba(15, 23, 42, 0.9) 100%);
            border-radius: 16px 16px 0 0;
        }
        .popup-city-title {
            position: relative;
            z-index: 2;
            font-family: 'Outfit', sans-serif;
            font-size: 16px;
            font-weight: 700;
            color: #ffffff;
            margin: 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.6);
        }
        .popup-body-content {
            padding: 14px;
        }
        .popup-quote {
            font-size: 11px;
            color: #94a3b8;
            font-style: italic;
            margin: 0 0 10px 0;
            border-left: 2px solid #00f2fe;
            padding-left: 8px;
            line-height: 1.4;
        }
        .popup-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
            margin-bottom: 12px;
        }
        .popup-tag {
            font-size: 10px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 4px;
            padding: 2px 6px;
            color: #cbd5e1;
        }
        .popup-action-btn {
            display: block;
            text-align: center;
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
            color: #04121d !important;
            font-weight: 700;
            font-size: 12px;
            padding: 8px 12px;
            border-radius: 8px;
            text-decoration: none !important;
            transition: all 0.2s ease;
        }
        .popup-action-btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0, 242, 254, 0.4);
        }
        """

        m.get_root().header.add_child(folium.Element(f"<style>{css_style}</style>"))

        # Ziyaret Edilen İllerin Badgeleri
        visited_badges_html = ""
        for k, p in sorted(self.engine.visited_provinces.items(), key=lambda x: x[1]["name"]):
            visited_badges_html += f'<span class="city-badge">{p["name"]}</span>'

        # Floating Panel HTML
        title_panel_html = f"""
        <div class="map-title-panel">
            <h1>🕌 ANADOLU SEYAHATNAMESİ</h1>
            <p class="subtitle">Bir seyyahın adımladığı kadim topraklar, kütüphaneler ve tefekkür günlüğü.</p>
            
            <div class="progress-container">
                <div class="progress-info">
                    <span>Keşif İlerlemesi</span>
                    <span class="pct">%{pct} ({visited_count}/{total_cities})</span>
                </div>
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill" style="width: {pct}%"></div>
                </div>
            </div>

            <div class="stats-pills">
                <div class="stat-pill">
                    <div class="num">{stats['estimated_km']:,} km</div>
                    <div class="lbl">Menzil</div>
                </div>
                <div class="stat-pill">
                    <div class="num">7 / 7</div>
                    <div class="lbl">Bölge</div>
                </div>
            </div>

            <div class="visited-cities-list">
                <h3>Ziyaret Edilen İller ({visited_count})</h3>
                <div class="visited-cities-grid">
                    {visited_badges_html}
                </div>
            </div>

            <p class="panel-quote">"İyi bir gezginin sabit planları ve varmak gibi bir amacı yoktur."</p>
        </div>
        """
        m.get_root().html.add_child(folium.Element(title_panel_html))

        # Seyahat İzi Çizgisi (Polyline - Ziyaret edilen noktaları sırayla bağla)
        visited_coords = []
        for p in sorted(self.engine.visited_provinces.values(), key=lambda c: (c["lng"], c["lat"])):
            visited_coords.append([p["lat"], p["lng"]])

        if len(visited_coords) > 1:
            folium.PolyLine(
                locations=visited_coords,
                color="#00f2fe",
                weight=2,
                opacity=0.35,
                dash_array="6, 8",
                tooltip="Seyyah Rota İzi"
            ).add_to(m)

        # Ziyaret Edilen İlleri Marker Olarak Ekle
        for key, p in self.engine.visited_provinces.items():
            quote_text = p.get("custom_quote", p.get("quote", "Anadolu'nun kadim menzili."))
            banner_img = p.get("banner_rel", "assets/banner.jpg")
            readme_url = p.get("readme_rel", "#")
            
            # İlk 2 landmark etiketi
            landmarks_tags = "".join([f'<span class="popup-tag">📍 {lm}</span>' for lm in p.get("landmarks", [])[:2]])
            specialty_tag = f'<span class="popup-tag">🍽️ {p.get("specialties", ["Lezzet"])[0]}</span>' if p.get("specialties") else ""

            popup_html = f"""
            <div class="custom-popup-card">
                <div class="popup-image-header" style="background-image: url('{banner_img}')">
                    <div class="popup-image-overlay"></div>
                    <h3 class="popup-city-title">📍 {p['name']} ({p['plate']:02d})</h3>
                </div>
                <div class="popup-body-content">
                    <p class="popup-quote">"{quote_text}"</p>
                    <div class="popup-tags">
                        {landmarks_tags}
                        {specialty_tag}
                    </div>
                    <a href="{readme_url}" target="_blank" class="popup-action-btn">Gezi Günlüğünü Aç ➔</a>
                </div>
            </div>
            """

            marker_html = """
            <div class="pulsing-marker">
                <div class="pulse"></div>
                <div class="dot"></div>
            </div>
            """

            folium.Marker(
                location=[p["lat"], p["lng"]],
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=folium.Tooltip(f"✅ {p['name']} ({p['plate']:02d}) - {p['region']}"),
                icon=folium.DivIcon(
                    html=marker_html,
                    class_name="custom-pulsing-icon",
                    icon_size=(18, 18),
                    icon_anchor=(9, 9)
                )
            ).add_to(m)

        # Henüz Ziyaret Edilmemiş İller (Küçük nokta markerlar)
        for key, p in self.engine.unvisited_provinces.items():
            folium.CircleMarker(
                location=[p["lat"], p["lng"]],
                radius=4,
                color="#64748b",
                fill=True,
                fill_color="#1e293b",
                fill_opacity=0.7,
                weight=1.5,
                tooltip=folium.Tooltip(f"⏳ {p['name']} ({p['plate']:02d}) - Keşfedilmeyi Bekliyor"),
            ).add_to(m)

        m.save(str(self.output_file))
        return self.output_file

if __name__ == "__main__":
    mg = MapGenerator()
    out = mg.generate()
    print(f"İnteraktif Harita başarıyla oluşturuldu: {out}")
