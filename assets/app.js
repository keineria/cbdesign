(function () {
  var grid = document.getElementById('grid');
  var VEL = 420; // píxeles por segundo del recorrido de la captura

  function tarjeta(p) {
    var a = document.createElement('a');
    a.className = 'card';
    a.href = p.url;
    a.target = '_blank';
    a.rel = 'noopener';
    a.dataset.cat = p.cat;
    a.setAttribute('aria-label', p.nombre + ': visitar ' + p.dominio);
    a.innerHTML =
      '<div class="bar"><i></i><i></i><i></i><b>' + p.dominio + '</b></div>' +
      '<div class="shot"><img src="assets/shots/' + p.slug + '.webp" alt="Captura del sitio ' + p.nombre + '" loading="lazy"></div>' +
      '<div class="info"><span class="tag">' + p.etiqueta + '</span><h3>' + p.nombre + '</h3><p>' + p.desc + '</p></div>';
    a.addEventListener('mouseenter', function () { reproducir(a, true); });
    a.addEventListener('mouseleave', function () { reproducir(a, false); });
    a.addEventListener('focus', function () { reproducir(a, true); });
    a.addEventListener('blur', function () { reproducir(a, false); });
    return a;
  }

  // Desplaza la captura hacia abajo dentro del marco, como si se recorriera el sitio.
  function reproducir(card, on) {
    var marco = card.querySelector('.shot');
    var img = marco.querySelector('img');
    if (on) {
      var dist = Math.max(0, img.offsetHeight - marco.offsetHeight);
      card.style.setProperty('--dy', -dist + 'px');
      card.style.setProperty('--dur', Math.max(1.5, dist / VEL) + 's');
    }
    card.classList.toggle('play', on && img.complete);
  }

  function pintar(lista) {
    lista.forEach(function (p) { grid.appendChild(tarjeta(p)); });

    // En pantallas táctiles no hay hover: se recorre la tarjeta que queda al centro.
    if (window.matchMedia('(hover: none)').matches && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { reproducir(e.target, e.isIntersecting); });
      }, { rootMargin: '-35% 0px -35% 0px' });
      grid.querySelectorAll('.card').forEach(function (c) { io.observe(c); });
    }
  }

  fetch('data/sitios.json')
    .then(function (r) { return r.json(); })
    .then(pintar)
    .catch(function () { grid.innerHTML = '<p class="lead">No pudimos cargar los proyectos. Recarga la página.</p>'; });

  document.querySelectorAll('.chip').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.chip').forEach(function (x) {
        x.classList.toggle('on', x === b);
        x.setAttribute('aria-pressed', x === b);
      });
      grid.querySelectorAll('.card').forEach(function (c) {
        c.hidden = b.dataset.f !== 'todos' && c.dataset.cat !== b.dataset.f;
      });
    });
  });

  window.addEventListener('pointermove', function (e) {
    document.documentElement.style.setProperty('--mx', e.clientX + 'px');
    document.documentElement.style.setProperty('--my', e.clientY + 'px');
  }, { passive: true });

  document.getElementById('anio').textContent = new Date().getFullYear();
})();
