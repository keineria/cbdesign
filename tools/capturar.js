// Genera capturas de página completa de cada sitio del portafolio.
// Uso: node tools/capturar.js [slug ...]  (requiere playwright)
// Genera PNG en assets/shots; luego conviértelas a WebP de 900 px de ancho (ver README).
const { chromium } = require('playwright');
const path = require('path');
const sites = require('../data/sitios.json').concat([{ slug: 'keiner', url: 'https://keiner.cbdesign.com.co' }]);
const OUT = path.join(__dirname, '..', 'assets', 'shots');
const only = process.argv.slice(2);

(async () => {
  const browser = await chromium.launch();
  for (const s of sites) {
    if (only.length && !only.includes(s.slug)) continue;
    const ctx = await browser.newContext({ viewport: { width: 1366, height: 900 }, deviceScaleFactor: 1, locale: 'es-CO' });
    const page = await ctx.newPage();
    try {
      await page.goto(s.url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
      // Desplazar despacio para activar lazy-load y animaciones de entrada
      for (let i = 0; i < 80; i++) {
        const fin = await page.evaluate(() => { window.scrollBy(0, 450); return window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 5; }).catch(() => false);
        await page.waitForTimeout(350);
        if (fin) break;
      }
      await page.waitForTimeout(1500);
      await page.evaluate(() => window.scrollTo(0, 0)).catch(() => {});
      await page.waitForTimeout(1500);
      // Limpieza: avisos de cookies, popups, chats flotantes y animaciones sin terminar
      await page.addStyleTag({ content: `
        [id*="cookie" i],[class*="cookie" i],[class*="popup" i],[id*="popup" i],.cky-consent-container,.cmplz-cookiebanner,
        #moove_gdpr_cookie_info_bar,[class*="joinchat" i],[id*="whatsapp" i][style*="fixed"],.elementor-popup-modal,
        iframe[src*="chat"],#shopify-chat,[class*="chat-widget" i]{display:none!important}
        .elementor-invisible,[data-aos],.wow,.reveal,.animate-on-scroll{visibility:visible!important;opacity:1!important;transform:none!important}
      ` });
      // Forzar imágenes con carga diferida (WoodMart, WP Rocket, lazysizes...)
      await page.evaluate(async () => {
        const pend = [];
        document.querySelectorAll('img').forEach(img => {
          const d = img.dataset;
          const src = d.woodSrc || d.src || d.lazySrc || d.original;
          const srcset = d.woodSrcset || d.srcset || d.lazySrcset;
          if (srcset) img.srcset = srcset;
          if (src && img.src !== src) { img.src = src; pend.push(img.decode().catch(() => {})); }
          img.loading = 'eager';
          img.style.setProperty('opacity', '1', 'important');
        });
        await Promise.all(pend);
      }).catch(() => {});
      await page.waitForTimeout(2500);
      const file = path.join(OUT, `${s.slug}.png`);
      await page.screenshot({ path: file, fullPage: true });
      console.log('ok', s.slug);
    } catch (e) { console.log('ERROR', s.slug, e.message); }
    await ctx.close();
  }
  await browser.close();
})();
