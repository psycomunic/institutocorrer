# -*- coding: utf-8 -*-
"""JSON-LD structured data."""
import json, datetime
BUILD_DATE = datetime.date.today().isoformat()
from partials import (SITE, NAME, PHONE_TEL, EMAIL, STREET, CITY, STATE, CEP, TREATMENTS,
                      WA, GEO, INSTAGRAM, FACEBOOK)

def _tag(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
            + '</script>')

ORG = {
    "@context": "https://schema.org",
    "@type": ["MedicalClinic", "Physiotherapy", "LocalBusiness"],
    "@id": SITE + "/#clinica",
    "name": NAME,
    "alternateName": "Instituto Correr Fisioterapia e Quiropraxia Blumenau",
    "url": SITE + "/",
    "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo.webp", "width": 220, "height": 69},
    "image": [SITE + "/assets/img/og-cover.jpg", SITE + "/assets/img/metodo.webp"],
    "description": "Clínica de fisioterapia, quiropraxia, pilates, liberação miofascial e terapias manuais em Blumenau/SC. Avaliação detalhada e tratamento individualizado para prevenção, reabilitação e performance.",
    "telephone": PHONE_TEL,
    "email": EMAIL,
    "contactPoint": [{
        "@type": "ContactPoint",
        "contactType": "Agendamento",
        "telephone": PHONE_TEL,
        "url": "https://wa.me/" + WA,
        "areaServed": "BR",
        "availableLanguage": "Portuguese",
    }],
    "hasMap": "https://www.google.com/maps/search/?api=1&query=Instituto+Correr+Blumenau",
    "isAcceptingNewPatients": True,
    "paymentAccepted": "Atendimento particular, com recibo para reembolso do plano de saúde",
    "knowsAbout": ["Fisioterapia", "Quiropraxia", "Pilates", "Liberação miofascial",
                   "Terapias manuais", "Acupuntura", "Ventosaterapia", "Reabilitação pós-operatória",
                   "Lesões esportivas", "Dor lombar", "Hérnia de disco", "Dor cervical", "LER/DORT"],
    "founder": {"@id": SITE + "/#roger"},
    "priceRange": "$$",
    "currenciesAccepted": "BRL",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": STREET,
        "addressLocality": CITY,
        "addressRegion": STATE,
        "postalCode": CEP,
        "addressCountry": "BR",
    },
    "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
    "areaServed": [
        {"@type": "City", "name": "Blumenau"},
        {"@type": "City", "name": "Gaspar"},
        {"@type": "City", "name": "Indaial"},
        {"@type": "City", "name": "Timbó"},
        {"@type": "City", "name": "Pomerode"},
    ],
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "07:00", "closes": "12:00",
    }, {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "13:00", "closes": "20:00",
    }],
    "sameAs": [INSTAGRAM, FACEBOOK],
    "medicalSpecialty": ["PhysicalTherapy", "Musculoskeletal"],
    "availableService": [
        {"@type": "MedicalTherapy", "name": t["nome"], "url": SITE + "/" + t["slug"] + ".html"}
        for t in TREATMENTS
    ],
    "employee": [{"@id": SITE + "/#roger"}, {"@id": SITE + "/#carla"}],
}

ROGER = {
    "@type": "Person", "@id": SITE + "/#roger",
    "name": "Roger Levi Andrade",
    "jobTitle": "Fisioterapeuta e Responsável Técnico",
    "description": "Fundador do Instituto Correr. Dez anos de prática clínica em prevenção, reabilitação e performance esportiva, com especialização em acupuntura e técnicas manuais.",
    "image": SITE + "/assets/img/roger.webp",
    "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "Registro profissional",
                      "name": "CREFITO 175512", "recognizedBy": {"@type": "Organization", "name": "CREFITO-10"}},
    "worksFor": {"@id": SITE + "/#clinica"},
    "knowsAbout": ["Fisioterapia", "Acupuntura", "Terapias manuais", "Fisioterapia esportiva"],
}
CARLA = {
    "@type": "Person", "@id": SITE + "/#carla",
    "name": "Carla Morgana Pintarelli",
    "jobTitle": "Fisioterapeuta",
    "description": "Fisioterapeuta formada pela FURB desde 2012. Atua com Método Busquet, treinamento funcional e pilates.",
    "image": SITE + "/assets/img/carla.webp",
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Universidade Regional de Blumenau (FURB)"},
    "worksFor": {"@id": SITE + "/#clinica"},
    "knowsAbout": ["Fisioterapia", "Pilates", "Método Busquet", "Treinamento funcional"],
}
for _p in (ROGER, CARLA):
    _p["@context"] = "https://schema.org"

WEBSITE = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": SITE + "/#site",
    "url": SITE + "/",
    "name": NAME,
    "inLanguage": "pt-BR",
    "publisher": {"@id": SITE + "/#clinica"},
}


def breadcrumb(items):
    """items = [(name, url_or_None), ...] com url relativo ou None p/ atual"""
    els = [{"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"}]
    for i, (name, url) in enumerate(items, start=2):
        el = {"@type": "ListItem", "position": i, "name": name}
        if url:
            el["item"] = SITE + "/" + url
        els.append(el)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": els}


def faq(pairs):
    import re
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{
            "@type": "Question", "name": re.sub(r"<[^>]+>", "", q),
            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)},
        } for q, a in pairs],
    }


def service(t, img=None, desc=None):
    # "Service" aceita provider/areaServed; o tipo clínico vai em "category".
    o = {
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": SITE + "/" + t["slug"] + ".html#servico",
        "name": t["nome"] + " em Blumenau",
        "serviceType": t["nome"],
        "category": "Saúde musculoesquelética",
        "url": SITE + "/" + t["slug"] + ".html",
        "description": desc or t["curto"],
        "provider": {"@id": SITE + "/#clinica"},
        "areaServed": [{"@type": "City", "name": c} for c in ("Blumenau", "Gaspar", "Indaial", "Timbó", "Pomerode")],
        "audience": {"@type": "PeopleAudience", "audienceType": ", ".join(t["bullets"])},
        "availableChannel": {"@type": "ServiceChannel", "serviceUrl": "https://wa.me/" + WA,
                             "servicePhone": {"@type": "ContactPoint", "telephone": PHONE_TEL}},
    }
    if img:
        o["image"] = SITE + "/assets/img/" + img
    return o


def webpage(path, name, desc, kind="WebPage", img=None, about=None):
    """path relativo ("" para a home). Liga a página ao site e à clínica."""
    url = SITE + "/" + path
    o = {
        "@context": "https://schema.org",
        "@type": kind,
        "@id": url + "#pagina",
        "url": url,
        "name": name,
        "description": desc,
        "inLanguage": "pt-BR",
        "isPartOf": {"@id": SITE + "/#site"},
        "about": {"@id": about or (SITE + "/#clinica")},
        "dateModified": BUILD_DATE,
    }
    if img:
        o["primaryImageOfPage"] = {"@type": "ImageObject", "url": SITE + "/assets/img/" + img}
    return o


def tags(*objs):
    return "\n".join(_tag(o) for o in objs)
