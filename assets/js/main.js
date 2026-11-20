/* Instituto Correr: interações e medição de conversões */
(function () {
  'use strict';

  var IS_PROD = /(^|\.)institutocorrerblumenau\.com$/i.test(location.hostname);

  /* Captura e persiste a origem do acesso (Google Ads, Meta, orgânico) na sessão
     para identificar no WhatsApp de onde veio o paciente mesmo que ele navegue
     entre páginas antes de clicar para conversar. */
  var ATTR_KEY = 'ic_lead_attr';
  function captureAttribution() {
    try {
      var sp = new URLSearchParams(location.search);
      var hasClickId = sp.get('gclid') || sp.get('gbraid') || sp.get('wbraid') || sp.get('fbclid');
      var utmSrc = sp.get('utm_source') || '';
      var existing = sessionStorage.getItem(ATTR_KEY);
      if (hasClickId || utmSrc) {
        var data = {
          source: (sp.get('gclid') || sp.get('gbraid') || sp.get('wbraid')) ? 'google_ads'
            : sp.get('fbclid') ? 'meta_ads'
            : utmSrc.toLowerCase(),
          campaign: sp.get('utm_campaign') || '',
          term: sp.get('utm_term') || '',
          landing: location.pathname
        };
        sessionStorage.setItem(ATTR_KEY, JSON.stringify(data));
        return data;
      }
      if (existing) return JSON.parse(existing);
      if (document.referrer) {
        var ref = document.referrer.toLowerCase();
        var rSrc = '';
        if (ref.indexOf('google.') !== -1) rSrc = 'google_organico';
        else if (ref.indexOf('instagram.') !== -1 || ref.indexOf('facebook.') !== -1) rSrc = 'instagram_facebook';
        else if (ref.indexOf('bing.') !== -1) rSrc = 'bing';
        if (rSrc) {
          var rData = { source: rSrc, campaign: '', term: '', landing: location.pathname };
          sessionStorage.setItem(ATTR_KEY, JSON.stringify(rData));
          return rData;
        }
      }
    } catch (err) { /* sessionStorage bloqueado não afeta navegação */ }
    return null;
  }

  var leadAttr = captureAttribution();

  function originLabel() {
    if (!leadAttr || !leadAttr.source) return '';
    var s = leadAttr.source;
    if (s === 'google_ads' || s === 'google' || s === 'cpc' || s === 'adwords') return 'Google';
    if (s === 'google_organico') return 'Pesquisa Google';
    if (s === 'meta_ads' || s === 'instagram' || s === 'facebook' || s === 'ig' || s === 'fb') return 'Instagram/Facebook';
    if (s === 'instagram_facebook') return 'Instagram';
    return '';
  }

  function enrichWaHref(href) {
    try {
      var u = new URL(href);
      if (u.hostname !== 'wa.me') return href;
      var txt = u.searchParams.get('text') || 'Olá! Gostaria de agendar uma avaliação no Instituto Correr.';
      var lbl = originLabel();
      if (lbl && txt.indexOf('(Vim pel') === -1 && txt.indexOf('Origem:') === -1) {
        txt = txt + '\n(Vim pelo ' + lbl + ')';
        u.searchParams.set('text', txt);
        return u.toString();
      }
    } catch (err) { /* mantém href original */ }
    return href;
  }

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

  /* Esconde a barra fixa mobile enquanto o teclado virtual está aberto em campos */
  document.addEventListener('focusin', function (e) {
    if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) {
      document.body.classList.add('kb-open');
    }
  });
  document.addEventListener('focusout', function () {
    setTimeout(function () {
      var act = document.activeElement;
      if (!act || !/^(INPUT|TEXTAREA|SELECT)$/.test(act.tagName)) {
        document.body.classList.remove('kb-open');
      }
    }, 120);
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
      }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });
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

  /* Vídeo: o iframe do YouTube só nasce no clique. */
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
     Empurra eventos no dataLayer (GTM) e, se existirem em produção, chama gtag (GA4/Ads)
     e fbq (Meta Pixel). Ambientes de homologação (.vercel.app / localhost) não disparam
     conversões na conta oficial do Google Ads. */
  function track(name, params) {
    params = params || {};
    params.page_path = location.pathname;
    if (leadAttr && leadAttr.source) params.traffic_origin = leadAttr.source;
    var phone = params.user_phone;
    delete params.user_phone;
    try {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(Object.assign({ event: name }, params));
      if (IS_PROD && typeof window.gtag === 'function') {
        window.gtag('event', name, params);
        var conv = window.__adsConv && window.__adsConv[name];
        if (conv) {
          if (phone) window.gtag('set', 'user_data', { phone_number: phone });
          conv.split('|').forEach(function (id) {
            window.gtag('event', 'conversion', { send_to: id, value: 1.0, currency: 'BRL' });
          });
        }
      }
      if (IS_PROD && typeof window.fbq === 'function') {
        window.fbq('track', name === 'generate_lead' ? 'Lead' : 'Contact', params);
      }
    } catch (err) { /* medição nunca pode quebrar o clique */ }
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    var where = a.dataset.trackLoc ? a.dataset.trackLoc
      : a.closest('.header__mcta') ? 'header_mobile'
      : a.closest('header, .mnav') ? 'header'
      : a.closest('.mbar') ? 'barra_mobile'
      : a.closest('.wa-float') ? 'botao_flutuante'
      : a.closest('.qgrid, .trust-strip') ? 'triagem_queixa'
      : a.closest('footer') ? 'rodape'
      : a.closest('.cta-band') ? 'cta_final'
      : a.closest('.hero, .phero, .thero') ? 'topo' : 'conteudo';
    if (/^https:\/\/wa\.me\//.test(href)) {
      a.setAttribute('href', enrichWaHref(href));
      track('whatsapp_click', { link_location: where });
    } else if (/^tel:/.test(href)) {
      track('phone_click', { link_location: where });
    } else if (/^mailto:/.test(href)) {
      track('email_click', { link_location: where });
    }
  });

  /* Form → WhatsApp (suporta múltiplos formulários rápidos nas páginas de serviço, home e contato) */
  document.querySelectorAll('[data-wa-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var rawPhone = String(f.get('telefone') || '').trim();
      var digits = rawPhone.replace(/\D/g, '');
      if (digits && digits.indexOf('55') !== 0) digits = '55' + digits;
      var servico = String(f.get('servico') || 'Avaliação');
      var periodo = String(f.get('periodo') || '');
      var queixa = String(f.get('mensagem') || '').trim();
      var nome = String(f.get('nome') || '').trim();

      track('generate_lead', {
        form_name: form.dataset.formName || 'agendamento',
        service: servico,
        shift: periodo || 'qualquer',
        user_phone: digits.length >= 12 ? '+' + digits : undefined
      });

      var lines = [
        'Olá, Instituto Correr! Gostaria de agendar uma avaliação.',
        '',
        'Nome: ' + (nome || 'não informado')
      ];
      if (rawPhone) lines.push('WhatsApp: ' + rawPhone);
      lines.push('Interesse: ' + servico);
      if (periodo) lines.push('Melhor período: ' + periodo);
      lines.push('Queixa principal: ' + (queixa || 'quero explicar na conversa'));
      var lbl = originLabel();
      if (lbl) lines.push('(Vim pelo ' + lbl + ')');

      var num = form.dataset.waForm;
      var url = 'https://wa.me/' + num + '?text=' + encodeURIComponent(lines.join('\n'));
      window.open(url, '_blank', 'noopener');
    });
  });

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
