/* CBdesign · sitio principal. Sin dependencias. */
(() => {
  'use strict';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const calma = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const WA = 'https://wa.me/573164956994?text=';

  /* Transición compartida: usa View Transitions si el navegador la soporta */
  const transicion = (fn) => {
    if (!document.startViewTransition || calma) { fn(); return Promise.resolve(); }
    return document.startViewTransition(fn).finished.catch(() => {});
  };

  /* ---------- Año ---------- */
  const anio = $('#anio');
  if (anio) anio.textContent = new Date().getFullYear();

  /* ---------- Menú móvil ---------- */
  const toggle = $('#nav-toggle'), menu = $('#menu');
  const cerrarMenu = () => { menu.classList.remove('abierto'); toggle.setAttribute('aria-expanded', 'false'); toggle.setAttribute('aria-label', 'Abrir menú'); };
  toggle.addEventListener('click', () => {
    const abre = !menu.classList.contains('abierto');
    menu.classList.toggle('abierto', abre);
    toggle.setAttribute('aria-expanded', String(abre));
    toggle.setAttribute('aria-label', abre ? 'Cerrar menú' : 'Abrir menú');
  });
  menu.addEventListener('click', (e) => { if (e.target.closest('a')) cerrarMenu(); });

  /* ---------- Aparición al entrar en pantalla ---------- */
  const io = new IntersectionObserver((ents) => {
    ents.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.classList.add('visto');
      io.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  $$('.reveal').forEach((el) => {
    /* escalonar hermanos que aparecen juntos */
    const hermanos = [...el.parentElement.children].filter((h) => h.classList.contains('reveal'));
    el.style.setProperty('--d', Math.min(hermanos.indexOf(el), 5));
    io.observe(el);
  });
  const chat = $('#chat');
  if (chat) io.observe(chat);

  /* ---------- Contadores ---------- */
  const ioCuenta = new IntersectionObserver((ents) => {
    ents.forEach((e) => {
      if (!e.isIntersecting) return;
      ioCuenta.unobserve(e.target);
      const el = e.target, fin = +el.dataset.cuenta, pre = el.dataset.pre || '', suf = el.dataset.suf || '';
      if (calma) return;
      const t0 = performance.now(), dur = 1600;
      const paso = (t) => {
        const p = Math.min((t - t0) / dur, 1), k = 1 - Math.pow(1 - p, 4);
        el.textContent = pre + Math.round(fin * k) + suf;
        if (p < 1) requestAnimationFrame(paso);
      };
      requestAnimationFrame(paso);
    });
  }, { threshold: 0.6 });
  $$('[data-cuenta]').forEach((el) => ioCuenta.observe(el));

  /* ---------- Animaciones ligadas al scroll ---------- */
  const mock = $('#hero-mock'), escena = $('#escena'), lienzo = $('.lienzo'), barra = $('#escena-progreso');
  const pasos = $$('.paso'), wa = $('.wa'), nav = $('#nav');
  const enlaces = $$('.nav-links a'), secciones = enlaces.map((a) => $(a.getAttribute('href'))).filter(Boolean);
  let pendiente = false;
  const limitar = (v) => Math.max(0, Math.min(1, v));
  const pintar = () => {
    pendiente = false;
    const vh = innerHeight, y = scrollY;
    if (mock && !calma) {
      const r = mock.parentElement.getBoundingClientRect();
      mock.style.setProperty('--p', limitar((vh - r.top) / (vh * 0.95)).toFixed(4));
    }
    if (escena) {
      const centro = vh * 0.55;
      let activo = 0;
      pasos.forEach((p, i) => { if (p.getBoundingClientRect().top < centro) activo = i; });
      if (lienzo.dataset.paso !== String(activo)) {
        lienzo.dataset.paso = activo;
        pasos.forEach((p, i) => p.classList.toggle('activo', i === activo));
      }
      const r = escena.getBoundingClientRect();
      barra.style.transform = `scaleX(${limitar((centro - r.top) / (r.height - vh * 0.3)).toFixed(4)})`;
    }
    wa.classList.toggle('visible', y > vh * 0.6);
    let actual = null;
    secciones.forEach((s) => { if (s.getBoundingClientRect().top < vh * 0.4) actual = s; });
    enlaces.forEach((a) => a.classList.toggle('actual', !!actual && a.getAttribute('href') === '#' + actual.id));
  };
  const pedir = () => { if (!pendiente) { pendiente = true; requestAnimationFrame(pintar); } };
  addEventListener('scroll', pedir, { passive: true });
  addEventListener('resize', pedir);
  pintar();

  /* ---------- Metas: pestañas con transición compartida ---------- */
  const tabs = $$('.metas-tabs [role=tab]');
  const elegirMeta = (tab, foco) => {
    if (tab.classList.contains('activo')) return;
    transicion(() => {
      tabs.forEach((t) => {
        const on = t === tab;
        t.classList.toggle('activo', on);
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        $('#' + t.getAttribute('aria-controls')).hidden = !on;
      });
    });
    if (foco) tab.focus();
    tab.scrollIntoView({ block: 'nearest', inline: 'center', behavior: calma ? 'auto' : 'smooth' });
  };
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => elegirMeta(tab));
    tab.addEventListener('keydown', (e) => {
      const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      elegirMeta(tabs[(i + d + tabs.length) % tabs.length], true);
    });
  });

  /* ---------- Servicios: la tarjeta se expande hasta ser el detalle ---------- */
  const telon = $('#telon');
  let abierta = null, focoPrevio = null;
  const abrir = (svc) => {
    if (abierta) return;
    const celda = svc.parentElement;
    celda.style.height = celda.offsetHeight + 'px';
    focoPrevio = document.activeElement;
    transicion(() => {
      svc.classList.add('abierta');
      telon.hidden = false;
      document.documentElement.style.overflow = 'hidden';
    });
    svc.setAttribute('role', 'dialog');
    svc.setAttribute('aria-modal', 'true');
    svc.setAttribute('aria-label', $('h3', svc).textContent);
    const b = $('.svc-abrir', svc);
    b.dataset.etiqueta = b.getAttribute('aria-label');
    b.setAttribute('aria-label', 'Cerrar');
    b.focus({ preventScroll: true });
    abierta = svc;
  };
  const cerrar = () => {
    if (!abierta) return Promise.resolve();
    const svc = abierta, celda = svc.parentElement;
    abierta = null;
    const fin = transicion(() => {
      svc.classList.remove('abierta');
      svc.scrollTop = 0;
      telon.hidden = true;
      document.documentElement.style.overflow = '';
    }).then(() => { celda.style.height = ''; });
    ['role', 'aria-modal', 'aria-label'].forEach((a) => svc.removeAttribute(a));
    const b = $('.svc-abrir', svc);
    b.setAttribute('aria-label', b.dataset.etiqueta);
    if (focoPrevio && focoPrevio.focus) focoPrevio.focus({ preventScroll: true });
    return fin;
  };
  $$('.svc').forEach((svc) => {
    svc.addEventListener('click', (e) => {
      if (e.target.closest('[data-cerrar]')) { cerrar(); return; }
      if (e.target.closest('.svc-abrir')) { svc === abierta ? cerrar() : abrir(svc); return; }
      if (e.target.closest('a')) return;
      if (svc !== abierta) abrir(svc);
    });
  });
  telon.addEventListener('click', cerrar);
  addEventListener('keydown', (e) => {
    if (!abierta) return;
    if (e.key === 'Escape') { cerrar(); return; }
    if (e.key === 'Tab') { /* mantener el foco dentro del detalle */
      const f = $$('a[href],button', abierta).filter((x) => x.offsetParent !== null);
      const pri = f[0], ult = f[f.length - 1];
      if (e.shiftKey && document.activeElement === pri) { e.preventDefault(); ult.focus(); }
      else if (!e.shiftKey && document.activeElement === ult) { e.preventDefault(); pri.focus(); }
    }
  });
  /* enlaces del pie que apuntan a un servicio: desplazan y abren el detalle */
  $$('a[href^="#servicio-"]').forEach((a) => a.addEventListener('click', () => {
    const svc = $(a.getAttribute('href'));
    if (svc) setTimeout(() => abrir(svc), calma ? 0 : 650);
  }));

  /* ---------- Carrusel de proyectos ---------- */
  const car = $('#carrusel'), prev = $('#car-prev'), next = $('#car-next');
  if (car) {
    const paso = () => (car.firstElementChild.offsetWidth + 22) * (innerWidth > 1000 ? 2 : 1);
    const estado = () => {
      prev.disabled = car.scrollLeft < 8;
      next.disabled = car.scrollLeft > car.scrollWidth - car.clientWidth - 8;
    };
    prev.addEventListener('click', () => car.scrollBy({ left: -paso(), behavior: calma ? 'auto' : 'smooth' }));
    next.addEventListener('click', () => car.scrollBy({ left: paso(), behavior: calma ? 'auto' : 'smooth' }));
    car.addEventListener('scroll', estado, { passive: true });
    estado();
  }

  /* ---------- Buscador de dominios ---------- */
  const form = $('#dom-form'), campo = $('#dom-q'), lista = $('#dom-res'), msg = $('#dom-msg');
  const TLDS = ['com', 'co', 'com.co', 'net', 'org', 'store', 'online', 'app', 'io', 'dev'];
  const ETIQUETA = { available: 'Disponible', likely: 'Posiblemente disponible', taken: 'Ocupado', unknown: 'Sin confirmar', wait: 'Consultando' };
  const CLASE = { available: 'libre', likely: 'libre posible', taken: 'ocupado', unknown: 'duda', wait: 'espera' };
  /* extensiones cuyo registro ofrece RDAP público (para el respaldo desde el navegador) */
  const CON_RDAP = ['com', 'net', 'org', 'store', 'online', 'app', 'dev'];

  const limpiar = (v) => {
    let s = v.trim().toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    s = s.replace(/^[a-z]+:\/\//, '').replace(/^www\./, '').replace(/[/?#].*$/, '').replace(/\s+/g, '').replace(/[^a-z0-9.-]/g, '');
    let tld = '';
    const punto = s.indexOf('.');
    if (punto > -1) {
      const resto = s.slice(punto + 1).replace(/\.+$/, '');
      if (TLDS.includes(resto)) tld = resto;
      s = s.slice(0, punto);
    }
    return { nombre: s.replace(/^-+|-+$/g, ''), tld };
  };
  const valido = (n) => /^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/.test(n) && n.length >= 2;

  const fila = (r, i) => {
    const li = document.createElement('li');
    li.className = CLASE[r.status];
    li.style.setProperty('--i', i);
    li.dataset.dominio = r.domain;
    const punto = r.domain.indexOf('.');
    const d = document.createElement('span'); d.className = 'd';
    d.append(r.domain.slice(0, punto));
    const em = document.createElement('em'); em.textContent = r.domain.slice(punto); d.append(em);
    const e = document.createElement('span'); e.className = 'e'; e.textContent = ETIQUETA[r.status];
    li.append(d, e);
    if (r.status === 'available' || r.status === 'likely' || r.status === 'unknown') {
      const a = document.createElement('a');
      a.className = 'btn btn-sm ' + (r.status === 'available' ? 'btn-brand' : 'btn-link');
      a.target = '_blank'; a.rel = 'noopener';
      a.href = WA + encodeURIComponent(r.status === 'available'
        ? `Hola CBdesign, quiero registrar el dominio ${r.domain}.`
        : `Hola CBdesign, ¿me ayudan a confirmar si el dominio ${r.domain} está disponible? Quiero registrarlo.`);
      a.textContent = r.status === 'available' ? 'Registrar' : r.status === 'likely' ? 'Confirmar' : 'Consultar';
      li.append(a);
    } else {
      const h = document.createElement('span'); h.className = 'hueco'; li.append(h);
    }
    return li;
  };
  const pintarLista = (res) => lista.replaceChildren(...res.map(fila));

  /* Respaldo: consulta RDAP directa desde el navegador si el servidor no responde */
  const rdapDirecto = async (dominio) => {
    if (!CON_RDAP.includes(dominio.slice(dominio.indexOf('.') + 1))) return 'unknown';
    try {
      const r = await fetch('https://rdap.org/domain/' + dominio);
      /* rdap.org redirige al registro oficial; un 404 solo vale si lo responde el registro */
      const delRegistro = r.redirected && !/\/\/rdap\.org\//.test(r.url);
      if (r.status === 404 && delRegistro) return 'available';
      if (r.ok) return 'taken';
    } catch (_) { /* red o CORS */ }
    return 'unknown';
  };

  let turno = 0;
  const buscar = async (texto) => {
    const { nombre, tld } = limpiar(texto);
    msg.className = 'dom-msg';
    if (!valido(nombre)) {
      msg.textContent = 'Escribe un nombre válido: solo letras, números y guiones (mínimo 2 caracteres).';
      msg.classList.add('error');
      lista.replaceChildren();
      campo.focus();
      return;
    }
    const mio = ++turno;
    const orden = tld ? [tld, ...TLDS.filter((t) => t !== tld)] : TLDS;
    let res = orden.map((t) => ({ domain: `${nombre}.${t}`, status: 'wait' }));
    campo.value = tld ? `${nombre}.${tld}` : nombre;
    form.classList.add('cargando');
    msg.textContent = 'Consultando disponibilidad…';
    pintarLista(res);

    let datos = null;
    try {
      const ctl = new AbortController();
      const reloj = setTimeout(() => ctl.abort(), 15000);
      const r = await fetch(`api/dominios.php?q=${encodeURIComponent(nombre)}${tld ? '&tld=' + tld : ''}`, { signal: ctl.signal, headers: { Accept: 'application/json' } });
      clearTimeout(reloj);
      if (r.status === 429) {
        if (mio === turno) { msg.textContent = 'Hiciste muchas búsquedas seguidas. Espera un momento e inténtalo de nuevo.'; msg.classList.add('error'); lista.replaceChildren(); form.classList.remove('cargando'); }
        return;
      }
      if (r.ok && (r.headers.get('content-type') || '').includes('json')) datos = await r.json();
    } catch (_) { /* se usa el respaldo */ }
    if (mio !== turno) return;

    if (datos && Array.isArray(datos.results)) {
      res = datos.results;
    } else {
      const estados = await Promise.all(res.map((x) => rdapDirecto(x.domain)));
      if (mio !== turno) return;
      res = res.map((x, i) => ({ domain: x.domain, status: estados[i] }));
    }
    pintarLista(res);
    form.classList.remove('cargando');
    const libres = res.filter((x) => x.status === 'available' || x.status === 'likely').length;
    const dudas = res.filter((x) => x.status === 'unknown').length;
    if (dudas === res.length) { msg.textContent = 'No pudimos consultar los registros en este momento. Escríbenos y lo verificamos por ti.'; msg.classList.add('error'); }
    else if (libres) msg.textContent = libres === 1 ? 'Hay 1 opción disponible para tu marca.' : `Hay ${libres} opciones disponibles para tu marca.`;
    else if (dudas) msg.textContent = 'No encontramos opciones libres confirmadas. Escríbenos y revisamos las que quedaron sin confirmar.';
    else msg.textContent = 'Esas opciones ya están registradas. Prueba con otra variación del nombre.';
  };
  if (form) {
    form.addEventListener('submit', (e) => { e.preventDefault(); buscar(campo.value); });
    /* permite enlazar una búsqueda: /?dominio=mimarca#dominios */
    const inicial = new URLSearchParams(location.search).get('dominio');
    if (inicial) { campo.value = inicial; buscar(inicial); }
  }
})();
