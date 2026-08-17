# Começar no Antigravity

## 1. Abrir

**File → Open Folder** → selecione a pasta `instituto-correr`.

Abra a pasta em si, não a pasta pai `INSTITUTO CORRER`, porque o `AGENTS.md`, as tasks e o
`package.json` só são detectados se a raiz do workspace for `instituto-correr`.

## 2. Inicializar o Git

O repositório precisa ser criado por você, no terminal do Antigravity
(**Terminal → New Terminal**):

```bash
git init -b main
git add -A
git commit -m "Site Instituto Correr: versão inicial"
```

## 3. Rodar

Terminal do Antigravity:

```bash
npm run dev      # http://localhost:8080
```

Ou use a paleta de comandos: **Ctrl+Shift+P → Tasks: Run Task → Servidor local (8080)**.

Não existe `npm install`: o projeto não tem dependência nenhuma.
Só precisa de **Python 3** (para o servidor e o gerador) e **Node** (para o verificador).

## 4. Os três comandos do dia a dia

```bash
npm run dev      # servidor local
npm run build    # regenera as 12 páginas a partir de build/
npm run check    # valida links, imagens, alt, JSON-LD, title/description
```

`npm run check` roda sozinho e falha com código de erro se achar problema, dá para
plugar em CI depois.

## 5. Antes de pedir qualquer coisa ao agente

O arquivo **`AGENTS.md`** na raiz é o briefing do projeto: stack, decisões de arquitetura,
onde fica cada coisa, convenções e as regras que não podem ser quebradas.

O Antigravity lê esse arquivo automaticamente. Se você usar outro agente, mande ele ler
o `AGENTS.md` primeiro.

**O ponto mais importante que está lá:** os arquivos `.html` da raiz são *gerados*.
Editar um `.html` direto funciona, mas some no próximo `npm run build`. Alterações
estruturais vão em `build/`.

## 6. Publicar

**Vercel (mais simples):**

```bash
npx vercel --prod
```

Ou conecte o repositório no painel da Vercel. Não há configuração de build,
é site estático puro, `output directory` = raiz.

Detalhes de FTP, redirects 301 das URLs antigas do WordPress e checklist de
pré-publicação estão no **`LEIA-ME.md`**.

---

## Mapa rápido dos arquivos

| Arquivo | Para quê |
|---|---|
| `AGENTS.md` | Briefing para o agente de IA, leia antes de mexer |
| `LEIA-ME.md` | Documentação geral, publicação, pendências |
| `build/partials.py` | Telefone, endereço, WhatsApp, header, footer, ícones |
| `build/build.py` | Conteúdo de cada página, equipe, textos dos tratamentos |
| `build/schema.py` | JSON-LD (SEO estruturado) |
| `assets/css/style.css` | Design system inteiro, tokens no `:root` |
| `assets/js/main.js` | Menu, acordeão, contadores, formulário → WhatsApp |
| `tools/check.mjs` | Verificador do site |
| `.vscode/tasks.json` | Tasks prontas: servidor, rebuild, verificar |
