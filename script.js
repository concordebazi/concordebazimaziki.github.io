/* =====================================================
   Concorde Bazimaziki — portfolio scripts
===================================================== */
document.documentElement.classList.add("js");

/* ---------- Translations (English / Svenska) ---------- */
const i18n = {
  en: {
    navAbout: "About", navExperience: "Experience", navExpertise: "Expertise", navProjects: "Projects", navContact: "Contact",
    heroRole: "GIS Engineer & Geomatics Specialist",
    heroLede: "I build maps, spatial analyses and Web GIS applications that turn location data into clear decisions, with a background in hydrographic survey and nautical charting.",
    btnCv: "Download CV", btnContact: "Get in touch", nowAt: "Open to GIS roles",
    labelAbout: "About", aboutTitle: "GIS professional, from raw data to finished map",
    focus1: "Spatial analysis", focus2: "Web GIS", focus3: "Spatial databases", focus4: "Terrain & raster analysis", focus5: "Cartography", focus6: "Data quality control",
    labelExperience: "Experience", experienceTitle: "Where I have worked",
    labelExpertise: "Expertise", expertiseTitle: "What I work with",
    area1: "Hydrographic processing", area1Text: "Multibeam bathymetry, side-scan sonar and backscatter, from raw soundings to cleaned surfaces.",
    area2: "GIS & cartography", area2Text: "Spatial analysis, geographic databases and map production, from planning maps to nautical charts.",
    area3: "Python & analysis", area3Text: "Raster and terrain analysis, automation and data APIs that make geospatial workflows repeatable.",
    area4: "Web GIS", area4Text: "Interactive map applications with layers, filters, search, routing, heatmaps and drawing tools.",
    labelProjects: "Projects", projectsTitle: "Web GIS projects you can try",
    featKicker: "Featured · Terrain analysis",
    featText: "A Web GIS for municipal planning in central Linköping. I processed Lantmäteriet's national elevation model in Python to derive terrain elevation, slope, surface depressions and low points, then modelled illustrative water-level scenarios for the Stångån river. The results are served as interactive layers with a GIS screening of each area.",
    openDemo: "Open live demo",
    d1: "Interactive business map", d1Text: "Business locations with category filters, map layers, search, drawing tools and proximity analysis.",
    d2: "Delivery zone analysis", d2Text: "Delivery zones, demand heatmaps, order grouping and road-network routing for local restaurants.",
    d3: "Mobile service routing", d3Text: "Customer bookings assigned to mobile mechanics, with optimised driving routes and live tracking.",
    d4: "Project and fleet planning", d4Text: "Allocates teams and machines to project sites using real road distances.",
    moreWork: "More web and GIS demos, including websites built for local businesses, are on",
    labelWork: "Work", workTitle: "In the field and on screen",
    g1: "Offshore survey operations", g2: "Bathymetric surface", g3: "Data processing & QC", g4: "GIS analysis",
    mapTitle: "Career map", mapText: "Places connected to my education and career, from Kigali to the Swedish west coast.",
    labelContact: "Contact", contactTitle: "Let's work together",
    contactText: "I am available for GIS roles in Sweden. Get in touch about GIS analysis, Web GIS or geospatial data projects.",
    email: "Email", location: "Location", copy: "Copy", copied: "Copied", backTop: "Back to top ↑",
    skip: "Skip to content",
    eyebrow: "57.71° N · 11.97° E — Gothenburg, Sweden",
    about1: "I am a Geomatics Engineer with a Master's degree in Geomatics from Lund University. I have worked with GIS since 2009: mapping mineral resources and managing geological databases in Rwanda, supporting urban development projects in Gothenburg, and producing nautical charts at the Swedish Maritime Administration.",
    about2: "My GIS work covers the whole chain: collecting and cleaning data, managing spatial databases, running analysis in ArcGIS Pro, QGIS and Python, and presenting results as clear maps and interactive web applications. I use Python with rasterio, NumPy and SciPy for raster and terrain analysis, and Leaflet and JavaScript to build Web GIS tools with routing, heatmaps, filtering and proximity analysis.",
    eduMsc: "Geomatics",
    eduLund: "Lund University, Sweden",
    eduBsc: "Geography, Environment & Development",
    date1: "Feb 2025 – Oct 2026",
    date2: "Mar 2021 – Mar 2025",
    date3: "Apr – Oct 2017",
    date4: "Jan 2009 – Jun 2013",
    job2: "Map Engineer",
    job3: "GIS Engineer",
    job4: "GIS & Geospatial Officer",
    org1: "Ocean Infinity AB · Gothenburg",
    org2: "Swedish Maritime Administration",
    org3: "Älvstranden Utveckling AB · Gothenburg",
    j1a: "Processed offshore hydrographic survey data from acquisition to final delivery",
    j1b: "Cleaned, validated and quality-controlled multibeam echo sounder (MBES) data",
    j1c: "Processed backscatter data",
    j1d: "Delivered marine data products to client and project specifications",
    j2a: "Hydrographic database management",
    j2b: "Nautical chart production and marine cartography",
    j2c: "Quality control of depth data",
    j3a: "GIS analysis and mapping solutions",
    j3b: "Spatial database administration",
    j4a: "Mineral resource mapping and geological GIS databases",
    j4b: "Permit management systems",
    j4c: "Cartographic production",
    tagSpatialDb: "Spatial databases",
    tagCharting: "Nautical charting",
    tagOsrm: "OSRM routing",
    tagDem: "Lantmäteriet DEM",
    type2: "GIS · Delivery analysis",
    type3: "GIS · Route planning",
    type4: "GIS · Resource planning",
    city: "Gothenburg, Sweden",
    cvEn: "English (PDF)",
    about3: "Most recently I processed multibeam and backscatter data at Ocean Infinity in Gothenburg, until the company closed its Swedish office in October 2026. I also run <a href=\"https://cbwebgis.se/\" target=\"_blank\" rel=\"noopener\">CB Web &amp; GIS</a>, where I design and build Web GIS demos and map applications. I am now looking for GIS roles where I can combine analysis, data management and web mapping.",
    altPortrait: "Portrait of Concorde Bazimaziki",
    altVessel: "Offshore survey vessel at sea",
    altBathy: "3D bathymetric surface of the seabed",
    altProc: "Hydrographic processing software showing a seabed profile",
    altGis: "GIS map with point data over a city",
    ariaMain: "Main",
    ariaLang: "Language",
    ariaMenu: "Open menu",
    ariaFocus: "GIS focus areas",
    ariaMap: "Map of career locations",
    docTitle: "Concorde Bazimaziki | GIS Engineer & Geomatics Specialist",
    popUR: "BSc Geography, Environment and Development",
    popRMB: "GIS & Geospatial Officer, 2009–2013",
    popLund: "MSc Geomatics",
    popAlv: "GIS Engineer, 2017",
    popSMA: "Map Engineer, 2021–2025",
    popOI: "Hydrographic Data Processor, 2025–2026",
    popOIname: "Ocean Infinity, Gothenburg",
    popSMAname: "Swedish Maritime Administration",
    popLundName: "Lund University"
  },
  sv: {
    navAbout: "Om mig", navExperience: "Erfarenhet", navExpertise: "Kompetens", navProjects: "Projekt", navContact: "Kontakt",
    heroRole: "GIS-ingenjör & geomatikspecialist",
    heroLede: "Jag bygger kartor, rumsliga analyser och Web GIS-applikationer som gör geodata till tydliga beslutsunderlag, med bakgrund inom hydrografisk mätning och sjökortsproduktion.",
    btnCv: "Ladda ner CV", btnContact: "Kontakta mig", nowAt: "Öppen för GIS-roller",
    labelAbout: "Om mig", aboutTitle: "GIS-specialist, från rådata till färdig karta",
    focus1: "Rumslig analys", focus2: "Web GIS", focus3: "Geodatabaser", focus4: "Terräng- & rasteranalys", focus5: "Kartografi", focus6: "Kvalitetskontroll av data",
    labelExperience: "Erfarenhet", experienceTitle: "Där jag har arbetat",
    labelExpertise: "Kompetens", expertiseTitle: "Det jag arbetar med",
    area1: "Hydrografisk databehandling", area1Text: "Multibeam-batymetri, sidescan-sonar och backscatter, från råa lodningar till rensade ytor.",
    area2: "GIS & kartografi", area2Text: "Rumslig analys, geografiska databaser och kartproduktion, från planeringskartor till sjökort.",
    area3: "Python & analys", area3Text: "Raster- och terränganalys, automatisering och data-API:er som gör geodataflöden repeterbara.",
    area4: "Web GIS", area4Text: "Interaktiva kartapplikationer med lager, filter, sök, ruttplanering, värmekartor och ritverktyg.",
    labelProjects: "Projekt", projectsTitle: "Web GIS-projekt att testa",
    featKicker: "Utvalt · Terränganalys",
    featText: "En Web GIS för kommunal planering i centrala Linköping. Jag bearbetade Lantmäteriets markhöjdmodell i Python för att ta fram markhöjd, lutning, sänkor och lågpunkter, och modellerade illustrativa vattennivåscenarier för Stångån. Resultaten visas som interaktiva lager med en GIS-screening av varje område.",
    openDemo: "Öppna live-demo",
    d1: "Interaktiv företagskarta", d1Text: "Företagsplatser med kategorifilter, kartlager, sökfunktion, ritverktyg och närhetsanalys.",
    d2: "Analys av leveranszoner", d2Text: "Leveranszoner, efterfrågevärmekartor, ordergruppering och ruttplanering i vägnätet för lokala restauranger.",
    d3: "Ruttplanering för mobil service", d3Text: "Kundbokningar fördelas till mobila mekaniker med optimerade körvägar och liveuppföljning.",
    d4: "Projekt- och maskinplanering", d4Text: "Fördelar team och maskiner till projektplatser utifrån verkliga vägavstånd.",
    moreWork: "Fler webb- och GIS-demon, bland annat webbplatser för lokala företag, finns på",
    labelWork: "Arbete", workTitle: "Till havs och vid skärmen",
    g1: "Offshore-undersökningar", g2: "Batymetrisk yta", g3: "Databehandling & QC", g4: "GIS-analys",
    mapTitle: "Karriärkarta", mapText: "Platser kopplade till min utbildning och karriär, från Kigali till svenska västkusten.",
    labelContact: "Kontakt", contactTitle: "Låt oss arbeta tillsammans",
    contactText: "Jag är tillgänglig för GIS-roller i Sverige. Hör av dig om GIS-analys, Web GIS eller geodataprojekt.",
    email: "E-post", location: "Ort", copy: "Kopiera", copied: "Kopierat", backTop: "Till toppen ↑",
    skip: "Hoppa till innehållet",
    eyebrow: "57.71° N · 11.97° E — Göteborg, Sverige",
    about1: "Jag är geomatikingenjör med masterexamen i geomatik från Lunds universitet. Jag har arbetat med GIS sedan 2009: med kartläggning av mineralresurser och geologiska databaser i Rwanda, stöd till stadsutvecklingsprojekt i Göteborg och sjökortsproduktion på Sjöfartsverket.",
    about2: "Mitt GIS-arbete täcker hela kedjan: insamling och rensning av data, hantering av geodatabaser, analyser i ArcGIS Pro, QGIS och Python samt presentation av resultat som tydliga kartor och interaktiva webbapplikationer. Jag använder Python med rasterio, NumPy och SciPy för raster- och terränganalys, och Leaflet och JavaScript för att bygga Web GIS-verktyg med ruttplanering, värmekartor, filtrering och närhetsanalys.",
    eduMsc: "Geomatik",
    eduLund: "Lunds universitet",
    eduBsc: "Geografi, miljö och utveckling",
    date1: "feb 2025 – okt 2026",
    date2: "mar 2021 – mar 2025",
    date3: "apr – okt 2017",
    date4: "jan 2009 – jun 2013",
    job2: "Kartingenjör",
    job3: "GIS-ingenjör",
    job4: "GIS- och geodatahandläggare",
    org1: "Ocean Infinity AB · Göteborg",
    org2: "Sjöfartsverket",
    org3: "Älvstranden Utveckling AB · Göteborg",
    j1a: "Bearbetade hydrografiska mätdata från offshore-undersökningar, från insamling till slutleverans",
    j1b: "Rensade, validerade och kvalitetskontrollerade multibeamdata (MBES)",
    j1c: "Bearbetade backscatterdata",
    j1d: "Levererade marina dataprodukter enligt kund- och projektspecifikationer",
    j2a: "Hantering av hydrografiska databaser",
    j2b: "Sjökortsproduktion och marin kartografi",
    j2c: "Kvalitetskontroll av djupdata",
    j3a: "GIS-analyser och kartlösningar",
    j3b: "Administration av geodatabaser",
    j4a: "Kartläggning av mineralresurser och geologiska GIS-databaser",
    j4b: "System för tillståndshantering",
    j4c: "Kartproduktion",
    tagSpatialDb: "Geodatabaser",
    tagCharting: "Sjökortsproduktion",
    tagOsrm: "OSRM-ruttplanering",
    tagDem: "Lantmäteriets höjdmodell",
    type2: "GIS · Leveransanalys",
    type3: "GIS · Ruttplanering",
    type4: "GIS · Resursplanering",
    city: "Göteborg, Sverige",
    cvEn: "Engelska (PDF)",
    about3: "Senast bearbetade jag multibeam- och backscatterdata på Ocean Infinity i Göteborg, tills företaget stängde sitt svenska kontor i oktober 2026. Jag driver också <a href=\"https://cbwebgis.se/\" target=\"_blank\" rel=\"noopener\">CB Web &amp; GIS</a>, där jag utformar och bygger Web GIS-demon och kartapplikationer. Nu söker jag GIS-roller där jag kan kombinera analys, datahantering och webbkartor.",
    altPortrait: "Porträtt av Concorde Bazimaziki",
    altVessel: "Mätfartyg till havs",
    altBathy: "Tredimensionell batymetrisk yta av havsbotten",
    altProc: "Programvara för hydrografisk databehandling med en havsbottenprofil",
    altGis: "GIS-karta med punktdata över en stad",
    ariaMain: "Huvudmeny",
    ariaLang: "Språk",
    ariaMenu: "Öppna menyn",
    ariaFocus: "GIS-fokusområden",
    ariaMap: "Karta över platser i min karriär",
    docTitle: "Concorde Bazimaziki | GIS-ingenjör & geomatikspecialist",
    popUR: "Kandidatexamen i geografi, miljö och utveckling",
    popRMB: "GIS- och geodatahandläggare, 2009–2013",
    popLund: "Masterexamen i geomatik",
    popAlv: "GIS-ingenjör, 2017",
    popSMA: "Kartingenjör, 2021–2025",
    popOI: "Hydrographic Data Processor, 2025–2026",
    popOIname: "Ocean Infinity, Göteborg",
    popSMAname: "Sjöfartsverket",
    popLundName: "Lunds universitet"
  }
};

