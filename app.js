/**
 * Anadolu Seyahatnamesi - Single Page Application Engine
 * Web Audio API Ambient Synthesizer, Dynamic Route Planner, City Explorer & Map Modal
 */

(function () {
  'use strict';

  // Global State
  const state = {
    data: typeof TRAVEL_DATA !== 'undefined' ? TRAVEL_DATA : null,
    filter: 'all', // 'all', 'visited', 'unvisited'
    selectedRegion: 'all',
    searchQuery: '',
    selectedCityKey: null,
    currentView: 'dashboard', // 'dashboard', 'city', 'route'
    ambientPlaying: false,
    audioCtx: null,
    audioNodes: []
  };

  // DOM Elements
  const els = {
    statsPct: document.getElementById('stats-pct'),
    statsCount: document.getElementById('stats-count'),
    statsBar: document.getElementById('stats-progress-bar'),
    citiesList: document.getElementById('cities-list'),
    searchInput: document.getElementById('search-input'),
    regionSelect: document.getElementById('region-select'),
    filterPills: document.querySelectorAll('.filter-pill'),
    viewportContent: document.getElementById('viewport-content'),
    logoSection: document.getElementById('logo-section'),
    btnDashboard: document.getElementById('btn-dashboard'),
    btnMap: document.getElementById('btn-map'),
    btnRoute: document.getElementById('btn-route'),
    btnAmbient: document.getElementById('btn-ambient'),
    btnQuote: document.getElementById('btn-quote'),
    btnExport: document.getElementById('btn-export'),
    mapModal: document.getElementById('map-modal'),
    modalCloseBtns: document.querySelectorAll('.modal-close-btn')
  };

  // Initialize App
  function init() {
    if (!state.data) {
      console.error("TRAVEL_DATA yüklenemedi!");
      return;
    }

    renderHeaderStats();
    populateRegionSelect();
    renderCitiesList();
    renderDashboard();
    setupEventListeners();
  }

  // Header Statistics
  function renderHeaderStats() {
    const s = state.data.stats;
    if (els.statsPct) els.statsPct.textContent = `%${s.progress_pct}`;
    if (els.statsCount) els.statsCount.textContent = `(${s.visited_cities}/${s.total_cities})`;
    if (els.statsBar) els.statsBar.style.width = `${s.progress_pct}%`;
  }

  // Populate Regions Dropdown
  function populateRegionSelect() {
    if (!els.regionSelect) return;
    els.regionSelect.innerHTML = '<option value="all">Tüm Bölgeler (7/7)</option>';
    for (const [code, info] of Object.entries(state.data.regions)) {
      const regStat = state.data.stats.regional_breakdown[code];
      const opt = document.createElement('option');
      opt.value = code;
      opt.textContent = `${info.icon} ${info.name} (%${regStat ? regStat.percentage : 0})`;
      els.regionSelect.appendChild(opt);
    }
  }

  // Filter Cities
  function getFilteredCities() {
    const entries = Object.entries(state.data.provinces);
    const q = state.searchQuery.toLowerCase().trim();

    return entries.filter(([key, p]) => {
      // Visited Filter
      if (state.filter === 'visited' && !p.visited) return false;
      if (state.filter === 'unvisited' && p.visited) return false;

      // Region Filter
      if (state.selectedRegion !== 'all' && p.region_code !== state.selectedRegion) return false;

      // Search Query Filter
      if (q) {
        const matchName = p.name.toLowerCase().includes(q);
        const matchPlate = String(p.plate).includes(q);
        const matchLandmarks = (p.landmarks || []).some(l => l.toLowerCase().includes(q));
        const matchSpecialties = (p.specialties || []).some(s => s.toLowerCase().includes(q));
        if (!matchName && !matchPlate && !matchLandmarks && !matchSpecialties) return false;
      }

      return true;
    });
  }

  // Render Cities List in Sidebar
  function renderCitiesList() {
    if (!els.citiesList) return;
    const cities = getFilteredCities();

    if (cities.length === 0) {
      els.citiesList.innerHTML = `
        <div style="padding: 24px; text-align: center; color: var(--text-muted); font-size: 0.85rem;">
          Aradığınız kriterlere uygun şehir bulunamadı.
        </div>
      `;
      return;
    }

    els.citiesList.innerHTML = cities.map(([key, p]) => {
      const isSelected = state.selectedCityKey === key;
      const statusClass = p.visited ? 'visited' : 'unvisited';
      const statusText = p.visited ? '✓ Gezildi' : '⏳ Bekliyor';

      return `
        <div class="city-item ${isSelected ? 'active' : ''}" data-city-key="${key}">
          <div class="city-info-group">
            <div class="city-plate">${String(p.plate).padStart(2, '0')}</div>
            <div>
              <div class="city-name-text">${p.name}</div>
              <div class="city-region-sub">${p.region}</div>
            </div>
          </div>
          <span class="city-status-badge ${statusClass}">${statusText}</span>
        </div>
      `;
    }).join('');

    // Attach click events
    els.citiesList.querySelectorAll('.city-item').forEach(el => {
      el.addEventListener('click', () => {
        const key = el.getAttribute('data-city-key');
        selectCity(key);
      });
    });
  }

  // Select City & Render Detail
  function selectCity(key) {
    state.selectedCityKey = key;
    state.currentView = 'city';
    renderCitiesList(); // Re-render to update active class
    renderCityDetail(key);
  }

  // Render Dashboard View
  function renderDashboard() {
    state.currentView = 'dashboard';
    state.selectedCityKey = null;
    renderCitiesList();

    const s = state.data.stats;
    const quote = state.data.quotes[Math.floor(Math.random() * state.data.quotes.length)];

    const regionsHtml = Object.entries(state.data.regions).map(([code, rInfo]) => {
      const rStat = s.regional_breakdown[code] || { visited: 0, total: 0, percentage: 0 };
      return `
        <div class="glass-card region-card" data-region-code="${code}" style="cursor: pointer;">
          <div class="region-card-top">
            <div class="region-card-title">${rInfo.icon} ${rInfo.name}</div>
            <div class="region-card-pct">%${rStat.percentage}</div>
          </div>
          <div class="mini-progress-bar" style="width: 100%; height: 6px;">
            <div class="mini-progress-fill" style="width: ${rStat.percentage}%; background: ${rInfo.color};"></div>
          </div>
          <div style="font-size: 0.75rem; color: var(--text-muted); display: flex; justify-content: space-between;">
            <span>${rStat.visited} / ${rStat.total} İl Ziyaret Edildi</span>
            <span style="color: ${rInfo.color};">Detay ➔</span>
          </div>
          <div class="region-card-desc">${rInfo.desc}</div>
        </div>
      `;
    }).join('');

    els.viewportContent.innerHTML = `
      <div class="dashboard-view">
        <!-- Hero Section -->
        <div class="hero-banner">
          <div class="hero-tag">🕌 Sefer Der Vatan</div>
          <h2>DİJİTAL SEYYAH: ANADOLU SEYAHATNAMESİ</h2>
          <p class="hero-quote">"${quote.quote}" — <strong>${quote.author}</strong></p>
          <div style="display: flex; gap: 12px; flex-wrap: wrap;">
            <button class="btn btn-primary" id="dash-btn-map">🗺️ İnteraktif Keşif Haritası</button>
            <button class="btn btn-outline" id="dash-btn-route">🧭 Gezi Rotası Planla</button>
            <button class="btn btn-outline" id="dash-btn-export">📚 Seyahatnameyi İndir</button>
          </div>
        </div>

        <!-- 4 Stat Cards -->
        <div class="stats-grid">
          <div class="glass-card stat-card">
            <div class="stat-card-header">
              <span>Keşif Oranı</span>
              <span>🎯</span>
            </div>
            <div class="stat-card-value" style="color: var(--accent-emerald);">%${s.progress_pct}</div>
            <div class="stat-card-desc">81 İlin ${s.visited_cities} tanesi adımlandı</div>
          </div>

          <div class="glass-card stat-card">
            <div class="stat-card-header">
              <span>Menzil İzi</span>
              <span>🛣️</span>
            </div>
            <div class="stat-card-value" style="color: var(--accent-cyan);">${s.estimated_km.toLocaleString()} km</div>
            <div class="stat-card-desc">Tahmini kat edilen seyahat hattı</div>
          </div>

          <div class="glass-card stat-card">
            <div class="stat-card-header">
              <span>Kütüphane Ofisleri</span>
              <span>📖</span>
            </div>
            <div class="stat-card-value" style="color: var(--accent-gold);">${s.visited_cities}</div>
            <div class="stat-card-desc">Yazılım ve ilim tahsil edilen il</div>
          </div>

          <div class="glass-card stat-card">
            <div class="stat-card-header">
              <span>Kapsanan Bölge</span>
              <span>🌍</span>
            </div>
            <div class="stat-card-value" style="color: var(--accent-purple);">7 / 7</div>
            <div class="stat-card-desc">Tüm coğrafi bölgelere ayak basıldı</div>
          </div>
        </div>

        <!-- Regional Progress -->
        <div>
          <div class="section-title">
            <span>🗺️ Bölgesel Keşif Dağılımı</span>
          </div>
          <div class="regions-grid">
            ${regionsHtml}
          </div>
        </div>

        <!-- Nomad & Library Guide -->
        <div class="glass-card detail-card">
          <h3 style="font-family: var(--font-heading); font-size: 1.1rem; color: var(--accent-cyan); display: flex; align-items: center; gap: 8px;">
            💻 Dijital Seyyahın Çalışma Disiplini
          </h3>
          <p style="font-size: 0.85rem; color: var(--text-secondary);">
            Gündüzün ilk 4 saati şehrin İl Halk Kütüphanesinde yazılım geliştirme, okuma ve araştırma mesaisi yapılır. 
            Öğleden sonra ise şehrin kadim sokakları, camileri ve tabiatı tefekkürle adımlanır. Konaklamalarda GSB Seyahatsever kervansarayları tercih edilir.
          </p>
        </div>
      </div>
    `;

    // Re-bind dashboard quick buttons
    const dMap = document.getElementById('dash-btn-map');
    const dRoute = document.getElementById('dash-btn-route');
    const dExport = document.getElementById('dash-btn-export');
    if (dMap) dMap.addEventListener('click', openMapModal);
    if (dRoute) dRoute.addEventListener('click', renderRoutePlanner);
    if (dExport) dExport.addEventListener('click', exportMarkdownBook);

    // Region cards click to filter
    document.querySelectorAll('.region-card').forEach(card => {
      card.addEventListener('click', () => {
        const code = card.getAttribute('data-region-code');
        state.selectedRegion = code;
        if (els.regionSelect) els.regionSelect.value = code;
        renderCitiesList();
      });
    });
  }

  // Render City Detail View
  function renderCityDetail(key) {
    const p = state.data.provinces[key];
    if (!p) return;

    const bannerImg = p.has_banner ? p.banner_rel : 'assets/banner.jpg';
    const quoteText = p.custom_quote || p.quote;
    const libraryText = p.custom_library || p.library;
    const statusBadge = p.visited 
      ? '<span class="tag-badge" style="background: rgba(16,185,129,0.2); color: #6ee7b7; border-color: #10b981;">✓ Ziyaret Edildi & Tefekkür Edildi</span>'
      : '<span class="tag-badge" style="background: rgba(245,158,11,0.2); color: #fcd34d; border-color: #f59e0b;">⏳ Gelecek Rotalarda Bekleniyor</span>';

    const landmarksHtml = (p.landmarks || []).map(lm => `
      <div class="landmark-item">
        <span style="color: ${p.visited ? '#10b981' : '#64748b'};">${p.visited ? '✓' : '○'}</span>
        <span>${lm}</span>
      </div>
    `).join('');

    const specialtiesHtml = (p.specialties || []).map(sp => `
      <span class="tag-badge" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24; border-color: rgba(245, 158, 11, 0.3);">
        🍽️ ${sp}
      </span>
    `).join('');

    els.viewportContent.innerHTML = `
      <div class="city-detail-view">
        <!-- Hero Header -->
        <div class="city-hero" style="background-image: url('${bannerImg}');">
          <div class="city-hero-overlay"></div>
          <div class="city-hero-content">
            <div class="city-hero-badges">
              <span class="tag-badge">${p.region} Bölgesi</span>
              <span class="tag-badge">Plaka: ${String(p.plate).padStart(2, '0')}</span>
              ${statusBadge}
            </div>
            <h1 class="city-hero-title">📍 ${p.name}</h1>
          </div>
        </div>

        <!-- Quote Card -->
        <div class="glass-card detail-card">
          <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-gold); text-transform: uppercase; letter-spacing: 0.5px;">
            📜 Şehrin Ruhu & Tefekkür Notu
          </div>
          <p style="font-size: 1.05rem; font-style: italic; color: var(--text-primary); border-left: 3px solid var(--accent-cyan); padding-left: 14px; line-height: 1.6;">
            "${quoteText}"
          </p>
        </div>

        <!-- Landmarks & Specialties Grid -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
          <div class="glass-card detail-card">
            <h3 style="font-family: var(--font-heading); font-size: 1rem; color: var(--accent-cyan);">
              🏛️ Öne Çıkan Miras & Duraklar
            </h3>
            <div class="landmarks-list" style="grid-template-columns: 1fr;">
              ${landmarksHtml}
            </div>
          </div>

          <div class="glass-card detail-card">
            <h3 style="font-family: var(--font-heading); font-size: 1rem; color: var(--accent-gold);">
              🍽️ Yöresel Tatlar & Kültür
            </h3>
            <div class="tags-cloud">
              ${specialtiesHtml}
            </div>
            
            <div style="margin-top: 16px; border-top: 1px solid var(--border-glass); padding-top: 14px;">
              <h4 style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 6px;">
                🗺️ Koordinat Bilgisi
              </h4>
              <p style="font-family: monospace; font-size: 0.85rem; color: var(--accent-cyan);">
                ${p.lat.toFixed(4)}° K, ${p.lng.toFixed(4)}° D
              </p>
            </div>
          </div>
        </div>

        <!-- Library Nomad Card -->
        <div class="glass-card detail-card">
          <h3 style="font-family: var(--font-heading); font-size: 1rem; color: var(--accent-emerald); display: flex; align-items: center; gap: 8px;">
            📖 Seyyahın Kütüphane Ofisi (Çalışma Ortamı)
          </h3>
          <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
            ${libraryText}
          </p>
        </div>

        <!-- Actions -->
        <div style="display: flex; gap: 12px; justify-content: flex-end;">
          <a href="${p.readme_rel}" target="_blank" class="btn btn-primary">
            📄 Markdown Günlüğünü Görüntüle ➔
          </a>
          <button class="btn btn-outline" id="city-back-btn">
            ⬅️ Genel Bakışa Dön
          </button>
        </div>
      </div>
    `;

    const backBtn = document.getElementById('city-back-btn');
    if (backBtn) backBtn.addEventListener('click', renderDashboard);
  }

  // Render Route Planner View
  function renderRoutePlanner() {
    state.currentView = 'route';
    state.selectedCityKey = null;
    renderCitiesList();

    const visitedKeys = Object.keys(state.data.provinces).filter(k => state.data.provinces[k].visited);
    const optionsHtml = Object.entries(state.data.provinces).map(([k, p]) => `
      <option value="${p.name}" ${p.name === 'Ankara' ? 'selected' : ''}>${p.name} (${p.region})</option>
    `).join('');

    els.viewportContent.innerHTML = `
      <div class="dashboard-view">
        <div class="glass-card detail-card">
          <h2 style="font-family: var(--font-heading); font-size: 1.4rem; color: var(--accent-cyan); display: flex; align-items: center; gap: 10px;">
            🧭 Akıllı Rota Planlayıcı (Greedy Route Optimizer)
          </h2>
          <p style="font-size: 0.85rem; color: var(--text-secondary);">
            Seçtiğiniz başlangıç noktasından itibaren henüz ziyaret edilmemiş iller arasından en kısa karayolu mesafesine göre optimize edilmiş keşif rotası hesaplar.
          </p>

          <div style="display: flex; gap: 16px; margin-top: 16px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 200px;">
              <label style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">Başlangıç Şehri</label>
              <select id="route-start-select" class="region-select" style="margin-top: 4px;">
                ${optionsHtml}
              </select>
            </div>

            <div style="width: 140px;">
              <label style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">Durak Sayısı</label>
              <select id="route-stops-select" class="region-select" style="margin-top: 4px;">
                <option value="5">5 Durak</option>
                <option value="7" selected>7 Durak</option>
                <option value="10">10 Durak</option>
                <option value="15">15 Durak</option>
              </select>
            </div>

            <div style="display: flex; align-items: flex-end;">
              <button class="btn btn-primary" id="btn-calc-route">⚡ Rotayı Hesapla</button>
            </div>
          </div>
        </div>

        <div id="route-results-container"></div>
      </div>
    `;

    document.getElementById('btn-calc-route').addEventListener('click', calculateAndRenderRoute);
    calculateAndRenderRoute();
  }

  // Calculate Haversine Distance in JS
  function calcDistKm(lat1, lon1, lat2, lon2) {
    const R = 6371.0;
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
              Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
              Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return Math.round(R * c);
  }

  function calculateAndRenderRoute() {
    const startName = document.getElementById('route-start-select').value;
    const stopsCount = parseInt(document.getElementById('route-stops-select').value, 10);

    const allProvinces = Object.values(state.data.provinces);
    const startCity = allProvinces.find(p => p.name.toLowerCase() === startName.toLowerCase()) || allProvinces[0];
    const unvisited = allProvinces.filter(p => !p.visited);

    if (unvisited.length === 0) {
      document.getElementById('route-results-container').innerHTML = `
        <div class="glass-card detail-card" style="text-align: center; color: var(--accent-emerald);">
          🎉 Tebrikler! 81 ilin tamamı keşfedildi!
        </div>
      `;
      return;
    }

    let current = startCity;
    let remaining = [...unvisited];
    const route = [{ ...current, distFromPrev: 0 }];

    while (remaining.length > 0 && route.length <= stopsCount) {
      let nearest = remaining[0];
      let minDist = Infinity;
      for (const candidate of remaining) {
        const d = calcDistKm(current.lat, current.lng, candidate.lat, candidate.lng);
        if (d < minDist) {
          minDist = d;
          nearest = candidate;
        }
      }
      route.push({ ...nearest, distFromPrev: Math.round(minDist * 1.35) });
      remaining = remaining.filter(c => c.name !== nearest.name);
      current = nearest;
    }

    let totalKm = route.reduce((acc, curr) => acc + curr.distFromPrev, 0);

    const stopsHtml = route.map((stop, idx) => `
      <div class="glass-card" style="padding: 14px 18px; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 14px;">
          <div style="width: 32px; height: 32px; border-radius: 50%; background: ${idx === 0 ? 'var(--accent-cyan)' : 'rgba(30,41,59,0.9)'}; color: ${idx === 0 ? '#04121d' : 'var(--accent-cyan)'}; border: 1px solid var(--accent-cyan); display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.85rem;">
            ${idx + 1}
          </div>
          <div>
            <div style="font-family: var(--font-heading); font-weight: 700; font-size: 1rem; color: #ffffff;">
              ${stop.name} <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: normal;">(${stop.region})</span>
            </div>
            <div style="font-size: 0.75rem; color: var(--text-secondary);">
              📍 ${stop.landmarks ? stop.landmarks[0] : 'Tarihi Merkez'} • 🍽️ ${stop.specialties ? stop.specialties[0] : 'Lezzet'}
            </div>
          </div>
        </div>
        <div style="text-align: right;">
          <div style="font-family: var(--font-heading); font-weight: 700; color: var(--accent-gold); font-size: 0.9rem;">
            ${idx === 0 ? 'BAŞLANGIÇ' : `+${stop.distFromPrev} km`}
          </div>
        </div>
      </div>
    `).join('');

    document.getElementById('route-results-container').innerHTML = `
      <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 4px;">
          <h3 style="font-family: var(--font-heading); font-size: 1.1rem; color: var(--text-primary);">
            🗺️ Önerilen Yolculuk Planı (${route.length} Durak)
          </h3>
          <div style="font-family: var(--font-heading); font-weight: 700; color: var(--accent-emerald); font-size: 1rem;">
            Toplam: ${totalKm.toLocaleString()} km
          </div>
        </div>
        ${stopsHtml}
      </div>
    `;
  }

  // Web Audio API Ambient Synthesizer (Zero External Dependencies)
  function toggleAmbientSound() {
    if (state.ambientPlaying) {
      stopAmbientSound();
    } else {
      startAmbientSound();
    }
  }

  function startAmbientSound() {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!state.audioCtx) {
        state.audioCtx = new AudioCtx();
      }
      if (state.audioCtx.state === 'suspended') {
        state.audioCtx.resume();
      }

      // Master Gain
      const masterGain = state.audioCtx.createGain();
      masterGain.gain.setValueAtTime(0.08, state.audioCtx.currentTime);
      masterGain.connect(state.audioCtx.destination);

      // Ney Drone Oscillator (D Minor / Rast / Saba meditation frequency - 220Hz & 440Hz harmonics)
      const osc1 = state.audioCtx.createOscillator();
      osc1.type = 'sine';
      osc1.frequency.setValueAtTime(146.83, state.audioCtx.currentTime); // D3

      const osc2 = state.audioCtx.createOscillator();
      osc2.type = 'triangle';
      osc2.frequency.setValueAtTime(220.00, state.audioCtx.currentTime); // A3

      // Wind Pink Noise Buffer
      const bufferSize = state.audioCtx.sampleRate * 2;
      const noiseBuffer = state.audioCtx.createBuffer(1, bufferSize, state.audioCtx.sampleRate);
      const output = noiseBuffer.getChannelData(0);
      let b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
      for (let i = 0; i < bufferSize; i++) {
        const white = Math.random() * 2 - 1;
        b0 = 0.99886 * b0 + white * 0.0555179;
        b1 = 0.99332 * b1 + white * 0.0750759;
        b2 = 0.96900 * b2 + white * 0.1538520;
        b3 = 0.86650 * b3 + white * 0.3104856;
        b4 = 0.55000 * b4 + white * 0.5329522;
        b5 = -0.7616 * b5 - white * 0.0168980;
        output[i] = (b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362) * 0.04;
        b6 = white * 0.115926;
      }

      const whiteNoise = state.audioCtx.createBufferSource();
      whiteNoise.buffer = noiseBuffer;
      whiteNoise.loop = true;

      // Lowpass Filter for Gentle Bozkır Wind
      const filter = state.audioCtx.createBiquadFilter();
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(400, state.audioCtx.currentTime);

      whiteNoise.connect(filter);
      filter.connect(masterGain);
      osc1.connect(masterGain);
      osc2.connect(masterGain);

      osc1.start();
      osc2.start();
      whiteNoise.start();

      state.audioNodes = [osc1, osc2, whiteNoise, masterGain];
      state.ambientPlaying = true;

      if (els.btnAmbient) {
        els.btnAmbient.classList.add('active');
        els.btnAmbient.innerHTML = '🔊 Tefekkür Sesi: Açık';
      }
    } catch (err) {
      console.warn("Audio Context başlatılamadı:", err);
    }
  }

  function stopAmbientSound() {
    if (state.audioNodes) {
      state.audioNodes.forEach(n => {
        try { if (n.stop) n.stop(); if (n.disconnect) n.disconnect(); } catch (e) {}
      });
      state.audioNodes = [];
    }
    state.ambientPlaying = false;
    if (els.btnAmbient) {
      els.btnAmbient.classList.remove('active');
      els.btnAmbient.innerHTML = '🎧 Tefekkür Sesleri';
    }
  }

  // Export Markdown Book
  function exportMarkdownBook() {
    const visited = Object.values(state.data.provinces).filter(p => p.visited);
    let md = `# 🕌 ANADOLU SEYAHATNAMESİ: DİJİTAL SEYYAH KÜLLİYATI\n\n`;
    md += `> *"Biz yolların bitmediği, keşfin son bulmadığı bir alemde Hakikati ve Güzelliği arayan yolcularız."*\n\n---\n\n`;
    md += `## 📊 Seyahatname Özeti\n`;
    md += `* **Toplam Ziyaret Edilen İl:** ${state.data.stats.visited_cities} / 81\n`;
    md += `* **Keşif Oranı:** %${state.data.stats.progress_pct}\n`;
    md += `* **Kat Edilen Tahmini Mesafe:** ${state.data.stats.estimated_km.toLocaleString()} km\n\n---\n\n`;

    visited.forEach((p, idx) => {
      md += `## ${idx + 1}. 📍 ${p.name} (${String(p.plate).padStart(2, '0')}) - ${p.region}\n\n`;
      md += `> *"${p.custom_quote || p.quote}"*\n\n`;
      md += `### 🏛️ Öne Çıkan Miras\n`;
      (p.landmarks || []).forEach(lm => { md += `- [x] ${lm}\n`; });
      md += `\n### 🍽️ Yöresel Tatlar\n${(p.specialties || []).join(', ')}\n\n`;
      md += `### 📖 Kütüphane Ofisi\n${p.custom_library || p.library}\n\n---\n\n`;
    });

    const blob = new Blob([md], { type: 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'ANADOLU_SEYAHATNAMESI.md';
    a.click();
    URL.revokeObjectURL(url);
  }

  // Modal Helpers
  function openMapModal() {
    if (els.mapModal) els.mapModal.classList.add('active');
  }

  function closeModals() {
    document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('active'));
  }

  // Show Quote Popup
  function showRandomQuote() {
    const q = state.data.quotes[Math.floor(Math.random() * state.data.quotes.length)];
    alert(`📜 GÜNÜN TEFEKKÜRÜ:\n\n"${q.quote}"\n\n— ${q.author}`);
  }

  // Event Listeners
  function setupEventListeners() {
    if (els.logoSection) els.logoSection.addEventListener('click', renderDashboard);
    if (els.btnDashboard) els.btnDashboard.addEventListener('click', renderDashboard);
    if (els.btnMap) els.btnMap.addEventListener('click', openMapModal);
    if (els.btnRoute) els.btnRoute.addEventListener('click', renderRoutePlanner);
    if (els.btnAmbient) els.btnAmbient.addEventListener('click', toggleAmbientSound);
    if (els.btnQuote) els.btnQuote.addEventListener('click', showRandomQuote);
    if (els.btnExport) els.btnExport.addEventListener('click', exportMarkdownBook);

    els.modalCloseBtns.forEach(btn => btn.addEventListener('click', closeModals));

    // Search
    if (els.searchInput) {
      els.searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        renderCitiesList();
      });
    }

    // Region Selector
    if (els.regionSelect) {
      els.regionSelect.addEventListener('change', (e) => {
        state.selectedRegion = e.target.value;
        renderCitiesList();
      });
    }

    // Filter Pills
    els.filterPills.forEach(pill => {
      pill.addEventListener('click', () => {
        els.filterPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state.filter = pill.getAttribute('data-filter');
        renderCitiesList();
      });
    });
  }

  // Run
  document.addEventListener('DOMContentLoaded', init);
})();
