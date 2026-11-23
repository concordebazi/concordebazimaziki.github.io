/* =====================================================
   Concorde Bazimaziki — portfolio scripts
===================================================== */
document.documentElement.classList.add("js");

/* ---------- Translations (English / Svenska) ---------- */
const i18n = {
  en: {
    navAbout: "About", navExperience: "Experience", navExpertise: "Expertise", navWork: "Work", navContact: "Contact",
    heroRole: "Hydrographic Data Processor & Geomatics Engineer",
    heroLede: "I turn raw multibeam, backscatter and survey data into accurate seabed models, nautical charts and GIS products for offshore and marine projects.",
    btnCv: "Download CV", btnContact: "Get in touch", nowAt: "Now at Ocean Infinity",
    labelAbout: "About", aboutTitle: "From survey line to finished chart",
    labelExperience: "Experience", experienceTitle: "Where I have worked", present: "Present",
    labelExpertise: "Expertise", expertiseTitle: "What I work with",
    area1: "Hydrographic processing", area1Text: "Multibeam bathymetry, side-scan sonar and backscatter, from raw soundings to cleaned surfaces.",
    area2: "GIS & cartography", area2Text: "Spatial analysis, geographic databases and map production, including nautical charts.",
    area3: "Data & automation", area3Text: "Quality control, validation and scripting to make geospatial workflows repeatable.",
    labelWork: "Work", workTitle: "In the field and on screen",
    g1: "Offshore survey operations", g2: "Bathymetric surface", g3: "Data processing & QC", g4: "GIS analysis",
    mapTitle: "Career map", mapText: "Places connected to my education and career, from Kigali to the Swedish west coast.",
    labelContact: "Contact", contactTitle: "Let's talk about your survey data",
    contactText: "Open to conversations about hydrographic processing, GIS and marine geospatial projects.",
    email: "Email", location: "Location", copy: "Copy", copied: "Copied", backTop: "Back to top ↑"
  },
  sv: {
    navAbout: "Om mig", navExperience: "Erfarenhet", navExpertise: "Kompetens", navWork: "Arbete", navContact: "Kontakt",
    heroRole: "Hydrographic Data Processor & geomatikingenjör",
    heroLede: "Jag omvandlar rå multibeam-, backscatter- och mätdata till noggranna havsbottenmodeller, sjökort och GIS-produkter för offshore- och marina projekt.",
    btnCv: "Ladda ner CV", btnContact: "Kontakta mig", nowAt: "Nu på Ocean Infinity",
    labelAbout: "Om mig", aboutTitle: "Från mätlinje till färdigt sjökort",
    labelExperience: "Erfarenhet", experienceTitle: "Där jag har arbetat", present: "Nu",
    labelExpertise: "Kompetens", expertiseTitle: "Det jag arbetar med",
    area1: "Hydrografisk databehandling", area1Text: "Multibeam-batymetri, sidescan-sonar och backscatter, från råa lodningar till rensade ytor.",
    area2: "GIS & kartografi", area2Text: "Rumslig analys, geografiska databaser och kartproduktion, inklusive sjökort.",
    area3: "Data & automatisering", area3Text: "Kvalitetskontroll, validering och skript som gör geodataflöden repeterbara.",
    labelWork: "Arbete", workTitle: "Till havs och vid skärmen",
    g1: "Offshore-undersökningar", g2: "Batymetrisk yta", g3: "Databehandling & QC", g4: "GIS-analys",
    mapTitle: "Karriärkarta", mapText: "Platser kopplade till min utbildning och karriär, från Kigali till svenska västkusten.",
    labelContact: "Kontakt", contactTitle: "Låt oss prata om era mätdata",
    contactText: "Öppen för samtal om hydrografisk databehandling, GIS och marina geodataprojekt.",
    email: "E-post", location: "Ort", copy: "Kopiera", copied: "Kopierat", backTop: "Till toppen ↑"
  }
};

let currentLang = "en";

function setLanguage(lang) {
  if (!i18n[lang]) lang = "en";
  currentLang = lang;
  document.documentElement.lang = lang;
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const text = i18n[lang][el.dataset.i18n];
    if (text) el.textContent = text;
  });
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
const revealTargets = document.querySelectorAll(".section h2, .about-body, .job, .skill-area, .shot, .journey, .contact-card");
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
    { name: "University of Rwanda", coords: [-1.95, 30.06], text: "BSc Geography, Environment and Development" },
    { name: "Rwanda Mines, Petroleum and Gas Board", coords: [-1.93, 30.10], text: "GIS & Geospatial Officer, 2009–2013" },
    { name: "Lund University", coords: [55.71, 13.20], text: "MSc Geomatics" },
    { name: "Älvstranden Utveckling AB", coords: [57.70, 11.94], text: "GIS Engineer, 2017" },
    { name: "Swedish Maritime Administration", coords: [58.59, 16.18], text: "Map Engineer, 2021–2025" },
    { name: "Ocean Infinity, Gothenburg", coords: [57.71, 11.97], text: "Hydrographic Data Processor, 2025–present" }
  ];

  const bounds = [];
  places.forEach(p => {
    L.marker(p.coords, { icon }).addTo(map)
      .bindPopup(`<strong>${p.name}</strong><p>${p.text}</p>`);
    bounds.push(p.coords);
  });
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
