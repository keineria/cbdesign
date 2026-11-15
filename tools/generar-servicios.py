#!/usr/bin/env python3
"""Genera las páginas de servicio de cbdesign.com.co (SEO local para Cali).

Uso:  python3 tools/generar-servicios.py
Escribe sitio/<slug>/index.html por cada servicio y actualiza sitio/sitemap.xml.
Para cambiar textos, edita SERVICIOS aquí y vuelve a ejecutar; no edites el HTML generado.
"""
import datetime
import html
import json
import pathlib
from urllib.parse import quote

RAIZ = pathlib.Path(__file__).resolve().parent.parent / "sitio"
BASE = "https://cbdesign.com.co"
WA = "https://wa.me/573164956994?text="
VERSION = "2"  # súbelo al cambiar CSS o JS

PROYECTOS = {
    "fajasmelibelt": ("Fajas Melibelt", "https://fajasmelibelt.com", "Tienda virtual · Colombia"),
    "fajasmelibeltusa": ("Melibelt USA", "https://fajasmelibeltusa.com", "Tienda virtual · Estados Unidos"),
    "conetco": ("Conetco", "https://conetco.co", "Tienda virtual · Fibra óptica"),
    "dauntoque": ("Da un Toque", "https://dauntoque.com", "Producto digital · Tarjetas NFC"),
    "colombiabirdfair": ("Colombia Birdfair", "https://colombiabirdfair.com", "Evento internacional"),
    "vectrar": ("Vectrar", "https://vectrar.com", "Corporativo · Arquitectura en Cali"),
    "evocapitalgroup": ("Evo Capital Group", "https://evocapitalgroup.com", "Corporativo · Finanzas"),
    "nexxosstudio": ("Nexxos Studio", "https://nexxosstudio.com", "Corporativo · Industria textil"),
    "lasevillana": ("La Sevillana", "https://lasevillana.com.co", "Corporativo · Gastronomía"),
}

