# Spec-as-source

[↑ Glosario](../../README.md) · [← Spec-anchored](./spec-anchored.md) · [Spec-first →](./spec-first.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

**Spec-as-source** es el uso de la especificación como único artefacto editable del que se genera el código ([SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md)). Es el tercer nivel de uso de una especificación, después de spec-first (guía y se archiva) y spec-anchored (se mantiene anclada al código).

## Por qué importa

La especificación es lo que se edita; el código se genera y no se toca a mano. La deriva entre especificación y código desaparece por construcción, y cambiar un contrato es editar un archivo. Cambia dónde se trabaja: se edita la fuente y se regenera.

## Cómo funciona

En spec-as-source el humano **no toca el código generado**. Se edita la especificación y se regenera; editar el código a mano está desaconsejado y se marca con un comentario («GENERADO; no editar»). [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) menciona a Tessl como la herramienta que, según Böckeler, explora este nivel, con una correspondencia de uno a uno entre un archivo de especificación y un archivo de código.

Los **costes** son reales, según [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md): hay que **confiar en el generador** (y revisar lo que produce), la especificación debe ser **lo bastante expresiva** para cubrir el comportamiento deseado (si no lo es, la gente edita el código y rompe el modelo) y, con modelos generativos, la regeneración puede no ser determinista. De ahí que la generación determinista sea una condición: un generador que ordena toda su salida y **marca la región generada**, más una comprobación que regenera y compara huellas, y falla si hay diferencias.

La práctica en la plataforma de entregas: los clientes de la API se generan desde el documento OpenAPI (spec-as-source), con un generador determinista, mientras el contrato mismo es spec-anchored y el documento de arquitectura es spec-first. Cada artefacto declara su nivel. Un fallo previsto: la regeneración borra trabajo manual porque se editó dentro de lo generado; se corrige delimitando la región generada y moviendo lo manual fuera.

## Ejemplo

El equipo edita `entregas.openapi.yaml` para añadir el campo opcional `comentario`. Ejecuta el generador: el cliente en TypeScript y el servidor de esqueleto se regeneran, con los archivos marcados «GENERADO; no editar». Una comprobación en CI regenera de nuevo y compara huellas con lo comprometido; si alguien editó a mano un archivo generado, la comparación falla. (Ilustración del flujo descrito en [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md).)

## Errores y confusiones comunes

- **Editar a mano el código generado**: se pierde en la próxima regeneración.
- **La regeneración borra trabajo manual**: ediciones dentro de lo generado.
- **Generador no determinista** que produce diffs ruidosos.
- **Confundirlo con spec-anchored**: allí el código se escribe aparte y se compara.

## Límites y cuándo no aplica

Solo sirve donde la especificación puede expresar todo lo necesario; la lógica compleja suele escribirse a mano en código no generado. Con generadores de IA, el resultado puede variar y exige revisión. El costo de montar el generador solo se justifica para artefactos que cambian a menudo y se repiten (clientes, esqueletos).

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
