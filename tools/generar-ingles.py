#!/usr/bin/env python3
"""Genera sitio/en/index.html (inicio en inglés) a partir de sitio/index.html y el sitemap.

El inicio en español es la fuente: aquí se traduce cada texto visible con el diccionario
de tools/inicio_en.py. Si aparece un texto sin traducción el script falla, para que las
dos versiones no se separen sin que nadie lo note.

Uso:  python3 tools/generar-servicios.py && python3 tools/generar-ingles.py
"""
import datetime
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).parent))
from inicio_en import TITLE, DESC, OG_TITLE, OG_DESC, H1, LOCAL, WA, CRUDO, FAQ_LD, T, IGUAL  # noqa: E402
from servicios_en import SERVICIOS_EN  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent / "sitio"
BASE = "https://cbdesign.com.co"
EN_POR_PAR = {s["par"]: s for s in SERVICIOS_EN}


def cambiar(html, viejo, nuevo, veces=1):
    if viejo not in html:
        sys.exit(f"No se encontró en index.html: {viejo[:80]!r}")
    return html.replace(viejo, nuevo, veces) if veces else html.replace(viejo, nuevo)


def cabeza(head, faqs):
    head = cambiar(head, '<html lang="es-CO">', '<html lang="en">')
    head = re.sub(r"<title>.*?</title>", lambda m: f"<title>{html.escape(TITLE)}</title>", head, count=1)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + DESC, head, count=1)
    head = cambiar(head, '<link rel="canonical" href="https://cbdesign.com.co/">', '<link rel="canonical" href="https://cbdesign.com.co/en/">')
    head = re.sub(r'<meta name="geo\.[a-z]+" content="[^"]*">\n', "", head)
    head = cambiar(head, 'og:locale" content="es_CO"', 'og:locale" content="en_US"')
    head = cambiar(head, '<meta property="og:type"', '<meta property="og:locale:alternate" content="es_CO">\n<meta property="og:type"')
    for prop, valor in (("og:title", OG_TITLE), ("og:description", OG_DESC), ("twitter:title", OG_TITLE), ("twitter:description", OG_DESC),
                        ("og:url", BASE + "/en/"), ("og:image:alt", "CBdesign, web development and digital marketing")):
        head, n = re.subn(rf'((?:property|name)="{prop}" content=")[^"]*', lambda m: m.group(1) + valor, head, count=1)
        if not n:
            sys.exit(f"Falta la etiqueta {prop}")
    # Rutas absolutas: la página vive en /en/
    head = re.sub(r'(href|imagesrcset)="(?!https?:|/)([^"]+)"', lambda m: f'{m.group(1)}="' + re.sub(r"(^|, )(?=[a-z])", r"\1/", m.group(2)) + '"', head)

    ini, fin = head.index('<script type="application/ld+json">'), head.index("</script>", head.index('<script type="application/ld+json">'))
    datos = json.loads(head[ini + len('<script type="application/ld+json">'):fin])
    org = datos["@graph"][0]
    org_en = {
        "@type": org["@type"], "@id": org["@id"], "name": org["name"], "url": BASE + "/en/",
        "description": "Web development and digital marketing agency based in Cali, Colombia, working with businesses in the United States, Colombia and Spain: websites, online stores, custom software, automation and AI agents.",
        "logo": org["logo"], "image": org["image"], "email": org["email"], "telephone": org["telephone"], "address": org["address"],
        "areaServed": [{"@type": "Country", "name": "United States"}, {"@type": "Country", "name": "Colombia"}, {"@type": "Country", "name": "Spain"}],
        "contactPoint": org["contactPoint"],
        "knowsAbout": ["Web development", "Ecommerce", "Custom software", "SEO", "Digital marketing", "AI automation"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "CBdesign services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["corto"], "url": f"{BASE}/en/{s['slug']}/"}} for s in SERVICIOS_EN]},
    }
    grafo = [
        org_en,
        {"@type": "WebSite", "@id": BASE + "/#sitio", "url": BASE + "/", "name": "CBdesign", "inLanguage": ["es-CO", "en"], "publisher": {"@id": org["@id"]}},
        {"@type": "WebPage", "@id": BASE + "/en/#pagina", "url": BASE + "/en/", "name": TITLE, "description": DESC, "isPartOf": {"@id": BASE + "/#sitio"},
         "about": {"@id": org["@id"]}, "primaryImageOfPage": BASE + "/assets/img/og.jpg", "inLanguage": "en"},
        {"@type": "FAQPage", "@id": BASE + "/en/#preguntas", "inLanguage": "en", "mainEntity": [
            {"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in faqs]},
    ]
    ld = json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, indent=1)
    return head[:ini] + '<script type="application/ld+json">\n' + ld + "\n" + head[fin:]


def traducir(texto, falta):
    limpio = texto.strip()
    if not limpio or limpio in IGUAL or not re.search(r"[A-Za-zÁÉÍÓÚáéíóúñ]", limpio):
        return texto
    if limpio not in T:
        falta.append(limpio)
        return texto
    return texto.replace(limpio, T[limpio])


def cuerpo(body):
    # Bloques que se reemplazan completos: se apartan antes de traducir y se insertan después.
    fijos = {}

    def apartar(patron, nuevo_html, nombre):
        nonlocal body
        marca = f"<!--{nombre}-->"
        fijos[marca] = nuevo_html
        body, n = re.subn(patron, lambda m: m.group(1) + marca + m.group(2), body, count=1, flags=re.S)
        if not n:
            sys.exit(f"No se encontró el bloque {nombre}")

    palabras = " ".join(f'<span class="pal{" grad" if g else ""}" style="--i:{i}">{p}</span>' for i, (p, g) in enumerate(H1))
    apartar(r'(<h1 class="palabras">).*?(</h1>)', palabras, "H1")
    apartar(r'(<section class="seccion claro" id="cali">\s*<div class="wrap">\n).*?(    </div>\n  </section>)', LOCAL, "LOCAL")
    preguntas = "\n".join(f'        <details class="reveal"><summary><h3>{html.escape(p, False)}</h3></summary><p>{html.escape(r, False)}</p></details>' for p, r in FAQ_LD)
    apartar(r'(<div class="faq">\n).*?(\n      </div>)', preguntas, "FAQ")
    m = re.search(r"<pre><code>.*?</code></pre>", body, flags=re.S)
    codigo = m.group(0)
    for viejo, nuevo in CRUDO:
        if viejo in codigo:
            codigo = codigo.replace(viejo, nuevo)
    fijos["<!--CODIGO-->"] = codigo
    body = body.replace(m.group(0), "<!--CODIGO-->")

    falta = []
    partes = re.split(r"(<[^>]+>)", body)
    en_script = False
    for i, parte in enumerate(partes):
        if parte.startswith("<"):
            if re.match(r"<(script|style)\b", parte):
                en_script = True
            elif re.match(r"</(script|style)>", parte):
                en_script = False
            else:
                partes[i] = re.sub(r'\b(alt|aria-label|placeholder|title)="([^"]*)"', lambda m: f'{m.group(1)}="{traducir(m.group(2), falta)}"', parte)
        elif not en_script:
            partes[i] = traducir(parte, falta)
    if falta:
        sys.exit("Faltan traducciones en tools/inicio_en.py:\n" + "\n".join(f"  {t!r}" for t in dict.fromkeys(falta)))
    body = "".join(partes)
    for marca, nuevo_html in fijos.items():
        body = body.replace(marca, nuevo_html)
    for viejo, nuevo in CRUDO:
        body = body.replace(viejo, nuevo)

    # Enlaces
    for es, s in EN_POR_PAR.items():
        body = body.replace(f'href="{es}/"', f'href="/en/{s["slug"]}/"')
    for es, en in WA.items():
        body = body.replace("text=" + quote(es), "text=" + quote(en))
    resto = re.findall(r"text=(Hola[^\"]*)", body)
    if resto:
        sys.exit(f"Mensajes de WhatsApp sin traducir: {resto}")
    body = re.sub(r'(src|srcset)="(?!https?:|/)([^"]+)"', lambda m: f'{m.group(1)}="' + re.sub(r"(^|, )(?=[a-z])", r"\1/", m.group(2)) + '"', body)
    body = cambiar(body, '<a class="idioma" href="en/" hreflang="en" lang="en" data-idioma="en" aria-label="ES, Español">EN</a>',
                   '<a class="idioma" href="/?lang=es" hreflang="es" lang="es" data-idioma="es" aria-label="ES, Español">ES</a>')
    return body


def sitemap():
    from importlib import import_module
    gs = import_module("generar-servicios")
    hoy = datetime.date.today().isoformat()
    pares = [("/", "/en/")] + [(f"/{s['slug']}/", f"/en/{gs.EN_POR_PAR[s['slug']]['slug']}/") for s in gs.SERVICIOS]
    filas = []
    for es, en in pares:
        alternos = (f'    <xhtml:link rel="alternate" hreflang="es" href="{BASE}{es}"/>\n'
                    f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE}{en}"/>\n'
                    f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{es}"/>\n')
        for u in (es, en):
            filas.append(f"  <url>\n    <loc>{BASE}{u}</loc>\n    <lastmod>{hoy}</lastmod>\n{alternos}  </url>\n")
    (RAIZ / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "".join(filas) + "</urlset>\n", encoding="utf-8")
    return len(filas)


def main():
    fuente = (RAIZ / "index.html").read_text(encoding="utf-8")
    corte = fuente.index("<body>")
    body = cuerpo(fuente[corte:])
    head = cabeza(fuente[:corte], FAQ_LD)
    (RAIZ / "en").mkdir(exist_ok=True)
    (RAIZ / "en" / "index.html").write_text(head + body, encoding="utf-8")
    print(f"en/index.html listo ({len(FAQ_LD)} preguntas) y sitemap con {sitemap()} URL")


if __name__ == "__main__":
    main()