SERVICIOS = [
    {
        "slug": "diseno-paginas-web-cali",
        "corto": "Diseño de páginas web",
        "title": "Diseño de páginas web en Cali | CBdesign",
        "desc": "Diseño y desarrollo de páginas web en Cali: sitios corporativos rápidos, adaptados a celular y optimizados para Google. Más de 120 sitios en 11 años.",
        "eyebrow": "Diseño y desarrollo web en Cali",
        "h1": "Diseño de páginas web en Cali que convierten visitas en clientes.",
        "lead": "Creamos sitios web a la medida para empresas de Cali y el Valle del Cauca: rápidos, claros y listos para aparecer en Google desde el primer día.",
        "intro": [
            "Una página web es el primer lugar donde un cliente de Cali decide si te escribe o sigue buscando. Por eso no trabajamos con plantillas genéricas: partimos de tu negocio, de lo que busca tu cliente y de lo que hace tu competencia, y diseñamos cada sección para llevar a esa persona a contactarte.",
            "Somos un equipo caleño con más de 11 años de experiencia y más de 120 sitios construidos. Nos encargamos de todo el proceso: estrategia, diseño, desarrollo, dominio, hosting y posicionamiento.",
        ],
        "incluye": [
            ("Diseño a la medida", "Una interfaz propia para tu marca, pensada primero para celular, que es donde llega la mayoría de tus visitas."),
            ("Velocidad de carga", "Código limpio, imágenes optimizadas y servidor configurado para que tu sitio abra en segundos."),
            ("SEO técnico incluido", "Estructura, metadatos, datos estructurados y sitemap listos para que Google entienda y muestre tu sitio."),
            ("Contacto directo", "Botones de WhatsApp, formularios, mapa y llamadas a la acción ubicados donde el cliente los necesita."),
            ("Panel de administración", "Edita textos, imágenes y secciones tú mismo, sin depender de un programador."),
            ("Dominio, hosting y soporte", "Registramos tu dominio, alojamos el sitio con certificado SSL y te acompañamos después del lanzamiento."),
        ],
        "pasos": [
            ("Diagnóstico", "Conversamos sobre tu negocio, tu cliente en Cali y tus objetivos."),
            ("Diseño", "Te presentamos el diseño completo para que lo apruebes antes de programar."),
            ("Desarrollo", "Construimos el sitio, cargamos el contenido y conectamos las herramientas."),
            ("Lanzamiento", "Publicamos, lo conectamos con Google y te enseñamos a administrarlo."),
        ],
        "proyectos": ["vectrar", "lasevillana", "nexxosstudio"],
        "faqs": [
            ("¿Cuánto cuesta una página web en Cali?", "Depende del número de secciones, las funcionalidades y el contenido. Después de una conversación corta te enviamos una propuesta con precio y cronograma definidos."),
            ("¿Cuánto tiempo tarda el desarrollo?", "El tiempo depende del alcance del proyecto y de qué tan pronto esté listo el contenido. En la propuesta incluimos un cronograma con fechas de entrega."),
            ("¿La página se ve bien en celulares?", "Sí. Diseñamos primero para celular y probamos el sitio en distintos tamaños de pantalla antes de publicarlo."),
            ("¿Puedo actualizar la página yo mismo?", "Sí. Entregamos el sitio con un panel para editar el contenido y te explicamos cómo usarlo."),
        ],
        "wa": "Hola CBdesign, quiero cotizar una página web.",
    },
    {
        "slug": "tiendas-virtuales-cali",
        "corto": "Tiendas virtuales",
        "title": "Tiendas virtuales en Cali | Ecommerce a la medida | CBdesign",
        "desc": "Creamos tiendas virtuales en Cali con pagos en línea, inventario y envíos. Ecommerce listo para vender en Colombia, Estados Unidos y España.",
        "eyebrow": "Ecommerce en Cali",
        "h1": "Tiendas virtuales en Cali listas para vender todos los días.",
        "lead": "Desarrollamos tu ecommerce con pagos en línea, inventario sincronizado y envíos, para que vendas en Cali, en Colombia y fuera del país.",
        "intro": [
            "Una tienda virtual no es un catálogo con precios. Es un canal de ventas que debe cobrar, despachar y medir cada pedido sin que tu equipo tenga que intervenir en cada paso. Así construimos las tiendas de nuestros clientes.",
            "Desde Cali hemos desarrollado ecommerce que hoy venden en Colombia, Estados Unidos y España, con catálogos, monedas e idiomas adaptados a cada mercado.",
        ],
        "incluye": [
            ("Pagos en línea", "Integración con pasarelas de pago locales e internacionales para recibir tarjetas, PSE y otros medios."),
            ("Inventario y pedidos", "Control de existencias, estados de pedido y notificaciones automáticas para ti y para el comprador."),
            ("Envíos y guías", "Cálculo de envíos y generación de guías conectados con tu operación logística."),
            ("Experiencia de compra", "Un proceso de pago corto y claro en celular, para que el cliente termine su pedido."),
            ("Promociones", "Cupones, descuentos, productos destacados y recuperación de carritos abandonados."),
            ("Venta internacional", "Tiendas en varios idiomas y monedas cuando tu marca está lista para otros países."),
        ],
        "pasos": [
            ("Estrategia", "Definimos catálogo, medios de pago, envíos y metas de venta."),
            ("Diseño", "Diseñamos la tienda y el proceso de compra pensando en el celular."),
            ("Desarrollo", "Integramos pagos, inventario, envíos y analítica."),
            ("Lanzamiento", "Publicamos, hacemos pedidos de prueba y capacitamos a tu equipo."),
        ],
        "proyectos": ["fajasmelibelt", "conetco", "fajasmelibeltusa"],
        "faqs": [
            ("¿Qué medios de pago puedo ofrecer?", "Integramos las pasarelas de pago que mejor se ajusten a tu negocio, con tarjetas de crédito y débito, PSE y otros medios disponibles en Colombia, además de pasarelas internacionales."),
            ("¿Puedo administrar productos y precios?", "Sí. Desde el panel de la tienda puedes crear productos, cambiar precios, manejar inventario y revisar pedidos."),
            ("¿La tienda sirve para vender fuera de Colombia?", "Sí. Hemos desarrollado tiendas para Estados Unidos y España, con moneda, idioma y medios de pago de cada país."),
            ("¿Cuánto cuesta una tienda virtual?", "Depende del tamaño del catálogo y de las integraciones que necesites. Te enviamos una propuesta con precio y cronograma definidos."),
        ],
        "wa": "Hola CBdesign, quiero cotizar una tienda virtual.",
    },
    {
        "slug": "software-a-la-medida-cali",
        "corto": "Software a la medida",
        "title": "Desarrollo de software a la medida en Cali | CBdesign",
        "desc": "Desarrollo de software y aplicativos web a la medida en Cali: inventarios, logística, portales de clientes e integraciones con tus sistemas.",
        "eyebrow": "Desarrollo de software en Cali",
        "h1": "Software a la medida en Cali para ordenar tu operación.",
        "lead": "Desarrollamos aplicativos web que reemplazan hojas de cálculo y tareas manuales por procesos claros, medibles y conectados.",
        "intro": [
            "Cuando una empresa crece, las hojas de cálculo y los procesos manuales empiezan a costar tiempo y errores. Un software hecho a la medida resuelve exactamente lo que tu operación necesita, sin pagar por funciones que no usas.",
            "Trabajamos con empresas de Cali y del Valle del Cauca en herramientas de inventario, logística, auditoría y portales para clientes, conectadas con los sistemas que ya tienen.",
        ],
        "incluye": [
            ("Levantamiento de procesos", "Entendemos cómo trabaja tu equipo hoy antes de proponer la herramienta."),
            ("Paneles internos", "Aplicativos web para controlar inventario, pedidos, guías, rastreo y reportes."),
            ("Portales para clientes", "Espacios privados donde tus clientes consultan estados, documentos o pedidos."),
            ("Integraciones por API", "Conectamos el software con tu tienda, ERP, CRM o pasarela de pagos."),
            ("Reportes en tiempo real", "Indicadores claros para tomar decisiones con datos actualizados."),
            ("Soporte y evolución", "Acompañamos la herramienta con mejoras a medida que cambia tu negocio."),
        ],
        "pasos": [
            ("Levantamiento", "Documentamos el proceso actual y definimos el alcance."),
            ("Prototipo", "Te mostramos las pantallas clave antes de programar."),
            ("Desarrollo por entregas", "Avanzamos en etapas que puedes probar y ajustar."),
            ("Puesta en marcha", "Migramos datos, capacitamos al equipo y damos soporte."),
        ],
        "proyectos": ["conetco", "dauntoque", "colombiabirdfair"],
        "faqs": [
            ("¿Qué tipo de software desarrollan?", "Aplicativos web a la medida: control de inventario, logística y guías, portales de clientes, sistemas de registro y pagos, y automatizaciones entre plataformas."),
            ("¿Se puede conectar con los sistemas que ya uso?", "En la mayoría de los casos sí. Integramos por API con tiendas virtuales, ERP, CRM y pasarelas de pago. Lo confirmamos en el levantamiento."),
            ("¿De quién es el software al terminar?", "Las condiciones de propiedad y licencia quedan definidas por escrito en la propuesta, antes de iniciar el proyecto."),
            ("¿Cómo se define el costo?", "A partir del alcance documentado en el levantamiento. Trabajamos por etapas para que cada entrega tenga un valor y una fecha claros."),
        ],
        "wa": "Hola CBdesign, necesito un software a la medida.",
    },
    {
        "slug": "posicionamiento-seo-cali",
        "corto": "Posicionamiento SEO",
        "title": "Posicionamiento SEO en Cali | Agencia SEO | CBdesign",
        "desc": "Agencia de posicionamiento SEO en Cali: auditoría, SEO técnico, SEO local y contenido para que tu empresa aparezca en Google cuando te buscan.",
        "eyebrow": "Agencia SEO en Cali",
        "h1": "Posicionamiento SEO en Cali para que te encuentren primero.",
        "lead": "Trabajamos la parte técnica, el contenido y la presencia local de tu sitio para que aparezca en Google cuando tu cliente busca lo que vendes.",
        "intro": [
            "La mayoría de las personas que buscan un producto o servicio en Cali eligen entre los primeros resultados de Google. El posicionamiento SEO es el trabajo de llevar tu sitio a esos lugares de forma estable, sin pagar por cada clic.",
            "Como también desarrollamos los sitios, podemos corregir de raíz lo que frena el posicionamiento: velocidad, estructura, contenido y datos estructurados.",
        ],
        "incluye": [
            ("Auditoría SEO", "Revisamos tu sitio, tu competencia en Cali y las búsquedas donde hoy apareces o deberías aparecer."),
            ("SEO técnico", "Velocidad, indexación, estructura de URLs, metadatos, datos estructurados y sitemap."),
            ("SEO local", "Perfil de Empresa en Google, reseñas, mapas y páginas pensadas para búsquedas en Cali."),
            ("Palabras clave", "Elegimos las búsquedas con intención de compra que tu negocio sí puede ganar."),
            ("Contenido", "Páginas de servicio y artículos que responden lo que tu cliente pregunta en Google."),
            ("Medición", "Reportes con Google Search Console y Analytics: posiciones, clics y contactos generados."),
        ],
        "pasos": [
            ("Auditoría", "Medimos el estado actual del sitio y de la competencia."),
            ("Plan", "Priorizamos acciones por impacto y esfuerzo."),
            ("Implementación", "Corregimos lo técnico y publicamos el contenido."),
            ("Seguimiento", "Medimos posiciones y contactos, y ajustamos cada mes."),
        ],
        "proyectos": ["vectrar", "fajasmelibelt", "dauntoque"],
        "faqs": [
            ("¿Cuánto tarda el SEO en dar resultados?", "El SEO es un trabajo de mediano plazo. Los primeros cambios suelen verse en algunas semanas y los resultados estables toman varios meses, según la competencia de cada búsqueda."),
            ("¿Garantizan el primer lugar en Google?", "No, y nadie puede garantizarlo de forma honesta, porque el orden lo decide Google. Sí nos comprometemos con un plan claro, trabajo medible y reportes transparentes."),
            ("¿Qué es el SEO local?", "Es el trabajo para aparecer en búsquedas con intención local, como 'cerca de mí' o 'en Cali', incluyendo el mapa de Google y el Perfil de Empresa."),
            ("¿Necesito rehacer mi página para hacer SEO?", "No siempre. Primero auditamos el sitio actual. Si su estructura o su velocidad lo impiden, te explicamos qué conviene corregir o reconstruir."),
        ],
        "wa": "Hola CBdesign, quiero mejorar mi posicionamiento en Google.",
    },
    {
        "slug": "marketing-digital-cali",
        "corto": "Marketing digital",
        "title": "Agencia de marketing digital en Cali | Google Ads y Meta | CBdesign",
        "desc": "Agencia de marketing digital en Cali: campañas en Google Ads y Meta, páginas de aterrizaje y medición de conversiones para conseguir clientes.",
        "eyebrow": "Marketing digital en Cali",
        "h1": "Marketing digital en Cali enfocado en conseguir clientes.",
        "lead": "Campañas en Google y Meta, páginas de aterrizaje y medición de conversiones para que cada peso invertido se pueda seguir hasta un contacto o una venta.",
        "intro": [
            "Invertir en publicidad sin medir es apostar. Antes de activar una campaña dejamos lista la medición: qué cuenta como un contacto, de dónde llega y cuánto cuesta conseguirlo.",
            "Unimos el desarrollo web con la pauta: construimos las páginas de aterrizaje, configuramos las campañas y ajustamos con datos reales de tu negocio en Cali.",
        ],
        "incluye": [
            ("Google Ads", "Campañas de búsqueda para aparecer cuando alguien en Cali busca lo que ofreces."),
            ("Meta Ads", "Anuncios en Instagram y Facebook para dar a conocer tu marca y generar mensajes."),
            ("Páginas de aterrizaje", "Páginas rápidas y enfocadas en una sola acción: escribirte, llamarte o comprar."),
            ("Medición de conversiones", "Google Analytics y etiquetas para registrar clics en WhatsApp, formularios y ventas."),
            ("Remarketing", "Anuncios para quienes ya visitaron tu sitio y aún no te contactan."),
            ("Reportes claros", "Inversión, contactos y costo por contacto, explicados sin tecnicismos."),
        ],
        "pasos": [
            ("Objetivos", "Definimos qué resultado buscas y cuánto vale para tu negocio."),
            ("Preparación", "Dejamos listas la medición y las páginas de aterrizaje."),
            ("Campañas", "Lanzamos con un presupuesto controlado y anuncios segmentados."),
            ("Optimización", "Ajustamos palabras clave, anuncios y presupuesto según los datos."),
        ],
        "proyectos": ["fajasmelibelt", "dauntoque", "lasevillana"],
        "faqs": [
            ("¿Cuánto debo invertir en publicidad?", "Depende de tu sector y de tus metas. Recomendamos empezar con un presupuesto de prueba, medir el costo por contacto y escalar solo lo que funciona."),
            ("¿Qué diferencia hay entre SEO y publicidad en Google?", "La publicidad da visibilidad inmediata mientras pagas por cada clic. El SEO toma más tiempo, pero trae visitas sin costo por clic. Lo más efectivo suele ser combinarlos."),
            ("¿Necesito una página web para hacer campañas?", "Sí, o al menos una página de aterrizaje. Sin una página rápida y clara, gran parte de la inversión en anuncios se pierde."),
            ("¿Cómo sé si la campaña funciona?", "Configuramos la medición antes de lanzar y te entregamos reportes con inversión, contactos generados y costo por contacto."),
        ],
        "wa": "Hola CBdesign, quiero información sobre campañas de marketing digital.",
    },
    {
        "slug": "agentes-ia-whatsapp-cali",
        "corto": "Agentes de IA para WhatsApp",
        "title": "Agentes de IA para WhatsApp en Cali | Automatización | CBdesign",
        "desc": "Implementamos agentes de inteligencia artificial para WhatsApp en Cali: atención inmediata, asesoría sobre tu catálogo y automatización de procesos.",
        "eyebrow": "Inteligencia artificial y automatización",
        "h1": "Agentes de IA para WhatsApp que atienden y venden a cualquier hora.",
        "lead": "Configuramos un asistente de inteligencia artificial que conoce tu catálogo y tus políticas, responde al instante y pasa la conversación a tu equipo cuando hace falta.",
        "intro": [
            "En Colombia las ventas se cierran por WhatsApp, y un mensaje sin respuesta es un cliente que le escribe a otro. Un agente de IA atiende de inmediato, a cualquier hora, con la información real de tu negocio.",
            "Desde Cali implementamos agentes conectados con tu tienda virtual, tu CRM o tu agenda, para que además de responder puedan consultar disponibilidad, tomar datos y agendar.",
        ],
        "incluye": [
            ("Entrenamiento con tu negocio", "El agente aprende tu catálogo, precios, políticas y preguntas frecuentes."),
            ("Atención inmediata", "Responde en segundos, todos los días, sin dejar mensajes en espera."),
            ("Paso a un asesor", "Entrega la conversación a una persona de tu equipo cuando el caso lo requiere."),
            ("Integraciones", "Se conecta por API con tu tienda, CRM, inventario o agenda."),
            ("Automatización", "Seguimientos, recordatorios y tareas repetitivas que dejan de ser manuales."),
            ("Mejora continua", "Revisamos las conversaciones y ajustamos las respuestas con datos reales."),
        ],
        "pasos": [
            ("Diagnóstico", "Revisamos qué preguntan tus clientes y cómo responde hoy tu equipo."),
            ("Configuración", "Entrenamos el agente con tu información y definimos sus límites."),
            ("Pruebas", "Lo validamos contigo en conversaciones reales antes de activarlo."),
            ("Operación", "Lo activamos, lo monitoreamos y lo mejoramos con el uso."),
        ],
        "proyectos": ["fajasmelibelt", "conetco", "dauntoque"],
        "faqs": [
            ("¿El agente reemplaza a mi equipo de ventas?", "No. Atiende las consultas repetitivas y fuera de horario, y le entrega a tu equipo las conversaciones que necesitan a una persona."),
            ("¿Funciona con mi número de WhatsApp actual?", "Se implementa sobre WhatsApp Business. En el diagnóstico revisamos tu número y te indicamos la forma de conectarlo."),
            ("¿Qué pasa si el agente no sabe una respuesta?", "Lo configuramos para que no invente: cuando no tiene la información, lo dice y pasa la conversación a un asesor."),
            ("¿Se puede conectar con mi tienda virtual?", "Sí. Puede consultar productos, precios y disponibilidad si tu tienda o tu sistema ofrecen una API."),
        ],
        "wa": "Hola CBdesign, quiero un agente de IA para mi WhatsApp.",
    },
]

