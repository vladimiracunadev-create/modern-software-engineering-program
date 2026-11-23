# Tablas de decisión

[↑ Glosario](../../README.md) · [← Tabla de diferencias](./tabla-de-diferencias.md) · [Táctica →](./tactica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Enumeración de combinaciones de condiciones con la acción de cada una, que permite comprobar completitud y consistencia.

Definición de trabajo de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).

## Por qué importa

En [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), el tema «Tablas de decisión» importa porque muestran huecos y contradicciones que el texto corrido oculta.

## Cómo funciona

Según [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), en la sección «Tablas de decisión»:

Cuando una regla depende de varias condiciones, el texto corrido invita a describir los casos felices y olvidar el resto. Una tabla de decisión enumera todas las combinaciones de condiciones y asigna una acción a cada una; permite comprobar dos propiedades: completitud (ninguna combinación sin acción) y consistencia (ninguna combinación con acciones contradictorias). El costo es exponencial —n condiciones binarias dan 2^n filas—, así que su uso se limita a reglas con pocas condiciones o se complementa con pruebas combinatorias (`SE-149`).

## Ejemplo

Ejemplo de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) (sección «Caso conductor»):

La plataforma de entregas sigue siendo el caso de la parte. Esta clase añade al expediente de `SE-145` una tabla de decisión de penalización y una política de plazo. Las clases siguientes preguntarán qué calidad debe tener la recuperación (`SE-147`), cómo se cuenta desde el punto de vista de quien usa (`SE-148`) y cómo se prueba con ejemplos (`SE-149`). Cambia después una sola regla —por ejemplo, que la prórroga se sume a la gracia— y revisa qué filas de la tabla cambian.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)) son:

- **Dos módulos calculan una nota distinta para la misma entrega** — causa: la regla vive duplicada en el código y cada copia evolucionó por su lado. Corrección: extraer la regla a un único punto con identificador y responsable.
- **El comité de política pregunta «¿qué pasa si…?» y nadie lo sabe** — causa: se redactaron solo los casos felices. Corrección: enumerar combinaciones y asignar a cada una una acción o una decisión pendiente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una tabla de decisión enumera todas las combinaciones de condiciones y asigna una acción a cada una; permite comprobar dos propiedades: completitud (ninguna combinación sin acción) y consistencia (ninguna combinación con acciones contradictorias). ([SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](../c/combinacion.md), [Condición](../c/condicion.md), [Enumeración](../e/enumeracion.md), [Estados e invariantes](../e/estados-e-invariantes.md), [Regla de negocio](../r/regla-de-negocio.md), [Requisito funcional](../r/requisito-funcional.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md).

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

[↑ Glosario](../../README.md) · [← Tabla de diferencias](./tabla-de-diferencias.md) · [Táctica →](./tactica.md)
