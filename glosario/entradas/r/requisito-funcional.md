# Requisito funcional

[↑ Glosario](../../README.md) · [← Requisito derivado](./requisito-derivado.md) · [Requisito negativo →](./requisito-negativo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Descripción de una respuesta observable del sistema ante un estímulo bajo una condición.

Definición de trabajo de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).

## Por qué importa

En [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), el tema «Requisito funcional» importa porque define qué hace el sistema ante un estímulo y una condición; sin ello no hay qué probar.

## Cómo funciona

Según [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), en la sección «Requisito funcional»:

Un requisito funcional describe una respuesta observable del sistema a un estímulo, bajo una condición. Las plantillas EARS ayudan porque obligan a nombrar las tres partes: «Cuando la sesión expira, el sistema conservará el borrador de los últimos 30 s». Sin estímulo no se sabe cuándo ocurre; sin condición no se sabe cuándo no; sin respuesta observable no se puede probar. Un requisito funcional también debe ser singular: «guardará y cifrará y avisará» son tres requisitos que fallan por separado y se prueban por separado.

## Ejemplo

Ejemplo de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) (sección «Preguntas frecuentes»):

No. La regla es una decisión de la organización («una entrega en gracia pierde el 10 %»); el requisito funcional es lo que el sistema hace con ella («calculará la nota final aplicando BR-07»). Si la regla cambia, cambia el requisito solo si cambia cómo se aplica; separarlas permite que quien decide la política la cambie sin tocar el código.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)) son:

- **Dos módulos calculan una nota distinta para la misma entrega** — causa: la regla vive duplicada en el código y cada copia evolucionó por su lado. Corrección: extraer la regla a un único punto con identificador y responsable.
- **El comité de política pregunta «¿qué pasa si…?» y nadie lo sabe** — causa: se redactaron solo los casos felices. Corrección: enumerar combinaciones y asignar a cada una una acción o una decisión pendiente.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con reglas y fechas sintéticas en Windows y Ubuntu (WSL2) con resultados idénticos. No se consultó ningún reglamento real, los mutantes y las reglas son del autor y las fechas de cambio de hora corresponden a la base de zonas instalada. La siguiente clase pregunta qué calidad debe tener lo que la regla produce: cuán rápido, cuán disponible, cuán seguro.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Estados e invariantes](../e/estados-e-invariantes.md), [Regla de negocio](./regla-de-negocio.md), [Tablas de decisión](../t/tablas-de-decision.md), [Tiempo, plazos y zonas](../t/tiempo-plazos-y-zonas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md).

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

[↑ Glosario](../../README.md) · [← Requisito derivado](./requisito-derivado.md) · [Requisito negativo →](./requisito-negativo.md)