e = html.escape
ICONO_WA = __import__("re").search(r'<a class="wa".*?(<svg.*?</svg>)', (RAIZ / "index.html").read_text(encoding="utf-8"), __import__("re").S).group(1)


def wa(texto):
    return WA + quote(texto)


def pie():
    enlaces = "\n".join(f'      <a href="/{s["slug"]}/">{e(s["corto"])}</a>' for s in SERVICIOS)
    return f"""<footer class="pie oscuro">
  <div class="wrap pie-in">
    <div class="pie-marca">
      <img src="/assets/img/logo-blanco.png" alt="CBdesign" width="225" height="72" loading="lazy">
      <p>Desarrollo web y marketing digital en Cali para empresas que quieren crecer.</p>
    </div>
    <nav aria-label="Servicios">
      <h2>Servicios</h2>
{enlaces}
    </nav>
    <nav aria-label="Empresa">
      <h2>Empresa</h2>
      <a href="/#proceso">Proceso</a>
      <a href="https://portafolio.cbdesign.com.co" target="_blank" rel="noopener">Portafolio</a>
      <a href="/#dominios">Buscar dominio</a>
      <a href="/#preguntas">Preguntas frecuentes</a>
    </nav>
    <address>
      <h2>Contacto</h2>
      <a href="https://wa.me/573164956994" target="_blank" rel="noopener">WhatsApp +57 316 495 6994</a>
      <a href="mailto:contacto@cbdesign.com.co">contacto@cbdesign.com.co</a>
      <span>Calle 6 # 9-45, Cali, Colombia</span>
    </address>
  </div>
  <div class="wrap pie-legal">
    <p>© <span id="anio">2026</span> CBdesign. Una marca de Commonbird · NIT 900792449. Todos los derechos reservados.</p>
  </div>
</footer>"""


