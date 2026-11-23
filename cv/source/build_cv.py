"""Build Concorde Bazimaziki's CV (English + Swedish) as HTML, then PDF.

Usage (from the repository root):
    python3 cv/source/build_cv.py          # writes cv/source/cv_en.html, cv_sv.html
    node cv/source/render_pdf.js           # renders cv/*.pdf from those files

Edit the CONTENT dictionaries below to change the CV text.
"""
from html import escape
from pathlib import Path

HERE = Path(__file__).parent

LINKS = {
    "email": ("concorde2007@gmail.com", "mailto:concorde2007@gmail.com"),
    "phone": ("+46 73 774 62 65", "tel:+46737746265"),
    "linkedin": ("linkedin.com/in/concorde-bazimaziki-70046b34", "https://www.linkedin.com/in/concorde-bazimaziki-70046b34/"),
    "portfolio": ("concordebazi.github.io/concordebazimaziki.github.io", "https://concordebazi.github.io/concordebazimaziki.github.io/"),
    "github": ("github.com/concordebazi", "https://github.com/concordebazi"),
    "cbweb": ("cbwebgis.se", "https://cbwebgis.se/"),
}
DEMOS = "https://concordebazi.github.io/CB-WebGIS-Demos/"

CONTENT = {
    "en": {
        "lang": "en",
        "title": "GIS Engineer & Geomatics Specialist",
        "location": "Gothenburg, Sweden",
        "citizenship": "Swedish and Rwandan citizen",
        "labels": {
            "contact": "Contact", "links": "Links", "profile": "Profile", "experience": "Experience",
            "projects": "Web GIS projects", "education": "Education", "skills": "Skills",
            "languages": "Languages", "personal": "Personal qualities", "references": "References",
            "email": "Email", "phone": "Phone", "location": "Location", "portfolio": "Portfolio",
            "website": "Company website", "live": "Live demo", "all_demos": "All demos",
        },
        "profile": [
            "Geomatics Engineer with an MSc from Lund University and GIS experience since 2009 across mining, urban development, national nautical charting and offshore survey. I work across the whole geospatial chain: collecting and cleaning data, managing spatial databases, running analysis in ArcGIS Pro, QGIS and Python, and delivering clear maps and interactive Web GIS applications.",
            "Known for accuracy and quality control from years of hydrographic data processing, and for building practical Web GIS tools through my own studio, CB Web & GIS. I am now looking for a GIS role where I can combine spatial analysis, data management and web mapping.",
        ],
        "jobs": [
            {
                "role": "Hydrographic Data Processor",
                "org": "Ocean Infinity AB", "place": "Gothenburg",
                "dates": "Feb 2025 – Oct 2026",
                "note": "Role ended when the company closed its Swedish office.",
                "bullets": [
                    "Processed hydrographic survey data from acquisition to final delivery.",
                    "Performed quality control, validation and cleaning of MBES and backscatter data.",
                    "Worked in CARIS HIPS, QPS Qimera, FMGT, EIVA NaviModel and Qinsy.",
                    "Made sure deliverables met project requirements, client specifications and internal quality standards.",
                    "Worked with senior data processors, offshore teams and international project groups on MBES, SSS and geophysical projects.",
                    "Documented workflows, checks and results.",
                ],
            },
            {
                "role": "Map Engineer, Hydrographic Data Processing",
                "org": "Swedish Maritime Administration (Sjöfartsverket)", "place": "Sweden",
                "dates": "Mar 2021 – Mar 2025",
                "bullets": [
                    "Processed and quality-controlled hydrographic survey data for nautical chart products.",
                    "Cleaned, analysed and validated depth data.",
                    "Worked with geographic databases and the production of geospatial information.",
                    "Managed and checked survey data against technical standards and requirements.",
                    "Contributed to the development and quality assurance of nautical chart data.",
                ],
            },
            {
                "role": "GIS Engineer",
                "org": "Älvstranden Utveckling AB", "place": "Gothenburg",
                "dates": "Apr 2017 – Oct 2017",
                "bullets": [
                    "Handled GIS data management, map production and geographic analysis.",
                    "Produced maps and GIS-based decision support.",
                    "Updated and administered geographic databases.",
                    "Supported the organisation with GIS questions and analysis.",
                ],
            },
            {
                "role": "GIS Specialist / Information Officer, Mining and Mineral Data",
                "org": "Rwanda Mines, Petroleum and Gas Board", "place": "Kigali, Rwanda",
                "dates": "Jan 2009 – Jun 2013",
                "bullets": [
                    "Produced maps of mineral resources and geographic information.",
                    "Mapped geological, geochemical and geophysical data together with geologists.",
                    "Contributed to geological maps and national geodatabases.",
                    "Managed databases of mining licences and permit data, and tracked permit status.",
                    "Reviewed documentation following standard procedures and reported permit status to management.",
                ],
            },
        ],
        "projects": [
            {
                "name": "GeoRisk AI", "slug": "georisk-ai/",
                "text": "Web GIS for municipal planning in central Linköping. Processed Lantmäteriet's elevation model in Python to derive elevation, slope, depressions and low points, with illustrative water-level scenarios for the Stångån river.",
                "tech": "Python · rasterio · NumPy · SciPy · FastAPI · Leaflet",
            },
            {
                "name": "Interactive business map", "slug": "business-map/",
                "text": "Business locations with category filters, map layers, search, drawing tools and proximity analysis.",
                "tech": "Leaflet · Leaflet.draw · JavaScript",
            },
            {
                "name": "Delivery zone analysis", "slug": "pizza-delivery/",
                "text": "Delivery zones, demand heatmaps, order grouping and road-network routing.",
                "tech": "Leaflet.heat · OSRM",
            },
            {
                "name": "Route and resource planning", "slug": "smart-projektplanering/",
                "text": "Assigns teams, vehicles and machines to sites using real road distances and optimised routes.",
                "tech": "Leaflet · OSRM",
            },
        ],
        "education": [
            ("MSc in Geomatics", "Lund University, Sweden"),
            ("BSc in Geography, Environment and Development", "University of Rwanda"),
        ],
        "skills": [
            ("GIS and geodata", ["GIS analysis", "Spatial databases", "Digital map production", "Cartography", "Spatial data management", "Terrain and raster analysis"]),
            ("Web GIS and programming", ["Python (rasterio, NumPy, SciPy)", "FastAPI", "Leaflet", "JavaScript", "SQL", "HTML / CSS"]),
            ("Hydrography", ["Multibeam echo sounder (MBES)", "Side-scan sonar (SSS)", "Sub-bottom profiler (SBP)", "Backscatter processing", "Bathymetric cleaning and QC"]),
            ("Software", ["ArcGIS Pro (Esri)", "QGIS", "CARIS HIPS", "QPS Qimera", "FMGT", "EIVA NaviModel", "Qinsy", "POSPac (Applanix)"]),
        ],
        "languages": [("Swedish", "Very good, spoken and written"), ("English", "Fluent"), ("French", "Fluent")],
        "personal": [
            "Accurate and quality-minded",
            "Strong analytical skills",
            "Experienced in international, technical project environments",
            "Independent and a good team player",
            "Quick to learn new systems and methods",
        ],
        "references": "Available on request.",
    },
    "sv": {
        "lang": "sv",
        "title": "GIS-ingenjör & geomatikspecialist",
        "location": "Göteborg",
        "citizenship": "Svenskt och rwandiskt medborgarskap",
        "labels": {
            "contact": "Kontakt", "links": "Länkar", "profile": "Profil", "experience": "Arbetslivserfarenhet",
            "projects": "Web GIS-projekt", "education": "Utbildning", "skills": "Kompetenser",
            "languages": "Språk", "personal": "Personliga egenskaper", "references": "Referenser",
            "email": "E-post", "phone": "Telefon", "location": "Ort", "portfolio": "Portfolio",
            "website": "Företagets webbplats", "live": "Live-demo", "all_demos": "Alla demon",
        },
        "profile": [
            "Geomatikingenjör med masterexamen från Lunds universitet och GIS-erfarenhet sedan 2009 inom gruvsektorn, stadsutveckling, nationell sjökortsproduktion och offshore-mätning. Jag arbetar i hela geodatakedjan: insamling och rensning av data, hantering av geodatabaser, analys i ArcGIS Pro, QGIS och Python samt leverans av tydliga kartor och interaktiva Web GIS-applikationer.",
            "Jag har en stark känsla för noggrannhet och kvalitetskontroll från flera års hydrografisk databehandling, och bygger praktiska Web GIS-verktyg i mitt eget företag CB Web & GIS. Nu söker jag en GIS-roll där jag kan kombinera rumslig analys, datahantering och webbkartor.",
        ],
        "jobs": [
            {
                "role": "Hydrographic Data Processor",
                "org": "Ocean Infinity AB", "place": "Göteborg",
                "dates": "Feb 2025 – okt 2026",
                "note": "Tjänsten upphörde när företaget stängde sitt svenska kontor.",
                "bullets": [
                    "Bearbetade hydrografiska mätdata från insamling till slutleverans.",
                    "Utförde kvalitetskontroll (QC), validering och rensning av MBES- och backscatterdata.",
                    "Arbetade i CARIS HIPS, QPS Qimera, FMGT, EIVA NaviModel och Qinsy.",
                    "Säkerställde att leveranser uppfyllde projektkrav, kundspecifikationer och interna kvalitetsstandarder.",
                    "Samarbetade med senior data processors, offshore-team och internationella projektgrupper i MBES-, SSS- och geofysiska projekt.",
                    "Dokumenterade arbetsflöden, kontroller och resultat.",
                ],
            },
            {
                "role": "Kartingenjör, hydrografisk databehandling",
                "org": "Sjöfartsverket", "place": "Sverige",
                "dates": "Mar 2021 – mar 2025",
                "bullets": [
                    "Bearbetade och kvalitetskontrollerade hydrografiska mätdata för sjökortsprodukter.",
                    "Utförde datarensning, analys och validering av djupdata.",
                    "Arbetade med geografiska databaser och produktion av geografisk information.",
                    "Hanterade och kontrollerade mätdata enligt tekniska standarder och krav.",
                    "Bidrog till utveckling och kvalitetssäkring av nautiska kartunderlag.",
                ],
            },
            {
                "role": "GIS-ingenjör",
                "org": "Älvstranden Utveckling AB", "place": "Göteborg",
                "dates": "Apr 2017 – okt 2017",
                "bullets": [
                    "Arbetade med GIS-datahantering, kartframställning och geografiska analyser.",
                    "Producerade kartor och GIS-baserade beslutsunderlag.",
                    "Uppdaterade och administrerade geografiska databaser.",
                    "Stödde verksamheten i GIS-relaterade frågor och analyser.",
                ],
            },
            {
                "role": "GIS-specialist / informationshandläggare, gruv- och mineraldata",
                "org": "Rwanda Mines, Petroleum and Gas Board", "place": "Kigali, Rwanda",
                "dates": "Jan 2009 – jun 2013",
                "bullets": [
                    "Producerade kartor över mineralresurser och geografisk information.",
                    "Kartlade geologiska, geokemiska och geofysiska data tillsammans med geologer.",
                    "Bidrog till geologiska kartor och nationella geodatabaser.",
                    "Hanterade databaser för gruvlicenser och tillståndsdata samt följde upp tillståndsstatus.",
                    "Granskade dokumentation enligt standardiserade rutiner och rapporterade status till ledningen.",
                ],
            },
        ],
        "projects": [
            {
                "name": "GeoRisk AI", "slug": "georisk-ai/",
                "text": "Web GIS för kommunal planering i centrala Linköping. Bearbetade Lantmäteriets markhöjdmodell i Python för att ta fram markhöjd, lutning, sänkor och lågpunkter, med illustrativa vattennivåscenarier för Stångån.",
                "tech": "Python · rasterio · NumPy · SciPy · FastAPI · Leaflet",
            },
            {
                "name": "Interaktiv företagskarta", "slug": "business-map/",
                "text": "Företagsplatser med kategorifilter, kartlager, sökfunktion, ritverktyg och närhetsanalys.",
                "tech": "Leaflet · Leaflet.draw · JavaScript",
            },
            {
                "name": "Analys av leveranszoner", "slug": "pizza-delivery/",
                "text": "Leveranszoner, efterfrågevärmekartor, ordergruppering och ruttplanering i vägnätet.",
                "tech": "Leaflet.heat · OSRM",
            },
            {
                "name": "Rutt- och resursplanering", "slug": "smart-projektplanering/",
                "text": "Fördelar team, fordon och maskiner till platser utifrån verkliga vägavstånd och optimerade rutter.",
                "tech": "Leaflet · OSRM",
            },
        ],
        "education": [
            ("Masterexamen (MSc) i geomatik", "Lunds universitet"),
            ("Kandidatexamen i geografi, miljö och utveckling", "University of Rwanda"),
        ],
        "skills": [
            ("GIS och geodata", ["GIS-analys", "Geodatabaser", "Digital kartproduktion", "Kartografi", "Spatial datahantering", "Terräng- och rasteranalys"]),
            ("Web GIS och programmering", ["Python (rasterio, NumPy, SciPy)", "FastAPI", "Leaflet", "JavaScript", "SQL", "HTML / CSS"]),
            ("Hydrografi", ["Multibeam (MBES)", "Sidescan-sonar (SSS)", "Sub-bottom profiler (SBP)", "Backscatterbearbetning", "Batymetrisk datarensning och QC"]),
            ("Programvara", ["ArcGIS Pro (Esri)", "QGIS", "CARIS HIPS", "QPS Qimera", "FMGT", "EIVA NaviModel", "Qinsy", "POSPac (Applanix)"]),
        ],
        "languages": [("Svenska", "Mycket goda kunskaper i tal och skrift"), ("Engelska", "Flytande"), ("Franska", "Flytande")],
        "personal": [
            "Noggrann och kvalitetsmedveten",
            "Stark analytisk förmåga",
            "Van vid internationella och tekniska projektmiljöer",
            "Självständig med god samarbetsförmåga",
            "Snabb på att lära mig nya system och arbetsmetoder",
        ],
        "references": "Lämnas på begäran.",
    },
}

