# Migración reversible

[↑ Glosario](../../README.md) · [← Migración](./migracion.md) · [Minificación →](./minificacion.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Cambio de datos cuya inversa devuelve los datos originales, comprobado por comparación.

Definición de trabajo de [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md).

## Por qué importa

La clase donde se define, [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md), existe con este propósito: la clase existe para distinguir las decisiones que se pueden deshacer de las que no, calcular cuánto cuesta deshacer cada una y diseñar los cambios para que el costo de equivocarse sea pequeño y se descubra pronto.

## Cómo funciona

Según [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md):

La reversibilidad de un cambio de datos se comprueba aplicando el cambio, su inverso y comparando con el estado original. Muchas migraciones «reversibles» no devuelven los datos: borrar una columna elimina su contenido; convertir decimales a enteros redondea; sustituir un correo por su hash es unidireccional por diseño. Un script «down» que recrea la estructura, vacía de datos, se parece a una reversión y no lo es.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md):

En la plataforma, `decision-reversibility.md` tiene una fila por decisión con su costo de equivocarse, su costo de reversión, su clasificación (dos sentidos, costosa de revertir, un sentido), la evidencia exigida y el mecanismo de salida. El contrato es que ninguna migración se despliega sin la comparación antes/después en un entorno de prueba y que las irreversibles requieren copia verificada, revisión de otra persona y ventana de observación. Esa estructura permite que una revisora entienda qué se puede deshacer y qué no.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md)) son:

- **Tras revertir faltan datos** — causa: la inversa recrea estructura, no contenido. Corrección: comparar antes y después y guardar copia verificada.
- **Un defecto afecta a miles de personas el viernes** — causa: despliegue a todos de golpe. Corrección: desplegar por etapas con detección entre etapas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Muchas migraciones «reversibles» no devuelven los datos: borrar una columna elimina su contenido; convertir decimales a enteros redondea; sustituir un correo por su hash es unidireccional por diseño. ([SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo de reversión](../c/costo-de-reversion.md), [Decisión irreversible (de un sentido)](../d/decision-irreversible-de-un-sentido.md), [Decisión reversible (de dos sentidos)](../d/decision-reversible-de-dos-sentidos.md), [Despliegue progresivo](../d/despliegue-progresivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Amazon: Letter to Shareholders](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) — decisiones de un sentido y de dos sentidos y el proceso que merece cada una; autoridad: Amazon (carta corporativa).
- [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/) — despliegue a una fracción y comparación con el control; autoridad: Google SRE.
- [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuesto de error y decisiones sobre riesgo; autoridad: Google SRE.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — qué cambios de esquema admite SQLite y con qué restricciones; autoridad: proyecto SQLite.
- [Martin Fowler: Evolutionary Database Design](https://martinfowler.com/articles/evodb.html) — cambios de esquema pequeños, reversibles y automatizados; autoridad: M. Fowler y P. Sadalage.

---

[↑ Glosario](../../README.md) · [← Migración](./migracion.md) · [Minificación →](./minificacion.md)