def pagina(s):
    url = f"{BASE}/{s['slug']}/"
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": url + "#servicio",
                "name": s["h1"].rstrip("."),
                "serviceType": s["corto"],
                "description": s["desc"],
                "url": url,
                "provider": {"@id": BASE + "/#organizacion"},
                "areaServed": [
                    {"@type": "City", "name": "Cali"},
                    {"@type": "AdministrativeArea", "name": "Valle del Cauca"},
                    {"@type": "Country", "name": "Colombia"},
                ],
            },
            {
                "@type": "WebPage",
                "@id": url + "#pagina",
                "url": url,
                "name": s["title"],
                "description": s["desc"],
                "inLanguage": "es-CO",
                "isPartOf": {"@id": BASE + "/#sitio"},
                "about": {"@id": url + "#servicio"},
                "breadcrumb": {"@id": url + "#migas"},
            },
            {
                "@type": "BreadcrumbList",
                "@id": url + "#migas",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE + "/"},
                    {"@type": "ListItem", "position": 2, "name": s["corto"], "item": url},
                ],
            },
            {
                "@type": "FAQPage",
                "@id": url + "#preguntas",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in s["faqs"]
                ],
            },
        ],
    }
    intro = "\n".join(f"        <p>{e(p)}</p>" for p in s["intro"])
    incluye = "\n".join(
        f'        <li class="reveal"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in s["incluye"]
    )
    pasos = "\n".join(
        f'        <li class="reveal"><span class="paso-n">0{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>'
        for i, (t, d) in enumerate(s["pasos"], 1)
    )
    proys = "\n".join(
        f'        <li class="reveal"><a class="proy" href="{PROYECTOS[p][1]}" target="_blank" rel="noopener">'
        f'<img src="/assets/img/{p}.webp" alt="Sitio de {e(PROYECTOS[p][0])}, desarrollado por CBdesign" width="720" height="496" loading="lazy" decoding="async">'
        f'<div class="proy-txt"><span>{e(PROYECTOS[p][2])}</span><h3>{e(PROYECTOS[p][0])}</h3></div></a></li>'
        for p in s["proyectos"]
    )
    faqs = "\n".join(
        f'        <details class="reveal"><summary><h3>{e(q)}</h3></summary><p>{e(a)}</p></details>'
        for q, a in s["faqs"]
    )
    otros = "\n".join(
        f'        <li><a href="/{o["slug"]}/">{e(o["corto"])} en Cali <span aria-hidden="true">›</span></a></li>'
        for o in SERVICIOS
        if o["slug"] != s["slug"]
    )
    return f"""<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(s['title'])}</title>
<meta name="description" content="{e(s['desc'])}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta name="geo.region" content="CO-VAC">
<meta name="geo.placename" content="Cali">
<meta property="og:locale" content="es_CO">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CBdesign">
<meta property="og:title" content="{e(s['title'])}">
<meta property="og:description" content="{e(s['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#000000">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/sitio.css?v={VERSION}">
<meta name="cb-ga4" content="">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>

<header class="nav" id="nav">
  <div class="nav-in">
    <a class="logo" href="/" aria-label="CBdesign, inicio">
      <img src="/assets/img/logo-blanco.png" alt="CBdesign" width="225" height="72">
    </a>
    <nav class="nav-links" id="menu" aria-label="Principal">
      <a href="/#servicios">Servicios</a>
      <a href="/#proceso">Proceso</a>
      <a href="/#proyectos">Proyectos</a>
      <a href="/#dominios">Dominios</a>
      <a href="/#preguntas">Preguntas</a>
    </nav>
    <a class="btn btn-brand btn-sm nav-cta" href="{wa(s['wa'])}" target="_blank" rel="noopener">Cotizar</a>
    <button class="nav-toggle" id="nav-toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu"><span></span><span></span></button>
  </div>
</header>

<main id="contenido">
  <section class="sub-hero oscuro">
    <div class="hero-glow" aria-hidden="true"></div>
    <div class="wrap sub-hero-in">
      <nav class="migas" aria-label="Ruta de navegación"><a href="/">Inicio</a><span aria-hidden="true">›</span><span aria-current="page">{e(s['corto'])}</span></nav>
      <p class="eyebrow">{e(s['eyebrow'])}</p>
      <h1>{e(s['h1'])}</h1>
      <p class="lead">{e(s['lead'])}</p>
      <div class="acciones">
        <a class="btn btn-brand" href="{wa(s['wa'])}" target="_blank" rel="noopener">Cotizar por WhatsApp</a>
        <a class="btn btn-link" href="#incluye">Ver qué incluye <span aria-hidden="true">›</span></a>
      </div>
    </div>
  </section>

  <section class="seccion claro" id="incluye">
    <div class="wrap">
      <div class="prosa reveal">
{intro}
      </div>
      <h2 class="reveal sub-h2">Qué incluye</h2>
      <ul class="incluye">
{incluye}
      </ul>
    </div>
  </section>

  <section class="seccion oscuro">
    <div class="wrap">
      <header class="cabecera">
        <p class="eyebrow reveal">Proceso</p>
        <h2 class="reveal">Cómo trabajamos contigo.</h2>
      </header>
      <ol class="pasos-mini">
{pasos}
      </ol>
    </div>
  </section>

  <section class="seccion claro">
    <div class="wrap">
      <header class="cabecera">
        <p class="eyebrow reveal">Proyectos</p>
        <h2 class="reveal">Trabajo real, en línea hoy.</h2>
      </header>
      <ul class="proy-grid">
{proys}
      </ul>
      <p class="reveal mas-proy"><a class="btn btn-oscuro" href="https://portafolio.cbdesign.com.co" target="_blank" rel="noopener">Ver el portafolio completo</a></p>
    </div>
  </section>

  <section class="seccion claro sin-tope" id="preguntas">
    <div class="wrap faq-wrap">
      <header class="cabecera">
        <p class="eyebrow reveal">Preguntas frecuentes</p>
        <h2 class="reveal">Lo que suelen preguntarnos.</h2>
      </header>
      <div class="faq">
{faqs}
      </div>
    </div>
  </section>

  <section class="cierre oscuro" id="contacto">
    <div class="cierre-glow" aria-hidden="true"></div>
    <div class="wrap centro">
      <h2 class="reveal cierre-h">Hablemos de <span class="grad">tu proyecto.</span></h2>
      <p class="lead reveal">Estamos en Cali, en la Calle 6 # 9-45, y trabajamos con empresas de todo el Valle del Cauca y de otros países.</p>
      <div class="acciones reveal">
        <a class="btn btn-brand btn-xl" href="{wa(s['wa'])}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
        <a class="btn btn-link" href="tel:+573164956994">316 495 6994 <span aria-hidden="true">›</span></a>
      </div>
      <ul class="otros reveal" aria-label="Otros servicios">
{otros}
      </ul>
    </div>
  </section>
</main>

{pie()}

<a class="wa" href="{wa(s['wa'])}" target="_blank" rel="noopener" aria-label="Escribir a CBdesign por WhatsApp">
  {ICONO_WA}
</a>

<script src="/assets/sitio.js?v={VERSION}" defer></script>
</body>
</html>
"""


def main():
    for s in SERVICIOS:
        d = RAIZ / s["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(pagina(s), encoding="utf-8")
        print("ok", s["slug"])
    hoy = datetime.date.today().isoformat()
    urls = [BASE + "/"] + [f"{BASE}/{s['slug']}/" for s in SERVICIOS]
    cuerpo = "\n".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{hoy}</lastmod>\n  </url>" for u in urls)
    (RAIZ / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + cuerpo + "\n</urlset>\n", encoding="utf-8")
    print("ok sitemap.xml")


if __name__ == "__main__":
    main()
