# Sitio principal de CBdesign

Rediseño de [cbdesign.com.co](https://cbdesign.com.co). Sitio estático (HTML, CSS y JavaScript sin dependencias ni compilación) con un único servicio en PHP para el buscador de dominios.

## Estructura

- `index.html`: la página, con metadatos SEO y datos estructurados (Organization, WebSite, WebPage, FAQPage).
- `assets/sitio.css`, `assets/sitio.js`: estilos y comportamiento.
- `assets/img/`, `assets/fonts/`: imágenes en WebP y la fuente Inter alojada en el propio sitio.
- `api/dominios.php`: buscador de dominios.
- `robots.txt`, `sitemap.xml`, `site.webmanifest`, `.htaccess`, `404.html`.

## Buscador de dominios

`api/dominios.php?q=mimarca` consulta la disponibilidad real en los registros oficiales, sin cuentas ni llaves:

1. **RDAP** para .com, .net, .org, .store, .online, .app y .dev.
2. **WHOIS** (puerto 43) para .co, .com.co y .io, que no ofrecen RDAP. El servidor debe permitir conexiones salientes al puerto 43.
3. **DNS** como último recurso: si el dominio tiene servidores de nombres está ocupado; si no existe, se muestra como "posiblemente disponible".

Requiere PHP 7.4 o superior con cURL. Tiene caché en disco y un límite de 20 consultas por minuto por IP. Si el servicio PHP no responde, la página consulta RDAP directamente desde el navegador (solo extensiones con RDAP).

Para cambiar las extensiones, edita `TLDS` en `api/dominios.php` y en `assets/sitio.js`.

## Publicar

Copia el contenido de esta carpeta (incluido `.htaccess`) a la raíz pública de `cbdesign.com.co`. Al cambiar CSS o JS, sube el número de `?v=` en `index.html`.

Después de publicar: enviar `https://cbdesign.com.co/sitemap.xml` en Google Search Console.

## Ver en local

`php -S localhost:8000` dentro de esta carpeta y abrir `http://localhost:8000`.