let currentLang = "en";
let updateMapPopups = null;

function setLanguage(lang) {
  if (!i18n[lang]) lang = "en";
  currentLang = lang;
  document.documentElement.lang = lang;
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const text = i18n[lang][el.dataset.i18n];
    if (text) el.textContent = text;
  });
  document.querySelectorAll("[data-i18n-html]").forEach(el => {
    const markup = i18n[lang][el.dataset.i18nHtml];
    if (markup) el.innerHTML = markup;
  });
  document.querySelectorAll("[data-i18n-alt]").forEach(el => {
    const text = i18n[lang][el.dataset.i18nAlt];
    if (text) el.alt = text;
  });
  document.querySelectorAll("[data-i18n-aria]").forEach(el => {
    const text = i18n[lang][el.dataset.i18nAria];
    if (text) el.setAttribute("aria-label", text);
  });
  document.title = i18n[lang].docTitle;
  if (updateMapPopups) updateMapPopups();
  document.querySelectorAll(".lang button").forEach(btn => {
    btn.setAttribute("aria-pressed", String(btn.dataset.lang === lang));
  });
  const cvButton = document.querySelector(".hero .btn-primary");
  if (cvButton) cvButton.href = lang === "sv" ? "cv/Concorde_Bazimaziki_CV_SV.pdf" : "cv/Concorde_Bazimaziki_CV_EN.pdf";
  try { localStorage.setItem("language", lang); } catch (e) {}
}

