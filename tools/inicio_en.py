"""English text for the home page (/en/). Used by generar-ingles.py.

T maps every visible Spanish string of sitio/index.html to English. The generator
fails if a string is missing, so the two versions cannot drift apart silently.
"""

TITLE = "Web Design & Development Agency for US Businesses | CBdesign"
DESC = "Nearshore web design, ecommerce, custom software and AI agents from Colombia for US businesses. 120+ websites delivered in 11 years."
OG_TITLE = "CBdesign | Nearshore web design and development"
OG_DESC = "Websites, online stores, custom software and AI agents that grow your business. 120+ websites delivered in 11 years."

H1 = [("Websites", 0), ("that", 0), ("sell.", 0), ("Software", 1), ("that", 1), ("scales.", 1)]

# Replaces the "Estamos en Cali" block: for US visitors the point is nearshore, not local.
LOCAL = """      <div class="local reveal">
        <div>
          <p class="eyebrow">Nearshore from Colombia</p>
          <h2>Your web team in the same time zone, working in English and Spanish.</h2>
          <p class="lead">We are based in Cali, Colombia (UTC-5), so our day overlaps with US business hours. We already work with brands selling in the United States, Colombia and Spain.</p>
          <address class="local-nap">
            <span><b>CBdesign</b> · Calle 6 # 9-45, Cali, Colombia</span>
            <a href="tel:+573164956994">+57 316 495 6994</a>
            <a href="mailto:contacto@cbdesign.com.co">contacto@cbdesign.com.co</a>
          </address>
        </div>
        <ul class="local-serv" aria-label="Services">
          <li><a href="/en/web-design/">Web design and development <span aria-hidden="true">›</span></a></li>
          <li><a href="/en/ecommerce-development/">Ecommerce development <span aria-hidden="true">›</span></a></li>
          <li><a href="/en/custom-software-development/">Custom software development <span aria-hidden="true">›</span></a></li>
          <li><a href="/en/seo-services/">SEO services <span aria-hidden="true">›</span></a></li>
          <li><a href="/en/digital-marketing/">Digital marketing <span aria-hidden="true">›</span></a></li>
          <li><a href="/en/whatsapp-ai-agents/">AI agents for WhatsApp <span aria-hidden="true">›</span></a></li>
        </ul>
      </div>
"""

WA = {
    "Hola CBdesign, mi meta es automatizar mi operación.": "Hi CBdesign, my goal is to automate my operation.",
    "Hola CBdesign, mi meta es conseguir más clientes.": "Hi CBdesign, my goal is to get more customers.",
    "Hola CBdesign, mi meta es vender en otros países.": "Hi CBdesign, my goal is to sell in other countries.",
    "Hola CBdesign, mi meta es vender más en línea.": "Hi CBdesign, my goal is to sell more online.",
    "Hola CBdesign, necesito un software a la medida.": "Hi CBdesign, I need custom software.",
    "Hola CBdesign, quiero cotizar un sitio web.": "Hi CBdesign, I would like a quote for a website.",
    "Hola CBdesign, quiero cotizar una tienda virtual.": "Hi CBdesign, I would like a quote for an online store.",
    "Hola CBdesign, quiero hablar de mi proyecto.": "Hi CBdesign, I would like to talk about my project.",
    "Hola CBdesign, quiero iniciar un proyecto.": "Hi CBdesign, I would like to start a project.",
    "Hola CBdesign, quiero mejorar mi posicionamiento en Google.": "Hi CBdesign, I would like to improve my Google rankings.",
    "Hola CBdesign, quiero un agente de IA para mi WhatsApp.": "Hi CBdesign, I would like an AI agent for my WhatsApp.",
}

# Raw replacements applied before the text pass (code sample, JSON-LD, links).
CRUDO = [
    ("tienda = ", "store = "), ("<span class=\"f\">crear</span>", "<span class=\"f\">create</span>"),
    ("  pagos: <span class=\"s\">'en línea'</span>", "  payments: <span class=\"s\">'online'</span>"),
    ("  inventario: <span class=\"s\">'sincronizado'</span>", "  inventory: <span class=\"s\">'synced'</span>"),
    ("// pruebas: 48 de 48 correctas", "// tests: 48 of 48 passing"),
    ("<span class=\"f\">publicar</span>(tienda)", "<span class=\"f\">publish</span>(store)"),
    ('placeholder="tumarca.com"', 'placeholder="yourbrand.com"'),
]

