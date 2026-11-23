# Estados e invariantes

[↑ Glosario](../../README.md) · [← Estado válido](./estado-valido.md) · [Estampida →](./estampida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Situaciones por las que pasa una entidad y propiedades que deben cumplirse en todas.

Definición de trabajo de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).

## Por qué importa

En [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), el tema «Estados e invariantes» importa porque lo que siempre debe ser cierto (una entrega enviada no se edita) se verifica en cada transición.

## Cómo funciona

Según [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), en la sección «Estados e invariantes»:

Una entrega pasa por estados (borrador, enviada, en revisión, calificada) y ciertas propiedades deben cumplirse siempre: una entrega calificada no se modifica sin reabrirse, una entrega enviada tiene fecha de envío. Un invariante es una regla que no depende de la transición que ocurra; se escribe una vez y se comprueba en cada una. Descubrir que algo debería ser un invariante es parte del análisis: aparece cuando alguien dice «eso nunca debería pasar» y nadie sabe dónde se garantiza.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md):

La política de entregas tardías se registra como regla con identificador, texto, responsable y fecha, separada del requisito que la aplica:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)) son:

- **Dos módulos calculan una nota distinta para la misma entrega** — causa: la regla vive duplicada en el código y cada copia evolucionó por su lado. Corrección: extraer la regla a un único punto con identificador y responsable.
- **El comité de política pregunta «¿qué pasa si…?» y nadie lo sabe** — causa: se redactaron solo los casos felices. Corrección: enumerar combinaciones y asignar a cada una una acción o una decisión pendiente.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con reglas y fechas sintéticas en Windows y Ubuntu (WSL2) con resultados idénticos. No se consultó ningún reglamento real, los mutantes y las reglas son del autor y las fechas de cambio de hora corresponden a la base de zonas instalada. La siguiente clase pregunta qué calidad debe tener lo que la regla produce: cuán rápido, cuán disponible, cuán seguro.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad](../p/propiedad.md), [Regla de negocio](../r/regla-de-negocio.md), [Requisito funcional](../r/requisito-funcional.md), [Tablas de decisión](../t/tablas-de-decision.md), [Tiempo, plazos y zonas](../t/tiempo-plazos-y-zonas.md).
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

[↑ Glosario](../../README.md) · [← Estado válido](./estado-valido.md) · [Estampida →](./estampida.md)
