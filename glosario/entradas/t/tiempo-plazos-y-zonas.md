# Tiempo, plazos y zonas

[↑ Glosario](../../README.md) · [← Tiempo hasta detectar](./tiempo-hasta-detectar.md) · [Time to first success →](./time-to-first-success.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Especificación de un instante límite que incluye zona, regla de cambio de hora y definición de día.

Definición de trabajo de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).

## Por qué importa

En [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), el tema «Tiempo, plazos y zonas» importa porque un plazo tiene significado distinto según zona, regla de cambio de hora y definición de día.

## Cómo funciona

Según [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), en la sección «Tiempo, plazos y zonas»:

«Hasta la medianoche» parece claro hasta que la medianoche no existe. Un plazo necesita cuatro decisiones: qué instante (con desplazamiento respecto de UTC, como en RFC 3339), en qué zona se interpreta, qué ocurre si la hora local se repite o se salta, y si el plazo es una hora fija o una duración. Escribir el plazo como instante UTC resuelve la ambigüedad pero cambia lo que la estudiante ve en pantalla: el requisito debe decir qué fuente manda.

## Ejemplo

Caso medido en la sección «Tiempo, plazos y zonas» de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md):

«Hasta la medianoche» parece claro hasta que la medianoche no existe. Un plazo necesita cuatro decisiones: qué instante (con desplazamiento respecto de UTC, como en RFC 3339), en qué zona se interpreta, qué ocurre si la hora local se repite o se salta, y si el plazo es una hora fija o una duración. Escribir el plazo como instante UTC resuelve la ambigüedad pero cambia lo que la estudiante ve en pantalla: el requisito debe decir qué fuente manda.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)) son:

- **Dos módulos calculan una nota distinta para la misma entrega** — causa: la regla vive duplicada en el código y cada copia evolucionó por su lado. Corrección: extraer la regla a un único punto con identificador y responsable.
- **El comité de política pregunta «¿qué pasa si…?» y nadie lo sabe** — causa: se redactaron solo los casos felices. Corrección: enumerar combinaciones y asignar a cada una una acción o una decisión pendiente.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con reglas y fechas sintéticas en Windows y Ubuntu (WSL2) con resultados idénticos. No se consultó ningún reglamento real, los mutantes y las reglas son del autor y las fechas de cambio de hora corresponden a la base de zonas instalada. La siguiente clase pregunta qué calidad debe tener lo que la regla produce: cuán rápido, cuán disponible, cuán seguro.

## Relación con otros conceptos

- **Prerrequisito:** [Especificación](../e/especificacion.md).
- **Ver también:** [Instante](../i/instante.md), [Límite](../l/limite.md), [Regla](../r/regla.md), [Zona](../z/zona.md), [Estados e invariantes](../e/estados-e-invariantes.md), [Regla de negocio](../r/regla-de-negocio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Mavin et al.: Easy Approach to Requirements Syntax, EARS (2009)](https://doi.org/10.1109/RE.2009.9) — plantillas de frase para requisitos; autoridad: IEEE International Requirements Engineering Conference.
- [Sitio de EARS (Alistair Mavin)](https://alistairmavin.com/ears/) — descripción de las plantillas por su autor.
- [Business Rules Manifesto](https://www.businessrulesgroup.org/brmanifesto.htm) — reglas como requisito de primer nivel; autoridad: Business Rules Group.
- [RFC 3339: Date and Time on the Internet](https://www.rfc-editor.org/rfc/rfc3339) — formato de instantes con desplazamiento; autoridad: IETF.
- [IANA: Time Zone Database](https://www.iana.org/time-zones) — origen de las reglas de zona y de sus cambios; autoridad: IANA.

---

[↑ Glosario](../../README.md) · [← Tiempo hasta detectar](./tiempo-hasta-detectar.md) · [Time to first success →](./time-to-first-success.md)
