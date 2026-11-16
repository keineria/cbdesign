"""Páginas por ciudad (SEO en las ciudades principales de Colombia).

CBdesign tiene sede en Cali y atiende a las demás ciudades a distancia. Los textos lo dicen
de frente: no se afirma tener oficina ni clientes en una ciudad si no es cierto.
Las genera tools/generar-servicios.py con la misma plantilla de las páginas de servicio.
"""

INCLUYE = [
    ("Páginas web corporativas", "Sitios rápidos y claros, adaptados a celular y listos para aparecer en Google."),
    ("Tiendas virtuales", "Ecommerce con pagos en línea, inventario y envíos a todo el país."),
    ("Software a la medida", "Aplicativos web para inventario, logística, portales de clientes e integraciones."),
    ("Posicionamiento SEO", "Auditoría, SEO técnico y contenido para que te encuentren cuando te buscan."),
    ("Marketing digital", "Campañas en Google Ads y Meta con medición de cada contacto."),
    ("Agentes de IA para WhatsApp", "Atención inmediata a tus clientes, a cualquier hora, conectada con tu catálogo."),
]

PASOS = [
    ("Videollamada", "Conocemos tu negocio, tu cliente y tus metas en una reunión corta."),
    ("Propuesta", "Recibes alcance, precio y cronograma definidos, sin costos ocultos."),
    ("Diseño y desarrollo", "Ves avances cada semana y apruebas cada etapa en línea."),
    ("Lanzamiento", "Publicamos, capacitamos a tu equipo y seguimos con soporte."),
]


def _ciudad(slug, nombre, gentilicio, h1, lead, intro, proyectos, faq_extra):
    return {
        "slug": f"diseno-paginas-web-{slug}",
        "ciudad": nombre,
        "corto": f"Páginas web en {nombre}",
        "title": f"Diseño de páginas web en {nombre} | CBdesign",
        "desc": f"Diseño de páginas web, tiendas virtuales y marketing digital para empresas de {nombre}. Agencia con sede en Cali, más de 120 sitios en 11 años.",
        "eyebrow": f"Diseño y desarrollo web para {nombre}",
        "h1": h1,
        "lead": lead,
        "intro": intro,
        "incluye_h2": f"Qué hacemos para empresas de {nombre}",
        "incluye": INCLUYE,
        "pasos": PASOS,
        "proyectos": proyectos,
        "faqs": [
            (f"¿Trabajan con empresas de {nombre} si están en Cali?",
             f"Sí. Nuestra sede está en Cali y atendemos a empresas de {nombre} a distancia: reuniones por videollamada, avances semanales en línea y soporte por WhatsApp y correo."),
            (f"¿Cuánto cuesta una página web en {nombre}?",
             "Depende del número de secciones, las funcionalidades y el contenido. Después de una videollamada corta te enviamos una propuesta con precio y cronograma definidos."),
            faq_extra,
            ("¿Quién administra el sitio después de la entrega?",
             "Tú, con un panel sencillo y una capacitación para tu equipo. Si prefieres, también nos encargamos del mantenimiento, el hosting y los cambios."),
        ],
        "cierre_p": f"Atendemos a empresas {gentilicio} desde nuestra sede en Cali, por videollamada y WhatsApp.",
        "wa": f"Hola CBdesign, escribo desde {nombre} y quiero cotizar un proyecto.",
    }