CSS = """
@page { size: A4; margin: 0; }
:root {
  --ink: #0b1e2d; --muted: #4d6475; --line: #d3dee6; --accent: #08799a;
  --magenta: #a8226f; --side: #06182a; --side-ink: #e8f1f6; --side-muted: #9fb7c7; --side-accent: #7fdcef;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: "Instrument Sans", "Segoe UI", Arial, sans-serif; color: var(--ink); font-size: 9.2pt; line-height: 1.45;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
a { color: inherit; text-decoration: none; }
.mono { font-family: "IBM Plex Mono", Menlo, monospace; }
h1, h2, h3 { font-family: "Bricolage Grotesque", "Segoe UI", Arial, sans-serif; margin: 0; }

.page { display: grid; grid-template-columns: 64mm 1fr; height: 297mm; overflow: hidden; }
.side { background: var(--side); color: var(--side-ink); padding: 14mm 7mm 12mm 9mm; }
.main { padding: 13mm 12mm 12mm 10mm; }

.photo { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; border-radius: 4mm; display: block; margin-bottom: 7mm; }
.side h2 { font-family: "IBM Plex Mono", Menlo, monospace; font-weight: 500; font-size: 7.2pt; letter-spacing: .14em;
  text-transform: uppercase; color: var(--side-accent); margin: 6.5mm 0 2.5mm; }
.side h2:first-of-type { margin-top: 0; }
.kv { display: grid; gap: 2.2mm; }
.kv div { display: grid; gap: .3mm; }
.kv dt { font-size: 7pt; color: var(--side-muted); }
.kv dd { margin: 0; overflow-wrap: anywhere; font-size: 8.6pt; }
.kv a { color: var(--side-ink); border-bottom: 1px solid rgba(127, 220, 239, .4); }
.side ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 1.2mm; }
.side .skill-group { margin-bottom: 3mm; }
.side .skill-group h3 { font-family: "Instrument Sans", Arial, sans-serif; font-size: 8.4pt; font-weight: 600; margin-bottom: 1.2mm; }
.chips { display: flex !important; flex-wrap: wrap; gap: 1.2mm !important; }
.chips li { font-size: 7.4pt; padding: .5mm 2mm; border-radius: 10mm; border: 1px solid rgba(159, 183, 199, .35); color: var(--side-ink); }
.langs li { display: grid; }
.langs span { color: var(--side-muted); font-size: 7.8pt; }
.plain li { color: var(--side-ink); padding-left: 3mm; position: relative; font-size: 8.4pt; }
.plain li::before { content: ""; position: absolute; left: 0; top: .62em; width: 1.6mm; height: 1px; background: var(--side-accent); }

header.top { border-bottom: 1px solid var(--line); padding-bottom: 5mm; margin-bottom: 5mm; }
header.top h1 { font-size: 27pt; letter-spacing: -.03em; line-height: 1; }
header.top .role { font-family: "Bricolage Grotesque", Arial, sans-serif; font-size: 12.5pt; color: var(--accent); margin-top: 2mm; font-weight: 500; }
header.top .meta { margin-top: 2.5mm; color: var(--muted); font-size: 8.4pt; display: flex; flex-wrap: wrap; gap: 1mm 4mm; }
header.top .meta a { color: var(--accent); }

section { margin-bottom: 5mm; }
.main h2 { font-family: "IBM Plex Mono", Menlo, monospace; font-weight: 500; font-size: 7.4pt; letter-spacing: .14em;
  text-transform: uppercase; color: var(--magenta); margin-bottom: 2.5mm; }
.profile p { margin: 0 0 2mm; font-size: 9.4pt; }

.job { display: grid; grid-template-columns: 27mm 1fr; gap: 4mm; padding: 2.6mm 0; border-top: 1px solid var(--line); break-inside: avoid; }
.job:first-of-type { border-top: 0; padding-top: 0; }
.job .dates { font-size: 7.6pt; color: var(--muted); padding-top: .6mm; }
.job h3 { font-size: 10.6pt; letter-spacing: -.01em; }
.job .org { color: var(--muted); font-weight: 500; margin-top: .3mm; }
.job .note { font-size: 7.8pt; color: var(--muted); font-style: italic; margin-top: .6mm; }
.job ul, .proj ul { margin: 1.6mm 0 0; padding-left: 3.6mm; }
.job li { margin-bottom: .5mm; }
.job li::marker { color: var(--accent); }

.projects { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; }
.proj { border: 1px solid var(--line); border-radius: 2.5mm; padding: 3mm; break-inside: avoid; }
.proj h3 { font-size: 9.8pt; }
.proj h3 a { color: var(--ink); }
.proj p { margin: 1mm 0; font-size: 8.4pt; color: var(--muted); }
.proj .tech { font-size: 7pt; color: var(--ink); }
.proj .link { font-size: 7.2pt; color: var(--accent); overflow-wrap: anywhere; display: block; margin-top: 1mm; }
.more { margin-top: 2.5mm; font-size: 8.4pt; color: var(--muted); }
.more a { color: var(--accent); }

.edu { display: grid; gap: 2mm; }
.edu div { display: grid; }
.edu strong { font-weight: 600; }
.edu span { color: var(--muted); }

.page + .page { break-before: page; }
.page + .page .main { padding-top: 11mm; }
.refs { margin: 0; font-size: 8.4pt; }
"""


