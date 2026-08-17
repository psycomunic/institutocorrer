#!/usr/bin/env node
/**
 * Verificação rápida do site, sem dependências.
 *   node tools/check.mjs
 *
 * Checa: links internos quebrados, imagens faltando, alt ausente,
 * quantidade de <h1>, JSON-LD válido, placeholders esquecidos,
 * title/description por página e tamanho dos assets.
 */
import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const problems = [];
const warnings = [];

const pages = readdirSync(ROOT).filter((f) => f.endsWith('.html')).sort();
if (!pages.length) {
  console.error('Nenhum .html encontrado na raiz. Rode `npm run build` primeiro.');
  process.exit(1);
}

const P = (file, msg) => problems.push(`${file}: ${msg}`);
const W = (file, msg) => warnings.push(`${file}: ${msg}`);

for (const page of pages) {
  const html = readFileSync(join(ROOT, page), 'utf8');

  // placeholders do gerador que não foram substituídos
  const leftovers = [...new Set(html.match(/@@[A-Z0-9_]+@@/g) || [])];
  if (leftovers.length) P(page, `placeholder não substituído: ${leftovers.join(', ')}`);

  // um <h1> por página
  const h1 = (html.match(/<h1[\s>]/g) || []).length;
  if (h1 !== 1) P(page, `esperado exatamente 1 <h1>, encontrado ${h1}`);

  // lang
  if (!html.includes('lang="pt-BR"')) P(page, 'falta lang="pt-BR" no <html>');

  // title e description
  const title = (html.match(/<title>([^<]*)<\/title>/) || [])[1] || '';
  if (!title) P(page, 'sem <title>');
  else if (title.length > 65) W(page, `title com ${title.length} caracteres (ideal ≤ 60)`);

  const desc = (html.match(/<meta name="description" content="([^"]*)"/) || [])[1] || '';
  if (!desc) P(page, 'sem meta description');
  else if (desc.length > 165) W(page, `description com ${desc.length} caracteres (ideal ≤ 158)`);

  // canonical
  if (!/rel="canonical"/.test(html)) P(page, 'sem link canonical');

  // imagens: existência e alt
  for (const m of html.matchAll(/<img\b[^>]*>/g)) {
    const tag = m[0];
    const src = (tag.match(/src="([^"]+)"/) || [])[1];
    if (!src) continue;
    if (!/alt="/.test(tag)) P(page, `<img> sem alt: ${src}`);
    if (!/^https?:/.test(src) && !existsSync(join(ROOT, src))) P(page, `imagem inexistente: ${src}`);
    if (!/width="/.test(tag) || !/height="/.test(tag)) W(page, `<img> sem width/height (CLS): ${src}`);
  }

  // links internos
  for (const m of html.matchAll(/href="([^"]+)"/g)) {
    const href = m[1];
    if (/^(https?:|mailto:|tel:|#|data:)/.test(href)) continue;
    const [path] = href.split('#');
    if (!path) continue;
    if (!existsSync(join(ROOT, path))) P(page, `link quebrado: ${href}`);
  }

  // JSON-LD
  for (const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
    try {
      JSON.parse(m[1]);
    } catch (e) {
      P(page, `JSON-LD inválido: ${e.message.slice(0, 80)}`);
    }
  }

  // links externos sem rel="noopener"
  for (const m of html.matchAll(/<a\b[^>]*target="_blank"[^>]*>/g)) {
    if (!/rel="[^"]*noopener/.test(m[0])) W(page, 'target="_blank" sem rel="noopener"');
  }
}

// arquivos auxiliares
for (const f of ['sitemap.xml', 'robots.txt', 'assets/css/style.css', 'assets/js/main.js']) {
  if (!existsSync(join(ROOT, f))) P('projeto', `arquivo ausente: ${f}`);
}

// peso dos assets
const walk = (dir) =>
  readdirSync(dir).flatMap((f) => {
    const p = join(dir, f);
    return statSync(p).isDirectory() ? walk(p) : [p];
  });
let total = 0;
for (const f of walk(join(ROOT, 'assets'))) {
  const kb = statSync(f).size / 1024;
  total += kb;
  if (kb > 300) W('assets', `${f.replace(ROOT + '/', '')} tem ${kb.toFixed(0)} KB, considere otimizar`);
}

// relatório
const line = '─'.repeat(58);
console.log(`\n${line}\nInstituto Correr: verificação\n${line}`);
console.log(`Páginas analisadas: ${pages.length}`);
console.log(`Peso total de assets: ${(total / 1024).toFixed(2)} MB`);

if (warnings.length) {
  console.log(`\n⚠  Avisos (${warnings.length}):`);
  for (const w of [...new Set(warnings)]) console.log('   ·', w);
}

if (problems.length) {
  console.log(`\n✗  Problemas (${problems.length}):`);
  for (const p of problems) console.log('   ·', p);
  console.log('');
  process.exit(1);
}

console.log('\n✓  Nenhum problema encontrado.\n');
