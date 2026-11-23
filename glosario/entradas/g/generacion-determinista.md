# Generación determinista

[↑ Glosario](../../README.md) · [← Generación](./generacion.md) · [Generación estática →](./generacion-estatica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Propiedad de un generador que produce salida idéntica para la misma entrada.

Definición de trabajo de [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md).

## Por qué importa

En [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), el tema «Generación determinista» importa porque un generador que no es reproducible hace imposible comparar y revisar lo generado.

## Cómo funciona

Según [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), en la sección «Generación determinista»:

Un generador debe producir la misma salida con la misma entrada: así se puede regenerar y comparar con lo comprometido, y detectar cambios con un diff. Las fuentes habituales de no determinación son iterar estructuras sin orden garantizado, incluir marcas de tiempo o rutas absolutas, y depender de la configuración regional. En Python, el orden de iteración de un conjunto de cadenas cambia entre procesos porque el hash de las cadenas se aleatoriza por proceso. Un generador debe ordenar explícitamente todo lo que serializa.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md):

En la plataforma, cada artefacto tiene un nivel declarado. El documento de arquitectura es spec-first (guía y se archiva). El contrato de la API es spec-anchored: un comprobador en integración continua compara las operaciones del código con el documento OpenAPI y falla con el nombre del parámetro que discrepa. Los clientes se generan desde el documento (spec-as-source) con un generador que ordena toda su salida y marca la región generada; una comprobación regenera y compara huellas, y falla si hay diferencias con lo comprometido.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md)) son:

- **La especificación dice una cosa y el código otra, y nadie lo sabe** — causa: spec-anchored sin comprobación mecánica. Corrección: comparar firmas o ejemplos en integración continua.
- **La regeneración borra trabajo manual** — causa: ediciones dentro de lo generado. Corrección: delimitar la región generada y mover lo manual fuera.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. La deriva se midió solo en firmas, la probabilidad de deriva es un supuesto y no se usó ningún generador de producción ni un asistente de programación. La siguiente clase convierte las comprobaciones de firmas en especificaciones que se ejecutan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Generador](./generador.md), [Propiedad](../p/propiedad.md), [Deriva](../d/deriva.md), [Spec-anchored](../s/spec-anchored.md), [Spec-as-source](../s/spec-as-source.md), [Spec-first](../s/spec-first.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md).

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

[↑ Glosario](../../README.md) · [← Generación](./generacion.md) · [Generación estática →](./generacion-estatica.md)