def link(key, label=None):
    text, href = LINKS[key]
    return f'<a href="{href}">{escape(label or text)}</a>'


def build(lang):
    c = CONTENT[lang]
    L = c["labels"]

    contact = f"""
      <dl class="kv">
        <div><dt>{L['email']}</dt><dd>{link('email')}</dd></div>
        <div><dt>{L['phone']}</dt><dd>{link('phone')}</dd></div>
        <div><dt>{L['location']}</dt><dd>{escape(c['location'])}</dd></div>
      </dl>"""
    links = f"""
      <dl class="kv">
        <div><dt>LinkedIn</dt><dd>{link('linkedin')}</dd></div>
        <div><dt>{L['portfolio']}</dt><dd>{link('portfolio')}</dd></div>
        <div><dt>GitHub</dt><dd>{link('github')}</dd></div>
        <div><dt>CB Web &amp; GIS</dt><dd>{link('cbweb')}</dd></div>
      </dl>"""

    skills = "".join(
        f'<div class="skill-group"><h3>{escape(name)}</h3><ul class="chips">'
        + "".join(f"<li>{escape(s)}</li>" for s in items)
        + "</ul></div>"
        for name, items in c["skills"]
    )
    langs = "".join(f"<li>{escape(n)}<span>{escape(lvl)}</span></li>" for n, lvl in c["languages"])
    personal = "".join(f"<li>{escape(p)}</li>" for p in c["personal"])

    def job_html(j):
        note = f'<p class="note">{escape(j["note"])}</p>' if j.get("note") else ""
        bullets = "".join(f"<li>{escape(b)}</li>" for b in j["bullets"])
        return f"""
        <article class="job">
          <p class="dates mono">{escape(j['dates'])}</p>
          <div>
            <h3>{escape(j['role'])}</h3>
            <p class="org">{escape(j['org'])} · {escape(j['place'])}</p>
            {note}
            <ul>{bullets}</ul>
          </div>
        </article>"""

    jobs_p1 = "".join(job_html(j) for j in c["jobs"][:2])
    jobs_p2 = "".join(job_html(j) for j in c["jobs"][2:])
    projects = "".join(
        f"""
        <article class="proj">
          <h3><a href="{DEMOS}{p['slug']}">{escape(p['name'])} ↗</a></h3>
          <p>{escape(p['text'])}</p>
          <p class="tech mono">{escape(p['tech'])}</p>
          <a class="link mono" href="{DEMOS}{p['slug']}">{escape((DEMOS + p['slug']).replace('https://', ''))}</a>
        </article>"""
        for p in c["projects"]
    )
    edu = "".join(f"<div><strong>{escape(d)}</strong><span>{escape(s)}</span></div>" for d, s in c["education"])
    profile = "".join(f"<p>{escape(p)}</p>" for p in c["profile"])

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>Concorde Bazimaziki – CV</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="page">
  <aside class="side">
    <img class="photo" src="photo.jpg" alt="Concorde Bazimaziki">
    <h2>{L['contact']}</h2>{contact}
    <h2>{L['links']}</h2>{links}
    <h2>{L['languages']}</h2><ul class="langs">{langs}</ul>
    <h2>{L['personal']}</h2><ul class="plain">{personal}</ul>
  </aside>
  <main class="main">
    <header class="top">
      <h1>Concorde Bazimaziki</h1>
      <p class="role">{escape(c['title'])}</p>
      <p class="meta"><span>{escape(c['location'])}</span><span>{escape(c['citizenship'])}</span>{link('linkedin', 'LinkedIn')}{link('portfolio', L['portfolio'])}</p>
    </header>
    <section class="profile"><h2>{L['profile']}</h2>{profile}</section>
    <section><h2>{L['experience']}</h2>{jobs_p1}</section>
  </main>
</div>
<div class="page">
  <aside class="side">
    <h2>{L['skills']}</h2>{skills}
    <h2>{L['references']}</h2><p class="refs">{escape(c['references'])}</p>
  </aside>
  <main class="main">
    <section><h2>{L['experience']}</h2>{jobs_p2}</section>
    <section>
      <h2>{L['projects']}</h2>
      <div class="projects">{projects}</div>
      <p class="more">{L['all_demos']}: <a href="{DEMOS}">{DEMOS.replace('https://', '')}</a> · {L['website']}: {link('cbweb')}</p>
    </section>
    <section><h2>{L['education']}</h2><div class="edu">{edu}</div></section>
  </main>
</div>
</body>
</html>"""


if __name__ == "__main__":
    for lang in CONTENT:
        (HERE / f"cv_{lang}.html").write_text(build(lang), encoding="utf-8")
        print("wrote", HERE / f"cv_{lang}.html")
