# Observador

[↑ Glosario](../../README.md) · [← Observación](./observacion.md) · [Observer →](./observer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Patrón en que un objeto avisa a quienes se suscribieron cuando su estado cambia.

Definición de trabajo de [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md).

## Por qué importa

La clase donde se define, [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), existe con este propósito: la clase existe para que uses los patrones de diseño como vocabulario de problemas recurrentes y no como plantillas que se instalan: sabrás nombrar el problema que un patrón resuelve, el costo que trae y la prueba que lo vuelve visible, y reconocerás cuándo el patrón solo añade estructura.

## Cómo funciona

Según [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md):

Un patrón de diseño nombra una solución recurrente a un problema recurrente, con sus consecuencias. Su valor principal es de comunicación: decir «aquí hay un observador» permite discutir el orden de las notificaciones y los fallos sin describir las clases. Su riesgo es la aplicación por catálogo: buscar un patrón para cada cosa y terminar con capas sin problema. La unidad de análisis es el problema: el patrón es una de las respuestas posibles.

Según [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md):

El equipo trata los tres problemas por separado. Para la configuración, deja de usar `Config.get()` y construye un objeto `Configuracion` una vez en el arranque que pasa a los módulos que lo necesitan; la suite pasa en cualquier orden y lo comprueba con una ejecución en orden aleatorio con semilla registrada. Para las notificaciones, mantiene el observador, copia la lista antes de recorrerla, aísla cada observador y registra cada excepción en un contador que sube una alarma. Para el proveedor internacional, escribe un adaptador con una prueba de contrato: gramos a kilos, códigos de texto a enteros, y un error explícito para una zona desconocida. En el registro de decisiones anota, para cada patrón, el problema, el cambio esperado y el costo.

## Ejemplo

Ejemplo de [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md) (sección «Ejemplo profesional»):

El equipo trata los tres problemas por separado. Para la configuración, deja de usar `Config.get()` y construye un objeto `Configuracion` una vez en el arranque que pasa a los módulos que lo necesitan; la suite pasa en cualquier orden y lo comprueba con una ejecución en orden aleatorio con semilla registrada. Para las notificaciones, mantiene el observador, copia la lista antes de recorrerla, aísla cada observador y registra cada excepción en un contador que sube una alarma. Para el proveedor internacional, escribe un adaptador con una prueba de contrato: gramos a kilos, códigos de texto a enteros, y un error explícito para una zona desconocida.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un servicio no recibe avisos cuando otro falla** — causa: observadores en un bucle que se corta con la primera excepción. Corrección: aislar cada observador y contar las excepciones. ([SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md))
- **Un observador se salta al darse de baja durante el reparto** — causa: modificación de la lista que se recorre. Corrección: recorrer una copia. ([SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Su valor principal es de comunicación: decir «aquí hay un observador» permite discutir el orden de las notificaciones y los fallos sin describir las clases. ([SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Objeto](./objeto.md), [Patrón](../p/patron.md), [Adaptador](../a/adaptador.md), [Inyección de dependencias](../i/inyeccion-de-dependencias.md), [Patrón de diseño](../p/patron-de-diseno.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-098](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gamma, Helm, Johnson y Vlissides, «Design Patterns» (1994)](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610) — catálogo de patrones; autoridad: los autores (Addison-Wesley).
- [Fowler, «Inversion of Control Containers and the Dependency Injection pattern»](https://martinfowler.com/articles/injection.html) — inyección de dependencias frente a localizador; autoridad: Martin Fowler.
- [Luo et al., «An empirical analysis of flaky tests» (FSE, 2014)](https://doi.org/10.1145/2635868.2635920) — pruebas intermitentes y dependencia del orden; autoridad: ACM SIGSOFT FSE.
- [Python: sentencia `for`](https://docs.python.org/3/reference/compound_stmts.html) — advertencia sobre modificar la secuencia que se recorre; autoridad: documentación de Python.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis sintáctico usado para la huella de cada patrón; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Observación](./observacion.md) · [Observer →](./observer.md)
