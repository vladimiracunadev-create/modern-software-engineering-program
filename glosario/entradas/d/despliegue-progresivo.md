# Despliegue progresivo

[↑ Glosario](../../README.md) · [← Despliegue por etapas](./despliegue-por-etapas.md) · [Desviación →](./desviacion.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Exposición gradual de un cambio a fracciones crecientes de personas con detección entre etapas.

Definición de trabajo de [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md).

## Por qué importa

En [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md), el tema «Despliegue progresivo» importa porque limitar la exposición reduce el daño de un defecto y acorta el tiempo hasta verlo.

## Cómo funciona

Según [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md), en la sección «Despliegue progresivo»:

Desplegar a una fracción creciente de personas limita cuántas ven un defecto antes de detectarlo. La detección depende de cuántas personas se ven afectadas y de qué fracción lo reporta: un defecto frecuente se ve en la primera etapa; uno raro, solo cuando la exposición es mayor. El diseño de las etapas y del umbral de detección es una decisión que se escribe antes de desplegar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md):

En la plataforma, `decision-reversibility.md` tiene una fila por decisión con su costo de equivocarse, su costo de reversión, su clasificación (dos sentidos, costosa de revertir, un sentido), la evidencia exigida y el mecanismo de salida. El contrato es que ninguna migración se despliega sin la comparación antes/después en un entorno de prueba y que las irreversibles requieren copia verificada, revisión de otra persona y ventana de observación. Esa estructura permite que una revisora entienda qué se puede deshacer y qué no.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md)) son:

- **Tras revertir faltan datos** — causa: la inversa recrea estructura, no contenido. Corrección: comparar antes y después y guardar copia verificada.
- **Un defecto afecta a miles de personas el viernes** — causa: despliegue a todos de golpe. Corrección: desplegar por etapas con detección entre etapas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El despliegue progresivo reduce la exposición, no sustituye las pruebas. ([SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Exposición](../e/exposicion.md), [Costo de reversión](../c/costo-de-reversion.md), [Decisión irreversible (de un sentido)](./decision-irreversible-de-un-sentido.md), [Decisión reversible (de dos sentidos)](./decision-reversible-de-dos-sentidos.md), [Migración reversible](../m/migracion-reversible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-142 — Decisiones reversibles e irreversibles](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md).

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

[↑ Glosario](../../README.md) · [← Despliegue por etapas](./despliegue-por-etapas.md) · [Desviación →](./desviacion.md)
