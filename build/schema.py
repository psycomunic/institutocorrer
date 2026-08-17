# -*- coding: utf-8 -*-
"""JSON-LD structured data."""
import json
from partials import SITE, NAME, PHONE_TEL, EMAIL, STREET, CITY, STATE, CEP, TREATMENTS

def _tag(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
            + '</script>')

ORG = {
    "@context": "https://schema.org",
    "@type": ["MedicalClinic", "Physiotherapy", "LocalBusiness"],
    "@id": SITE + "/#clinica",
    "name": NAME,
    "alternateName": "Instituto Correr — Fisioterapia e Quiropraxia Blumenau",
    "url": SITE + "/",
    "logo": SITE + "/assets/img/logo.webp",
    "image": SITE + "/assets/img/og-cover.jpg",
    "description": "Clínica de fisioterapia, quiropraxia, pilates, liberação miofascial e terapias manuais em Blumenau/SC. Avaliação detalhada e tratamento individualizado para prevenção, reabilitação e performance.",
    "telephone": PHONE_TEL,
    "email": EMAIL,
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
    "geo": {"@type": "GeoCoordinates", "latitude": -26.9194, "longitude": -49.0661},
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
    "sameAs": [
        "https://www.instagram.com/institutocorrer/",
        "https://www.facebook.com/institutocorrer",
    ],
    "medicalSpecialty": "PhysicalTherapy",
    "availableService": [
        {"@type": "MedicalTherapy", "name": t["nome"], "url": SITE + "/" + t["slug"] + ".html"}
        for t in TREATMENTS
    ],
    "employee": [{
        "@type": "Person", "name": "Roger Levi Andrade",
        "jobTitle": "Fisioterapeuta e Responsável Técnico",
        "identifier": "CREFITO 175512",
    }, {
        "@type": "Person", "name": "Carla Morgana Pintarelli",
        "jobTitle": "Fisioterapeuta",
    }],
}

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
    """items = [(name, url_or_None), ...] — url relativo ou None p/ atual"""
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


def service(t):
    return {
        "@context": "https://schema.org",
        "@type": "MedicalTherapy",
        "name": t["nome"],
        "url": SITE + "/" + t["slug"] + ".html",
        "description": t["curto"],
        "provider": {"@id": SITE + "/#clinica"},
        "areaServed": {"@type": "City", "name": "Blumenau"},
    }


def tags(*objs):
    return "\n".join(_tag(o) for o in objs)