document.querySelectorAll(".lang button").forEach(btn => {
  btn.addEventListener("click", () => setLanguage(btn.dataset.lang));
});

(function initLanguage() {
  let saved = null;
  try { saved = localStorage.getItem("language"); } catch (e) {}
  const browser = (navigator.language || "en").toLowerCase();
  const lang = saved || (browser.startsWith("sv") ? "sv" : "en");
  if (lang !== "en") setLanguage(lang);
  else document.documentElement.lang = "en";
})();

/* ---------- Mobile menu ---------- */
const menuBtn = document.querySelector(".menu-btn");
const nav = document.getElementById("nav");

function closeMenu() {
  nav.classList.remove("open");
  menuBtn.setAttribute("aria-expanded", "false");
}
menuBtn.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  menuBtn.setAttribute("aria-expanded", String(open));
});
nav.querySelectorAll("a").forEach(a => a.addEventListener("click", closeMenu));
document.addEventListener("keydown", e => { if (e.key === "Escape") closeMenu(); });

/* ---------- Header style + active section ---------- */
const header = document.querySelector(".site-header");
const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 40);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

const navLinks = [...nav.querySelectorAll("a")];
const sectionObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    navLinks.forEach(a => a.classList.toggle("active", a.getAttribute("href") === "#" + entry.target.id));
  });
}, { rootMargin: "-45% 0px -50% 0px" });
document.querySelectorAll("main section[id]").forEach(s => sectionObserver.observe(s));

