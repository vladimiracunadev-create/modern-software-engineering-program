# Expresión de licencia

[↑ Glosario](../../README.md) · [← Expresión](./expresion.md) · [Extensión →](./extension.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Combinación de identificadores de licencia con `AND`, `OR` y `WITH` que declara bajo qué condiciones se ofrece un componente.

Definición de trabajo de [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md): Combinación de identificadores con `AND`, `OR`, `WITH` y paréntesis que describe bajo qué licencias se ofrece una pieza.

## Por qué importa

La clase donde se define, [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md), existe con este propósito: la clase existe para que reconozcas cuándo una decisión técnica es también una decisión legal o ética y para que la trates con procesos verificables en vez de con suposiciones.

## Cómo funciona

Según [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md):

Se generan 60 dependencias sintéticas con expresiones de licencia (permisivas, débiles, fuertes, combinadas, con excepción, vacías o propias). El analizador respeta `OR` (elige la mejor opción), `AND` (la peor) y `WITH` (una excepción de tipo Classpath rebaja una licencia fuerte a «revisar»). Se compara con una búsqueda ingenua de la cadena `GPL`.

## Ejemplo

Ejemplo de [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md) (sección «Ejemplo mínimo»):

El fragmento clasifica tres expresiones de licencia con una regla simple (`OR` toma la mejor, `AND` la peor). Antes de ejecutarlo, predice cuál se bloquea.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md)) son:

- **Se frena trabajo por una licencia inofensiva** — causa: búsqueda de cadena sin analizar la expresión. Corrección: analizar `AND`, `OR` y `WITH`.
- **Una licencia incompatible llega a producción** — causa: campo vacío tratado como seguro. Corrección: tratar lo desconocido como bloqueado hasta resolverlo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se generan 60 dependencias sintéticas con expresiones de licencia (permisivas, débiles, fuertes, combinadas, con excepción, vacías o propias). ([SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](../c/combinacion.md), [Componente](../c/componente.md), [Condición](../c/condicion.md), [Certificación de origen](../c/certificacion-de-origen.md), [Copyleft](../c/copyleft.md), [Dependencia transitiva](../d/dependencia-transitiva.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SPDX, expresiones de licencia](https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/) — sintaxis de combinación de licencias; autoridad: proyecto SPDX (Linux Foundation).
- [Open Source Initiative, licencias](https://opensource.org/licenses) — licencias aprobadas; autoridad: Open Source Initiative.
- [Open Source Guides, «The Legal Side of Open Source»](https://opensource.guide/legal/) — introducción a propiedad y licencias; autoridad: GitHub y comunidad.
- [Developer Certificate of Origin](https://developercertificate.org/) — texto de la certificación de origen; autoridad: Linux Foundation.
- [Git, `git interpret-trailers`](https://git-scm.com/docs/git-interpret-trailers) — pies de mensaje; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Expresión](./expresion.md) · [Extensión →](./extension.md)
