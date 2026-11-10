# Portafolio CBdesign

Micrositio estático con los sitios web desarrollados por [CBdesign](https://cbdesign.com.co).
Se publica en `portafolio.cbdesign.com.co`.

## Estructura

- `index.html`: la página.
- `assets/estilos.css`, `assets/app.js`: estilos y comportamiento (sin dependencias ni compilación).
- `data/sitios.json`: lista de proyectos. Cada tarjeta sale de aquí.
- `assets/shots/<slug>.webp`: captura de página completa de cada sitio (900 px de ancho).
- `tools/capturar.js`: genera las capturas con Playwright.

## Agregar un proyecto

1. Añade una entrada en `data/sitios.json` (`slug`, `nombre`, `dominio`, `url`, `cat`, `etiqueta`, `desc`).
   `cat` puede ser `tienda`, `corporativo`, `evento` o `producto`.
2. Genera la captura: `node tools/capturar.js <slug>` y conviértela a WebP de 900 px de ancho
   en `assets/shots/<slug>.webp`.

## Publicar

Es un sitio estático: basta con copiar el contenido del repo (sin `tools/`) a la raíz pública del subdominio.

## Ver en local

`python3 -m http.server` y abrir `http://localhost:8000`.
