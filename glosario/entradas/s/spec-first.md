# Spec-first

[↑ Glosario](../../README.md) · [← Spec-as-source](./spec-as-source.md) · [Spec-first, spec-anchored, spec-as-source →](./spec-first-spec-anchored-spec-as-source.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

**Spec-first** es el uso de la especificación como guía previa a la implementación, sin mantenerla después ([SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md)). La especificación se escribe antes del código y dirige la construcción; cumple su función cuando el código existe. Es el primero de los tres niveles de uso de una especificación, junto con spec-anchored y spec-as-source.

## Por qué importa

Es el uso más extendido y el más barato, y por eso es el que más conviene entender bien. Cambia cuánto esfuerzo se pone en mantener una especificación: aquí ninguno, y se acepta que quede obsoleta. Su riesgo es que alguien la consulte meses después creyendo que describe el sistema.

## Cómo funciona

En spec-first la especificación es un instrumento de **planificación y diálogo**: ayuda a acordar qué construir, a descubrir ambigüedades antes de programar y a repartir el trabajo. [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) lo ubica en el desarrollo guiado por especificaciones: de la especificación salen un plan, tareas y la implementación, como describen herramientas del tipo Spec Kit. Lo que ocurre después es la pregunta que queda abierta: Böckeler anota que, en los ejemplos que encontró de una herramienta, la especificación se usa para una tarea o una historia y no se explica cómo mantenerla a lo largo de varias tareas.

Por eso [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) advierte que la especificación se convierte en una **fotografía de la intención inicial**. Funciona bien para decisiones que se toman una vez y se revisan con pocas modificaciones (un documento de arquitectura, que «guía y se archiva»), y mal para contratos que cambian a menudo, donde la discrepancia con el código crece sin que nada la señale. La salida no es abandonar spec-first, sino declarar el nivel de cada artefacto y, para los que lo necesiten, subir a spec-anchored.

En la plataforma de entregas, cada artefacto tiene un nivel declarado: el documento de arquitectura es spec-first; el contrato de la API es spec-anchored; los clientes generados son spec-as-source.

## Ejemplo

Antes de construir el módulo de prórrogas, el equipo escribe una especificación de dos páginas con requisitos, ejemplos y casos límite; con ella acuerdan el alcance y reparten tareas. Cuando el módulo se termina, la especificación se archiva con la fecha y una nota «refleja la intención al inicio; el comportamiento vigente está en el código y en las pruebas». Quien la lea un año después sabe qué es. (Ilustración del uso descrito en [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md).)

## Errores y confusiones comunes

- **Creer que la especificación sigue describiendo el sistema** meses después: no se marcó su nivel ni su fecha.
- **Aplicar spec-first a un contrato que cambia a menudo**: la especificación se desactualiza y los consumidores se confunden.
- **Confundirlo con spec-driven development completo**: spec-first es solo el primer nivel.
- **Descartar el valor de la especificación inicial** porque no se mantiene: sirvió para acordar.

## Límites y cuándo no aplica

No sirve como fuente de verdad para consumidores de una API o para auditoría posterior, donde la especificación debe reflejar el sistema vigente. En proyectos que cambian de dirección durante la construcción, una especificación previa muy detallada puede ser un lastre. Su declaración de nivel y fecha mitiga el riesgo de lectura errónea.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Especificación](../e/especificacion.md), [Anclaje](../a/anclaje.md), [Archivo generado](../a/archivo-generado.md), [Deriva](../d/deriva.md), [Generación determinista](../g/generacion-determinista.md), [Huella](../h/huella.md).
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

[↑ Glosario](../../README.md) · [← Spec-as-source](./spec-as-source.md) · [Spec-first, spec-anchored, spec-as-source →](./spec-first-spec-anchored-spec-as-source.md)
