# -*- coding: utf-8 -*-
"""Instituto Correr: dados e partials compartilhados."""

SITE = "https://institutocorrer.com.br"
NAME = "Instituto Correr"
PHONE_DISPLAY = "(47) 3222-3565"
PHONE_TEL = "+554732223565"
WA = "554732223565"
EMAIL = "contato@institutocorrer.com.br"
STREET = "Rua Frederico Busch Júnior, 101, Ed. Oswaldo Cruz"
CITY = "Blumenau"
STATE = "SC"
CEP = "89020-400"
ADDRESS_FULL = STREET + ", " + CITY + "/" + STATE + ", CEP " + CEP
HOURS = "Seg. a sex., das 7h às 12h e das 13h às 20h"

def wa_link(msg="Olá! Gostaria de agendar uma avaliação no Instituto Correr."):
    from urllib.parse import quote
    return "https://wa.me/" + WA + "?text=" + quote(msg)

# --------------------------------------------------------------------------
# ÍCONES (Lucide-style, stroke)
# --------------------------------------------------------------------------
def _svg(paths, fill=False):
    if fill:
        return ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">' + paths + '</svg>')
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + paths + '</svg>')

IC = {
"activity": _svg('<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>'),
"bone": _svg('<path d="M17 10c.7-.7 1.69 0 2.5 0a2.5 2.5 0 1 0 0-5 .5.5 0 0 1-.5-.5 2.5 2.5 0 1 0-5 0c0 .81.7 1.8 0 2.5l-7 7c-.7.7-1.69 0-2.5 0a2.5 2.5 0 0 0 0 5c.28 0 .5.22.5.5a2.5 2.5 0 1 0 5 0c0-.81-.7-1.8 0-2.5Z"/>'),
"heart": _svg('<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>'),
"hand": _svg('<path d="M18 11V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2"/><path d="M14 10V4a2 2 0 0 0-2-2a2 2 0 0 0-2 2v2"/><path d="M10 10.5V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/>'),
"sparkles": _svg('<path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"/><path d="M5 3v4"/><path d="M19 17v4"/><path d="M3 5h4"/><path d="M17 19h4"/>'),
"stethoscope": _svg('<path d="M11 2v2"/><path d="M5 2v2"/><path d="M5 3H4a2 2 0 0 0-2 2v4a6 6 0 0 0 12 0V5a2 2 0 0 0-2-2h-1"/><path d="M8 15a6 6 0 0 0 12 0v-3"/><circle cx="20" cy="10" r="2"/>'),
"target": _svg('<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>'),
"shield": _svg('<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1Z"/><path d="m9 12 2 2 4-4"/>'),
"microscope": _svg('<path d="M6 18h8"/><path d="M3 22h18"/><path d="M14 22a7 7 0 1 0 0-14h-1"/><path d="M9 14h2"/><path d="M9 12a2 2 0 0 1-2-2V6h6v4a2 2 0 0 1-2 2Z"/><path d="M12 6V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3"/>'),
"users": _svg('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>'),
"clock": _svg('<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>'),
"map": _svg('<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>'),
"phone": _svg('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/>'),
"mail": _svg('<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>'),
"check": _svg('<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>'),
"plus": _svg('<path d="M5 12h14"/><path d="M12 5v14"/>'),
"arrow": _svg('<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'),
"chev": _svg('<path d="m6 9 6 6 6-6"/>'),
"chevr": _svg('<path d="m9 18 6-6-6-6"/>'),
"star": _svg('<path d="M11.48 3.5a.56.56 0 0 1 1.04 0l2.13 4.32 4.77.7a.56.56 0 0 1 .31.95l-3.45 3.36.81 4.75a.56.56 0 0 1-.81.59L12 15.92l-4.27 2.25a.56.56 0 0 1-.81-.59l.81-4.75-3.45-3.36a.56.56 0 0 1 .31-.95l4.77-.7Z"/>', fill=True),
"whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.22 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.23 1.36.19 1.87.12.57-.09 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35ZM12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.87 9.87 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 18.13h-.01a8.23 8.23 0 0 1-4.19-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.36c0-4.54 3.7-8.24 8.25-8.24 2.2 0 4.27.86 5.83 2.42a8.19 8.19 0 0 1 2.41 5.83c0 4.54-3.7 8.21-8.24 8.21Z"/></svg>',
"instagram": _svg('<rect width="20" height="20" x="2" y="2" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37Z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/>'),
"facebook": _svg('<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3Z"/>'),
"youtube": _svg('<path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/>'),
"waves": _svg('<path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 1.3 0 1.9-.5 2.5-1"/><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 1.3 0 1.9-.5 2.5-1"/><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 1.3 0 1.9-.5 2.5-1"/>'),
"trending": _svg('<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>'),
"brain": _svg('<path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"/><path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"/>'),
"award": _svg('<path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"/><circle cx="12" cy="8" r="6"/>'),
"calendar": _svg('<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>'),
"file": _svg('<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 13h4"/><path d="M10 17h4"/>'),
"repeat": _svg('<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>'),
"zap": _svg('<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>'),
"play": _svg('<path d="M6.5 4.6a1 1 0 0 1 1.52-.85l10.1 6.4a1 1 0 0 1 0 1.7l-10.1 6.4a1 1 0 0 1-1.52-.85Z"/>', fill=True),
}


