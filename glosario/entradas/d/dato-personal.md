# Dato personal

[↑ Glosario](../../README.md) · [← Datagrama](./datagrama.md) · [Dato tardío →](./dato-tardio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Información sobre una persona identificada o que puede identificarse.

Definición de trabajo de [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md): Información sobre una persona identificada o identificable.

## Por qué importa

La clase donde se define, [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), existe con este propósito: la clase existe para que diseñes el ciclo de vida de los datos personales de la plataforma (qué se recoge, cuánto se conserva, cómo se borra y cómo se reduce el riesgo de lo que queda), y para que verifiques con una medida si un dato «borrado» o «anonimizado» realmente dejó de ser recuperable o identificable.

## Cómo funciona

Según [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md):

El equipo de la plataforma mantiene un inventario con cada dato personal, su finalidad, su plazo y las copias donde vive: el correo (acceso, mientras la cuenta esté activa y 12 meses después), las entregas (finalidad académica, 5 años por la normativa de la institución), los eventos de acceso (seguridad, 12 meses) y las exportaciones (solo bajo petición y 30 días). Un trabajo mensual purga lo vencido y publica cuántas filas borró y cuántas quedan fuera de plazo; si el número no es cero, avisa.

Según [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md):

No: sin clave, se invierte con una lista de candidatos y sigue siendo un identificador estable que permite enlazar registros. Con una clave guardada aparte reduce el riesgo, pero sigue siendo un seudónimo, es decir, un dato personal.

## Ejemplo

Ejemplo de [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma mantiene un inventario con cada dato personal, su finalidad, su plazo y las copias donde vive: el correo (acceso, mientras la cuenta esté activa y 12 meses después), las entregas (finalidad académica, 5 años por la normativa de la institución), los eventos de acceso (seguridad, 12 meses) y las exportaciones (solo bajo petición y 30 días). Un trabajo mensual purga lo vencido y publica cuántas filas borró y cuántas quedan fuera de plazo; si el número no es cero, avisa.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md)) son:

- **El dato borrado aparece en el archivo o en un respaldo** — causa: borrado lógico y copias no tratadas. Corrección: `secure_delete`, `VACUUM` si procede y plazo de expiración de las copias.
- **La tabla de eventos crece sin parar** — causa: retención sin purga programada. Corrección: trabajo de purga con medida de lo vencido.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia ni con definiciones legales en sinónimos y deben contrastarse con la normativa y con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El análisis de retención es aritmético y su plazo es un supuesto; el de unicidad usa atributos uniformes e independientes; el del borrado es de SQLite y de una cadena fija; y el del diccionario usa correos predecibles.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sobre](../s/sobre.md), [Cuasi-identificador](../c/cuasi-identificador.md), [HMAC](../h/hmac.md), [K-anonimato](../k/k-anonimato.md), [Minimización](../m/minimizacion.md), [Retención](../r/retencion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (24 clases más lo mencionan; las que más):

[SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — principios de minimización, limitación del plazo y supresión; autoridad: texto oficial de la Unión Europea.
- [NIST SP 800-88 Rev. 1](https://csrc.nist.gov/pubs/sp/800/88/r1/final) — saneamiento de medios; autoridad: NIST.
- [SQLite: PRAGMA](https://www.sqlite.org/pragma.html) — `secure_delete`; autoridad: documentación oficial de SQLite.
- [SQLite: VACUUM](https://www.sqlite.org/lang_vacuum.html) — reconstrucción del archivo; autoridad: documentación oficial de SQLite.
- [Sweeney, «k-anonymity»](https://doi.org/10.1142/S0218488502001648) — k-anonimato; autoridad: artículo original (2002).

---

[↑ Glosario](../../README.md) · [← Datagrama](./datagrama.md) · [Dato tardío →](./dato-tardio.md)
