// Renders cv/source/cv_en.html and cv_sv.html to cv/*.pdf with Chromium (Playwright).
// Run from the repository root:  node cv/source/render_pdf.js
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const [lang, out] of [['en', 'Concorde_Bazimaziki_CV_EN.pdf'], ['sv', 'Concorde_Bazimaziki_CV_SV.pdf']]) {
    await page.goto('file://' + path.resolve(__dirname, `cv_${lang}.html`), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({ path: path.resolve(__dirname, '..', out), format: 'A4', printBackground: true, preferCSSPageSize: true });
    console.log('wrote cv/' + out);
  }
  await browser.close();
})();