FAQ_LD = [
    ("What kind of projects does CBdesign build?", "Corporate websites, online stores, custom software, automations and AI agents for WhatsApp. We also handle SEO, domains, hosting and maintenance."),
    ("How much does a website or an online store cost?", "It depends on the scope: number of sections, catalog, integrations and features. After a short call we send a proposal with a fixed price and a timeline, with no hidden costs."),
    ("Can you work with companies in the United States?", "Yes. We have active projects in the United States, Colombia and Spain. We work in English and Spanish, and Colombia's time zone (UTC-5) overlaps with US business hours."),
    ("Will my site show up on Google?", "Yes. Every project ships with technical SEO: semantic structure, fast load times, structured data, sitemap and Google Search Console set up. Rankings also depend on content and competition, and we support you in that work."),
    ("Can I manage the content myself?", "Yes. We deliver the site with an admin panel so you can edit text, images, products and prices without a developer, and we train you to use it."),
    ("Do you help with domains and hosting?", "Yes. You can check domain availability on this page and we register it and set up hosting, the SSL certificate and business email."),
]

T = {
    "tumarca.com": "yourbrand.com",
    "Saltar al contenido": "Skip to content",
    "Servicios": "Services", "Proceso": "Process", "Proyectos": "Work", "Dominios": "Domains",
    "Agente IA": "AI agent", "Preguntas": "FAQ", "Iniciar proyecto": "Start a project",
    "Desarrollo web y marketing digital en Cali y toda Colombia": "Nearshore web design and development",
    "Diseñamos y desarrollamos sitios web, tiendas virtuales y herramientas a la medida para que tu empresa venda más y opere mejor.":
        "We design and build websites, online stores and custom tools so your company sells more and runs better.",
    "Ver proyectos": "See our work",
    "sitios web construidos": "websites delivered", "años en el mercado": "years in business",
    "países con clientes activos": "countries with active clients", "desarrollo a la medida": "custom development",
    "Tu meta": "Your goal",
    "Dinos a dónde quieres llegar. Nosotros trazamos la ruta.": "Tell us where you want to go. We map the route.",
    "Vender más en línea": "Sell more online", "Conseguir más clientes": "Get more customers",
    "Ahorrar tiempo operativo": "Save operating time", "Llegar a otros países": "Reach new countries",
    "Una tienda que cobra, despacha y mide cada venta.": "A store that charges, ships and measures every sale.",
    "Convertimos tu catálogo en un canal de ventas que trabaja todos los días, con una experiencia de compra tan simple que el cliente termina el pedido.":
        "We turn your catalog into a sales channel that works every day, with a checkout so simple that customers finish the order.",
    "Tienda virtual": "Online store", "con pagos en línea y envíos": "with online payments and shipping",
    "Agente de IA": "AI agent", "que resuelve dudas por WhatsApp": "that answers questions on WhatsApp",
    "Campañas y SEO": "Campaigns and SEO", "que traen compradores": "that bring buyers",
    "Quiero vender más": "I want to sell more", "Un ejemplo:": "An example:",
    "Un sitio que te encuentra clientes mientras trabajas.": "A site that finds you customers while you work.",
    "Diseñamos tu sitio para que aparezca en Google, transmita confianza en segundos y lleve a cada visitante a escribirte o pedir una cotización.":
        "We design your site to show up on Google, build trust in seconds and lead every visitor to contact you or request a quote.",
    "Sitio corporativo": "Corporate site", "rápido y claro": "fast and clear",
    "SEO técnico": "Technical SEO", "y contenido para posicionar": "and content built to rank",
    "WhatsApp y formularios": "Forms and WhatsApp", "que convierten": "that convert",
    "Quiero más clientes": "I want more customers",
    "Menos tareas repetidas. Más tiempo para crecer.": "Fewer repetitive tasks. More time to grow.",
    "Automatizamos lo que hoy haces a mano: inventarios, guías, reportes y respuestas. Tu equipo deja de digitar y se dedica a lo que genera valor.":
        "We automate what you do by hand today: inventory, shipping labels, reports and replies. Your team stops typing and focuses on work that creates value.",
    "Software a la medida": "Custom software", "para tu operación": "for your operation",
    "Integraciones": "Integrations", "entre tus sistemas": "between your systems",
    "Automatización": "Automation", "de atención y procesos": "of support and processes",
    "Quiero automatizar": "I want to automate",
    "Tu marca, lista para vender en otro idioma y otra moneda.": "Your brand, ready to sell in another language and currency.",
    "Llevamos tu negocio a nuevos mercados con tiendas adaptadas a cada país: idioma, moneda, medios de pago y logística.":
        "We take your business into new markets with stores adapted to each country: language, currency, payment methods and logistics.",
    "Tiendas por país": "Country stores", "con checkout internacional": "with international checkout",
    "Infraestructura": "Infrastructure", "rápida en cada región": "fast in every region",
    "SEO internacional": "International SEO", "para cada mercado": "for each market",
    "Quiero expandirme": "I want to expand",
    "Todo lo que tu marca necesita para vender en internet.": "Everything your brand needs to sell online.",
    "Un solo equipo para la estrategia, el diseño, el código y el crecimiento. Toca un servicio para ver el detalle.":
        "One team for strategy, design, code and growth. Tap a service to see the details.",
    "Diseño y desarrollo de sitios web": "Web design and development",
    "Sitios corporativos rápidos, claros y pensados para convertir visitas en clientes.":
        "Fast, clear corporate websites designed to turn visitors into customers.",
    "Diseñamos cada página a partir de tu marca y de lo que busca tu cliente. Nada de plantillas genéricas: estructura, textos y diseño trabajan para que te contacten o te compren.":
        "We design every page around your brand and what your customer is looking for. No generic templates: structure, copy and design work together so people contact you or buy.",
    "Diseño a la medida, adaptable a celular, tableta y computador": "Custom design that adapts to phone, tablet and desktop",
    "Carga rápida y SEO técnico desde el primer día": "Fast loading and technical SEO from day one",
    "Panel para editar el contenido sin programador": "Admin panel to edit content without a developer",
    "Formularios, WhatsApp, mapas, reservas y analítica": "Forms, WhatsApp, maps, bookings and analytics",
    "Cotizar mi sitio web": "Get a website quote", "Ver el servicio completo": "See the full service",
    "Tiendas virtuales": "Online stores",
    "Ecommerce con pagos en línea, inventario y envíos, listo para vender dentro y fuera del país.":
        "Ecommerce with online payments, inventory and shipping, ready to sell at home and abroad.",
    "No hacemos simples catálogos. Construimos tiendas que cobran, despachan y miden cada venta, con experiencia en mercados de Colombia, Estados Unidos y España.":
        "We do not build simple catalogs. We build stores that charge, ship and measure every sale, with experience in the United States, Colombia and Spain.",
    "Pasarelas de pago locales e internacionales": "Local and international payment gateways",
    "Varios idiomas y monedas": "Multiple languages and currencies",
    "Sincronización de inventario y generación de guías": "Inventory sync and shipping labels",
    "Promociones, cupones y recuperación de carritos": "Promotions, coupons and cart recovery",
    "Cotizar mi tienda": "Get a store quote",
    "Aplicativos web que ordenan tu operación: inventarios, logística, auditoría y reportes.":
        "Web apps that organize your operation: inventory, logistics, audits and reports.",
    "Cuando una hoja de cálculo ya no alcanza, desarrollamos la herramienta exacta que necesita tu equipo, conectada con los sistemas que ya usas.":
        "When a spreadsheet is no longer enough, we build the exact tool your team needs, connected to the systems you already use.",
    "Paneles internos y portales para clientes": "Internal dashboards and client portals",
    "Integraciones por API con tu ERP, CRM o tienda": "API integrations with your ERP, CRM or store",
    "Control de inventario, guías y rastreo": "Inventory, shipping label and tracking control",
    "Código limpio y arquitectura preparada para crecer": "Clean code and an architecture ready to grow",
    "Hablar de mi software": "Talk about my software",
    "Agentes de IA y automatización": "AI agents and automation",
    "Un asistente en WhatsApp que responde, asesora y vende a cualquier hora.":
        "A WhatsApp assistant that answers, advises and sells at any hour.",
    "Configuramos un agente de inteligencia artificial que conoce tu catálogo y tus políticas, resuelve dudas en segundos y pasa la conversación a tu equipo cuando hace falta.":
        "We set up an AI agent that knows your catalog and policies, answers questions in seconds and hands the conversation to your team when needed.",
    "Atención inmediata, 24 horas, por WhatsApp": "Instant replies on WhatsApp, 24 hours a day",
    "Entiende tu catálogo, precios y disponibilidad": "Understands your catalog, prices and availability",
    "Conectado con tu tienda, CRM o agenda": "Connected to your store, CRM or calendar",
    "Automatización de tareas repetitivas del equipo": "Automation of your team's repetitive tasks",
    "Quiero mi agente": "I want my agent",
    "SEO y marketing digital": "SEO and digital marketing",
    "Posicionamiento en Google, campañas y analítica para atraer clientes reales.":
        "Google rankings, campaigns and analytics to attract real customers.",
    "Un sitio bonito que nadie encuentra no vende. Trabajamos la parte técnica, el contenido y la pauta para que aparezcas cuando tu cliente te está buscando.":
        "A beautiful site nobody finds does not sell. We work on the technical side, the content and the ads so you show up when your customer is searching.",
    "Auditoría y SEO técnico: velocidad, estructura y datos estructurados": "Audit and technical SEO: speed, structure and structured data",
    "Estrategia de palabras clave y contenido": "Keyword and content strategy",
    "Campañas en Google y Meta orientadas a conversión": "Conversion-focused Google and Meta campaigns",
    "Reportes claros con Google Analytics y Search Console": "Clear reports with Google Analytics and Search Console",
    "Mejorar mi posicionamiento": "Improve my rankings",
    "Dominios, hosting y mantenimiento": "Domains, hosting and maintenance",
    "Tu sitio siempre en línea, seguro y actualizado. Nosotros nos ocupamos de la parte técnica.":
        "Your site always online, secure and up to date. We take care of the technical side.",
    "Registramos tu dominio, alojamos tu sitio en servidores optimizados y lo mantenemos al día para que no tengas que preocuparte por nada técnico.":
        "We register your domain, host your site on optimized servers and keep it current so you never have to worry about the technical details.",
    "Registro y renovación de dominios": "Domain registration and renewal",
    "Hosting rápido con certificado SSL": "Fast hosting with SSL certificate",
    "Correos corporativos con tu dominio": "Business email on your domain",
    "Copias de seguridad, actualizaciones y soporte directo": "Backups, updates and direct support",
    "Buscar mi dominio": "Search my domain",
    "De la idea al lanzamiento,": "From idea to launch,", "sin fricción.": "without friction.",
    "Objetivo: más cotizaciones": "Goal: more quote requests", "Público: empresas B2B": "Audience: B2B companies",
    "Rendimiento": "Performance", "Accesibilidad": "Accessibility",
    "Estrategia": "Strategy",
    "Entendemos tu negocio, tu cliente y tu competencia. Definimos objetivos medibles, la estructura del sitio y las palabras clave antes de diseñar una sola pantalla.":
        "We learn your business, your customer and your competition. We define measurable goals, the site structure and the keywords before designing a single screen.",
    "Diseño": "Design",
    "Creamos una interfaz propia para tu marca, primero en celular. Apruebas el diseño completo antes de pasar a desarrollo, sin sorpresas.":
        "We create an interface made for your brand, mobile first. You approve the full design before development starts, with no surprises.",
    "Desarrollo": "Development",
    "Programamos con código limpio y optimizado. Integramos pagos, inventario, WhatsApp y las herramientas que tu operación necesita.":
        "We write clean, optimized code. We integrate payments, inventory, WhatsApp and the tools your operation needs.",
    "Lanzamiento y crecimiento": "Launch and growth",
    "Publicamos, medimos y mejoramos. Entregamos el sitio con SEO técnico, analítica conectada y capacitación para tu equipo, y seguimos contigo.":
        "We publish, measure and improve. We deliver the site with technical SEO, analytics connected and training for your team, and we stay with you.",
    "Trabajo real, en línea hoy.": "Real work, live today.",
    "Tienda virtual · Colombia, EE. UU. y España": "Online store · Colombia, USA and Spain",
    "Ecommerce en tres países, con catálogo, pagos en línea y checkout internacional.":
        "Ecommerce in three countries, with catalog, online payments and international checkout.",
    "Tienda virtual · Fibra óptica": "Online store · Fiber optics",
    "Catálogo y venta en línea de conectores, patchcords y mufas para redes.":
        "Catalog and online sales of connectors, patch cords and closures for fiber networks.",
    "Producto digital · Tarjetas NFC": "Digital product · NFC cards",
    "Tarjetas de presentación inteligentes con perfil digital, estadísticas y compra en línea.":
        "Smart business cards with a digital profile, statistics and online purchase.",
    "Evento internacional": "International event",
    "Sitio oficial de la feria de aves: conferencistas, salidas, registro y pagos.":
        "Official site of the bird fair: speakers, field trips, registration and payments.",
    "Corporativo · Arquitectura": "Corporate · Architecture",
    "Portafolio de proyectos, inmuebles, casas modulares y cotización por WhatsApp.":
        "Project portfolio, properties, modular homes and quotes through WhatsApp.",
    "Corporativo · Finanzas · EE. UU.": "Corporate · Finance · USA",
    "Plataforma de banca de inversión con soluciones, transacciones y solicitud en línea.":
        "Investment banking platform with solutions, transactions and online application.",
    "Corporativo · Industria textil": "Corporate · Textile industry",
    "Estudio textil que crea marcas de principio a fin: proceso, servicios y contacto.":
        "Textile studio that builds brands end to end: process, services and contact.",
    "Corporativo · Gastronomía": "Corporate · Food service",
    "Presencia digital para carnicerías y restaurantes, con sedes y reservas.":
        "Digital presence for butcher shops and restaurants, with locations and reservations.",
    "Ver el portafolio completo": "See the full portfolio",
    "Conoce todos los proyectos destacados y recórrelos en vivo.": "Browse all featured projects and visit them live.",
    "Tu marca empieza": "Your brand starts", "con un nombre.": "with a name.",
    "Consulta en tiempo real si tu dominio está disponible. Si está libre, lo registramos por ti.":
        "Check in real time whether your domain is available. If it is free, we register it for you.",
    "Nombre de dominio": "Domain name", "Buscar": "Search",
    "Disponibilidad consultada en los registros oficiales de cada extensión. El registro se confirma al momento de la compra.":
        "Availability is checked against the official registry of each extension. Registration is confirmed at purchase.",
    "Agente de IA para WhatsApp": "AI agent for WhatsApp",
    "Tu mejor vendedor no duerme.": "Your best salesperson never sleeps.",
    "Implementamos un agente de inteligencia artificial que atiende tu WhatsApp, conoce tu catálogo y resuelve objeciones al instante. Tu equipo se queda con las conversaciones que de verdad necesitan a una persona.":
        "We deploy an AI agent that handles your WhatsApp, knows your catalog and answers objections instantly. Your team keeps the conversations that truly need a person.",
    "Responde en segundos, a cualquier hora": "Replies in seconds, at any hour",
    "Entrenado con tus productos, precios y políticas": "Trained on your products, prices and policies",
    "Conectado por API con tu tienda y tus sistemas": "Connected by API to your store and systems",
    "Quiero mi agente de IA": "I want my AI agent",
    "Agente CBdesign": "CBdesign agent", "en línea": "online",
    "Hola, vi la solución de automatización en su catálogo, pero manejo volúmenes variables. ¿Cómo funciona la tarifa?":
        "Hi, I saw the automation solution in your catalog, but my volume varies. How does pricing work?",
    "¡Hola! La tarifa se adapta a tu volumen mensual y el agente se integra por API con tus sistemas. ¿Te calculo el ahorro estimado?":
        "Hi! Pricing adapts to your monthly volume and the agent integrates with your systems by API. Want me to estimate your savings?",
    "Sí, por favor. Recibimos unos 800 mensajes al mes.": "Yes, please. We get about 800 messages a month.",
    "Con 800 mensajes, tu equipo recupera cerca de 40 horas al mes. ¿Agendamos una demostración de 15 minutos?":
        "With 800 messages, your team gets back about 40 hours a month. Shall we book a 15-minute demo?",
    "Clientes": "Clients", "Metas cumplidas,": "Goals reached,", "contadas por ellos.": "in their words.",
    "Desde que implementamos el ecommerce con ellos, nuestras ventas aquí en Estados Unidos han despegado bárbaro. ¡Un trabajo nítido y de altísima calidad!":
        "Since we launched the ecommerce site with them, our sales here in the United States have taken off. Sharp, top-quality work!",
    "Miami, Estados Unidos ·": "Miami, United States ·",
    "El desarrollo de nuestra plataforma de sincronización en tiempo real soportó picos de tráfico altísimos sin caerse. Simplemente brutal el rendimiento de los servidores.":
        "Our real-time sync platform handled very high traffic peaks without going down. The server performance is simply outstanding.",
    "Madrid, España ·": "Madrid, Spain ·",
    "La implementación de su sistema de guías y rastreo logístico redujo nuestros tiempos operativos a la mitad. Un nivel de ingeniería de procesos impecable.":
        "Their shipping label and tracking system cut our operating times in half. Flawless process engineering.",
    "Director de Logística ·": "Logistics Director ·",
    "El equipo de CBdesign nos ayudó a escalar la empresa de una forma increíble. La organización de procesos y el desarrollo que nos hicieron son una berraquera, nos ahorra horas de trabajo.":
        "The CBdesign team helped us scale the company in an incredible way. The process organization and the development they did for us are fantastic and save us hours of work.",
    "Preguntas frecuentes": "Frequently asked questions", "Lo que suelen preguntarnos.": "What clients usually ask.",
    "¿Listo para tu": "Ready for your", "próximo proyecto?": "next project?",
    "Cuéntanos qué necesitas. Te respondemos con una ruta clara para llegar a tu meta.":
        "Tell us what you need. We will reply with a clear route to reach your goal.",
    "Escribir por WhatsApp": "Message us on WhatsApp",
    "Desarrollo web y marketing digital para empresas de Cali y de toda Colombia.":
        "Nearshore web development and digital marketing for companies that want to grow.",
    "Diseño de páginas web": "Web design", "Posicionamiento SEO": "SEO services", "Marketing digital": "Digital marketing",
    "Agentes de IA para WhatsApp": "AI agents for WhatsApp",
    "Empresa": "Company", "Portafolio": "Portfolio", "Buscar dominio": "Domain search", "Contacto": "Contact",
    "CBdesign. Una marca de Commonbird · NIT 900792449. Todos los derechos reservados.":
        "CBdesign. A Commonbird brand · NIT 900792449. All rights reserved.",
    # attributes
    "CBdesign, inicio": "CBdesign, home", "Principal": "Main", "Abrir menú": "Open menu",
    "Tienda virtual de Fajas Melibelt desarrollada por CBdesign": "Fajas Melibelt online store, built by CBdesign",
    "CBdesign en cifras": "CBdesign in numbers", "Elige tu meta": "Choose your goal",
    "Tienda virtual de Fajas Melibelt": "Fajas Melibelt online store",
    "Sitio corporativo de Vectrar": "Vectrar corporate website",
    "Tienda virtual de Conetco": "Conetco online store",
    "Tienda de Melibelt para Estados Unidos": "Melibelt store for the United States",
    "Ver detalle de diseño y desarrollo de sitios web": "See details of web design and development",
    "Ver detalle de tiendas virtuales": "See details of online stores",
    "Ver detalle de software a la medida": "See details of custom software",
    "Ver detalle de agentes de IA y automatización": "See details of AI agents and automation",
    "Ver detalle de SEO y marketing digital": "See details of SEO and digital marketing",
    "Ver detalle de dominios, hosting y mantenimiento": "See details of domains, hosting and maintenance",
    "Proyectos anteriores": "Previous projects", "Proyectos siguientes": "Next projects",
    "Proyectos destacados": "Featured projects",
    "Tienda virtual de Conetco, fibra óptica": "Conetco online store, fiber optics",
    "Sitio de Da un Toque, tarjetas NFC": "Da un Toque website, NFC cards",
    "Sitio oficial de Colombia Birdfair": "Official Colombia Birdfair website",
    "Sitio corporativo de Vectrar, arquitectura e inmobiliaria": "Vectrar corporate website, architecture and real estate",
    "Sitio corporativo de Evo Capital Group": "Evo Capital Group corporate website",
    "Sitio corporativo de Nexxos Studio": "Nexxos Studio corporate website",
    "Sitio corporativo de La Sevillana": "La Sevillana corporate website",
    "Resultados de disponibilidad": "Availability results",
    "Ejemplo de conversación con el agente de IA": "Sample conversation with the AI agent",
    "Escribir a CBdesign por WhatsApp": "Message CBdesign on WhatsApp",
    "EN, English": "ES, Español",
}

# Strings that stay the same in both languages.
IGUAL = {
    "fajasmelibelt.com", "Fajas Melibelt", "Conetco", "Da un Toque", "Colombia Birdfair", "Vectrar", "La Sevillana",
    "Nexxos Studio", "Evo Capital Group", "Dacnis Valle", "Melibelt USA", "SEO", "CB", "RS", "Roberto S.",
    "fajasmelibeltusa.com", "EG", "Elena G.", "melibelt.es", "DL", "David L.", "conetco.co", "CM", "Carlos M.",
    "Bogotá, Colombia ·", "nexxosstudio.com", "contacto@cbdesign.com.co", "WhatsApp +57 316 495 6994",
    "Calle 6 # 9-45, Cali, Colombia", "CBdesign", "ES", "EN",
}