/* ---------- Reveal on scroll ---------- */
const revealTargets = document.querySelectorAll(".section h2, .about-body, .job, .skill-area, .feature, .demo, .shot, .journey, .contact-card");
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("in");
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
revealTargets.forEach(el => {
  // Anything already on screen stays visible immediately
  if (el.getBoundingClientRect().top < window.innerHeight) return;
  el.classList.add("reveal");
  revealObserver.observe(el);
});

/* ---------- Copy email ---------- */
const copyBtn = document.getElementById("copy-email");
copyBtn.addEventListener("click", async () => {
  const email = document.getElementById("email").textContent.trim();
  try {
    await navigator.clipboard.writeText(email);
  } catch (e) {
    const range = document.createRange();
    range.selectNodeContents(document.getElementById("email"));
    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    return;
  }
  copyBtn.textContent = i18n[currentLang].copied;
  setTimeout(() => { copyBtn.textContent = i18n[currentLang].copy; }, 1800);
});

/* ---------- Footer year ---------- */
document.getElementById("year").textContent = new Date().getFullYear();

/* ---------- Career map ---------- */
(function initMap() {
  const el = document.getElementById("map");
  if (!el || typeof L === "undefined") return;

  const map = L.map(el, { scrollWheelZoom: false });
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution: "© OpenStreetMap contributors"
  }).addTo(map);

  const icon = L.divIcon({ className: "", html: '<div class="pin"></div>', iconSize: [16, 16], iconAnchor: [8, 8] });

  const places = [
    { name: "University of Rwanda", coords: [-1.95, 30.06], text: "popUR" },
    { name: "Rwanda Mines, Petroleum and Gas Board", coords: [-1.93, 30.10], text: "popRMB" },
    { name: "popLundName", coords: [55.71, 13.20], text: "popLund" },
    { name: "Älvstranden Utveckling AB", coords: [57.70, 11.94], text: "popAlv" },
    { name: "popSMAname", coords: [58.59, 16.18], text: "popSMA" },
    { name: "popOIname", coords: [57.71, 11.97], text: "popOI" }
  ];
  const t = key => i18n[currentLang][key] || key;
  const markers = [];

  const bounds = [];
  const popupHtml = p => `<strong>${t(p.name)}</strong><p>${t(p.text)}</p>`;
  places.forEach(p => {
    markers.push([L.marker(p.coords, { icon }).addTo(map).bindPopup(popupHtml(p)), p]);
    bounds.push(p.coords);
  });
  updateMapPopups = () => markers.forEach(([m, p]) => m.setPopupContent(popupHtml(p)));
  map.fitBounds(bounds, { padding: [40, 40] });
})();

