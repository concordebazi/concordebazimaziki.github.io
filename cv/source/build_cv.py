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
    "sv": {
        "lang": "sv",
        "title": "GIS-ingenjör · Geodata, Web GIS och kartografi",
        "location": "Göteborg",
        "citizenship": "Svenskt medborgarskap",
        "labels": {
            "contact": "Kontakt", "links": "Länkar", "profile": "Profil", "strengths": "Kompetens i korthet",
            "experience": "Arbetslivserfarenhet", "earlier": "Tidigare arbetslivserfarenhet",
            "projects": "GIS-projekt och demonstrationer", "education": "Utbildning", "skills": "System och verktyg",
            "languages": "Språk", "personal": "Personliga egenskaper", "references": "Referenser",
            "email": "E-post", "phone": "Telefon", "location": "Ort", "portfolio": "Portfolio",
            "website": "Företagets webbplats", "all_demos": "Alla demon",
        },
        "profile": [
            "GIS-ingenjör och geomatiker med masterexamen från Lunds universitet och GIS-erfarenhet sedan 2005: från markförvaltning och gruvsektorn i Rwanda till stadsutveckling i Göteborg, sjökortsproduktion på Sjöfartsverket och offshore-mätning på Ocean Infinity.",
            "Jag är van att förvalta och ajourhålla geodata i geografiska databaser, följa dokumenterade rutiner och ta fram tillförlitliga kartor och underlag i ArcGIS Pro, QGIS och Python. Genom mitt företag CB Web & GIS bygger jag interaktiva Web GIS-prototyper.",
            "Jag trivs med att ge stöd till användare och samarbeta med olika verksamheter, och vill gärna utvecklas vidare inom ArcGIS Enterprise, systemförvaltning och GIS-stöd i offentlig verksamhet.",
        ],
        "strengths": ["GIS-plattformar och karttjänster", "ArcGIS Pro och QGIS", "Geodataförvaltning och ajourhållning",
                      "Geodatabaser", "Datakvalitet och dokumentation", "GIS-analys och kartografi", "Web GIS",
                      "Användarstöd och kunskapsdelning"],
        "jobs": [
            {"role": "Hydrographic Data Processor, Grade 1", "org": "Ocean Infinity AB", "place": "Göteborg",
             "dates": "feb 2025 – sep 2026",
             "note": "Tjänsten upphörde när företaget stängde sitt svenska kontor.",
             "bullets": [
                 "Bearbetade multibeam-ekolodsdata (MBES) i CARIS HIPS och QPS Qimera, från datarensning och kontroll till kvalitetssäkrade leveranser.",
                 "Kontrollerade navigerings- och tidvattenunderlag, SVP och refraktion samt hanterade SBET-relaterade leveransunderlag.",
                 "Tog fram batymetriska ytor och DTM med 0,2 m och 1 m upplösning enligt projektspecifikationer; bearbetade backscatter i FMGT.",
                 "Säkerställde att leveranser uppfyllde projektkrav, kundspecifikationer och interna kvalitetsstandarder.",
                 "Dokumenterade arbetsflöden och överlämningar och samarbetade med offshore-team och internationella projektgrupper för att lösa datafrågor och hålla kvalitet och tidsramar.",
             ]},
            {"role": "Kartingenjör, Sjögeografi / Källdata", "org": "Sjöfartsverket", "place": "Sverige",
             "dates": "mar 2021 – mar 2025",
             "bullets": [
                 "Kvalitetsgranskade sjömätningsresultat och förde in samt ajourhöll geografisk information i myndighetens djupdatabas.",
                 "Bearbetade sjögeografiska datateman i DIS och tog fram kartor och djupdataprodukter enligt fastställda rutiner.",
                 "Rensade, analyserade och validerade djupdata enligt tekniska standarder och krav.",
                 "Kontrollerade bland annat vrak och avvikelser i sjökort samt bidrog i kartografi, korrekturläsning och dokumenterad kvalitetssäkring.",
             ]},
            {"role": "GIS-ingenjör", "org": "Älvstranden Utveckling AB", "place": "Göteborg",
             "dates": "apr – okt 2017",
             "bullets": [
                 "Tog fram tematiska kartor och GIS-underlag från detaljplaner, arkitektritningar och annan geografisk information.",
                 "Mätte och analyserade ytor, beräknade BTA och sammanställde underlag för stadsutveckling och fastighetsfrågor.",
                 "Uppdaterade och administrerade geografiska databaser och gav GIS-stöd till verksamheten.",
             ]},
            {"role": "GIS- och geodatamedarbetare", "org": "Rwanda Mines, Petroleum and Gas Board", "place": "Kigali, Rwanda",
             "dates": "jan 2009 – jun 2013",
             "bullets": [
                 "Hanterade geografiska databaser för gruvlicenser och tillstånd, inklusive registrering, uppdatering och uppföljning av geodata.",
                 "Tog fram och uppdaterade geologiska och geokemiska kartunderlag, bland annat i skala 1:50 000, i samarbete med geologer.",
                 "Producerade kartor över mineralresurser och bidrog till nationella geodatabaser.",
                 "Stödde datakontroll och rapportering till ledningen inom resurskartläggning och förvaltning av geografisk information.",
             ]},
            {"role": "Lantmätare", "org": "Nyarugenge och Kamonyi kommuner", "place": "Rwanda",
             "dates": "2007 – 2009",
             "bullets": [
                 "Arbetade med mark- och stadsområdesinformation tillsammans med offentliga och privata aktörer, med GIS som stöd för markförvaltning.",
             ]},
            {"role": "GIS-tekniker", "org": "GIS Centre, University of Rwanda", "place": "Rwanda",
             "dates": "2005 – 2006",
             "bullets": [
                 "Digitaliserade och kartlade geodata och bidrog till datastrukturer för GIS-lagring.",
                 "Demonstrerade GIS-lösningar och gav stöd till användare.",
             ]},
        ],
        "projects": [
            {"name": "Platsvy", "slug": None, "text": "Webbverktyg för förstudier av mark inför industrietableringar i Sverige."},
            {"name": "GeoRisk AI", "slug": "georisk-ai/", "text": "Terränganalys i Linköping: Lantmäteriets markhöjdmodell bearbetad i Python (lutning, sänkor, lågpunkter) med illustrativa vattennivåscenarier för Stångån."},
            {"name": "Interaktiv företagskarta", "slug": "business-map/", "text": "Kategorifilter, kartlager, sökfunktion, ritverktyg och närhetsanalys."},
            {"name": "Smart projektplanering", "slug": "smart-projektplanering/", "text": "Fördelar team och maskiner till projektplatser utifrån verkliga vägavstånd."},
            {"name": "Mobil bilservice", "slug": "mobile-mechanic/", "text": "Uppdragsfördelning och optimerade körvägar för mobila mekaniker."},
            {"name": "Analys av leveranszoner", "slug": "pizza-delivery/", "text": "Leveranszoner, efterfrågevärmekartor och ruttplanering i vägnätet."},
        ],
        "projects_note": "Byggda med Leaflet, JavaScript, Python och OSRM. Demonstrationerna använder delvis exempel- eller simulerade data.",
        "education": [
            ("Masterexamen (MSc) i geomatik", "Lunds universitet", "2018 – 2021", "Forskningsprojekt om geografisk spårning och kartläggning av covid-19 i Sverige."),
            ("Kandidatexamen i geografi, miljö och utveckling", "University of Rwanda", "", ""),
        ],
        "skills": [
            ("GIS och kartografi", ["ArcGIS Pro (Esri)", "QGIS", "AutoCAD", "GDAL", "DIS / Djupdata", "GIS-analys", "Kartografi", "Terräng- och rasteranalys"]),
            ("Geodata och databaser", ["Geodatabaser", "PostgreSQL / PostGIS", "SQL (grundläggande)", "Geodataförvaltning", "Datakvalitet och QC"]),
            ("Skriptning och Web GIS", ["Python", "GeoPandas", "rasterio", "NumPy / SciPy", "Jupyter", "FastAPI", "Leaflet", "HTML / CSS / JavaScript", "API:er"]),
            ("Hydrografi", ["MBES", "Sidescan-sonar (SSS)", "Sub-bottom profiler (SBP)", "Backscatter", "CARIS HIPS / SIPS", "QPS Qimera", "FMGT", "Qinsy", "POSPac", "EIVA NaviModel / NaviEdit"]),
            ("Övrigt", ["FME Form / Flow (begränsad erfarenhet)"]),
        ],
        "languages": [("Svenska", "God arbetsnivå i tal och skrift"), ("Engelska", "Flytande"), ("Franska", "Flytande")],
        "personal": ["Noggrann och kvalitetsmedveten", "Stark analytisk förmåga", "Van vid internationella och tekniska projektmiljöer",
                     "Självständig med god samarbetsförmåga", "Snabb på att lära mig nya system och arbetsmetoder"],
        "references": "Lämnas på begäran.",
    },
    "en": {
        "lang": "en",
        "title": "GIS Engineer · Geodata, Web GIS and Cartography",
        "location": "Gothenburg, Sweden",
        "citizenship": "Swedish citizen",
        "labels": {
            "contact": "Contact", "links": "Links", "profile": "Profile", "strengths": "Key skills",
            "experience": "Experience", "earlier": "Earlier experience",
            "projects": "GIS projects and demos", "education": "Education", "skills": "Systems and tools",
            "languages": "Languages", "personal": "Personal qualities", "references": "References",
            "email": "Email", "phone": "Phone", "location": "Location", "portfolio": "Portfolio",
            "website": "Company website", "all_demos": "All demos",
        },
        "profile": [
            "GIS Engineer and geomatics specialist with an MSc from Lund University and GIS experience since 2005: from land administration and the mining sector in Rwanda to urban development in Gothenburg, nautical charting at the Swedish Maritime Administration and offshore survey at Ocean Infinity.",
            "I am used to maintaining and updating geodata in geographic databases, following documented procedures, and producing reliable maps and analyses in ArcGIS Pro, QGIS and Python. Through my company CB Web & GIS I build interactive Web GIS prototypes.",
            "I enjoy supporting users and working across departments, and I want to develop further in ArcGIS Enterprise, system administration and GIS support for public-sector organisations.",
        ],
        "strengths": ["GIS platforms and map services", "ArcGIS Pro and QGIS", "Geodata management and updating",
                      "Geodatabases", "Data quality and documentation", "GIS analysis and cartography", "Web GIS",
                      "User support and knowledge sharing"],
        "jobs": [
            {"role": "Hydrographic Data Processor, Grade 1", "org": "Ocean Infinity AB", "place": "Gothenburg",
             "dates": "Feb 2025 – Sep 2026",
             "note": "Role ended when the company closed its Swedish office.",
             "bullets": [
                 "Processed multibeam echo sounder (MBES) data in CARIS HIPS and QPS Qimera, from cleaning and checks to quality-assured deliverables.",
                 "Checked navigation and tide data, SVP and refraction, and handled SBET-related delivery data.",
                 "Produced bathymetric surfaces and DTMs at 0.2 m and 1 m resolution to project specifications; processed backscatter in FMGT.",
                 "Made sure deliverables met project requirements, client specifications and internal quality standards.",
                 "Documented workflows and handovers, and worked with offshore teams and international project groups to resolve data issues and keep quality and deadlines.",
             ]},
            {"role": "Map Engineer, Marine Geography / Source Data", "org": "Swedish Maritime Administration", "place": "Sweden",
             "dates": "Mar 2021 – Mar 2025",
             "bullets": [
                 "Quality-reviewed hydrographic survey results, and entered and maintained geographic information in the agency's depth database.",
                 "Processed marine geographic data themes in DIS and produced maps and depth data products following established procedures.",
                 "Cleaned, analysed and validated depth data against technical standards and requirements.",
                 "Checked wrecks and discrepancies in nautical charts, and contributed to cartography, proofreading and documented quality assurance.",
             ]},
            {"role": "GIS Engineer", "org": "Älvstranden Utveckling AB", "place": "Gothenburg",
             "dates": "Apr – Oct 2017",
             "bullets": [
                 "Produced thematic maps and GIS data from detailed development plans, architectural drawings and other geographic information.",
                 "Measured and analysed areas, calculated gross floor area (BTA) and compiled data for urban development and property matters.",
                 "Updated and administered geographic databases and provided GIS support to the organisation.",
             ]},
            {"role": "GIS and Geodata Officer", "org": "Rwanda Mines, Petroleum and Gas Board", "place": "Kigali, Rwanda",
             "dates": "Jan 2009 – Jun 2013",
             "bullets": [
                 "Managed geographic databases for mining licences and permits, including registering, updating and following up geodata.",
                 "Produced and updated geological and geochemical maps, including at 1:50,000 scale, together with geologists.",
                 "Produced maps of mineral resources and contributed to national geodatabases.",
                 "Supported data checks and reporting to management for resource mapping and geographic information management.",
             ]},
            {"role": "Land Surveyor", "org": "Nyarugenge and Kamonyi districts", "place": "Rwanda",
             "dates": "2007 – 2009",
             "bullets": [
                 "Worked with land and urban area information together with public and private stakeholders, using GIS to support land administration.",
             ]},
            {"role": "GIS Technician", "org": "GIS Centre, University of Rwanda", "place": "Rwanda",
             "dates": "2005 – 2006",
             "bullets": [
                 "Digitised and mapped geodata and contributed to data structures for GIS storage.",
                 "Demonstrated GIS solutions and supported users.",
             ]},
        ],
        "projects": [
            {"name": "Platsvy", "slug": None, "text": "Web tool for land pre-studies ahead of industrial site development in Sweden."},
            {"name": "GeoRisk AI", "slug": "georisk-ai/", "text": "Terrain analysis in Linköping: Lantmäteriet's elevation model processed in Python (slope, depressions, low points) with illustrative water-level scenarios for the Stångån river."},
            {"name": "Interactive business map", "slug": "business-map/", "text": "Category filters, map layers, search, drawing tools and proximity analysis."},
            {"name": "Smart project planning", "slug": "smart-projektplanering/", "text": "Assigns teams and machines to project sites using real road distances."},
            {"name": "Mobile service routing", "slug": "mobile-mechanic/", "text": "Job allocation and optimised driving routes for mobile mechanics."},
            {"name": "Delivery zone analysis", "slug": "pizza-delivery/", "text": "Delivery zones, demand heatmaps and road-network routing."},
        ],
        "projects_note": "Built with Leaflet, JavaScript, Python and OSRM. The demos partly use example or simulated data.",
        "education": [
            ("MSc in Geomatics", "Lund University, Sweden", "2018 – 2021", "Research project on geographic tracking and mapping of COVID-19 in Sweden."),
            ("BSc in Geography, Environment and Development", "University of Rwanda", "", ""),
        ],
        "skills": [
            ("GIS and cartography", ["ArcGIS Pro (Esri)", "QGIS", "AutoCAD", "GDAL", "DIS / depth database", "GIS analysis", "Cartography", "Terrain and raster analysis"]),
            ("Geodata and databases", ["Geodatabases", "PostgreSQL / PostGIS", "SQL (basic)", "Geodata management", "Data quality and QC"]),
            ("Scripting and Web GIS", ["Python", "GeoPandas", "rasterio", "NumPy / SciPy", "Jupyter", "FastAPI", "Leaflet", "HTML / CSS / JavaScript", "APIs"]),
            ("Hydrography", ["MBES", "Side-scan sonar (SSS)", "Sub-bottom profiler (SBP)", "Backscatter", "CARIS HIPS / SIPS", "QPS Qimera", "FMGT", "Qinsy", "POSPac", "EIVA NaviModel / NaviEdit"]),
            ("Other", ["FME Form / Flow (limited experience)"]),
        ],
        "languages": [("Swedish", "Good professional level, spoken and written"), ("English", "Fluent"), ("French", "Fluent")],
        "personal": ["Accurate and quality-minded", "Strong analytical skills", "Experienced in international, technical project environments",
                     "Independent and a good team player", "Quick to learn new systems and methods"],
        "references": "Available on request.",
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
body { font-family: "Instrument Sans", "Segoe UI", Arial, sans-serif; color: var(--ink); font-size: 8.6pt; line-height: 1.38;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
a { color: inherit; text-decoration: none; }
.mono { font-family: "IBM Plex Mono", Menlo, monospace; }
h1, h2, h3 { font-family: "Bricolage Grotesque", "Segoe UI", Arial, sans-serif; margin: 0; }

.page { display: grid; grid-template-columns: 64mm 1fr; height: 297mm; overflow: hidden; }
.side { background: var(--side); color: var(--side-ink); padding: 14mm 7mm 12mm 9mm; }
.main { padding: 11mm 11mm 10mm 9mm; }

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

header.top { border-bottom: 1px solid var(--line); padding-bottom: 4mm; margin-bottom: 4mm; }
header.top h1 { font-size: 27pt; letter-spacing: -.03em; line-height: 1; }
header.top .role { font-family: "Bricolage Grotesque", Arial, sans-serif; font-size: 12.5pt; color: var(--accent); margin-top: 2mm; font-weight: 500; }
header.top .meta { margin-top: 2.5mm; color: var(--muted); font-size: 8.4pt; display: flex; flex-wrap: wrap; gap: 1mm 4mm; }
header.top .meta a { color: var(--accent); }

section { margin-bottom: 4mm; }
.main h2 { font-family: "IBM Plex Mono", Menlo, monospace; font-weight: 500; font-size: 7.4pt; letter-spacing: .14em;
  text-transform: uppercase; color: var(--magenta); margin-bottom: 1.8mm; }
.profile p { margin: 0 0 1.4mm; font-size: 8.8pt; }

.job { display: grid; grid-template-columns: 25mm 1fr; gap: 4mm; padding: 2mm 0; border-top: 1px solid var(--line); break-inside: avoid; }
.job:first-of-type { border-top: 0; padding-top: 0; }
.job .dates { font-size: 7.6pt; color: var(--muted); padding-top: .6mm; }
.job h3 { font-size: 10pt; letter-spacing: -.01em; }
.job .org { color: var(--muted); font-weight: 500; margin-top: .3mm; }
.job .note { font-size: 7.8pt; color: var(--muted); font-style: italic; margin-top: .6mm; }
.job ul, .proj ul { margin: 1mm 0 0; padding-left: 3.6mm; }
.job li { margin-bottom: .2mm; }
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

.edu { display: grid; gap: 1.6mm; }
.edu div { display: grid; }
.edu strong { font-weight: 600; }
.edu span { color: var(--muted); }

.strengths { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 1.4mm; }
.strengths li { font-size: 8pt; padding: .6mm 2.4mm; border-radius: 10mm; background: #e7f3f7; color: var(--ink); }
.edu em { font-style: normal; color: var(--muted); font-size: 8.4pt; }
.edu-years { font-size: 7.8pt; }
.plist { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 2mm 5mm; }
.plist li { break-inside: avoid; }
.plist strong { font-family: "Bricolage Grotesque", Arial, sans-serif; font-size: 9.4pt; }
.plist strong a { color: var(--ink); }
.plist span { color: var(--muted); }
.plink { display: block; font-size: 7pt; color: var(--accent); }

.page + .page { break-before: page; }
.page + .page .main { padding-top: 10mm; }
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
    strengths = "".join(f"<li>{escape(s)}</li>" for s in c["strengths"])

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

    def proj_html(p):
        if p["slug"]:
            url = DEMOS + p["slug"]
            name = f'<a href="{url}">{escape(p["name"])} ↗</a>'
            tail = ""
        else:
            name, tail = escape(p["name"]), ""
        return f'<li><strong>{name}</strong> <span>{escape(p["text"])}</span>{tail}</li>'

    projects = "".join(proj_html(p) for p in c["projects"])

    def edu_html(e):
        degree, school, years, note = e
        yrs = f'<span class="mono edu-years">{escape(years)}</span>' if years else ""
        nt = f'<em>{escape(note)}</em>' if note else ""
        return f"<div><strong>{escape(degree)}</strong><span>{escape(school)}{' · ' if years else ''}{yrs}</span>{nt}</div>"

    edu = "".join(edu_html(e) for e in c["education"])
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
    <section><h2>{L['strengths']}</h2><ul class="strengths">{strengths}</ul></section>
    <section><h2>{L['experience']}</h2>{jobs_p1}</section>
  </main>
</div>
<div class="page">
  <aside class="side">
    <h2>{L['skills']}</h2>{skills}
    <h2>{L['references']}</h2><p class="refs">{escape(c['references'])}</p>
  </aside>
  <main class="main">
    <section><h2>{L['earlier']}</h2>{jobs_p2}</section>
    <section><h2>{L['education']}</h2><div class="edu">{edu}</div></section>
    <section>
      <h2>{L['projects']}</h2>
      <ul class="plist">{projects}</ul>
      <p class="more">{escape(c['projects_note'])} {L['all_demos']}: <a href="{DEMOS}">{DEMOS.replace('https://', '')}</a> · {L['website']}: {link('cbweb')}</p>
    </section>
  </main>
</div>
</body>
</html>"""


if __name__ == "__main__":
    for lang in CONTENT:
        (HERE / f"cv_{lang}.html").write_text(build(lang), encoding="utf-8")
        print("wrote", HERE / f"cv_{lang}.html")
