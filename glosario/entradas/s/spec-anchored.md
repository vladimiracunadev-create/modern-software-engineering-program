# Spec-anchored

[↑ Glosario](../../README.md) · [← Span](./span.md) · [Spec-as-source →](./spec-as-source.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Uso de la especificación como documento vivo que se actualiza junto con el código.

Definición de trabajo de [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md).

## Por qué importa

En [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), el tema «Spec-anchored» importa porque la especificación se mantiene viva con el código; exige un mecanismo que detecte la deriva.

## Cómo funciona

Según [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), en la sección «Spec-anchored»:

En spec-anchored la especificación se mantiene con el código a lo largo de la vida del sistema: un cambio de comportamiento exige actualizar ambos. El valor es que el contrato sigue siendo una fuente fiable para consumidores y revisores; el coste, que exige un mecanismo que haga fallar la integración continua cuando discrepan. Sin ese mecanismo, el anclaje es una promesa: la deriva aparece en el primer apuro. La comprobación se puede hacer por firmas, por ejemplos o por pruebas contractuales, con distinta potencia y coste.

Según [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md), en la sección «Spec-anchored»:

En el segundo nivel la especificación se **mantiene** y se **ancla** al código y a las pruebas con comprobaciones: cada regla tiene un identificador que el código y las pruebas citan; los valores que la especificación declara (umbrales, límites) se comparan con los del código; un cambio en el código sin cambio en la especificación se señala. La especificación es una fuente que se revisa con cada cambio, como una prueba. El costo es disciplina y herramientas: alguien debe escribir el comprobador y alguien debe atender sus alertas.

## Ejemplo

Ejemplo de [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) (sección «Ejemplo profesional»):

En la plataforma, cada artefacto tiene un nivel declarado. El documento de arquitectura es spec-first (guía y se archiva). El contrato de la API es spec-anchored: un comprobador en integración continua compara las operaciones del código con el documento OpenAPI y falla con el nombre del parámetro que discrepa. Los clientes se generan desde el documento (spec-as-source) con un generador que ordena toda su salida y marca la región generada; una comprobación regenera y compara huellas, y falla si hay diferencias con lo comprometido. Una nota por artefacto registra la señal que haría cambiar de nivel.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La especificación dice una cosa y el código otra, y nadie lo sabe** — causa: spec-anchored sin comprobación mecánica. Corrección: comparar firmas o ejemplos en integración continua. ([SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. La deriva se midió solo en firmas, la probabilidad de deriva es un supuesto y no se usó ningún generador de producción ni un asistente de programación. La siguiente clase convierte las comprobaciones de firmas en especificaciones que se ejecutan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Especificación](../e/especificacion.md), [Anclaje](../a/anclaje.md), [Archivo generado](../a/archivo-generado.md), [Deriva](../d/deriva.md), [Generación determinista](../g/generacion-determinista.md).
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

[↑ Glosario](../../README.md) · [← Span](./span.md) · [Spec-as-source →](./spec-as-source.md)
