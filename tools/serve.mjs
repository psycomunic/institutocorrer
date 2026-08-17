#!/usr/bin/env node
// Servidor estatico de desenvolvimento, sem dependencias.
// Uso: node tools/serve.mjs [porta]

import { createServer } from 'node:http';
import { createReadStream } from 'node:fs';
import { stat } from 'node:fs/promises';
import { extname, join, normalize, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('..', import.meta.url));
const PORT = Number(process.argv[2] || process.env.PORT || 8080);

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.png': 'image/png',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
};

async function resolve(urlPath) {
  // Impede escapar da raiz do projeto (path traversal).
  const rel = normalize(decodeURIComponent(urlPath)).replace(/^([/\\]|\.\.[/\\]?)+/, '');
  let file = join(ROOT, rel);
  if (!file.startsWith(ROOT.endsWith(sep) ? ROOT : ROOT + sep) && file !== ROOT.slice(0, -1)) return null;

  try {
    const info = await stat(file);
    if (info.isDirectory()) file = join(file, 'index.html');
  } catch {
    return null;
  }
  try {
    const info = await stat(file);
    return info.isFile() ? file : null;
  } catch {
    return null;
  }
}

const server = createServer(async (req, res) => {
  const urlPath = new URL(req.url, 'http://localhost').pathname;
  let file = await resolve(urlPath);
  let status = 200;

  if (!file) {
    status = 404;
    file = join(ROOT, '404.html');
    try {
      await stat(file);
    } catch {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end('404 Not Found');
      console.log(`404 ${urlPath}`);
      return;
    }
  }

  res.writeHead(status, {
    'Content-Type': TYPES[extname(file).toLowerCase()] || 'application/octet-stream',
    'Cache-Control': 'no-store',
  });
  createReadStream(file).pipe(res);
  console.log(`${status} ${urlPath}`);
});

server.listen(PORT, () => {
  console.log(`Instituto Correr: servidor local em http://localhost:${PORT}`);
  console.log(`Servindo: ${ROOT}`);
  console.log('Ctrl+C para parar.');
});

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`Porta ${PORT} ja esta em uso. Tente: node tools/serve.mjs 8081`);
    process.exit(1);
  }
  throw err;
});
