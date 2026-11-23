# Regla de negocio

[↑ Glosario](../../README.md) · [← Regla de las tres condiciones](./regla-de-las-tres-condiciones.md) · [Regla de permisos →](./regla-de-permisos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Decisión de la organización, independiente del sistema, sobre qué se acepta, se calcula o se rechaza.

Definición de trabajo de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).

## Por qué importa

En [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), el tema «Regla de negocio» importa porque pertenece a la organización y cambia con la política, no con el código.

## Cómo funciona

Según [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), en la sección «Regla de negocio»:

Una regla de negocio es una decisión de la organización que existiría aunque no hubiera sistema: «una entrega en gracia pierde el 10 % de la nota». El requisito funcional dice cómo el sistema la aplica; la regla dice qué se aplica. Distinguirlas importa por quién puede cambiarlas: la coordinación académica cambia la regla; el equipo cambia el modo de aplicarla. Si la regla vive solo en el código, cada cambio de política es un cambio de software y cada discusión sobre la política se convierte en una discusión sobre código.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md):

La política de entregas tardías se registra como regla con identificador, texto, responsable y fecha, separada del requisito que la aplica:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)) son:

- **Dos módulos calculan una nota distinta para la misma entrega** — causa: la regla vive duplicada en el código y cada copia evolucionó por su lado. Corrección: extraer la regla a un único punto con identificador y responsable.
- **El comité de política pregunta «¿qué pasa si…?» y nadie lo sabe** — causa: se redactaron solo los casos felices. Corrección: enumerar combinaciones y asignar a cada una una acción o una decisión pendiente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una regla de negocio es una decisión de la organización que existiría aunque no hubiera sistema: ([SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Organización](../o/organizacion.md), [Sobre](../s/sobre.md), [Estados e invariantes](../e/estados-e-invariantes.md), [Requisito funcional](./requisito-funcional.md), [Tablas de decisión](../t/tablas-de-decision.md), [Tiempo, plazos y zonas](../t/tiempo-plazos-y-zonas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (31 clases más lo mencionan; las que más):

[SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), [SE-084](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md).

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

[↑ Glosario](../../README.md) · [← Regla de las tres condiciones](./regla-de-las-tres-condiciones.md) · [Regla de permisos →](./regla-de-permisos.md)