# --------------------------------------------------------------------------
# VÍDEO
# --------------------------------------------------------------------------
# O iframe do YouTube só é criado quando a pessoa clica no play. Até lá a
# página mostra um poster local, sem nenhuma requisição a terceiros e sem
# os cookies que o embed padrão instala em quem apenas passa pela página.
VIDEO_METODO = dict(
    id="Ld49dnbaHvk",
    poster="video-metodo.webp",
    poster_w=1280, poster_h=720,
    label="Assistir ao vídeo institucional do Instituto Correr",
)


def video(v=VIDEO_METODO):
    if not v.get("id"):
        return ""
    return ('<div class="video reveal">'
            '<button class="video__btn" type="button" data-video="' + v["id"] + '" '
            'data-title="' + v["label"] + '" aria-label="' + v["label"] + '">'
            '<img src="assets/img/' + v["poster"] + '" alt="" width="' + str(v["poster_w"])
            + '" height="' + str(v["poster_h"]) + '" loading="lazy">'
            '<span class="video__play" aria-hidden="true">' + IC["play"] + '</span>'
            '</button></div>')

# --------------------------------------------------------------------------
# TRATAMENTOS
# --------------------------------------------------------------------------
TREATMENTS = [
    dict(slug="fisioterapia", nome="Fisioterapia", icon="stethoscope",
         tag="Reabilitação e prevenção",
         curto="Avaliação detalhada e conduta individualizada para resolver a causa da dor, não apenas o sintoma.",
         bullets=["Dor lombar, cervical e de ombro", "Lesões esportivas e pós-operatório", "Retorno seguro às atividades"]),
    dict(slug="quiropraxia", nome="Quiropraxia", icon="bone",
         tag="Ajuste articular",
         curto="Ajustes precisos que devolvem mobilidade às articulações e reorganizam a mecânica da coluna.",
         bullets=["Dores de coluna e cervicalgia", "Cefaleias de origem cervical", "Hérnia de disco e ciática"]),
    dict(slug="pilates", nome="Pilates", icon="activity",
         tag="Estúdio completo",
         curto="Estúdio com aparelhos e acessórios, com séries desenhadas a partir da sua avaliação de movimento.",
         bullets=["Controle postural e core", "Condicionamento físico e mental", "Prevenção e manutenção"]),
    dict(slug="liberacao-miofascial", nome="Liberação Miofascial", icon="waves",
         tag="Pontos-gatilho",
         curto="Técnica que desativa pontos-gatilho e libera a fáscia muscular, reduzindo tensão e dor.",
         bullets=["Tensão muscular crônica", "Pontos-gatilho e nódulos", "Ganho imediato de amplitude"]),
    dict(slug="terapias-manuais", nome="Terapias Manuais", icon="hand",
         tag="Toque terapêutico",
         curto="Mobilizações, manipulações e técnicas de tecidos moles aplicadas com raciocínio clínico.",
         bullets=["Mobilização articular", "Técnicas de tecidos moles", "Acupuntura e ventosaterapia"]),
]
TMAP = {t["slug"]: t for t in TREATMENTS}

NAV = [
    ("index.html", "Início"),
    ("sobre.html", "Sobre nós"),
    ("metodo.html", "Nosso método"),
    ("equipe.html", "Equipe"),
]

# --------------------------------------------------------------------------
# HEAD / HEADER / FOOTER
# --------------------------------------------------------------------------
def head(title, desc, canonical, schema_extra="", og_type="website"):
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@TITLE@@</title>
<meta name="description" content="@@DESC@@">
<link rel="canonical" href="@@CANON@@">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Instituto Correr">
<meta name="theme-color" content="#232F1B">
<meta name="geo.region" content="BR-SC">
<meta name="geo.placename" content="Blumenau">

<meta property="og:type" content="@@OGTYPE@@">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Instituto Correr">
<meta property="og:title" content="@@TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:url" content="@@CANON@@">
<meta property="og:image" content="@@SITE@@/assets/img/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:alt" content="Instituto Correr, Blumenau/SC. Volte a fazer o que quiser, sem se preocupar com a dor.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="@@TITLE@@">
<meta name="twitter:description" content="@@DESC@@">
<meta name="twitter:image" content="@@SITE@@/assets/img/og-cover.jpg">
<meta name="twitter:image:alt" content="Instituto Correr, Blumenau/SC. Volte a fazer o que quiser, sem se preocupar com a dor.">

