# Spec-anchored

[↑ Glosario](../../README.md) · [← Span](./span.md) · [Spec-as-source →](./spec-as-source.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

**Spec-anchored** es el uso de la especificación como un documento vivo que se mantiene junto con el código a lo largo de la vida del sistema ([SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md)). Es el segundo de tres niveles: spec-first (la especificación guía y se abandona), spec-anchored (se mantiene anclada al código) y spec-as-source (la especificación es la fuente de la que se genera el código).

## Por qué importa

Hace que la especificación siga siendo una fuente fiable para consumidores y revisores. Cuando cambia el comportamiento, cambian ambos. Su coste es disciplina: sin un mecanismo que detecte la discrepancia, el anclaje es una promesa y la deriva aparece en el primer apuro ([SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md)). Cambia la decisión de qué artefactos merecen este nivel: los que otros consumen y cambian a menudo.

## Cómo funciona

El anclaje requiere un **mecanismo que haga fallar la integración continua cuando especificación y código discrepan**. [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) menciona tres formas de comprobarlo, con distinta potencia: por firmas (nombres y tipos), por ejemplos y por pruebas contractuales. [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) lo describe en el contexto de desarrollo guiado por especificaciones: cada regla tiene un identificador que el código y las pruebas citan; los valores que la especificación declara (umbrales, límites) se comparan con los del código; un cambio en el código sin cambio en la especificación se señala. La especificación es una fuente que se revisa con cada cambio, como una prueba.

El costo es disciplina y herramientas: alguien debe escribir el comprobador y alguien debe mantenerlo. En la plataforma de entregas ([SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md)), cada artefacto tiene un nivel declarado: el documento de arquitectura es spec-first (guía y se archiva); el contrato de la API es spec-anchored, con un comprobador en integración continua que compara las operaciones del código con el documento OpenAPI y falla con el nombre del parámetro que discrepa; los clientes se generan desde el documento (spec-as-source).

## Ejemplo

El documento OpenAPI declara que `POST /entregas` acepta el parámetro `archivo` obligatorio. Un desarrollador renombra el parámetro a `adjunto` en el código sin tocar el documento. El comprobador de integración continua compara ambos y falla con el mensaje «parámetro `archivo` ausente en el código; `adjunto` ausente en la especificación». Hasta que alguien actualice uno, la integración no pasa. (Ilustración del mecanismo descrito en [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md).)

## Errores y confusiones comunes

- **La especificación dice una cosa y el código otra, y nadie lo sabe**: anclaje sin comprobación automática.
- **Anclar todo**: el costo de mantener comprobadores para documentos que casi no cambian no se justifica.
- **Confundirlo con spec-as-source**: aquí el código se escribe aparte y se compara; allí se genera.
- **Comprobar solo la forma** y no el comportamiento.

## Límites y cuándo no aplica

Para decisiones puntuales que se toman una vez (un documento de arquitectura), el anclaje es excesivo y es preferible spec-first con archivo. Si la comprobación es débil (solo firmas), la deriva de comportamiento pasa sin ser detectada. Y si el equipo no tiene capacidad de mantener el comprobador, el anclaje se rompe en silencio.

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