/* ---------- Hero: animated depth contours ---------- */
(function initContours() {
  const canvas = document.querySelector(".hero-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const STEP = 14;
  const LEVELS = 14;
  let w = 0, h = 0, dpr = 1, t = 0, running = true, last = 0;

  // Sounding labels, like depths printed on a nautical chart
  let soundings = [];

  function resize() {
    const rect = canvas.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = rect.width; h = rect.height;
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    soundings = Array.from({ length: Math.round((w * h) / 26000) }, () => ({ x: Math.random() * w, y: Math.random() * h }));
    draw();
  }

  function field(x, y) {
    const nx = x / 260, ny = y / 260;
    return Math.sin(nx * 1.3 + t * 0.6) * Math.cos(ny * 1.1 - t * 0.4)
      + 0.6 * Math.sin((nx + ny) * 1.7 + t * 0.3)
      + 0.4 * Math.cos(nx * 2.6 - ny * 1.9 + t * 0.5)
      + 0.9 * (x / w);  // deepening toward the right
  }

  function depthAt(x, y) {
    return Math.round(12 + (field(x, y) + 2) * 21);
  }

  function lerp(a, b, va, vb, level) {
    const k = (level - va) / (vb - va || 1e-6);
    return a + (b - a) * k;
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    const cols = Math.ceil(w / STEP) + 1, rows = Math.ceil(h / STEP) + 1;
    const values = new Float32Array(cols * rows);
    let min = Infinity, max = -Infinity;
    for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
      const v = field(i * STEP, j * STEP);
      values[j * cols + i] = v;
      if (v < min) min = v;
      if (v > max) max = v;
    }

    for (let l = 1; l < LEVELS; l++) {
      const level = min + (max - min) * (l / LEVELS);
      const f = l / LEVELS;
      const major = l % 4 === 0;
      ctx.strokeStyle = `rgba(${Math.round(60 + 80 * (1 - f))}, ${Math.round(195 - 40 * f)}, ${Math.round(223 - 20 * f)}, ${major ? 0.42 : 0.18})`;
      ctx.lineWidth = major ? 1.3 : 0.8;
      ctx.beginPath();
      for (let j = 0; j < rows - 1; j++) for (let i = 0; i < cols - 1; i++) {
        const x = i * STEP, y = j * STEP;
        const a = values[j * cols + i], b = values[j * cols + i + 1];
        const c = values[(j + 1) * cols + i + 1], d = values[(j + 1) * cols + i];
        const idx = (a > level ? 8 : 0) | (b > level ? 4 : 0) | (c > level ? 2 : 0) | (d > level ? 1 : 0);
        if (idx === 0 || idx === 15) continue;
        const top = [lerp(x, x + STEP, a, b, level), y];
        const right = [x + STEP, lerp(y, y + STEP, b, c, level)];
        const bottom = [lerp(x, x + STEP, d, c, level), y + STEP];
        const left = [x, lerp(y, y + STEP, a, d, level)];
        let segs;
        switch (idx) {
          case 1: case 14: segs = [left, bottom]; break;
          case 2: case 13: segs = [bottom, right]; break;
          case 3: case 12: segs = [left, right]; break;
          case 4: case 11: segs = [top, right]; break;
          case 5: segs = [left, top, bottom, right]; break;
          case 6: case 9: segs = [top, bottom]; break;
          case 7: case 8: segs = [left, top]; break;
          case 10: segs = [left, bottom, top, right]; break;
        }
        for (let s = 0; s < segs.length; s += 2) {
          ctx.moveTo(segs[s][0], segs[s][1]);
          ctx.lineTo(segs[s + 1][0], segs[s + 1][1]);
        }
      }
      ctx.stroke();
    }

    ctx.font = "10px 'IBM Plex Mono', monospace";
    ctx.fillStyle = "rgba(159, 183, 199, 0.38)";
    soundings.forEach(s => ctx.fillText(depthAt(s.x, s.y), s.x, s.y));
  }

  function loop(now) {
    if (!running) return;
    if (now - last > 60) {
      t += 0.012;
      draw();
      last = now;
    }
    requestAnimationFrame(loop);
  }

  window.addEventListener("resize", resize);
  resize();

  if (!reduceMotion) {
    new IntersectionObserver(([entry]) => {
      const visible = entry.isIntersecting;
      if (visible && !running) { running = true; requestAnimationFrame(loop); }
      if (!visible) running = false;
    }).observe(canvas);
    requestAnimationFrame(loop);
  }
})();