<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/logo.webp">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300..700&family=Inter:wght@400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
@@SCHEMA@@
</head>
<body>
<a class="skip-link" href="#main">Pular para o conteúdo</a>
""".replace("@@TITLE@@", title).replace("@@DESC@@", desc)\
   .replace("@@CANON@@", canonical).replace("@@SITE@@", SITE)\
   .replace("@@SCHEMA@@", schema_extra).replace("@@OGTYPE@@", og_type)


def header(active="", overlay=False):
    """overlay=True deixa o header transparente sobre o hero de imagem cheia,
    trocando o logo pela versao branca ate a pagina rolar."""
    links = ""
    for href, label in NAV:
        cls = "nav__link is-active" if href == active else "nav__link"
        links += '<a class="' + cls + '" href="' + href + '">' + label + '</a>'

    drop_items = ""
    for t in TREATMENTS:
        drop_items += ('<a href="' + t["slug"] + '.html"><span class="di">' + IC[t["icon"]] + '</span>'
                       '<span><b>' + t["nome"] + '</b><span>' + t["tag"] + '</span></span></a>')

    tr_active = "nav__link is-active" if active in TMAP or active == "tratamentos.html" else "nav__link"

    m_links = ""
    for href, label in NAV:
        m_links += '<a href="' + href + '">' + label + '</a>'
    m_sub = ""
    for t in TREATMENTS:
        m_sub += '<a href="' + t["slug"] + '.html">' + t["nome"] + '</a>'

    return """
<header class="header@@OVER@@">
  <div class="header__inner">
    <a class="brand" href="index.html" aria-label="Instituto Correr, página inicial">
      <img class="brand__dark" src="assets/img/logo.webp" alt="Instituto Correr" width="220" height="69" fetchpriority="high">
      <img class="brand__light" src="assets/img/logo-branca.webp" alt="" aria-hidden="true" width="200" height="75">
    </a>
    <nav class="nav" aria-label="Navegação principal">
      @@LINKS@@
      <div class="has-drop">
        <button class="@@TRACT@@" aria-expanded="false" aria-haspopup="true">Tratamentos @@CHEV@@</button>
        <div class="drop" role="menu">
          @@DROP@@
          <a href="tratamentos.html" style="border-top:1px solid var(--line-soft);margin-top:.35rem;padding-top:.85rem">
            <span class="di">@@ICARROW@@</span><span><b>Ver todos os tratamentos</b><span>Comparativo completo</span></span></a>
        </div>
      </div>
      <a class="nav__link" href="contato.html">Contato</a>
    </nav>
    <a class="btn btn--primary btn--sm header__cta" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Agendar avaliação</a>
    <button class="burger" aria-label="Abrir menu" aria-expanded="false" aria-controls="mnav">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<div class="mnav" id="mnav">
  @@MLINKS@@
  <button data-msub aria-expanded="false">Tratamentos</button>
  <div class="sub">@@MSUB@@<a href="tratamentos.html">Ver todos</a></div>
  <a href="contato.html">Contato</a>
  <a class="btn btn--primary" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Agendar avaliação</a>
</div>
""".replace("@@OVER@@", " header--overlay" if overlay else "")\
   .replace("@@LINKS@@", links).replace("@@DROP@@", drop_items).replace("@@TRACT@@", tr_active)\
   .replace("@@MLINKS@@", m_links).replace("@@MSUB@@", m_sub)\
   .replace("@@CHEV@@", IC["chev"]).replace("@@ICARROW@@", IC["arrow"])\
   .replace("@@ICWA@@", IC["whatsapp"]).replace("@@WA@@", wa_link())


def cta_band(title="Sua próxima consulta pode ser o começo do fim da dor",
             text="Agende uma avaliação completa e descubra, com clareza, o que está acontecendo com o seu corpo e qual é o caminho mais curto para você voltar a se mover sem medo."):
    return """
<section class="section cta-band">
  <div class="container center">
    <span class="eyebrow eyebrow--center reveal">Agende agora</span>
    <h2 class="reveal mt-5" style="max-width:20ch;margin-inline:auto">@@T@@</h2>
    <p class="lead reveal measure mx-auto mt-5" data-d="1">@@X@@</p>
    <div class="btn-row reveal mt-8" data-d="2" style="justify-content:center">
      <a class="btn btn--primary btn--lg" href="@@WA@@" target="_blank" rel="noopener">@@ICWA@@ Falar no WhatsApp</a>
      <a class="btn btn--light btn--lg" href="tel:@@TEL@@">@@ICPH@@ @@PH@@</a>
    </div>
    <p class="reveal mt-6" data-d="3" style="font-size:.87rem;color:rgba(255,255,255,.5)">@@HOURS@@ &nbsp;·&nbsp; @@STREET@@</p>
  </div>
