# Retención legal

[↑ Glosario](../../README.md) · [← Retención bruta y neta](./retencion-bruta-y-neta.md) · [Retención por cohorte →](./retencion-por-cohorte.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Suspensión de la eliminación de ciertos registros por un litigio, una auditoría o una obligación.

Definición de trabajo de [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md).

## Por qué importa

La clase donde se define, [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), existe con este propósito: la clase existe para que retires un sistema sin romper a quien aún lo usa, sin guardar datos que ya no deberías tener y sin perder los que debes conservar.

## Cómo funciona

Según [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md):

La retención responde cuánto tiempo se guarda cada tipo de dato y por qué. Hay obligaciones de **conservar** (actas académicas, registros contables) y de **no conservar más de lo necesario** (datos personales sin finalidad vigente), y ambas pueden aplicarse a la misma base. Una regla única («borrar lo que tenga más de cinco años») viola alguna de las dos para casi todos los tipos. La regla correcta es **por tipo de dato**, con un plazo y un fundamento, y con una excepción para la **retención legal** (un registro bajo litigio o auditoría no se borra aunque venza su plazo).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo hace el inventario de consumidores del módulo: 11 aplicaciones, 3 informes programados y, tras preguntar a las áreas, dos consultas manuales (una anual de finanzas y otra trimestral de la coordinación académica). Fija una ventana de observación de 400 días, desactiva la lectura por etapas con aviso y mantiene el sistema apagado pero restaurable durante noventa días.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se borran actas que debían conservarse** — causa: corte único de retención. Corrección: reglas por tipo con fundamento y retención legal. ([SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La regla correcta es **por tipo de dato**, con un plazo y un fundamento, y con una excepción para la **retención legal** (un registro bajo litigio o auditoría no se borra aunque venza su plazo). ([SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](./registro.md), [Disposición](../d/disposicion.md), [Periodicidad](../p/periodicidad.md), [Retención](./retencion.md), [Suma de verificación](../s/suma-de-verificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-88 Rev. 1](https://csrc.nist.gov/pubs/sp/800/88/r1/final) — saneamiento de medios; autoridad: NIST.
- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — limitación del plazo de conservación; autoridad: Unión Europea (no es asesoría legal).
- [CCSDS 650.0-B-2, OAIS](https://public.ccsds.org/Pubs/650x0m2.pdf) — modelo de referencia de archivo a largo plazo; autoridad: CCSDS.
- [Library of Congress: Recommended Formats Statement](https://www.loc.gov/preservation/resources/rfs/) — criterios de formatos para preservación; autoridad: Library of Congress.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — base embebida usada como formato de archivo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Retención bruta y neta](./retencion-bruta-y-neta.md) · [Retención por cohorte →](./retencion-por-cohorte.md)
