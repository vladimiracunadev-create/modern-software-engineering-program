# Spec-as-source

[↑ Glosario](../../README.md) · [← Spec-anchored](./spec-anchored.md) · [Spec-first →](./spec-first.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Uso de la especificación como único artefacto editable del que se genera el código.

Definición de trabajo de [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md).

## Por qué importa

En [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), el tema «Spec-as-source» importa porque la especificación es lo que se edita; el código se genera y no se toca a mano.

## Cómo funciona

Según [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), en la sección «Spec-as-source»:

En spec-as-source la especificación es lo único que se edita y el código se genera a partir de ella; el humano no toca el código generado. El beneficio es que la deriva desaparece por construcción y que cambiar un contrato es editar un archivo. Los costes son reales: hay que confiar en el generador (y revisar lo que produce), la especificación debe ser lo bastante expresiva para cubrir el comportamiento, y todo lo que no se pueda expresar vive fuera. Cuando la especificación no alcanza, alguien edita lo generado, y entonces la regeneración destruye ese trabajo.

Según [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md), en la sección «Spec-as-source»:

En el tercer nivel la especificación es la fuente y el código se **genera**. Se edita la especificación y se regenera; editar el código a mano está desaconsejado y se marca con un comentario («GENERADO; no editar»). Böckeler describe a Tessl como la herramienta que explora este nivel, con una correspondencia de uno a uno entre un archivo de especificación y un archivo de código, y la califica de beta en el momento del análisis. La ventaja es que la deriva desaparece por construcción; el costo es que lo que la especificación no puede expresar no se puede construir, y que el generador es ahora una pieza que hay que confiar.

## Ejemplo

Ejemplo de [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) (sección «Ejemplo profesional»):

En la plataforma, cada artefacto tiene un nivel declarado. El documento de arquitectura es spec-first (guía y se archiva). El contrato de la API es spec-anchored: un comprobador en integración continua compara las operaciones del código con el documento OpenAPI y falla con el nombre del parámetro que discrepa. Los clientes se generan desde el documento (spec-as-source) con un generador que ordena toda su salida y marca la región generada; una comprobación regenera y compara huellas, y falla si hay diferencias con lo comprometido. Una nota por artefacto registra la señal que haría cambiar de nivel.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md)) son:

- **La especificación dice una cosa y el código otra, y nadie lo sabe** — causa: spec-anchored sin comprobación mecánica. Corrección: comparar firmas o ejemplos en integración continua.
- **La regeneración borra trabajo manual** — causa: ediciones dentro de lo generado. Corrección: delimitar la región generada y mover lo manual fuera.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En spec-as-source la especificación es lo único que se edita y el código se genera a partir de ella; el humano no toca el código generado. ([SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Especificación](../e/especificacion.md), [Anclaje](../a/anclaje.md), [Archivo generado](../a/archivo-generado.md), [Deriva](../d/deriva.md), [Generación determinista](../g/generacion-determinista.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Böckeler, «Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl»](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) — distinción entre spec-first, spec-anchored y spec-as-source; autoridad: martinfowler.com.
- [GitHub: spec-kit](https://github.com/github/spec-kit) — herramienta de código abierto de flujo guiado por especificación; autoridad: GitHub.
- [OpenAPI Generator](https://openapi-generator.tech/) — generación de clientes y servidores desde un documento de especificación; autoridad: proyecto OpenAPI Generator.
- [Python: `PYTHONHASHSEED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED) — aleatorización del hash y semilla fija; autoridad: documentación de Python.
- [Python: `inspect`](https://docs.python.org/3/library/inspect.html) — lectura de firmas de funciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Spec-anchored](./spec-anchored.md) · [Spec-first →](./spec-first.md)
