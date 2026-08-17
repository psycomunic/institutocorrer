# Instituto Correr: novo site

Site estático (HTML + CSS + JS puro), sem build, sem dependências. Basta abrir `index.html`
ou subir a pasta inteira em qualquer hospedagem.

---

## ⚠️ Antes de publicar, 4 coisas para conferir

Estes pontos foram montados a partir do que estava no site atual. Confirme antes de ir ao ar:

1. **Número de WhatsApp**: hoje está `554732223565` (o telefone fixo do site atual).
   Se o WhatsApp for outro número, troque em **`build/partials.py` → `WA`** e rode o build,
   ou faça um localizar-e-substituir de `554732223565` em todos os `.html`.
2. **Endereço**: está como `Rua Frederico Busch Júnior, 101, Ed. Oswaldo Cruz`.
   Confirme número e complemento. Ajuste em `build/partials.py` → `STREET`.
3. **E-mail**: coloquei `contato@institutocorrer.com.br` como padrão. Ajuste em `EMAIL`.
4. **Depoimentos**: os 3 depoimentos da home são **exemplos de layout**, não são reais.
   Substitua por avaliações reais (Google Meu Negócio, com autorização do paciente)
   antes de publicar. Estão marcados com comentário `⚠️` dentro de `index.html`.

Além disso: as coordenadas do mapa no schema (`build/schema.py` → `geo`) são aproximadas
do centro de Blumenau. Ajuste para a latitude/longitude exata da clínica.

---

## Estrutura

```
index.html              Home
sobre.html              Sobre nós
metodo.html             Nosso método
equipe.html             Equipe
tratamentos.html        Hub de tratamentos
fisioterapia.html
quiropraxia.html
pilates.html
liberacao-miofascial.html
terapias-manuais.html
contato.html            Contato + formulário → WhatsApp
404.html
sitemap.xml / robots.txt
assets/css/style.css    Design system completo
assets/js/main.js       Interações (menu, acordeão, contadores, formulário)
assets/img/             Logos, fotos da equipe, capa de compartilhamento
build/                  Gerador Python das páginas (opcional)
```

## Como publicar

**Opção A, Vercel / Netlify (recomendado, grátis):**
arraste a pasta para o painel, ou conecte o repositório do GitHub.

O `vercel.json` já resolve o único ponto de atenção: como existe um `package.json`
com script `build`, a Vercel roda `npm run build` e depois procura a saída em `public/`.
Como o gerador escreve na raiz, o arquivo declara `"outputDirectory": "."`.
Sem isso o deploy falha com *No Output Directory named "public" found*.

`cleanUrls` está desligado de propósito: os links internos, o `sitemap.xml` e as tags
`canonical` usam `.html`. Ligar essa opção faria cada link interno passar por um
redirect e brigaria com as canônicas.

**Opção B, hospedagem tradicional:**
suba tudo por FTP para a raiz (`public_html`). Configure o 404 apontando para `404.html`.

**Opção C, substituir o WordPress atual:**
mantenha o domínio e aponte para a nova hospedagem. Se quiser preservar as URLs antigas
(`/sobre-nos/`, `/nosso-metodo/`, etc.), crie redirects 301 para os novos arquivos:

```
/sobre-nos/            → /sobre.html
/nosso-metodo/         → /metodo.html
/fisioterapia/         → /fisioterapia.html
/quiropraxia/          → /quiropraxia.html
/pilates/              → /pilates.html
/liberacao-miofascial/ → /liberacao-miofascial.html
```

## Como editar

**Textos e seções:** edite o `.html` diretamente. É HTML limpo, sem framework.

**Dados que se repetem** (telefone, endereço, horário, lista de tratamentos, equipe):
edite `build/partials.py` e `build/build.py` e rode:

```bash
cd build && python3 build.py
```

Isso regenera todas as 12 páginas de uma vez, com o rodapé, menu e schema atualizados.

**Cores e tipografia:** tudo em variáveis no topo de `assets/css/style.css` (`:root`).
A paleta é verde profundo sobre off-white: verde `#4C6438`, seções escuras em `#232F1B`
e fundo `#EFF1EA`.

## O que foi feito de SEO

- Title e meta description únicos por página, com "Blumenau" nos termos principais
- Schema.org `MedicalClinic` + `Physiotherapy` + `LocalBusiness` com endereço, horários,
  geolocalização, área atendida (Blumenau, Gaspar, Indaial, Timbó, Pomerode) e equipe
- Schema `MedicalTherapy` em cada página de tratamento
- `FAQPage` na home, no método e em cada tratamento (elegível para rich snippet no Google)
- `BreadcrumbList` em todas as páginas internas
- Open Graph + Twitter Card com imagem de capa própria (`assets/img/og-cover.jpg`)
- `sitemap.xml`, `robots.txt`, canonical em todas as páginas
- HTML semântico, um `<h1>` por página, `alt` em todas as imagens, skip link,
  foco visível, suporte a `prefers-reduced-motion`

## Conversão

- Botão flutuante de WhatsApp em todas as páginas
- CTA fixo no cabeçalho (desktop e menu mobile)
- Faixa de CTA antes do rodapé em todas as páginas
- Formulário de contato que **monta a mensagem e abre o WhatsApp já preenchido**,
  sem servidor, sem backend, sem e-mail para configurar
- Links de WhatsApp das páginas de tratamento já vêm com o tratamento na mensagem

---

Feito por Angelo · Vettor 28