</section>
""".replace("@@T@@", title).replace("@@X@@", text).replace("@@WA@@", wa_link())\
   .replace("@@ICWA@@", IC["whatsapp"]).replace("@@ICPH@@", IC["phone"])\
   .replace("@@TEL@@", PHONE_TEL).replace("@@PH@@", PHONE_DISPLAY)\
   .replace("@@HOURS@@", HOURS).replace("@@STREET@@", STREET)


def footer():
    tr = ""
    for t in TREATMENTS:
        tr += '<li><a href="' + t["slug"] + '.html">' + t["nome"] + '</a></li>'
    return """
<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <img class="flogo" src="assets/img/logo-branca.webp" alt="Instituto Correr" width="180" height="52" loading="lazy">
        <p>Fisioterapia, quiropraxia e pilates em Blumenau. Cuidamos da saúde do seu movimento para você fazer o que quiser, sem se preocupar com a dor.</p>
        <div class="socials">
          <a href="https://www.instagram.com/institutocorrer/" target="_blank" rel="noopener" aria-label="Instagram">@@IG@@</a>
          <a href="https://www.facebook.com/institutocorrer" target="_blank" rel="noopener" aria-label="Facebook">@@FB@@</a>
          <a href="@@WA@@" target="_blank" rel="noopener" aria-label="WhatsApp">@@WAI@@</a>
        </div>
      </div>
      <div>
        <h4>Tratamentos</h4>
        <ul>@@TR@@</ul>
      </div>
      <div>
        <h4>Instituto</h4>
        <ul>
          <li><a href="sobre.html">Sobre nós</a></li>
          <li><a href="metodo.html">Nosso método</a></li>
          <li><a href="equipe.html">Equipe</a></li>
          <li><a href="tratamentos.html">Tratamentos</a></li>
          <li><a href="contato.html">Contato</a></li>
        </ul>
      </div>
      <div>
        <h4>Atendimento</h4>
        <ul>
          <li><a href="tel:@@TEL@@">@@PH@@</a></li>
          <li><a href="mailto:@@EMAIL@@">@@EMAIL@@</a></li>
          <li style="color:rgba(255,255,255,.6)">@@HOURS@@</li>
          <li><a href="https://www.google.com/maps/search/?api=1&amp;query=@@MAPQ@@" target="_blank" rel="noopener">@@STREET@@<br>@@CITY@@/@@STATE@@, CEP @@CEP@@</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> Instituto Correr. Todos os direitos reservados.</span>
      <span>Responsável técnico: Roger Levi Andrade, CREFITO 175512</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="@@WA@@" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">
  @@WAI@@<span>Agendar pelo WhatsApp</span>
</a>

<script src="assets/js/main.js" defer></script>
</body>
</html>
""".replace("@@TR@@", tr).replace("@@IG@@", IC["instagram"]).replace("@@FB@@", IC["facebook"])\
   .replace("@@WAI@@", IC["whatsapp"]).replace("@@WA@@", wa_link())\
   .replace("@@TEL@@", PHONE_TEL).replace("@@PH@@", PHONE_DISPLAY).replace("@@EMAIL@@", EMAIL)\
   .replace("@@HOURS@@", HOURS).replace("@@STREET@@", STREET).replace("@@CITY@@", CITY)\
   .replace("@@STATE@@", STATE).replace("@@CEP@@", CEP)\
   .replace("@@MAPQ@@", "Instituto+Correr+Blumenau")


def phero(crumbs, eyebrow, h1, lead):
    c = '<a href="index.html">Início</a>'
    for label, href in crumbs:
        c += IC["chevr"]
        c += ('<a href="' + href + '">' + label + '</a>') if href else ('<span>' + label + '</span>')
    return """
<section class="phero">
  <div class="container">
    <div class="phero__inner">
      <nav class="crumbs" aria-label="Você está aqui">@@C@@</nav>
      <span class="eyebrow">@@E@@</span>
      <h1>@@H@@</h1>
      <p class="lead measure">@@L@@</p>
    </div>
  </div>
</section>
""".replace("@@C@@", c).replace("@@E@@", eyebrow).replace("@@H@@", h1).replace("@@L@@", lead)


def acc(items, klass=""):
    out = '<div class="acc ' + klass + '">'
    for i, (q, a) in enumerate(items):
        out += ('<div class="acc__item"><button class="acc__btn" aria-expanded="false">'
                '<span>' + q + '</span><span class="acc__ic">' + IC["plus"] + '</span></button>'
                '<div class="acc__panel"><div>' + a + '</div></div></div>')
    return out + '</div>'
