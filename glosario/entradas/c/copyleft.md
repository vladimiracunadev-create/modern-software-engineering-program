# Copyleft

[↑ Glosario](../../README.md) · [← Copia superficial](./copia-superficial.md) · [Copyright y licencia →](./copyright-y-licencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Familia de licencias que exigen que las obras derivadas se distribuyan bajo condiciones análogas.

Definición de trabajo de [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-201 — Licencias de software y obligaciones básicas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md): Familia de licencias que condiciona la redistribución de obras derivadas a términos similares.

## Por qué importa

La clase donde se define, [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md), existe con este propósito: la clase existe para que reconozcas cuándo una decisión técnica es también una decisión legal o ética y para que la trates con procesos verificables en vez de con suposiciones.

## Cómo funciona

Según [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md):

Las licencias de código abierto, reunidas por la Open Source Initiative, caen en familias con obligaciones distintas. Las **permisivas** (MIT, BSD, Apache 2.0, ISC) piden conservar el aviso de derechos y, en el caso de Apache, mencionar cambios y conceder patentes. Las de **copyleft débil** (MPL 2.0, LGPL) exigen compartir las modificaciones de los archivos o la biblioteca bajo la misma licencia, sin extender la obligación al resto del producto cuando se usan como se indica. Las de **copyleft fuerte** (GPL, AGPL) extienden la obligación de ofrecer el código fuente al trabajo derivado, y la AGPL también cuando se ofrece como servicio en red.

Según [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo genera el inventario de sesenta dependencias con licencia y versión y lo clasifica con la política. Tres quedan «desconocidas»: abre incidencias en cada proyecto y mientras tanto las trata como bloqueadas; dos responden que su licencia es MIT y se actualiza el inventario con el enlace a la respuesta. De las once por revisar, nueve son de copyleft débil usadas sin modificar y dos son combinaciones; las dos se envían a una abogada con el contexto técnico (cómo se enlazan, si se distribuyen).

## Ejemplo

Ejemplo de [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md) (sección «Ejemplo mínimo»):

Imprime `0 2 1`: con `OR` se elige la permisiva y no hay obligación copyleft; con `AND` se deben cumplir ambas y gana la más restrictiva; la débil queda en «revisar». Observa que una búsqueda de `GPL` marcaría las tres con la misma alarma. Registra versión de Python, comando y salida.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md)) son:

- **Se frena trabajo por una licencia inofensiva** — causa: búsqueda de cadena sin analizar la expresión. Corrección: analizar `AND`, `OR` y `WITH`.
- **Una licencia incompatible llega a producción** — causa: campo vacío tratado como seguro. Corrección: tratar lo desconocido como bloqueado hasta resolverlo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las de **copyleft débil** (MPL 2.0, LGPL) exigen compartir las modificaciones de los archivos o la biblioteca bajo la misma licencia, sin extender la obligación al resto del producto cuando se usan como se indica. ([SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](./condicion.md), [Certificación de origen](./certificacion-de-origen.md), [Dependencia transitiva](../d/dependencia-transitiva.md), [Expresión de licencia](../e/expresion-de-licencia.md), [Huella de texto](../h/huella-de-texto.md), [Licencia de software](../l/licencia-de-software.md).
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

[↑ Glosario](../../README.md) · [← Copia superficial](./copia-superficial.md) · [Copyright y licencia →](./copyright-y-licencia.md)
