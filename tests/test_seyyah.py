"""
Anadolu Seyahatnamesi - Kapsamlı Test ve Doğrulama Paketi
"""

import os
import json
import pytest
from pathlib import Path
from travel_core import SeyyahEngine, PROVINCES_DATA, REGIONS_INFO

@pytest.fixture
def engine():
    return SeyyahEngine()

def test_total_provinces_count(engine):
    """Türkiye'nin 81 ilinin tamamının veritabanında olduğunu doğrular."""
    assert len(PROVINCES_DATA) == 81
    assert len(engine.provinces) == 81

def test_seven_geographical_regions():
    """Türkiye'nin 7 coğrafi bölgesinin tanımlı olduğunu doğrular."""
    assert len(REGIONS_INFO) == 7
    expected_regions = ["01_Marmara", "02_Ege", "03_Akdeniz", "04_IcAnadolu", "05_Karadeniz", "06_DoguAnadolu", "07_GuneydoguAnadolu"]
    for reg in expected_regions:
        assert reg in REGIONS_INFO

def test_provinces_coordinates_within_turkey_bounds():
    """Tüm il koordinatlarının Türkiye sınırları içerisinde olduğunu doğrular."""
    for key, p in PROVINCES_DATA.items():
        lat = p["lat"]
        lng = p["lng"]
        # Türkiye yaklaşık enlem: 35.8 - 42.2, boylam: 25.6 - 44.9
        assert 35.5 <= lat <= 42.5, f"{p['name']} enlemi hatalı: {lat}"
        assert 25.5 <= lng <= 45.0, f"{p['name']} boylamı hatalı: {lng}"
        assert 1 <= p["plate"] <= 81, f"{p['name']} plaka kodu hatalı: {p['plate']}"

def test_visited_cities_detection(engine):
    """Ziyaret edilen şehirlerin ve istatistiklerin doğru tespit edildiğini doğrular."""
    assert engine.stats["visited_cities"] >= 30
    assert 0 < engine.stats["progress_pct"] <= 100
    assert engine.stats["estimated_km"] > 5000

def test_haversine_distance_calculation(engine):
    """Ankara - İstanbul arası mesafenin yaklaşık 350-450 km aralığında olduğunu doğrular."""
    ankara = PROVINCES_DATA["04_IcAnadolu/Ankara"]
    istanbul = PROVINCES_DATA["01_Marmara/Istanbul"]
    dist = engine.calculate_distance_km(ankara["lat"], ankara["lng"], istanbul["lat"], istanbul["lng"])
    assert 300 <= dist <= 400

def test_route_planner_returns_valid_stops(engine):
    """Rota planlayıcının geçerli ve sıralı duraklar döndürdüğünü doğrular."""
    route = engine.plan_optimal_route(start_city_name="Ankara", max_stops=5)
    assert len(route) >= 2
    assert route[0]["name"] == "Ankara"
    for stop in route:
        assert "name" in stop
        assert "lat" in stop
        assert "lng" in stop

def test_web_data_json_generation(engine):
    """travel_data.json ve web_data.js dosyalarının üretilip geçerli olduğunu doğrular."""
    json_path, js_path = engine.generate_web_data_json()
    assert json_path.exists()
    assert js_path.exists()

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert "stats" in data
        assert "provinces" in data
        assert "regions" in data
        assert "quotes" in data
        assert len(data["provinces"]) == 81

def test_all_visited_city_readmes_exist(engine):
    """Ziyaret edilen tüm illerin README dosyalarının varlığını ve bütünlüğünü doğrular."""
    for key, p in engine.visited_provinces.items():
        readme_path = Path(p["readme_rel"])
        assert readme_path.exists(), f"README eksik: {readme_path}"
        content = readme_path.read_text(encoding="utf-8")
        assert len(content) > 500, f"README çok kısa: {readme_path}"
