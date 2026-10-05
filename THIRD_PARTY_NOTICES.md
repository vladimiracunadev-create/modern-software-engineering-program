# Avisos de terceros

Inventario técnico revisado el **2026-10-05**. Este documento identifica software,
servicios y obras externas que intervienen en el repositorio. No sustituye los
avisos que acompañen a una distribución concreta ni concede derechos sobre material
de terceros.

## Dependencias de ejecución

El árbol versionado no contiene `package.json`, lockfiles, `requirements.txt`,
`pyproject.toml`, imágenes de contenedor ni bibliotecas vendorizadas. Los scripts de
generación y validación usan únicamente la biblioteca estándar de Python. Por ello,
el repositorio no redistribuye actualmente un árbol de dependencias de aplicación.

| Componente | Uso comprobado | Licencia o condición |
| --- | --- | --- |
| Python | Ejecuta generadores, validadores y pruebas locales/CI | Python Software Foundation License; no se redistribuye el runtime |
| GitHub Actions | Servicio de automatización para validación, seguridad y Pages | Sujeto a los términos de GitHub; las acciones concretas se detallan abajo |
| GitHub Pages | Aloja el portal estático generado | Sujeto a los términos de GitHub |
| Mermaid | GitHub renderiza diagramas textuales presentes en Markdown | El proyecto Mermaid es MIT; este repositorio no incorpora su runtime |
| Shields.io | Sirve badges remotos enlazados desde el README | Servicio externo; no se redistribuye su código ni sus imágenes |

## Acciones y herramientas de CI

| Componente | Dónde se usa | Licencia / control |
| --- | --- | --- |
| `actions/checkout` | Todos los workflows | MIT; fijada a un commit SHA completo |
| `actions/setup-python` | Validación, seguridad y Pages | MIT; fijada a un commit SHA completo |
| `actions/configure-pages` | Preparación de GitHub Pages | MIT; fijada a un commit SHA completo |
| `actions/upload-pages-artifact` | Empaquetado del sitio | MIT; fijada a un commit SHA completo |
| `actions/deploy-pages` | Publicación del sitio | MIT; fijada a un commit SHA completo |
| Gitleaks 8.18.4 | Escaneo de secretos en el árbol | MIT; versión fijada y checksum oficial verificado durante la descarga |
| Bandit 1.9.4 | Análisis estático de los scripts Python | Apache-2.0; versión fijada para evitar cambios de reglas inesperados |

Los pins por SHA reducen el riesgo de que una etiqueta mutable cambie el código de
una acción. No prueban por sí solos que el proveedor o la cadena de construcción
sean confiables; las actualizaciones deben revisar release notes, procedencia y
licencia antes de cambiar el pin.

## Especificaciones, cuerpos de conocimiento y documentación

El programa cita o enlaza materiales de IEEE, ACM, ISO, IEC, IETF, NIST, OWASP,
CNCF, OpenSSF, SLSA, W3C, WHATWG, Python, Rust, Git, Microsoft, Google y otros
titulares. Las entradas de `sources/` son registros y enlaces: no incorporan el
texto íntegro de esas obras ni cambian sus términos.

Algunas normas requieren compra o acceso bajo condiciones específicas. Este
programa puede explicar conceptos y aplicaciones, pero una referencia no autoriza
copiar la norma ni reemplaza la consulta de la edición oficial vigente.

## Contratos y formatos

`blueprints/reference-product/api/openapi.yaml` es un contrato original escrito con
el formato OpenAPI. Usar una especificación abierta para expresar un contrato no
convierte el contenido en una copia de la especificación. Los JSON Schema propios
se tratan del mismo modo.

## Mantenimiento

Cuando se agregue o actualice un manifest, lockfile, acción, herramienta descargada,
contenedor, fuente tipográfica o biblioteca vendorizada, la misma contribución debe:

1. registrar aquí nombre, versión, fuente y licencia;
2. conservar avisos obligatorios;
3. comprobar compatibilidad con Apache-2.0 y CC BY-NC-SA 4.0 según el material;
4. fijar versiones o digests cuando sea razonable;
5. generar SBOM y avisos de distribución si se publica un artefacto que incorpore
   dependencias.

Fuentes primarias: [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0),
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode),
[Python licensing](https://docs.python.org/3/license.html),
[GitHub Actions](https://github.com/actions),
[Gitleaks](https://github.com/gitleaks/gitleaks) y
[Bandit](https://github.com/PyCQA/bandit).

