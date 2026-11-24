# Requisito funcional

[↑ Glosario](../../README.md) · [← Requisito derivado](./requisito-derivado.md) · [Requisito negativo →](./requisito-negativo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Un **requisito funcional** describe una respuesta observable del sistema ante un estímulo, bajo una condición ([SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)). Dice *qué hace* el sistema, a diferencia de los requisitos de calidad, que dicen *qué tan bien* lo hace, y de las reglas de negocio, que son decisiones de la organización.

## Por qué importa

Sin una respuesta observable no hay qué probar. Un requisito funcional bien formado permite construir y verificar; uno vago produce acuerdos aparentes. Cambia cómo se redacta: se nombra el estímulo, la condición y la respuesta, en lugar de describir deseos generales.

## Cómo funciona

[SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) recomienda plantillas como EARS (Easy Approach to Requirements Syntax), que obligan a nombrar las tres partes. Un ejemplo de la clase: «Cuando la sesión expira, el sistema conservará el borrador de los últimos 30 s». El **estímulo** (la sesión expira) dice cuándo ocurre; la **condición** acota cuándo no; la **respuesta observable** (conservará el borrador de los últimos 30 s) se puede probar. Sin estímulo no se sabe cuándo ocurre; sin condición no se sabe cuándo no; sin respuesta observable no se puede probar.

Un requisito funcional también debe ser **singular**: «guardará y cifrará y avisará» son tres requisitos que fallan por separado y se prueban por separado.

La clase distingue además el requisito de la **regla de negocio**. La regla es una decisión de la organización («una entrega en gracia pierde el 10 %»); el requisito es lo que el sistema hace con ella («calculará la nota final aplicando BR-07»). Separarlas permite que quien decide la política la cambie sin tocar el código, y que el requisito cambie solo cuando cambie cómo se aplica la regla. Y la regla debe vivir en un solo punto con identificador y responsable: si vive duplicada en el código, cada copia evoluciona por su lado y dos módulos calculan una nota distinta para la misma entrega.

## Ejemplo

«Cuando una estudiante envíe una entrega después del plazo y la tarea admita entregas en gracia, el sistema calculará la nota final aplicando BR-07 y mostrará el descuento aplicado.» Estímulo: el envío tardío. Condición: la tarea admite gracia. Respuesta: cálculo con BR-07 y muestra del descuento. Se prueba con una entrega concreta y se verifica el valor. (Redacción construida con el patrón de EARS y las referencias de [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).)

## Errores y confusiones comunes

- **Dos módulos calculan distinta nota**: la regla vive duplicada; corrección: extraerla a un único punto con identificador y responsable.
- **El comité pregunta «¿qué pasa si…?» y nadie lo sabe**: solo se redactaron los casos felices; corrección: enumerar combinaciones y asignar a cada una una acción o una decisión pendiente.
- **Requisitos compuestos** («y… y…»).
- **Mezclar la regla de negocio con el requisito.**

## Límites y cuándo no aplica

Los requisitos funcionales no capturan atributos de calidad (rendimiento, seguridad), que se expresan como escenarios medibles. En desarrollos exploratorios, enumerarlos por adelantado puede ser prematuro; se trabaja con historias y se refinan al construir. Una lista completa de requisitos funcionales no garantiza que el producto sea útil: eso depende de que correspondan a necesidades reales.

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
