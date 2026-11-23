# Publicación pública

## Identidad activa

- Nombre: `modern-software-engineering-program`
- Visibilidad: pública
- Rama predeterminada: `main`
- Pages: `https://vladimiracunadev-create.github.io/modern-software-engineering-program/`

## About publicado

> 🧭 Currículo abierto en español para aprender ingeniería de software de los fundamentos a la operación, la arquitectura y la IA con agentes · 612 clases desarrolladas en 51 partes, 47 rutas por rol y 17 casos de estudio de plataformas reales · práctica reproducible, figuras y fuentes verificadas · Python + Pages

Reglas del texto:

- no repite el nombre del repositorio, que GitHub ya muestra encima de la descripción;
- cada cifra aparece una sola vez (aquí, «612 clases desarrolladas»; el resto va en el README y en `STATUS.md`);
- las cifras (clases, partes, rutas por rol y casos de estudio) salen del repositorio y las comprueba
  `tests/test_about.py` contra `catalog.json`, `roles/` y `casos/`; también comprueba el límite de 350
  caracteres de GitHub y que este documento cite el texto exacto;
- no usa «planificadas»: si volviera a haber partes sin publicar diría «y N partes en preparación»
  (`tests/test_about.py` comprueba que coincide con `catalog.json`); hoy no hay ninguna y el estado
  de cada parte vive en `STATUS.md`.

## Topics publicados

`software-engineering`, `software-development`, `computer-science`, `curriculum`,
`learning-path`, `software-architecture`, `system-design`, `requirements-engineering`,
`software-testing`, `secure-coding`, `devops`, `devsecops`, `sre`,
`spec-driven-development`, `ai-assisted-development`, `coding-agents`, `mcp`,
`open-source`, `spanish`, `education`.

## Gates de publicación

- [x] validación local y pruebas verdes;
- [x] historial Git inicial sin secretos ni artefactos generados impropios;
- [x] remoto público verificado por API;
- [x] About releído desde la API en UTF-8;
- [ ] protección de `main`, pendiente de definir la política de colaboración;
- [x] ejecución verde del workflow remoto;
- [x] Pages habilitado únicamente después de validar el sitio generado.

## Evidencia remota

- Repositorio público: <https://github.com/vladimiracunadev-create/modern-software-engineering-program>
- Portal: <https://vladimiracunadev-create.github.io/modern-software-engineering-program/>
- Validación multiplataforma: verde en Python 3.11–3.14, Windows y macOS.
- Pages: artefacto y despliegue en verde.
- Respuesta del portal: HTTP 200 y catálogo de 612 clases en 51 partes (se comprobará tras publicar este cambio; las comprobaciones de 588 clases del 2026-11-17, de 540 del 2026-11-16 y de 480 del 3 de octubre de 2026 quedan como antecedente).