CIUDADES = [
    _ciudad(
        "bogota", "Bogotá", "de Bogotá",
        "Diseño de páginas web en Bogotá para destacar en el mercado más competido.",
        "Creamos páginas web, tiendas virtuales y campañas para empresas de Bogotá que necesitan diferenciarse y conseguir clientes en Google.",
        [
            "Bogotá es el mercado más grande del país y también el más competido: para casi cualquier servicio hay decenas de empresas buscando el mismo cliente en Google. Un sitio lento o genérico se pierde entre los resultados.",
            "Por eso construimos cada sitio a la medida, con una estructura pensada para las búsquedas de tu sector, tiempos de carga cortos y un camino claro para que el visitante te escriba o pida una cotización.",
            "Trabajamos a distancia con empresas de Bogotá, con el mismo proceso que usamos con nuestros clientes de Colombia, Estados Unidos y España: reuniones por videollamada, avances cada semana y un solo equipo responsable de principio a fin.",
        ],
        ["nexxosstudio", "evocapitalgroup", "vectrar"],
        ("¿Pueden posicionar mi sitio en Bogotá?",
         "Sí. Trabajamos el SEO técnico del sitio y el SEO local con tu Perfil de Empresa en Google, que es el que te hace aparecer en el mapa de tu ciudad."),
    ),
    _ciudad(
        "medellin", "Medellín", "de Medellín",
        "Diseño de páginas web en Medellín para marcas que quieren crecer.",
        "Desarrollamos páginas web y tiendas virtuales para empresas de Medellín y el Valle de Aburrá, listas para vender en Colombia y en otros países.",
        [
            "Medellín es una ciudad de marcas: moda, confección, emprendimientos y empresas de tecnología que compiten por atención dentro y fuera del país. La página web es donde esa marca se convierte en ventas.",
            "Diseñamos sitios y tiendas virtuales que cuentan bien el producto, cargan rápido en celular y hacen fácil comprar o pedir una cotización. Tenemos experiencia en ecommerce de moda con venta en Colombia, Estados Unidos y España.",
            "Atendemos a empresas de Medellín, Envigado, Itagüí y Sabaneta a distancia, con videollamadas, avances semanales y soporte directo por WhatsApp.",
        ],
        ["fajasmelibelt", "fajasmelibeltusa", "nexxosstudio"],
        ("¿Tienen experiencia con marcas de moda y confección?",
         "Sí. Desarrollamos las tiendas virtuales de Fajas Melibelt para Colombia, Estados Unidos y España, con catálogo, pagos, inventario y envíos."),
    ),
    _ciudad(
        "barranquilla", "Barranquilla", "de Barranquilla",
        "Diseño de páginas web en Barranquilla para empresas que venden más allá de la ciudad.",
        "Creamos páginas web, tiendas virtuales y software para empresas de Barranquilla y la región Caribe que quieren ordenar su operación y llegar a más clientes.",
        [
            "Barranquilla mueve comercio, industria y logística para toda la región Caribe. Muchas empresas de la ciudad venden a otras empresas, y sus clientes revisan el sitio web antes de pedir una cotización.",
            "Construimos sitios corporativos que explican bien lo que haces, catálogos y tiendas virtuales para vender en línea, y herramientas a la medida para inventario, despachos y seguimiento de pedidos.",
            "Trabajamos a distancia con empresas de Barranquilla, Soledad y el Atlántico: reuniones por videollamada, avances cada semana y soporte por WhatsApp.",
        ],
        ["conetco", "vectrar", "evocapitalgroup"],
        ("¿Desarrollan catálogos y tiendas para venta entre empresas?",
         "Sí. Desarrollamos la tienda virtual de Conetco, de fibra óptica, con catálogo técnico, y hacemos portales de clientes y cotizadores a la medida."),
    ),
    _ciudad(
        "cartagena", "Cartagena", "de Cartagena",
        "Diseño de páginas web en Cartagena para que te encuentren antes de llegar.",
        "Desarrollamos páginas web en español e inglés para hoteles, restaurantes, operadores de turismo y empresas de Cartagena.",
        [
            "En Cartagena buena parte de los clientes decide desde otra ciudad o desde otro país. Buscan en Google, comparan en el celular y reservan con quien les da confianza en pocos segundos.",
            "Hacemos sitios rápidos, en español e inglés, con fotos que cargan bien, reservas o contacto directo por WhatsApp y SEO para aparecer en las búsquedas de quienes están planeando su viaje o su evento.",
            "Atendemos a empresas de Cartagena a distancia, con videollamadas, avances semanales y soporte por WhatsApp. También implementamos agentes de IA que responden a tus clientes a cualquier hora y en su idioma.",
        ],
        ["colombiabirdfair", "lasevillana", "dauntoque"],
        ("¿Pueden hacer el sitio en español e inglés?",
         "Sí. Desarrollamos sitios en varios idiomas, con cada versión preparada para aparecer en Google en el país que te interesa."),
    ),
    _ciudad(
        "bucaramanga", "Bucaramanga", "de Bucaramanga",
        "Diseño de páginas web en Bucaramanga para empresas que quieren vender en todo el país.",
        "Creamos páginas web y tiendas virtuales para empresas de Bucaramanga y su área metropolitana que quieren llegar a clientes fuera de Santander.",
        [
            "Bucaramanga tiene un tejido fuerte de pequeñas y medianas empresas: calzado, joyería, confección, salud y educación. Muchas ya venden bien en la región y necesitan un canal para llegar al resto del país.",
            "Construimos tiendas virtuales con pagos en línea y envíos nacionales, y sitios corporativos que transmiten confianza y aparecen en Google cuando alguien busca lo que ofreces.",
            "Trabajamos a distancia con empresas de Bucaramanga, Floridablanca, Girón y Piedecuesta, con reuniones por videollamada, avances cada semana y soporte por WhatsApp.",
        ],
        ["fajasmelibelt", "conetco", "lasevillana"],
        ("¿La tienda virtual sirve para enviar a todo el país?",
         "Sí. Configuramos el cálculo de envíos y las guías con la transportadora que uses, y los pagos en línea con tarjetas y PSE."),
    ),
]
