/* Instituto Correr: interações */
(function () {
  'use strict';

  /* Header shrink on scroll */
  var header = document.querySelector('.header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 24);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* Mobile nav */
  var burger = document.querySelector('.burger');
  var mnav = document.querySelector('.mnav');
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      var open = mnav.classList.toggle('is-open');
      burger.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.classList.toggle('no-scroll', open);
    });
    mnav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mnav.classList.remove('is-open');
        burger.classList.remove('is-open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('no-scroll');
      });
    });
    /* Mobile submenu toggle */
    mnav.querySelectorAll('[data-msub]').forEach(function (btn) {
      var sub = btn.nextElementSibling;
      if (!sub) return;
      sub.style.display = 'none';
      btn.addEventListener('click', function () {
        var vis = sub.style.display === 'none';
        sub.style.display = vis ? 'block' : 'none';
        btn.setAttribute('aria-expanded', vis ? 'true' : 'false');
      });
    });
  }

  /* Desktop dropdown: keyboard + click support */
  document.querySelectorAll('.has-drop').forEach(function (dd) {
    var btn = dd.querySelector('button');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = dd.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function () {
    document.querySelectorAll('.has-drop.is-open').forEach(function (dd) {
      dd.classList.remove('is-open');
      var b = dd.querySelector('button');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.has-drop.is-open').forEach(function (dd) { dd.classList.remove('is-open'); });
      if (mnav && mnav.classList.contains('is-open')) burger.click();
    }
  });

  /* Accordion */
  document.querySelectorAll('.acc').forEach(function (acc) {
    acc.querySelectorAll('.acc__btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var item = btn.closest('.acc__item');
        var panel = item.querySelector('.acc__panel');
        var open = item.classList.contains('is-open');
        acc.querySelectorAll('.acc__item.is-open').forEach(function (o) {
          o.classList.remove('is-open');
          o.querySelector('.acc__panel').style.maxHeight = null;
          o.querySelector('.acc__btn').setAttribute('aria-expanded', 'false');
        });
        if (!open) {
          item.classList.add('is-open');
          panel.style.maxHeight = panel.scrollHeight + 'px';
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });
  });

  /* Scroll reveal */
  var reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add('is-in'); });
    }
  }

  /* Counters */
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target, end = parseFloat(el.dataset.count), suf = el.dataset.suffix || '';
        var dur = 1400, t0 = performance.now();
        var tick = function (t) {
          var p = Math.min((t - t0) / dur, 1);
          var e = 1 - Math.pow(1 - p, 3);
          el.textContent = (end % 1 ? (end * e).toFixed(1) : Math.round(end * e)) + suf;
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        cio.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* Vídeo: o iframe do YouTube só nasce no clique.
     Antes disso a página não fala com o YouTube nem carrega os cookies dele. */
  document.querySelectorAll('[data-video]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + btn.dataset.video +
              '?autoplay=1&rel=0&modestbranding=1';
      f.title = btn.dataset.title || 'Vídeo';
      f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; web-share';
      f.setAttribute('allowfullscreen', '');
      f.setAttribute('loading', 'lazy');
      btn.replaceWith(f);
      f.focus();
    });
  });

  /* Medição de conversões
     Empurra eventos no dataLayer (GTM) e, se existirem, chama gtag (GA4/Ads)
     e fbq (Meta Pixel). Sem nenhuma tag configurada, não faz nada. */
  function track(name, params) {
    params = params || {};
    params.page_path = location.pathname;
    var phone = params.user_phone;
    delete params.user_phone; // dado pessoal: só vai para o Google Ads (hash automático)
    try {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(Object.assign({ event: name }, params));
      if (typeof window.gtag === 'function') {
        window.gtag('event', name, params);
        var conv = window.__adsConv && window.__adsConv[name];
        if (conv) {
          if (phone) window.gtag('set', 'user_data', { phone_number: phone });
          window.gtag('event', 'conversion', { send_to: conv, value: 1.0, currency: 'BRL' });
        }
      }
      if (typeof window.fbq === 'function') {
        window.fbq('track', name === 'generate_lead' ? 'Lead' : 'Contact', params);
      }
    } catch (err) { /* medição nunca pode quebrar o clique */ }
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    var where = a.closest('header, .mnav') ? 'header'
      : a.closest('.wa-float') ? 'botao_flutuante'
      : a.closest('footer') ? 'rodape'
      : a.closest('.cta-band') ? 'cta_final'
      : a.closest('.hero, .phero') ? 'topo' : 'conteudo';
    if (/^https:\/\/wa\.me\//.test(href)) track('whatsapp_click', { link_location: where });
    else if (/^tel:/.test(href)) track('phone_click', { link_location: where });
    else if (/^mailto:/.test(href)) track('email_click', { link_location: where });
  });

  /* Form → WhatsApp */
  var form = document.querySelector('[data-wa-form]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var digits = String(new FormData(form).get('telefone') || '').replace(/\D/g, '');
      if (digits && digits.indexOf('55') !== 0) digits = '55' + digits;
      track('generate_lead', {
        form_name: 'agendamento',
        service: String(new FormData(form).get('servico') || ''),
        user_phone: digits.length >= 12 ? '+' + digits : undefined
      });
      var f = new FormData(form);
      var msg =
        'Olá, Instituto Correr! Gostaria de agendar uma avaliação.\n\n' +
        'Nome: ' + (f.get('nome') || '') + '\n' +
        'Telefone: ' + (f.get('telefone') || '') + '\n' +
        'Serviço de interesse: ' + (f.get('servico') || '') + '\n' +
        'Queixa principal: ' + (f.get('mensagem') || 'não informado');
      var num = form.dataset.waForm;
      window.open('https://wa.me/' + num + '?text=' + encodeURIComponent(msg), '_blank', 'noopener');
    });
  }

  /* Phone mask (BR) */
  document.querySelectorAll('[data-mask="phone"]').forEach(function (inp) {
    inp.addEventListener('input', function () {
      var v = inp.value.replace(/\D/g, '').slice(0, 11);
      if (v.length > 6) inp.value = '(' + v.slice(0, 2) + ') ' + v.slice(2, v.length - 4) + '-' + v.slice(-4);
      else if (v.length > 2) inp.value = '(' + v.slice(0, 2) + ') ' + v.slice(2);
      else if (v.length) inp.value = '(' + v;
      else inp.value = '';
    });
  });

  /* Current year */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
