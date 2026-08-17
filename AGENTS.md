# Instituto Correr — contexto do projeto

> Arquivo de contexto para agentes de IA (Antigravity, Claude Code, Cursor, Copilot).
> Leia isto antes de qualquer alteração.

## O que é

Site institucional do **Instituto Correr** — clínica de fisioterapia, quiropraxia, pilates,
liberação miofascial e terapias manuais em **Blumenau/SC**.
Substitui o site WordPress antigo (`institutocorrer.com.br`).

**Objetivos de negócio, em ordem:**

1. Conversão — agendamento pelo WhatsApp
2. SEO local — ranquear para "fisioterapia Blumenau", "quiropraxia Blumenau", "pilates Blumenau"
3. Autoridade — método, equipe, CREFITO, base científica

## Stack

**HTML + CSS + JavaScript puro. Sem framework, sem bundler, sem dependência de runtime.**

Isso é uma decisão deliberada, não uma limitação. Não introduza React, Tailwind, Vite,
Sass ou qualquer build step sem que o usuário peça explicitamente.

- CSS: um arquivo, `assets/css/style.css`, com design tokens em `:root`
- JS: um arquivo, `assets/js/main.js`, vanilla, sem dependências
- Fontes: Google Fonts (Fraunces + Inter) via `<link>`
- Imagens: WebP, com `width`/`height` declarados e `loading="lazy"` fora do hero

## ⚠️ As páginas são GERADAS — não edite os `.html` às cegas

Os 12 arquivos `.html` da raiz são **saída** do gerador em `build/`.
Editar um `.html` direto funciona, mas a alteração é **perdida** na próxima vez que
alguém rodar `npm run build`.

**Regra:**

| Tipo de alteração | Onde mexer |
|---|---|
| Header, footer, menu, ícones, CTA final, dados de contato | `build/partials.py` |
| Conteúdo de uma página, seções, textos, FAQ | `build/build.py` |
| Structured data / JSON-LD | `build/schema.py` |
| Estilo, cores, tipografia, espaçamento, responsivo | `assets/css/style.css` |
| Comportamento (menu, acordeão, contador, formulário) | `assets/js/main.js` |

Depois de mexer em qualquer coisa dentro de `build/`, rode:

```bash
npm run build      # equivale a: cd build && python3 build.py
```

Se você **só** vai mexer em CSS/JS/imagens, não precisa rodar o build.

## Estrutura

```
.
├── index.html                    Home
├── sobre.html                    Sobre nós
├── metodo.html                   Nosso método (4 pilares + jornada em 5 etapas)
├── equipe.html                   Equipe
├── tratamentos.html              Hub dos 5 tratamentos
├── fisioterapia.html             ┐
├── quiropraxia.html              │
├── pilates.html                  ├ páginas de tratamento (mesmo template)
├── liberacao-miofascial.html     │
├── terapias-manuais.html         ┘
├── contato.html                  Formulário → WhatsApp + mapa
├── 404.html
├── sitemap.xml  robots.txt
├── assets/
│   ├── css/style.css             Design system completo (~700 linhas)
│   ├── js/main.js                Interações
│   └── img/                      Logos, fotos da equipe, hero, og-cover, favicon
└── build/
    ├── partials.py               Dados do negócio, ícones SVG, head/header/footer
    ├── schema.py                 JSON-LD (MedicalClinic, MedicalTherapy, FAQ, Breadcrumb)
    └── build.py                  Conteúdo de cada página + orquestração
```

## Onde ficam os dados do negócio

Tudo em `build/partials.py`, no topo do arquivo:

```python
PHONE_DISPLAY = "(47) 3222-3565"
WA            = "554732223565"     # número do link wa.me
EMAIL         = "contato@institutocorrer.com.br"
STREET        = "Rua Frederico Busch Júnior, 101 — Ed. Oswaldo Cruz"
HOURS         = "Seg. a Sex., 7h–12h e 13h–20h"
TREATMENTS    = [...]              # 5 tratamentos: slug, nome, ícone, resumo, bullets
```

Mudou o telefone? Muda ali e roda `npm run build`. Atualiza nas 12 páginas de uma vez,
incluindo os links `wa.me`, o schema e o rodapé.

Equipe fica em `build/build.py` → lista `TEAM`.
Conteúdo das páginas de tratamento fica em `build/build.py` → dict `TDATA`.

## Design tokens

Em `assets/css/style.css`, bloco `:root`. Paleta extraída do próprio logo:

- `--navy-800: #1C1F2B` — texto e seções escuras
- `--gold-500: #E5B31D` — cor de ação (CTA, destaques, eyebrows)
- `--bg-soft: #F8F9FB` / `--bg-mute: #F1F3F7` — alternância entre seções
- Display: `Fraunces` (serifada) · Corpo/UI: `Inter`

Não invente cores novas fora dos tokens. Se precisar de um tom novo, adicione ao `:root`.

## Convenções

- Idioma: **português do Brasil**, incluindo nomes de classe quando fizer sentido
- Copy: direta, sem jargão de marketing, sem promessa de cura. É saúde — não prometa resultado
- Classes CSS: BEM frouxo (`.card`, `.card__img`, `.card--dark`), utilitários curtos (`.mt-6`, `.center`)
- Animação de entrada: adicione `class="reveal"` e opcionalmente `data-d="1..4"` para delay
- Contador animado: `<span data-count="10">0</span>`
- Todo link externo: `target="_blank" rel="noopener"`
- Um `<h1>` por página. Sempre `alt` em imagem

## Regras que não podem quebrar

1. **Não fabricar depoimento, número ou credencial.** Os 3 depoimentos da home são
   marcados como exemplo com comentário `⚠️` no HTML — só podem ser trocados por
   avaliações reais.
2. **Não prometer cura ou resultado garantido.** Conteúdo de saúde.
3. **Manter os CTAs de WhatsApp** em toda página — é o objetivo primário do site.
4. **Manter o JSON-LD válido** ao mexer em conteúdo de página. Valide em
   https://validator.schema.org/ depois de mudanças estruturais.
5. **Não adicionar backend.** O formulário monta a mensagem e abre o WhatsApp
   (`data-wa-form` em `main.js`). Não há servidor e nenhum dado é armazenado.

## Pendências conhecidas

- [ ] Confirmar o número de WhatsApp (hoje usa o telefone fixo)
- [ ] Confirmar endereço completo (número e complemento vieram truncados do site antigo)
- [ ] Confirmar e-mail de contato
- [ ] Trocar os 3 depoimentos de exemplo por avaliações reais
- [ ] Ajustar `geo` (lat/long) em `build/schema.py` para as coordenadas exatas da clínica
- [ ] Fotos próprias da clínica e do estúdio de pilates (hoje o hero é uma imagem genérica)
- [ ] Considerar redirects 301 das URLs antigas do WordPress (ver `LEIA-ME.md`)

## Comandos

```bash
npm run dev      # servidor local em http://localhost:8080 (só precisa de Python)
npm run build    # regenera as 12 páginas a partir de build/
npm run check    # valida HTML, JSON-LD, alt de imagens e links internos
```

`npm run dev` e `npm run check` usam apenas Python 3 e Node — não há `npm install`.
