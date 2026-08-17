# Instituto Correr: contexto do projeto

> Arquivo de contexto para agentes de IA (Antigravity, Claude Code, Cursor, Copilot).
> Leia isto antes de qualquer alteração.

## O que é

Site institucional do **Instituto Correr**, clínica de fisioterapia, quiropraxia, pilates,
liberação miofascial e terapias manuais em **Blumenau/SC**.
Substitui o site WordPress antigo (`institutocorrer.com.br`).

**Objetivos de negócio, em ordem:**

1. Conversão: agendamento pelo WhatsApp
2. SEO local: ranquear para "fisioterapia Blumenau", "quiropraxia Blumenau", "pilates Blumenau"
3. Autoridade: método, equipe, CREFITO, base científica

## Stack

**HTML + CSS + JavaScript puro. Sem framework, sem bundler, sem dependência de runtime.**

Isso é uma decisão deliberada, não uma limitação. Não introduza React, Tailwind, Vite,
Sass ou qualquer build step sem que o usuário peça explicitamente.

- CSS: um arquivo, `assets/css/style.css`, com design tokens em `:root`
- JS: um arquivo, `assets/js/main.js`, vanilla, sem dependências
- Fontes: Google Fonts (Outfit + Inter) via `<link>`
- Imagens: WebP, com `width`/`height` declarados e `loading="lazy"` fora do hero

## ⚠️ As páginas são GERADAS. Não edite os `.html` às cegas

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
npm run build      # equivale a: cd build && python3 build.py || python build.py
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
│   ├── css/style.css             Design system completo (~640 linhas)
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
STREET        = "Rua Frederico Busch Júnior, 101, Ed. Oswaldo Cruz"
HOURS         = "Seg. a sex., das 7h às 12h e das 13h às 20h"
TREATMENTS    = [...]              # 5 tratamentos: slug, nome, ícone, resumo, bullets
```

Mudou o telefone? Muda ali e roda `npm run build`. Atualiza nas 12 páginas de uma vez,
incluindo os links `wa.me`, o schema e o rodapé.

### O domínio das URLs absolutas

`og:image`, `og:url`, `canonical` e o `sitemap.xml` precisam de URL absoluta, e essa
URL tem que existir de verdade. `SITE` resolve nesta ordem:

1. variável de ambiente `SITE_URL`, se definida
2. `VERCEL_PROJECT_PRODUCTION_URL`, que a Vercel injeta no build
3. `SITE_FINAL`, o `institutocorrer.com.br`

Isso existe porque, enquanto o domínio próprio ainda serve o WordPress antigo, apontar
o `og:image` para lá devolve 404 e o preview de compartilhamento sai sem banner.
Quando o domínio for adicionado ao projeto na Vercel, o passo 2 já retorna ele e nada
precisa ser alterado.

**Consequência:** o HTML commitado usa o domínio final, mas o HTML publicado usa o
domínio de produção da Vercel. Quem manda é o build que roda no deploy.

Equipe fica em `build/build.py` → lista `TEAM`.
Conteúdo das páginas de tratamento fica em `build/build.py` → dict `TDATA`.

## Design tokens

Em `assets/css/style.css`, bloco `:root`. Paleta verde profundo sobre off-white:

- `--forest-800: #232F1B` para seções escuras, `--forest-900: #1B2415` para o rodapé
- `--forest-500: #4C6438` é a cor de ação (CTA, ícones, eyebrows, foco)
- `--paper: #EFF1EA` é o fundo padrão da página; `--white` e `--sand-100: #F4EDDD`
  alternam entre seções (`.section--soft`, `.section--sand`, `.section--mute`)
- `--ink: #1F2A18` para títulos, `--ink-mid` para corpo, `--ink-dim` para apoio
- Display: `Outfit` (geométrica, peso 500) · Corpo/UI: `Inter`

Não invente cores novas fora dos tokens. Se precisar de um tom novo, adicione ao `:root`.

### Formas

A linguagem visual é de cantos generosos e arcos:

- `--r-arch` é o arco usado em foto de hero e nos cards de equipe. A curva do topo é
  rasa (26%) de propósito: as fotos disponíveis têm pouco espaço acima da cabeça e
  uma cúpula alta corta o rosto.
- `.svc` é o card branco de serviço usado sobre a faixa verde, com ícone circular.
- `.statpill` é a pílula de número do hero; `.rulelist` é a lista com filete.
- Botões são sempre pílula (`--r-full`).

### Copy

**Não use travessão (—) em texto visível.** Prefira vírgula, dois-pontos ou frase nova.
A regra vale para `build/`, `assets/js/main.js` e qualquer texto novo.

## Convenções

- Idioma: **português do Brasil**, incluindo nomes de classe quando fizer sentido
- Copy: direta, sem jargão de marketing, sem promessa de cura. É saúde, então não prometa resultado
- Classes CSS: BEM frouxo (`.card`, `.card__img`, `.card--dark`), utilitários curtos (`.mt-6`, `.center`)
- Animação de entrada: adicione `class="reveal"` e opcionalmente `data-d="1..4"` para delay
- Contador animado: `<span data-count="10">0</span>`
- Todo link externo: `target="_blank" rel="noopener"`
- Um `<h1>` por página. Sempre `alt` em imagem

## Regras que não podem quebrar

1. **Não fabricar depoimento, número ou credencial.** Os 3 depoimentos da home são
   marcados como exemplo com comentário `⚠️` no HTML. Só podem ser trocados por
   avaliações reais.
2. **Não prometer cura ou resultado garantido.** Conteúdo de saúde.
3. **Manter os CTAs de WhatsApp** em toda página, que é o objetivo primário do site.
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
npm run dev      # servidor local em http://localhost:8080 (tools/serve.mjs, só Node)
npm run build    # regenera as 12 páginas a partir de build/ (precisa de Python 3)
npm run check    # valida HTML, JSON-LD, alt de imagens e links internos (só Node)
```

Não há `npm install`: nenhum dos comandos tem dependência externa.
Só `npm run build` precisa de Python 3 no PATH.
