# Historial de licencias

Este documento permite determinar qué licencia corresponde a una revisión del
repositorio sin reescribir el historial.

## Línea temporal

| Periodo | Evidencia | Régimen |
| --- | --- | --- |
| Desde el commit inicial `b24578d03c4014148bf3e76948379383f0ffaae6` del 2026-10-04 hasta la revisión inmediatamente anterior al cambio de 2026-10-05 | `LICENSE` presente en cada revisión | MIT para el material publicado en esas revisiones |
| Desde la revisión del 2026-10-05 que incorpora la política dual y en versiones posteriores | `LICENSE`, `LICENSE-CONTENT.md`, `NOTICE` e inventarios asociados | Apache-2.0 para software propio; CC BY-NC-SA 4.0 para contenido, datos y activos educativos propios; terceros bajo sus términos |

## No retroactividad

El cambio no revoca los permisos otorgados sobre revisiones recibidas bajo MIT. Una
persona puede seguir usando esa revisión conforme a su licencia. Tampoco puede
aplicar retrospectivamente Apache-2.0 o CC BY-NC-SA 4.0 a una copia histórica que
nunca se publicó bajo esas condiciones.

## Cómo comprobar una revisión

1. Resuelve el commit o tag exacto que recibiste.
2. Lee el archivo `LICENSE` contenido en esa revisión, no el de la rama actual.
3. Si existen `LICENSE-CONTENT.md` y `NOTICE`, usa su matriz para clasificar el
   archivo concreto.
4. Comprueba avisos locales y los inventarios de terceros, activos y datos.
5. Conserva la revisión y los avisos usados como evidencia de tu decisión.

Ejemplo:

```bash
git show <revision>:LICENSE
git show <revision>:LICENSE-CONTENT.md
git show <revision>:NOTICE
```

Si el segundo o tercer archivo no existe, esa ausencia forma parte de la evidencia
histórica y no debe suplirse con documentos de una revisión posterior.

## Alcance de la evidencia

El historial Git visible demuestra los archivos publicados y una identidad humana
de autor de commits, Vladimir Acuña. No demuestra acuerdos privados, cesiones,
borradores externos o material nunca incorporado. Ante una disputa sobre
titularidad o explotación comercial, se requiere revisión jurídica de la evidencia
completa.

